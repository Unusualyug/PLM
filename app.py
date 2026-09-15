from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, send_file
import sqlite3, os, secrets
from functools import wraps

BASE=os.path.dirname(__file__)
DATA_DIR=os.environ.get('DATA_DIR', os.path.join(BASE,'data'))
DB=os.environ.get('DB_PATH', os.path.join(DATA_DIR,'plm_exam.db'))
app=Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY', secrets.token_hex(24))

def db():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c

def ensure_column(c, table, column, definition):
    cols=[r['name'] for r in c.execute(f'PRAGMA table_info({table})').fetchall()]
    if column not in cols:
        c.execute(f'ALTER TABLE {table} ADD COLUMN {column} {definition}')

def init():
    os.makedirs(os.path.dirname(DB),exist_ok=True); c=db()
    c.execute('PRAGMA journal_mode=WAL')
    c.execute('PRAGMA busy_timeout=5000')
    c.executescript('''
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT, name TEXT, enrollment TEXT);
    CREATE TABLE IF NOT EXISTS exams(id INTEGER PRIMARY KEY, name TEXT, subject TEXT, semester TEXT, duration INTEGER, max_marks INTEGER);
    CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY, code TEXT UNIQUE, title TEXT, prompt TEXT, type TEXT, marks INTEGER, resource TEXT);
    CREATE TABLE IF NOT EXISTS assignments(id INTEGER PRIMARY KEY, exam_id INTEGER, student_id INTEGER, task_no INTEGER, question_id INTEGER, marks INTEGER, status TEXT DEFAULT 'OPEN', submitted_at TEXT);
    CREATE TABLE IF NOT EXISTS answers(id INTEGER PRIMARY KEY, assignment_id INTEGER, answer TEXT DEFAULT '', locked INTEGER DEFAULT 0, updated_at TEXT);
    ''')
    ensure_column(c,'users','paper','TEXT DEFAULT "A"')
    ensure_column(c,'users','active','INTEGER DEFAULT 1')
    ensure_column(c,'users','exam_started_at','TEXT DEFAULT NULL')
    ensure_column(c,'users','paper_final_submitted','INTEGER DEFAULT 0')
    ensure_column(c,'users','final_submitted_at','TEXT DEFAULT NULL')
    ensure_column(c,'assignments','awarded_marks','REAL DEFAULT NULL')
    ensure_column(c,'assignments','evaluation_note',"TEXT DEFAULT ''")
    ensure_column(c,'answers','screenshot_path',"TEXT DEFAULT ''")
    if not c.execute('select 1 from users where username="examiner"').fetchone():
        examiner_pw=os.environ.get('EXAMINER_PASSWORD','exam123')
        c.execute('insert into users(username,password,role,name,enrollment,paper) values(?,?,?,?,?,?)',('examiner',examiner_pw,'examiner','PLM Examiner','','A'))
    else:
        c.execute('update users set paper="A" where role="examiner" and (paper is null or paper="")')
        c.execute('update users set active=1 where active is null')
        env_pw=os.environ.get('EXAMINER_PASSWORD')
        if env_pw:
            c.execute('update users set password=? where role="examiner"',(env_pw,))
    if not c.execute('select 1 from exams').fetchone():
        c.execute('insert into exams(name,subject,semester,duration,max_marks) values(?,?,?,?,?)',('PLM MESA Examination','MESA','1st Sem B.Tech.',120,30))
    else:
        c.execute('update exams set name=?, subject=?, semester=?, duration=?, max_marks=?',('PLM MESA Examination','MESA','1st Sem B.Tech.',120,30))
    # Paper A + Paper B question bank
    core=[
      ('Q4-A','Boiler Working Model & Nomenclature','Operate the interactive boiler working model, observe fuel-air-combustion-water-steam-flue-gas flow, and identify the numbered boiler components by correct engineering nomenclature. Demonstrate the working of the boiler and answer the engineering observation prompts.','Interactive Working Model',10),
      ('Q2-A','Fuel Selection Challenge — 10 Applications','Study the real application image. For each of 10 engineering applications, select the most appropriate fuel category (solid, liquid or gaseous), select a suitable fuel from that category, and give an engineering reason for the selection. Each application carries 1 mark for fuel category/fuel selection and engineering justification.','PFL Engineering Challenge',10),
      ('Q3-A','Interactive Gas Process Analyzer','Configure the piston-cylinder gas system, select a thermodynamic process, run the live P–V demonstration, determine the final state and energy quantities, and provide engineering interpretation using Chapter 3 relations.','Interactive Gas Process',10),
      ('Q2-B','Interactive Combustion & Air Requirement Analyzer','Operate a virtual fuel burner/combustion chamber. Select a fuel, determine the oxygen and theoretical air requirement from the fuel composition, compare supplied air with theoretical air, run combustion, and interpret whether the combustion condition is sufficient.','Interactive Combustion Analysis',10),
      ('Q3-B','Interactive Gas Law Laboratory','Use the virtual gas-law laboratory to investigate Boyle’s law, Charles’ law or the combined gas law. Configure the gas state, run the experiment, observe the live P–V, V–T and P–T behaviour, determine the final state and interpret the result.','Interactive Gas Law Laboratory',10),
      ('Q4-B','Interactive Steam Property & Dryness Analyzer','Operate the virtual steam vessel, set the steam condition, identify the phase region, determine dryness fraction where applicable and obtain important steam properties including h, v, u and s. Interpret the steam condition for engineering use.','Interactive Steam Property Laboratory',10)
    ]
    for newq in core:
        if not c.execute('select 1 from questions where code=?',(newq[0],)).fetchone():
            c.execute('insert into questions(code,title,prompt,type,marks) values(?,?,?,?,?)',newq)
        else:
            c.execute('update questions set title=?, prompt=?, type=?, marks=? where code=?',(newq[1],newq[2],newq[3],newq[4],newq[0]))
    # Remove legacy inactive questions from the selectable bank only by giving them a legacy prefix.
    c.execute('update questions set title="[Legacy] " || title where code in ("Q004","Q005") and title not like "[Legacy]%"')
    c.commit(); c.close()
init()

def login_required(role=None):
    def deco(f):
        @wraps(f)
        def w(*a,**kw):
            if not session.get('uid'): return redirect(url_for('login'))
            if role and session.get('role')!=role: return redirect(url_for('index'))
            if session.get('role')=='student':
                c=db(); r=c.execute('select active from users where id=?',(session['uid'],)).fetchone(); c.close()
                if not r or int(r['active'] or 0)==0:
                    session.clear(); return render_template('login.html',error='Exam access has been disabled by the examiner.')
            return f(*a,**kw)
        return w
    return deco

@app.route('/')
def index():
    if session.get('role')=='examiner': return redirect(url_for('examiner'))
    if session.get('role')=='student': return redirect(url_for('student'))
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        u=request.form['username'].strip(); p=request.form['password']
        c=db(); r=c.execute('select * from users where username=? and password=?',(u,p)).fetchone(); c.close()
        if r and int(r['active'] if r['active'] is not None else 1)==0:
            return render_template('login.html',error='Exam access has been disabled by the examiner.')
        if r:
            session.update(uid=r['id'],role=r['role'],name=r['name'],enrollment=r['enrollment'],paper=(r['paper'] or 'A'))
            return redirect(url_for('index'))
        return render_template('login.html',error='Invalid login')
    return render_template('login.html')

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))

@app.route('/examiner',methods=['GET','POST'])
@login_required('examiner')
def examiner():
    c=db(); exam=c.execute('select * from exams order by id limit 1').fetchone()
    if request.method=='POST':
        action=request.form.get('action','enroll')
        if action=='enroll':
            name=request.form.get('name','').strip(); enrollment=request.form.get('enrollment','').strip(); password=request.form.get('password') or 'student123'
            paper=(request.form.get('paper') or 'A').upper()
            try:
                cur=c.execute('insert into users(username,password,role,name,enrollment,paper,active) values(?,?,?,?,?,?,1)',(enrollment,password,'student',name,enrollment,paper)); sid=cur.lastrowid
                codes=['Q2-A','Q3-A','Q4-A'] if paper=='A' else ['Q2-B','Q3-B','Q4-B']
                for i,code in enumerate(codes,1):
                    q=c.execute('select * from questions where code=?',(code,)).fetchone()
                    if q:
                        cur=c.execute('insert into assignments(exam_id,student_id,task_no,question_id,marks) values(?,?,?,?,?)',(exam['id'],sid,i,q['id'],q['marks']))
                        c.execute('insert into answers(assignment_id) values(?)',(cur.lastrowid,))
                c.commit()
            except sqlite3.IntegrityError: c.rollback()
        elif action=='toggle_access':
            sid=int(request.form.get('student_id')); current=c.execute('select active from users where id=? and role="student"',(sid,)).fetchone()
            if current:
                c.execute('update users set active=? where id=?',(0 if int(current['active'] or 0) else 1,sid)); c.commit()
        elif action=='save_marks':
            sid=int(request.form.get('student_id'))
            for aid in request.form.getlist('assignment_id'):
                val=request.form.get('mark_'+aid,'').strip(); note=request.form.get('note_'+aid,'').strip()
                try: marks=float(val) if val!='' else None
                except ValueError: marks=None
                if marks is not None:
                    qmax=c.execute('select marks from assignments where id=? and student_id=?',(int(aid),sid)).fetchone()
                    if qmax: marks=max(0,min(float(qmax['marks']),marks))
                c.execute('update assignments set awarded_marks=?, evaluation_note=? where id=? and student_id=?',(marks,note,int(aid),sid))
            c.commit()
    students=c.execute("""select u.*, count(a.id) tasks, sum(case when a.status='SUBMITTED' then 1 else 0 end) submitted,
        sum(coalesce(a.awarded_marks,0)) total_awarded
        from users u left join assignments a on a.student_id=u.id where u.role='student' group by u.id order by u.id""").fetchall()
    student_details={st['id']:c.execute("""select a.id,a.task_no,a.status,a.submitted_at,a.marks,a.awarded_marks,a.evaluation_note,q.code,q.title from assignments a join questions q on q.id=a.question_id where a.student_id=? order by a.task_no""",(st['id'],)).fetchall() for st in students}
    questions=c.execute('select * from questions where code in ("Q2-A","Q3-A","Q4-A","Q2-B","Q3-B","Q4-B") order by code').fetchall(); c.close()
    return render_template('examiner.html',exam=exam,students=students,questions=questions,student_details=student_details)

@app.route('/student', methods=['GET','POST'])
@login_required('student')
def student():
    c=db(); exam=c.execute('select * from exams limit 1').fetchone()
    st=c.execute('select * from users where id=? and role="student"',(session['uid'],)).fetchone()
    if not st['exam_started_at']:
        c.execute('update users set exam_started_at=datetime("now") where id=?',(session['uid'],)); c.commit()
        st=c.execute('select * from users where id=?',(session['uid'],)).fetchone()
    if request.method=='POST' and request.form.get('action')=='final_submit' and int(st['paper_final_submitted'] or 0)==0:
        rows=c.execute('select a.id,a.status,an.answer,an.screenshot_path from assignments a join answers an on an.assignment_id=a.id where a.student_id=? order by a.task_no',(session['uid'],)).fetchall()
        for r in rows:
            ans=normalize_final_answer(r['answer'])
            shot=r['screenshot_path'] or ''
            if not shot: shot=make_answer_snapshot(r['id'], ans, 'FINAL PAPER SUBMISSION')
            c.execute('update answers set answer=?,locked=1,updated_at=datetime("now"),screenshot_path=? where assignment_id=?',(ans,shot,r['id']))
            c.execute('update assignments set status="SUBMITTED",submitted_at=coalesce(submitted_at,datetime("now")) where id=?',(r['id'],))
        c.execute('update users set paper_final_submitted=1,final_submitted_at=datetime("now") where id=?',(session['uid'],))
        c.commit()
        st=c.execute('select * from users where id=?',(session['uid'],)).fetchone()
    tasks=c.execute('''select a.*,q.code,q.title,q.prompt,q.type,q.marks,an.answer,an.locked
        from assignments a join questions q on q.id=a.question_id join answers an on an.assignment_id=a.id
        where a.student_id=? order by a.task_no''',(session['uid'],)).fetchall(); c.close()
    return render_template('student.html',exam=exam,tasks=tasks,paper=session.get('paper','A'),student=st)

@app.route('/task/<int:aid>',methods=['GET','POST'])
@login_required('student')
def task(aid):
    c=db(); st=c.execute('select * from users where id=? and role="student"',(session['uid'],)).fetchone()
    row=c.execute('''select a.*,q.*,an.answer,an.locked,an.screenshot_path from assignments a join questions q on q.id=a.question_id join answers an on an.assignment_id=a.id where a.id=? and a.student_id=?''',(aid,session['uid'])).fetchone()
    if not row: c.close(); return redirect(url_for('student'))
    if int(st['paper_final_submitted'] or 0)==1 or row['status']=='SUBMITTED':
        c.close(); return redirect(url_for('student'))
    if request.method=='POST':
        action=request.form.get('action'); answer=request.form.get('answer',''); screenshot=request.form.get('screenshot','')
        if action in ('save','lock') and not row['locked']:
            shot_path=row['screenshot_path'] or ''
            if screenshot.startswith('data:image/'): shot_path=save_data_image(screenshot, aid)
            c.execute('update answers set answer=?,updated_at=datetime("now"),locked=?,screenshot_path=? where assignment_id=?',(answer,1 if action=='lock' else 0,shot_path,aid))
        elif action=='unlock':
            c.execute('update answers set locked=0,updated_at=datetime("now") where assignment_id=?',(aid,))
        elif action=='submit':
            ans=normalize_final_answer(answer if answer.strip() else row['answer'])
            shot_path=row['screenshot_path'] or ''
            if screenshot.startswith('data:image/'): shot_path=save_data_image(screenshot, aid)
            if not shot_path: shot_path=make_answer_snapshot(aid, ans, 'TASK SUBMITTED')
            c.execute('update answers set answer=?,locked=1,updated_at=datetime("now"),screenshot_path=? where assignment_id=?',(ans,shot_path,aid))
            c.execute('update assignments set status="SUBMITTED",submitted_at=datetime("now") where id=?',(aid,))
        c.commit()
        if action=='submit': c.close(); return redirect(url_for('student'))
        row=c.execute('''select a.*,q.*,an.answer,an.locked,an.screenshot_path from assignments a join questions q on q.id=a.question_id join answers an on an.assignment_id=a.id where a.id=?''',(aid,)).fetchone()
    c.close()
    if row['code']=='Q2-A': return render_template('task_fuel.html',task=row)
    if row['code']=='Q3-A': return render_template('task_gas.html',task=row)
    if row['code']=='Q4-A': return render_template('task_boiler.html',task=row)
    if row['code']=='Q2-B': return render_template('task_combustion.html',task=row)
    if row['code']=='Q3-B': return render_template('task_gaslaw.html',task=row)
    if row['code']=='Q4-B': return render_template('task_steam.html',task=row)
    return render_template('task.html',task=row)

def normalize_final_answer(raw):
    import json
    if raw is None or not str(raw).strip(): return 'NIL'
    try:
        data=json.loads(raw)
        def clean(v):
            if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
            if isinstance(v,list): return [clean(x) for x in v]
            if v is None or (isinstance(v,str) and not v.strip()): return 'NIL'
            return v
        return json.dumps(clean(data),ensure_ascii=False)
    except Exception:
        return raw if str(raw).strip() else 'NIL'

def save_data_image(data_url, aid):
    try:
        import base64, re
        m=re.match(r'data:image/[^;]+;base64,(.*)', data_url or '', re.S)
        if not m: return ''
        raw=base64.b64decode(m.group(1)); d=os.path.join(DATA_DIR,'screenshots'); os.makedirs(d,exist_ok=True)
        path=os.path.join(d,f'assignment_{aid}.jpg'); open(path,'wb').write(raw); return path
    except Exception: return ''

def make_answer_snapshot(aid, answer, label):
    try:
        from PIL import Image, ImageDraw, ImageFont
        d=os.path.join(DATA_DIR,'screenshots'); os.makedirs(d,exist_ok=True); path=os.path.join(d,f'assignment_{aid}.jpg')
        W,H=1200,700; im=Image.new('RGB',(W,H),'white'); draw=ImageDraw.Draw(im)
        try: bold=ImageFont.truetype('DejaVuSans-Bold.ttf',28); normal=ImageFont.truetype('DejaVuSans.ttf',22); small=ImageFont.truetype('DejaVuSans.ttf',18)
        except: bold=normal=small=None
        draw.rectangle((0,0,W,82),fill='#312e81'); draw.text((35,22),'PLM MESA EXAMINATION',fill='white',font=bold)
        draw.text((35,105),'FINAL ANSWER SNAPSHOT',fill='#be185d',font=bold); draw.text((35,150),label,fill='#64748b',font=small)
        y=205
        for line in (answer or 'NIL').splitlines():
            if y>640: break
            draw.rounded_rectangle((35,y-6,W-35,y+38),radius=8,fill='#f8fafc',outline='#dbe4f0'); draw.text((52,y+2),line[:105],fill='#172033',font=normal); y+=52
        im.save(path,'JPEG',quality=88); return path
    except Exception: return ''

def answer_sections(code, raw):
    import json
    try: data=json.loads(raw or '')
    except Exception: return [('Student response', raw or 'NIL')]
    out=[]
    if code=='Q2-A':
        for i in range(1,11):
            out.append((f'Application {i}', ''))
            for k,label in [('category','Fuel category'),('fuel','Selected fuel'),('reason','Engineering reason')]:
                v=data.get(f'app{i}_{k}',{})
                if isinstance(v,dict): v=v.get('value','')
                out.append((label,str(v or 'NIL')))
    elif code=='Q3-A':
        for k,label in [('process_answer','Selected process'),('q3_process_reason','Process & engineering reason'),('q3_final_state','Final state calculation'),('q3_energy','Energy analysis'),('q3_interpretation','P-V & engineering interpretation')]:
            v=data.get(k,{})
            if isinstance(v,dict): v=v.get('value','')
            out.append((label,str(v or 'NIL')))
        sim=data.get('simulator')
        if sim: out.append(('Simulator configuration',', '.join(f'{k}: {v}' for k,v in sim.items() if v not in ('',None))))
    elif isinstance(data,dict):
        for k,v in data.items():
            if isinstance(v,dict): v=v.get('value','')
            out.append((k.replace('_',' ').title(),str(v or 'NIL')))
    else: out=[('Student response',raw or 'NIL')]
    return out

@app.route('/examiner/student/<int:sid>/pdf')
@login_required('examiner')
def student_pdf(sid):
    from io import BytesIO
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image as RLImage, KeepTogether
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER
    from xml.sax.saxutils import escape
    c=db(); st=c.execute('select * from users where id=? and role="student"',(sid,)).fetchone()
    if not st: c.close(); return redirect(url_for('examiner'))
    rows=c.execute("""select a.*,q.code,q.title,q.type,an.answer,an.locked,an.screenshot_path from assignments a join questions q on q.id=a.question_id join answers an on an.assignment_id=a.id where a.student_id=? order by a.task_no""",(sid,)).fetchall(); c.close()
    if not all(r['status']=='SUBMITTED' for r in rows): return redirect(url_for('examiner'))
    buf=BytesIO()
    def page_decor(canvas, doc):
        from reportlab.lib.pagesizes import A4 as _A4
        w,hp=_A4
        canvas.saveState()
        canvas.setFillColor(colors.HexColor('#f5f3ff')); canvas.rect(0,0,w,hp,fill=1,stroke=0)
        canvas.setFillColor(colors.HexColor('#312e81')); canvas.rect(0,hp-24,w,24,fill=1,stroke=0)
        canvas.setFillColor(colors.HexColor('#db2777')); canvas.rect(0,0,w,8,fill=1,stroke=0)
        canvas.setFillColor(colors.HexColor('#64748b')); canvas.setFont('Helvetica',7.5); canvas.drawRightString(w-36,16,f'PLM MESA · Page {doc.page}')
        canvas.restoreState()
    doc=SimpleDocTemplate(buf,pagesize=A4,rightMargin=36,leftMargin=36,topMargin=42,bottomMargin=30)
    styles=getSampleStyleSheet(); title=ParagraphStyle('title',parent=styles['Title'],alignment=TA_CENTER,textColor=colors.HexColor('#312e81'),fontSize=20,spaceAfter=8); h=ParagraphStyle('h',parent=styles['Heading2'],textColor=colors.HexColor('#4338ca'),fontSize=15,spaceBefore=10,spaceAfter=6);
    body=ParagraphStyle('body',parent=styles['BodyText'],fontSize=9.5,leading=13,spaceAfter=5); shot=ParagraphStyle('shot',parent=body,textColor=colors.HexColor('#be185d'),fontSize=10,leading=12,spaceAfter=5)
    story=[Paragraph('PLM MESA EXAMINATION',title),Paragraph('<b>Mechanical Engineering Department</b> | 1st Sem B.Tech. | Proficient Learning Method | Mid Exam 2026',body),Spacer(1,6)]
    info=[[Paragraph('<b>Student</b>',body),Paragraph(escape(st['name'] or ''),body)],[Paragraph('<b>Enrollment</b>',body),Paragraph(escape(st['enrollment'] or ''),body)],[Paragraph('<b>Question Paper</b>',body),Paragraph('Paper '+escape(st['paper'] or 'A'),body)]]
    t=Table(info,colWidths=[110,390]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),colors.HexColor('#eef2ff')),('BOX',(0,0),(-1,-1),.5,colors.HexColor('#c7d2fe')),('INNERGRID',(0,0),(-1,-1),.25,colors.HexColor('#e5e7eb')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7)])); story += [t,Spacer(1,12)]
    for idx,r in enumerate(rows):
        story.append(Paragraph(f'{r["code"]} — {escape(r["title"])}',h))
        story.append(Paragraph(f'Status: {r["status"]} &nbsp;&nbsp; Submitted: {escape(str(r["submitted_at"] or "—"))} &nbsp;&nbsp; Awarded marks: {escape(str(r["awarded_marks"] if r["awarded_marks"] is not None else "Not evaluated"))} / {r["marks"]}',body))
        for label,val in answer_sections(r['code'],r['answer']):
            if val=='': story.append(Paragraph(f'<b>{escape(label)}</b>',body))
            else: story.append(Paragraph(f'<b>{escape(label)}:</b> {escape(val).replace(chr(10),"<br/>")}',body))
        if r['screenshot_path'] and os.path.exists(r['screenshot_path']):
            story.append(Spacer(1,8))
            story.append(Paragraph('📸 FINAL SAVED-ANSWER SCREENSHOT', shot))
            try:
                from PIL import Image as PILImage
                src=PILImage.open(r['screenshot_path']).convert('RGB')
                # Split tall task screenshots into readable PDF pages instead of shrinking them.
                max_w_px=1180; max_h_px=1500
                if src.width > max_w_px:
                    ratio=max_w_px/src.width; src=src.resize((max_w_px,int(src.height*ratio)))
                slice_dir=os.path.join(DATA_DIR,'pdf_slices',str(r['id'])); os.makedirs(slice_dir,exist_ok=True)
                paths=[]
                for n,top in enumerate(range(0,src.height,max_h_px),1):
                    bottom=min(top+max_h_px,src.height)
                    part=src.crop((0,top,src.width,bottom))
                    sp=os.path.join(slice_dir,f'slice_{n}.jpg'); part.save(sp,'JPEG',quality=88); paths.append(sp)
                for n,sp in enumerate(paths,1):
                    im=RLImage(sp)
                    maxw=520
                    scale=maxw/im.imageWidth
                    im.drawWidth=maxw; im.drawHeight=im.imageHeight*scale
                    story.append(im)
                    if n < len(paths): story.append(PageBreak())
            except Exception as e:
                story.append(Paragraph('Screenshot could not be rendered: '+escape(str(e)),body))
        if r['evaluation_note']: story.append(Paragraph(f'<b>Examiner note:</b> {escape(r["evaluation_note"])}',body))
        if idx<len(rows)-1: story.append(PageBreak())
    total=sum((r['awarded_marks'] or 0) for r in rows); maxm=sum(r['marks'] for r in rows); story += [Spacer(1,12),Paragraph(f'<b>Total Awarded: {total:g} / {maxm}</b>',h)]
    doc.build(story,onFirstPage=page_decor,onLaterPages=page_decor); buf.seek(0); return send_file(buf,as_attachment=True,download_name=f'{st["enrollment"]}_PLM_MESA_Exam.pdf',mimetype='application/pdf')

@app.route('/boiler-model')
@login_required('student')
def boiler_model(): return send_from_directory(os.path.join(BASE,'static'),'Boiler_Working_Model_PFL_V2.html')

if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=False)
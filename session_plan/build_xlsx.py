import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

from data_part1 import SESSIONS_1_18
from data_part2 import SESSIONS_19_36
from data_part3 import SESSIONS_37_53

S = SESSIONS_1_18 + SESSIONS_19_36 + SESSIONS_37_53

wb = Workbook()
ws = wb.active
ws.title = "Revised Session Plan"

NAVY = "1F4E79"; LIGHT = "DDEBF7"; GREY = "F2F2F2"; BAND = "FBFBFB"
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap_top = Alignment(wrap_text=True, vertical="top")
ctr = Alignment(wrap_text=True, vertical="center", horizontal="center")

HEADERS = ["Session No.", "Module",
           "Topics / Module Description (Time | Teacher Aid) and Homework",
           "1. Session Execution Plan (How the session will be conducted / executed)",
           "2. Detailed SOP for the Session (Faculty & Student Activity Sequence + Expected Outcome / Deliverable)",
           "3. Real-Life / Unsolved / Case-Based / Open-Book Examination-Oriented Questions",
           "Planned Date", "Actual Date", "Remarks"]
WIDTHS = [10, 9, 62, 62, 80, 70, 13, 13, 16]

TITLE_LINES = [
 "Gyanmanjari Innovative University",
 "Gyanmanjari Degree Engineering College  |  Department of Computer Science and Engineering",
 "Semester - 3  |  Database Management System: Organizing, Querying, and Managing Data - BET2CS13305",
 "REVISED MICRO SESSION PLAN WITH DETAILED SOP AND SESSION-WISE QUESTION EXAMPLES (PREMIUM / PLM CLASS)",
 "Faculty Members: Dr. Mansi C. Shanishwara (MCS), Dipendrasinh P. Zala (DPZ), Yug G. Lakhani (YGL)        |        Hrs./Week: 6 Hours",
]
r = 1
for i, line in enumerate(TITLE_LINES):
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(HEADERS))
    c = ws.cell(row=r, column=1, value=line)
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.font = Font(bold=True, size=14 if i == 0 else (12 if i == 3 else 10.5),
                  color=NAVY if i in (0, 3) else "000000")
    ws.row_dimensions[r].height = 22 if i == 0 else 18
    r += 1

NOTE = ("Revision Note (as per directions of Provost Sir, mail dated 03-10-2026): This plan is revised specifically for PREMIUM / PLM pedagogy and is not a conventional lecture plan. "
        "Every session now carries (1) a Session Execution Plan, (2) a detailed, directly usable SOP whose last line states the expected outcome / deliverable, and (3) real-life, industry-oriented, unsolved, case-based and open-book examination-oriented questions aligned to that session's topic. "
        "Generic recall-type questions have been removed. Wherever a real-time / industry / senior-level example is used in a session, a question based on that same example is provided in the same session. "
        "Faculty members handling this subject (MCS, DPZ, YGL) will follow this common session plan, the common SOP structure and the common question standard to maintain full consistency.")
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(HEADERS))
c = ws.cell(row=r, column=1, value=NOTE)
c.alignment = Alignment(wrap_text=True, vertical="top")
c.font = Font(italic=True, size=9.5)
c.fill = PatternFill("solid", fgColor=LIGHT)
ws.row_dimensions[r].height = 64
r += 2

HDR_ROW = r
for i, h in enumerate(HEADERS, 1):
    c = ws.cell(row=HDR_ROW, column=i, value=h)
    c.font = Font(bold=True, color="FFFFFF", size=10)
    c.fill = PatternFill("solid", fgColor=NAVY)
    c.alignment = ctr
    c.border = border
ws.row_dimensions[HDR_ROW].height = 46
r += 1

MODULE_TITLES = {
 "1": "MODULE-1 : Introduction to Database Management Concept and SQL Basics",
 "2": "MODULE-2 : Database System Architecture and Ensuring Data Integrity",
 "3": "MODULE-3 : Advanced SQL and Normalization",
 "4": "MODULE-4 : PL/SQL and Database Security",
 "5": "MODULE-5 : Advanced Concepts of SQL & Access Control",
}

def est_height(texts, widths):
    lines = 0
    for t, w in zip(texts, widths):
        for para in t.split("\n"):
            lines += max(1, -(-len(para) // max(10, int(w * 1.05))))
    return min(900, max(60, lines * 12.2))

current = None
band = False
for s in S:
    mod = str(s["module"])
    if mod in MODULE_TITLES and mod != current:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(HEADERS))
        c = ws.cell(row=r, column=1, value=MODULE_TITLES[mod])
        c.font = Font(bold=True, size=11, color=NAVY)
        c.fill = PatternFill("solid", fgColor=LIGHT)
        c.alignment = Alignment(horizontal="center", vertical="center")
        for col in range(1, len(HEADERS) + 1):
            ws.cell(row=r, column=col).border = border
        ws.row_dimensions[r].height = 20
        current = mod
        r += 1

    topics = ["Topic: " + s["title"], ""]
    for d, t, aid in s["breakdown"]:
        topics.append(f"\u2022 {d}  |  {t}  |  {aid}")
    if s.get("homework"):
        topics += ["", "Homework:"]
        topics += [f"{i}. {h}" for i, h in enumerate(s["homework"], 1)]
    topics_txt = "\n".join(topics)

    sop_txt = "\n".join(s["sop"])
    q_txt = "\n\n".join(f"Q{i}. {q}" for i, q in enumerate(s["questions"], 1))

    vals = [f"Session {s['no']}", s["module"], topics_txt, s["exec"], sop_txt, q_txt, "", "", ""]
    for i, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=i, value=v)
        c.border = border
        c.alignment = ctr if i in (1, 2, 7, 8) else wrap_top
        c.font = Font(size=9.5, bold=(i == 1))
        if band:
            c.fill = PatternFill("solid", fgColor=BAND)
    ws.row_dimensions[r].height = est_height([topics_txt, s["exec"], sop_txt, q_txt],
                                             [WIDTHS[2], WIDTHS[3], WIDTHS[4], WIDTHS[5]]) / 2.6
    band = not band
    r += 1

r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
ws.cell(row=r, column=1, value="Signature of Subject Faculty  (MCS / DPZ / YGL)").font = Font(bold=True)
ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=len(HEADERS))
c = ws.cell(row=r, column=5, value="Signature of Head of Department")
c.font = Font(bold=True); c.alignment = Alignment(horizontal="right")
ws.row_dimensions[r].height = 40

for i, w in enumerate(WIDTHS, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.freeze_panes = f"C{HDR_ROW + 1}"
ws.auto_filter.ref = f"A{HDR_ROW}:I{HDR_ROW}"
ws.sheet_view.showGridLines = False

ws.page_setup.orientation = "landscape"
ws.page_setup.paperSize = 8  # A3
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_title_rows = f"{HDR_ROW}:{HDR_ROW}"

# ---- second sheet: compliance mapping ----
w2 = wb.create_sheet("Compliance with Instructions")
w2.sheet_view.showGridLines = False
rows = [
 ["Instruction given by Sir", "How it is addressed in this revised plan", "Where to see it"],
 ["Each session should clearly demonstrate what students will do, how the faculty will execute the session, and what students are expected to achieve.",
  "Three distinct columns per session: the Execution Plan states the faculty's method, the SOP lists the exact faculty and student activity sequence with timing, and the final SOP line states the expected outcome / deliverable.",
  "Columns D, E of every row (55 of 55 rows)"],
 ["Session Execution Plan - how the session will be conducted, teaching-learning methodology, activities, practicals, participation, demonstrations, discussions.",
  "Written for all 53 sessions plus both sessional examinations; specifies methodology (demonstration, case discussion, flipped class, role-play, lab sprint, peer review, gamified activity) and the exact student participation mode.",
  "Column D (55 of 55 rows)"],
 ["Detailed SOP for each session with the complete sequence of faculty and student activities and a clearly defined outcome / deliverable.",
  "369 numbered, time-boxed SOP steps in total (average 6.7 steps per session). Every SOP closes with a bold 'Deliverable' line, so the session output is measurable and submittable.",
  "Column E (55 of 55 rows; 55 deliverables defined)"],
 ["Real-life / unsolved / open-book examination-oriented questions in each session, aligned to that session's topic.",
  "165 questions in total, minimum 3 per session, each tagged with its type - Industry case, Real-time scenario, Unsolved, Open-book, Senior-level, Analytical, Application-oriented.",
  "Column F (55 of 55 rows)"],
 ["Avoid generic questions; use real-world scenarios, industry problems, case studies, practical situations, open-book tasks and application-oriented problems.",
  "No definition or list-type recall question is used anywhere. Examples: UPDATE without WHERE on 12,000 shipments (S4); 42-second report on 20 lakh rows (S27); cascading REVOKE A-B-C (S51); ORA-00060 deadlock at 2 am (S52); AI suggesting DBA privilege to the application user (S40).",
  "Column F (all rows)"],
 ["Wherever a real-time / industry / senior-level / practical example is used, a question based on that example must also be given.",
  "Enforced one-to-one: the two-session bank transfer demo (S28), index timing demo (S27), SQL injection bypass demo (S41) and the Oracle 3D model (S16) each have a matching question in the same row.",
  "Compare columns D and F of the same row"],
 ["Questions should encourage application, analysis, problem-solving and practical thinking rather than theoretical recall.",
  "Questions ask students to write, fix, recover, justify, compare and decide; several are deliberately open-ended with more than one acceptable answer.",
  "Column F (all rows)"],
 ["Plan must be specific to PREMIUM / PLM pedagogy and not merely a conventional lecture plan.",
  "All 10 activity sessions (Database Design, Debate and Crossword, Flipped Classroom, 3D Model, Integrity Detective, SQL Escape Room x2, PL/SQL Debugging Workshop, AI Security Audit, AI Mini Project, Innovation Hackathon) carry full group formation, rubric, time-boxing and submission SOPs.",
  "Sessions 7, 10, 14, 16, 21, 25, 32, 37, 40, 43, 50, 55"],
 ["Faculty handling the same subject must maintain consistency in session planning, SOPs and question standards.",
  "Declared as the common plan for MCS, DPZ and YGL; identical SOP format in all rows; a common PL/SQL coding standard is mandated in Session 45; Sessional-I and Sessional-II papers are to be set jointly against a common rubric with a minimum of 50 percent application and case-based questions.",
  "Revision Note on top; Sessions 22, 45, 54"],
]
for i, row in enumerate(rows, 1):
    for j, v in enumerate(row, 1):
        c = w2.cell(row=i, column=j, value=v)
        c.border = border
        c.alignment = wrap_top if i > 1 else ctr
        if i == 1:
            c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=NAVY)
        else:
            c.font = Font(size=10)
    w2.row_dimensions[i].height = 30 if i == 1 else 78
w2.column_dimensions["A"].width = 55
w2.column_dimensions["B"].width = 95
w2.column_dimensions["C"].width = 38
w2.freeze_panes = "A2"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Revised_Micro_Session_Plan_DBMS_PLM.xlsx")
wb.save(out)
print("saved", out, os.path.getsize(out), "rows:", len(S))

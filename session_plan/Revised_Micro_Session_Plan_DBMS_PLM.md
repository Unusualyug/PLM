# Revised Micro Session Plan - DBMS (BET2CS13305) | PREMIUM / PLM, Semester-3
**Gyanmanjari Innovative University | Gyanmanjari Degree Engineering College | Dept. of Computer Science & Engineering**
**Faculty: MCS / DPZ / YGL  |  Hrs./Week: 6**

> Revised as per Provost Sir's directions (mail dated 03-10-2026): every session now carries a Session Execution Plan, a detailed SOP with a defined deliverable, and real-life / unsolved / open-book examination-oriented questions.

## Session 1 (Module 1) - Introduction to DBMS and its Terminologies

**Topics / Time / Teacher aid**

- Subject Introduction and Evaluation Methodology | 20 Min | Explanation, Smartboard
- Oracle Installation | 40 Min | Smartboard, Laptop
- Introduction of DBMS | 10 Min | PPT, Smartboard
- Introduction, Data, Information | 15 Min | PPT, Smartboard
- Data Items, Fields, Records, Files | 20 Min | PPT, Smartboard
- Data Dictionary, Metadata, Database, Database Systems | 15 Min | PPT, Smartboard
- Revision | 10 Min | Discussion

**1. Session Execution Plan**

Session starts with an interactive orientation on the subject, PLM evaluation pattern (SEE, CCE, ALA, Sessional) and the industry relevance of DBMS. Faculty demonstrates live Oracle 21c XE + SQL*Plus installation on the smartboard while students mirror the same on their own laptops (learning-by-doing). Concepts of data vs information are built using a live, relatable dataset - the class attendance register and a Swiggy/Zomato order slip - converted step by step into fields, records and files. Metadata and data dictionary are explained by opening an actual table description in SQL*Plus. Methodology: demonstration + guided hands-on + question-answer + concept mapping on board.

**2. Detailed SOP**

- Step 1 (05 min): Faculty takes attendance, states the session outcome on the board: 'By the end of this session every student will have a working Oracle instance and will be able to classify data, information and metadata for a real dataset.'
- Step 2 (20 min): Faculty explains syllabus, module split, PLM evaluation methodology (SEE-1 to SEE-5, CCE, ALA, Sessional-I & II) and the practical/assignment submission process on ERP.
- Step 3 (40 min): Faculty demonstrates Oracle XE installation step-by-step; students install in parallel; faculty and class CR move around to resolve errors (port conflict, listener, password policy). Checkpoint: every student runs CONNECT system/<pwd> and gets 'Connected'.
- Step 4 (25 min): Faculty shows a printed Zomato order receipt and the college attendance sheet, asks students to identify raw data and derived information; builds the Data to Information to Knowledge chain on the smartboard.
- Step 5 (20 min): Faculty maps the same receipt into data items, fields, records and a file; then runs DESC and SELECT * FROM USER_TAB_COLUMNS in SQL*Plus to show that the metadata itself is stored as data.
- Step 6 (10 min): Rapid-fire oral revision; students write a 3-line reflection 'one thing I installed, one thing I understood, one doubt'.
- Deliverable: Working Oracle installation screenshot (uploaded to ERP) + handwritten data dictionary of any one real-life document.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A local medical store keeps a paper bill containing bill no., date, customer name, medicine name, batch no., expiry date, quantity and amount. Identify which of these are data items, which form a record and what constitutes the file. Justify why expiry date must be stored as DATE and not as text. (Open-book)
2. Zomato stores crores of orders every month. Explain with a concrete example what 'information' the business extracts from this raw order data that a restaurant owner would actually pay for. Write the two columns you would need for each insight.
3. Your senior at an IT company says 'we never hard-code column names, we read them from the data dictionary'. Using USER_TAB_COLUMNS, write the query you would run to list every column name and datatype of a table whose structure you have never seen. (Unsolved/practical)

**Homework**

1. Complete Oracle installation if pending and upload the screenshot.
2. Prepare the data dictionary of a Student table.
3. Prepare the data dictionary of an Employee table.

---

## Session 2 (Module 1) - DBMS Purpose and Applications, Oracle Database and RDBMS Architecture

**Topics / Time / Teacher aid**

- Database management system: Introduction, Purpose, Applications | 15 Min | PPT, Smartboard
- Introduction to Oracle Database, RDBMS Architecture | 10 Min | PPT, Smartboard
- Explanation of SEE-1 and CCE of Module 1 - student instructions | 15 Min | Explanation
- Practical 1: SQL queries for creating and describing tables (CREATE, DESC) | 15 Min | SQL Plus
- Practical 9: Create student table with common data types using DDL | 15 Min | SQL Plus
- Practical Assignment-1: Problem solving and practice (Q1-Q5) | 40 Min | SQL Plus
- Revision | 15 Min | Discussion

**1. Session Execution Plan**

Session is executed as a problem-first class. Faculty opens with a real failure story - a college that maintained results in Excel and lost consistency during re-evaluation - and asks students to list the problems (redundancy, inconsistency, concurrent access, security, atomicity). Each problem is then mapped live to the DBMS feature that solves it. RDBMS architecture is explained using a drawn client-server diagram and verified practically by showing SQL*Plus (client) talking to the Oracle instance (server). Second half is a fully hands-on lab where every student creates and describes tables and attempts Assignment-1 Q1-Q5 on their own machine while faculty does bench-wise verification.

**2. Detailed SOP**

- Step 1 (05 min): State outcome - 'student will justify why a business must move from file system to DBMS and will independently create and describe tables in Oracle.'
- Step 2 (15 min): Case discussion on Excel-based result management failure; students list drawbacks in pairs; faculty consolidates them on board and maps each to a DBMS purpose.
- Step 3 (10 min): Faculty explains Oracle client-server RDBMS architecture with a labelled diagram; relates SQL*Plus, listener and instance to what students installed in Session 1.
- Step 4 (15 min): Faculty explains SEE-1 and CCE rubric of Module 1, submission format, deadline and ERP upload procedure. Students note it in their lab file.
- Step 5 (30 min): Guided practical - faculty demonstrates CREATE TABLE and DESC once, then students execute Practical 1 and Practical 9 independently; faculty verifies output on at least 50 percent of machines.
- Step 6 (40 min): Students solve Assignment-1 Q1-Q5 individually; faculty circulates, notes common errors (missing datatype size, reserved words) and corrects them publicly on the smartboard.
- Step 7 (15 min): Revision through 5 oral questions; doubts logged for next session.
- Deliverable: Executed Practical 1 and 9 with output pasted in the lab file; Assignment-1 Q1-Q5 solved.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A hospital currently maintains patient records in separate Excel files kept by the OPD, the lab and the pharmacy. Identify any four problems that will certainly occur, and state which specific DBMS feature removes each one. (Case-based)
2. Design and create the table structure that an e-commerce startup would need to store product details, choosing the correct Oracle datatype and size for each column. Justify why you chose NUMBER(8,2) over NUMBER for price. (Open-book)
3. Your team lead asks you to verify, without opening any design document, whether a production table ORDERS has a column for GST amount and what its datatype is. Write the exact commands you would run and explain the output you expect.

**Homework**

1. Create table EMPLOYEE with employee_id (number), employee_name (varchar2), dob (date), email (varchar2).
2. Create table DEPARTMENT with department_id, department_name, location, budget.
3. Alter EMPLOYEE to add phone_number (varchar2).
4. Rename column email in EMPLOYEE to employee_email.
5. Drop the DEPARTMENT table.

---

## Session 3 (Module 1) - Open Source vs Commercial DBMS, Data Types in Oracle, DDL Commands

**Topics / Time / Teacher aid**

- Open source and Commercial DBMS (MySQL, Oracle, DB2, SQL Server) | 10 Min | PPT, Smartboard
- Basics of SQL: Data Types in Oracle | 10 Min | PPT, Smartboard
- About SQL Commands and its types | 15 Min | PPT, Smartboard
- DDL Commands: CREATE, ALTER, DROP | 20 Min | PPT, Smartboard, SQL Plus
- Practical 2: Modifying tables using ALTER | 10 Min | SQL Plus
- Practical 3: Deleting tables using DROP | 05 Min | SQL Plus
- Practical Assignment-1: Problem solving and practice (Q6-Q14) | 35 Min | SQL Plus
- Revision | 10 Min | Discussion

**1. Session Execution Plan**

Conducted as comparison-and-demonstration session. Faculty puts a procurement scenario on the board - 'a 20-member startup must choose a database within a 2 lakh budget' - and students compare MySQL, PostgreSQL, Oracle and SQL Server on cost, support, scalability and licensing. Oracle datatypes are taught through a 'choose the right datatype' rapid activity using real columns (Aadhaar no., PIN code, salary, remarks, joining date). DDL is demonstrated live with immediate student replication, including the deliberate demonstration of a DROP mistake and the FLASHBACK/recycle bin recovery, so students understand DDL is auto-committed.

**2. Detailed SOP**

- Step 1 (05 min): Outcome stated - 'student will select an appropriate DBMS product and correct datatypes for a given business case and will apply CREATE, ALTER, DROP confidently.'
- Step 2 (10 min): Startup procurement case; students work in pairs for 4 minutes and present a one-line recommendation with justification; faculty tabulates the comparison on the smartboard.
- Step 3 (10 min): Datatype drill - faculty names a real column, students call out the datatype and size; faculty corrects misconceptions (CHAR vs VARCHAR2, NUMBER precision, DATE vs TIMESTAMP).
- Step 4 (15 min): Classification of SQL commands DDL, DML, DQL, DCL, TCL with one live example of each.
- Step 5 (20 min): Live demonstration of CREATE, ALTER (ADD, MODIFY, RENAME) and DROP; faculty drops a table deliberately and recovers it from the recycle bin to prove DDL behaviour.
- Step 6 (15 min): Students execute Practical 2 and Practical 3 on their machines; faculty verifies output.
- Step 7 (35 min): Assignment-1 Q6-Q14 solved individually; faculty resolves doubts bench-wise and notes repeated errors.
- Step 8 (10 min): Oral revision and summary of DDL syntax card pasted in the lab file.
- Deliverable: Practical 2 and 3 completed; Assignment-1 Q6-Q14 solved; one-page DBMS comparison chart.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A fintech startup expects 50,000 transactions a day and must satisfy RBI audit requirements. Recommend an open-source or commercial DBMS, giving three technical and two commercial reasons. State one risk of your own recommendation. (Industry case)
2. For a government portal you must store: Aadhaar number, PIN code, monthly income, date of application and a 500-word grievance text. Give the exact Oracle datatype with size for each and explain why NUMBER is wrong for Aadhaar and PIN code. (Open-book)
3. A junior developer ran DROP TABLE CUSTOMER on the production schema at 4 pm. Explain what exactly happened to the data and the transaction, and write the statement sequence you would use to recover the table. Also state one preventive control.

**Homework**

1. Create table DEPARTMENT with department_id, department_name, location, head_of_department.
2. Create table EXAM with exam_id, exam_name, exam_date, total_marks, course_id.
3. Alter DEPARTMENT to add contact_number (varchar2).
4. Rename exam_name in EXAM to exam_title.
5. Drop the EXAM table.

---

## Session 4 (Module 1) - DML Commands - INSERT, UPDATE, DELETE

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- DML Commands: INSERT | 15 Min | PPT, Smartboard, SQL Plus
- DML Commands: UPDATE | 10 Min | PPT, Smartboard, SQL Plus
- DML Commands: DELETE | 10 Min | PPT, Smartboard, SQL Plus
- Practical 4: Create table and insert sample data | 15 Min | SQL Plus
- Practical 8: Create Students and Employees tables with 5 fields and insert data | 15 Min | SQL Plus
- Practical 5: Inserting and updating records using INSERT, UPDATE, DELETE | 10 Min | SQL Plus
- Practical Assignment-1: Problem solving and practice (Q15-Q20) | 35 Min | SQL Plus

**1. Session Execution Plan**

Executed as a simulated data-entry operator role-play. Each student acts as a back-office executive of a courier company and must load, correct and remove shipment records using DML. Faculty demonstrates the single most important industry lesson of this session - an UPDATE or DELETE without a WHERE clause - by running it on a dummy table and showing all rows affected, then rolling it back. Students then practise insert variants (all columns, selected columns, NULL handling, INSERT with SELECT). The session is largely lab-driven with 75 minutes of continuous hands-on work.

**2. Detailed SOP**

- Step 1 (10 min): Revision of DDL through 5 oral questions; faculty states the outcome - 'student will manipulate live data safely using INSERT, UPDATE and DELETE with correct filtering.'
- Step 2 (15 min): Faculty demonstrates INSERT in three forms - all columns, selected columns, and INSERT ... SELECT - on a COURIER table created live.
- Step 3 (10 min): UPDATE demonstrated with and without WHERE; faculty shows 'rows updated' count, then ROLLBACK, and derives the rule: always SELECT before you UPDATE.
- Step 4 (10 min): DELETE demonstrated and compared with TRUNCATE and DROP in a three-column board table.
- Step 5 (40 min): Students execute Practical 4, Practical 8 and Practical 5 independently; faculty checks the row counts on each machine before signing the lab file.
- Step 6 (35 min): Assignment-1 Q15-Q20 solved individually; faculty gives a 2-minute correction talk on the two most common errors observed.
- Deliverable: Students and Employees tables populated with at least 5 valid records each, with evidence of one update and one delete operation.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A courier company's operator updated the delivery status of all 12,000 shipments instead of one because the WHERE clause was missed. Explain what you would do in the next 60 seconds if the transaction is not yet committed, and what you would do if it is already committed. Write the exact statements. (Real-time situation)
2. Write a single statement that increases the salary of all employees of the 'Sales' department by 8 percent but only for those who joined before 01-JAN-2023, and then write the SELECT you would run first to verify how many rows will be affected. (Open-book)
3. A bank must archive all accounts with zero balance that have been inactive for two years into a table OLD_ACCOUNT and then remove them from ACCOUNT. Write the complete sequence of DML statements in the correct order and explain why that order matters.

**Homework**

1. Insert 5 records into the LIBRARY table.
2. Insert 3 records into the DEPARTMENT table.
3. Update the salary of the teacher where teacher_id = 101.
4. Delete the record from COURSE where course_id = 3.
5. Update available_copies in LIBRARY where book_id = 1.

---

## Session 5 (Module 1) - DQL Commands - SELECT with WHERE and ORDER BY, Aggregate Functions

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- DQL Command: SELECT with WHERE Clause | 15 Min | PPT, Smartboard, SQL Plus
- DQL Command: SELECT with ORDER BY | 20 Min | PPT, Smartboard, SQL Plus
- Aggregate Functions - examples | 20 Min | PPT, Smartboard, SQL Plus
- Practical 6: Retrieving data using SELECT, WHERE, ORDER BY | 10 Min | SQL Plus
- Practical Assignment-1: Problem solving and practice (Q21-Q22) | 45 Min | SQL Plus

**1. Session Execution Plan**

Conducted as a 'business question to SQL query' translation workshop. Faculty writes business questions asked by a real sales manager (top 5 highest paid employees, employees who joined this quarter, average salary per city) and students translate each into SQL within a fixed time. A pre-loaded EMPLOYEE table of 25 rows is distributed as a script so that every student works on identical data and outputs can be compared instantly. Peer-checking is used: students exchange machines and verify each other's output against the expected result shown on the smartboard.

**2. Detailed SOP**

- Step 1 (10 min): Revision of DML; faculty runs the data-load script on all machines and states the outcome - 'student will convert a business requirement into a correct SELECT query with filtering and sorting.'
- Step 2 (15 min): WHERE clause with relational, logical and NULL operators demonstrated; faculty highlights the IS NULL trap (= NULL returns no rows).
- Step 3 (20 min): ORDER BY on single and multiple columns, ASC/DESC, ordering by column position and by expression; TOP-N logic shown using ROWNUM with a sorted inline view.
- Step 4 (20 min): Aggregate functions COUNT, SUM, AVG, MIN, MAX demonstrated; faculty deliberately shows COUNT(*) vs COUNT(column) difference on a column containing NULLs.
- Step 5 (10 min): Students execute Practical 6 and get the output verified.
- Step 6 (45 min): Assignment-1 Q21-Q22 plus the business-question drill; students exchange seats for peer verification in the last 10 minutes.
- Deliverable: Query sheet with 8 business questions and the student's SQL solution with output, peer-verified and signed.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The sales head of a retail chain asks: 'show me the five highest paid employees of the Surat branch, highest first'. Write the query and then explain what will change in your query if two employees have exactly the same salary at the fifth position. (Industry scenario)
2. An HR dashboard shows 'Average Salary = 42,000' but the finance team computes 38,500 from the same table. The salary column contains NULL for 12 employees. Explain the difference mathematically and write the query that reproduces each of the two values. (Case-based analysis)
3. Using the EMPLOYEE table, write queries to answer: total payroll cost per department, the department with the maximum headcount, and the number of employees who have no manager assigned. State which of these cannot be answered by COUNT(*) and why. (Open-book)

**Homework**

1. Create table EMPLOYEE(emp_id, emp_name, department, salary, joining_date), add 25 records and apply Q1-Q10 insert/update/delete queries given in the original plan.

---

## Session 6 (Module 1) - DQL - ORDER BY and HAVING Clauses, Data Dictionary in Oracle

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- DQL Command: SELECT with GROUP BY, ORDER BY and HAVING Clauses | 20 Min | PPT, Smartboard, SQL Plus
- Practical 7: Aggregate functions with GROUP BY and HAVING | 10 Min | SQL Plus
- Practical Assignment-2: Problem solving and practice (Q1-Q2) | 40 Min | SQL Plus
- Use of Data Dictionary in Oracle (USER_TABLES, ALL_TABLES) | 15 Min | SQL Plus
- Complete pending assignment and homework | 20 Min | SQL Plus

**1. Session Execution Plan**

Executed as an analytics-report building session. Students are given a role - MIS executive who must produce a department-wise salary report with exceptions. The WHERE vs HAVING distinction, which is the most frequently examined concept, is taught by making students deliberately write a wrong query using WHERE with an aggregate, observing the Oracle error, and then correcting it. The data dictionary portion is executed as a discovery exercise where students explore their own schema using USER_TABLES, USER_TAB_COLUMNS and USER_CONSTRAINTS and document what they find.

**2. Detailed SOP**

- Step 1 (15 min): Revision of aggregates; outcome stated - 'student will produce grouped analytical reports and will explore schema metadata independently.'
- Step 2 (20 min): GROUP BY logic explained with a physical grouping activity (students physically group by branch), then HAVING is introduced as 'filter after grouping'; faculty shows the ORA-00934 error from using WHERE with an aggregate and corrects it.
- Step 3 (10 min): Students execute Practical 7 and verify the grouped output.
- Step 4 (40 min): Assignment-2 Q1-Q2 solved individually with faculty circulation.
- Step 5 (15 min): Data dictionary discovery - each student runs queries on USER_TABLES and USER_TAB_COLUMNS and writes down how many tables they own and which table has the most columns.
- Step 6 (20 min): Buffer slot for completing pending practicals and homework; faculty signs completed lab files.
- Deliverable: Department-wise analytical report query sheet and a schema inventory note generated from the data dictionary.

**3. Real-Life / Unsolved / Open-Book Questions**

1. An MIS executive must list only those departments whose average salary exceeds 50,000 and which have more than 3 employees, sorted by average salary descending. Write the query and explain exactly why the two conditions cannot be placed in the WHERE clause. (Open-book)
2. A manager claims 'our Pune branch has the highest total sales'. Using a SALES(branch, sales_person, amount, sale_date) table, write the queries that would either prove or disprove this claim for the current financial year, and state one way the claim could be misleading. (Analytical)
3. You join a project and get access to a schema with no documentation. Write the data dictionary queries you would run to find (i) all table names you own, (ii) all columns of the largest table, (iii) all constraints defined on it. (Practical, industry-oriented)

**Homework**

1. Create a Student table with Student_ID, Student_Name, Department, Semester, Marks and insert 10 records; then run the five retrieval/update/delete queries listed in the original plan.

---

## Session 7 (Module 1) - Database Design Activity - Design Your College Database (Group Activity)

**Topics / Time / Teacher aid**

- Group formation and problem briefing | 10 Min | Explanation
- Design a database for a college management system - identify entities, fields, records, tables | 115 Min | Database Design Activity
- Activity work submission | 05 Min | Submission

**1. Session Execution Plan**

Full activity-based learning session. Students work in groups of 3-4 as a 'database consulting team' for the college. Each group is assigned one real sub-system (Admission, Library, Examination, Hostel, Placement) so that no two groups produce the same output and the outputs can later be integrated into one college database. Groups identify entities, attributes, keys and relationships, prepare a complete data dictionary and present the structure using a chart or a Lucidchart diagram. Faculty acts as the 'client' and challenges each group with a change request during the design to test flexibility of their model.

**2. Detailed SOP**

- Step 1 (10 min): Faculty forms groups of 3-4, allots one college sub-system per group and shares the evaluation rubric (entity identification 30 percent, data dictionary 30 percent, diagram 20 percent, presentation 20 percent).
- Step 2 (25 min): Groups list all entities and attributes of their sub-system on a worksheet; faculty verifies that each group has at least 4 entities.
- Step 3 (35 min): Groups define datatypes, primary keys and foreign keys for each table and prepare a complete data dictionary in the prescribed format.
- Step 4 (20 min): Faculty visits each group as the 'client' and gives one change request (for example 'a student can now take two hostel rooms in a year'); groups modify the design and record the impact.
- Step 5 (30 min): Groups prepare the chart or diagram and a 3-minute presentation; two groups present and the class cross-questions.
- Step 6 (05 min): Submission of the data dictionary sheet and diagram on ERP with all group member names and the contribution of each.
- Deliverable: Complete data dictionary and structure diagram of one college sub-system per group, with a change-impact note.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Your group designed the Library sub-system. The college now says a single book can be issued to a student as well as reserved by another at the same time. Redesign the affected table(s) and justify the change in one paragraph. (Change-request case)
2. Identify three attributes in your college design that look like a single field but must actually be split into separate columns (for example address). Explain the practical problem that would arise at report time if they are not split. (Application-oriented)
3. Two groups designed STUDENT and FEES separately. Explain what common key must exist for the two to be integrated, and write the CREATE TABLE statement for FEES with the correct foreign key. (Open-book integration task)

**Homework**

1. Complete and upload the group data dictionary and design diagram on ERP.

---

## Session 8 (Module 1) - DDL Commands, DML Commands and Data Dictionary - Practical Session

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Practical 10: Create 5 tables and perform all DDL operations on them | 20 Min | SQL Plus
- Practical 11: Insert sample data and verify insertion | 20 Min | SQL Plus
- Practical 16: Browsing data dictionary - USER_TABLES, ALL_TABLES | 15 Min | SQL Plus
- Practical Assignment-2: Problem solving and practice (Q3-Q4) | 40 Min | SQL Plus
- Revision | 15 Min | Discussion

**1. Session Execution Plan**

Pure laboratory execution session conducted in 'build your own schema' mode. Each student implements the college sub-system designed in Session 7 as actual tables, thereby connecting design to implementation. Faculty follows a checkpoint model - students must get each practical verified before moving to the next. The data dictionary practical is executed as a self-audit where students verify their own created objects through USER_TABLES rather than by memory.

**2. Detailed SOP**

- Step 1 (15 min): Revision of DDL and DML syntax; outcome stated - 'student will implement a designed schema end-to-end and will verify it through the data dictionary.'
- Step 2 (20 min): Practical 10 - students create 5 tables from their Session 7 design and perform ADD, MODIFY, RENAME and DROP COLUMN operations. Checkpoint 1 verified by faculty.
- Step 3 (20 min): Practical 11 - insert at least 5 valid rows into each table and verify through SELECT and COUNT(*). Checkpoint 2.
- Step 4 (15 min): Practical 16 - students query USER_TABLES and ALL_TABLES, compare the two and record the difference in their lab file.
- Step 5 (40 min): Assignment-2 Q3-Q4 solved; faculty resolves individual doubts and marks the lab file.
- Step 6 (15 min): Class-level revision of the errors most frequently seen during the session.
- Deliverable: Five implemented and populated tables verified through the data dictionary, lab file signed.

**3. Real-Life / Unsolved / Open-Book Questions**

1. You created a table with 5 columns but later realise column marks must not accept negative values and column email must be unique. Write the ALTER statements and explain what will happen if the existing data already violates these rules. (Practical situation)
2. Explain the practical difference between USER_TABLES, ALL_TABLES and DBA_TABLES with one real situation in which a developer in a company would use each. (Open-book)
3. A tester reports that your INSERT 'worked' but the row is not visible to his session. Give two possible technical reasons and the exact statement that resolves the issue. (Industry-oriented)

**Homework**

1. Create a Student table with PRIMARY KEY, NOT NULL and UNIQUE constraints.
2. Insert at least 5 records, display all records, retrieve department-wise students and count the total students.

---

## Session 9 (Module 1) - DML, DDL and DQL Commands - Integrated Practical Session

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Practical 12: DML commands - insert 10 records and perform modifications | 15 Min | SQL Plus
- Practical 13: Practice DDL-create and DML-insert commands | 15 Min | SQL Plus
- Practical 14: Retrieve data using SELECT from tables | 15 Min | SQL Plus
- Practical 15: Practice SQL UPDATE and DELETE to modify data | 15 Min | SQL Plus
- Practical Assignment-2: Problem solving and practice (Q5-Q6) | 30 Min | SQL Plus
- Practical questions checking and submission | 15 Min | SQL Plus

**1. Session Execution Plan**

Consolidation lab executed as a timed 'mini sprint'. Students receive a single integrated problem statement (a canteen billing system) and must complete the full cycle - create, insert, retrieve, modify - within fixed time boxes announced by the faculty. This simulates the pace expected in the PLM sessional practical examination. Last 15 minutes are used for formal checking and submission so that no practical remains pending.

**2. Detailed SOP**

- Step 1 (15 min): Revision and announcement of the sprint rules and time boxes; outcome stated - 'student will complete a full DDL-DML-DQL cycle for a given business problem within the examination time limit.'
- Step 2 (15 min): Practical 12 executed in a strict 15-minute box; faculty announces the remaining time at 5-minute intervals.
- Step 3 (15 min): Practical 13 executed; faculty checks that constraints and datatypes are appropriate, not just syntactically valid.
- Step 4 (15 min): Practical 14 - retrieval queries of increasing difficulty; faculty displays the expected output on the smartboard for self-check.
- Step 5 (15 min): Practical 15 - UPDATE and DELETE with correct WHERE; faculty insists on a verification SELECT before and after each operation.
- Step 6 (30 min): Assignment-2 Q5-Q6 solved.
- Step 7 (15 min): Formal checking, viva of two questions per student and submission on ERP.
- Deliverable: All pending practicals of Module 1 completed, checked and submitted; sprint performance recorded in CCE.

**3. Real-Life / Unsolved / Open-Book Questions**

1. For a college canteen, create the required table(s), insert one day of sales, and then answer: which item earned the highest revenue today and which item was not sold at all. Write all statements in sequence. (Integrated practical)
2. During the sprint, a student's DELETE removed 10 rows instead of 1. Before committing, demonstrate recovery and then write the corrected statement. Explain the one habit that prevents this error. (Real situation)
3. You have 20 minutes in a practical exam and a question asks for 'the second highest salary'. Write at least two different working approaches and state which one you would submit and why. (Open-book, application-oriented)

**Homework**

1. Create Student table with Student_ID, Student_Name, Department, Semester, Marks; insert 10 records and complete the five retrieval, update and delete queries given in the original plan.

---

## Session 10 (Module 1) - Debate Activity - Open Source vs Commercial DBMS and DBMS Vocabulary Crossword

**Topics / Time / Teacher aid**

- Discussion groups conducted by selected student chairpersons on Open source DBMS v/s Commercial DBMS | 60 Min | Discussion
- Students solve a printed DBMS Vocabulary Crossword in class and submit the scanned copy through the ERP portal | 60 Min | DBMS Vocabulary Crossword Sheet

**1. Session Execution Plan**

Activity and communication oriented session. The class is divided into two houses - 'Open Source' and 'Commercial' - with student chairpersons managing the floor while the faculty acts as moderator and timekeeper only. Each house must support arguments with real evidence (licensing cost, TCO, support SLA, known migrations such as companies moving from Oracle to PostgreSQL). The second half is an individual timed crossword on DBMS terminology which reinforces vocabulary needed for theory answers and viva.

**2. Detailed SOP**

- Step 1 (10 min): Faculty divides the class into two houses, appoints two student chairpersons and one timekeeper, and announces the debate rules and the evaluation rubric (content 40, evidence 30, delivery 20, rebuttal 10).
- Step 2 (15 min): Preparation time - each house prepares five arguments with supporting facts; use of mobile for fact-checking is permitted and sources must be quoted.
- Step 3 (25 min): Debate - 2 minutes per speaker, alternating houses, chairperson manages the sequence.
- Step 4 (10 min): Rebuttal round and faculty summary which converts the debate into a decision framework (when to choose open source, when commercial).
- Step 5 (50 min): Printed DBMS vocabulary crossword solved individually under examination conditions.
- Step 6 (10 min): Scanning and uploading the solved crossword on ERP; faculty records participation marks.
- Deliverable: Debate evaluation sheet with individual marks and scanned solved crossword uploaded by each student.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A 300-bed hospital must choose between PostgreSQL and Oracle for its HIS. Prepare a five-point written recommendation covering licence cost, 24x7 support, compliance and in-house skill availability, and state the decision you would defend before the management. (Case study)
2. Name one real organisation that migrated from a commercial DBMS to an open-source DBMS and state two technical challenges that such a migration creates at the SQL level (for example datatype and PL/SQL incompatibility). (Research-oriented)
3. Define in one precise line each, as a sessional answer would require: instance, schema, metadata, data dictionary, DDL, constraint, normalization, cursor. (Open-book vocabulary)

**Homework**

1. Upload the scanned crossword and submit a one-page written summary of the debate conclusion.

---

## Session 11 (Module 2) - Architecture of Oracle, Components of DBMS, Data Integrity and Constraints

**Topics / Time / Teacher aid**

- Architecture of Oracle: Instance and Database | 30 Min | PPT, Smartboard
- Components of DBMS (SGA, PGA, Background Processes, Data Files, Control Files) | 30 Min | PPT, Smartboard
- Data Integrity and Constraints: concept and need of constraints | 30 Min | PPT, Smartboard
- Practical 1: Apply primary key and NOT NULL constraints | 15 Min | SQL Plus
- Practical 2: Implementing NOT NULL, CHECK, UNIQUE | 15 Min | SQL Plus

**1. Session Execution Plan**

Architecture is taught using a physical analogy walk-through - the Oracle instance is compared to a bank branch (memory, staff, processes) and the database to its vault (data files, control files, redo logs). Faculty draws the architecture incrementally on the smartboard, adding one component at a time and explaining the failure that occurs if that component is lost. Constraints are introduced through a 'bad data' demonstration - a table without constraints is loaded with duplicate and invalid rows, students see the damage, and then the same table is rebuilt with constraints and the same bad data is rejected by Oracle.

**2. Detailed SOP**

- Step 1 (05 min): Outcome stated - 'student will explain the role of each Oracle architectural component and will enforce data quality at the database level using constraints.'
- Step 2 (30 min): Instance vs database explained with the bank-branch analogy; students draw the labelled diagram in their notebooks as the faculty builds it on the board.
- Step 3 (30 min): SGA, PGA, background processes (SMON, PMON, DBWR, LGWR, CKPT), data files, control files and redo log files explained; for each component faculty asks 'what breaks if this is lost'.
- Step 4 (20 min): Bad-data demonstration - faculty inserts duplicate roll numbers, NULL names and negative marks into an unconstrained table; class lists the business consequences.
- Step 5 (10 min): Need and types of constraints derived from the above list; faculty shows the correct CREATE TABLE with constraints and re-runs the same bad inserts to show rejection.
- Step 6 (30 min): Students execute Practical 1 and Practical 2 and record the exact Oracle error number for each violation in the lab file.
- Deliverable: Labelled Oracle architecture diagram and a constraint-violation error log (error code against violation type).

**3. Real-Life / Unsolved / Open-Book Questions**

1. The DBA of a bank reports that the control file is corrupted while the data files are intact. Explain whether the database can be opened, what information was lost, and what recovery step is required. (Industry scenario)
2. A student result table allowed marks of 150 out of 100 and two students with the same enrolment number. Write the ALTER statements to prevent both problems permanently and state the Oracle error number the user will now see for each violation. (Practical)
3. Explain with one example each the difference between an Oracle instance and an Oracle database, and state what exactly happens to SGA contents during a SHUTDOWN ABORT. (Open-book, senior-level)

**Homework**

1. Create STUDENT, EMPLOYEE, PRODUCT, CUSTOMER and COURSE tables with PRIMARY KEY, NOT NULL, CHECK and UNIQUE constraints as given in the original plan and test valid and invalid inserts.

---

## Session 12 (Module 2) - Database Administrator, DBA Roles and Responsibilities, Constraints - Domain, Entity and Referential

**Topics / Time / Teacher aid**

- Database administrator (DBA) | 15 Min | PPT, Smartboard
- DBA role and responsibilities | 15 Min | PPT, Smartboard
- Domain constraints: NOT NULL, CHECK | 15 Min | PPT, Smartboard
- Entity constraints: UNIQUE, PRIMARY KEY | 15 Min | PPT, Smartboard, SQL Plus
- Referential constraints: FOREIGN KEY | 15 Min | PPT, Smartboard, SQL Plus
- Practical 3: Using IN operator in queries | 15 Min | SQL Plus
- Practical 4: Queries involving predicates LIKE, BETWEEN, IN | 15 Min | SQL Plus
- Practical 6: Add Primary key, NOT NULL and UNIQUE constraints to your tables | 15 Min | SQL Plus

**1. Session Execution Plan**

The DBA portion is delivered as a career-oriented discussion with an actual DBA job description taken from a job portal projected on the smartboard; students map each listed responsibility to the topics of this syllabus. Constraints are classified practically (domain, entity, referential) and demonstrated by building a two-table parent-child model (DEPARTMENT and EMPLOYEE) live, including the deliberate attempt to delete a parent row to show the referential error and the behaviour of ON DELETE CASCADE.

**2. Detailed SOP**

- Step 1 (05 min): Outcome stated - 'student will describe the DBA role in an IT organisation and will implement all three categories of constraints including referential integrity.'
- Step 2 (25 min): Real DBA job description discussed; students map responsibilities (backup, tuning, user management, security) to syllabus modules in a two-column table.
- Step 3 (15 min): Domain constraints NOT NULL and CHECK implemented live with business rules (salary > 0, gender IN ('M','F','O')).
- Step 4 (15 min): Entity constraints UNIQUE and PRIMARY KEY implemented; the difference is proved by inserting a NULL into each.
- Step 5 (15 min): Referential constraint - parent-child tables created, child row with invalid parent rejected, parent deletion blocked, then ON DELETE CASCADE demonstrated.
- Step 6 (45 min): Students execute Practical 3, 4 and 6; faculty verifies that each student's table shows all constraints in USER_CONSTRAINTS.
- Deliverable: Parent-child schema with working referential integrity and a constraint listing taken from USER_CONSTRAINTS.

**3. Real-Life / Unsolved / Open-Book Questions**

1. An e-commerce company allows a customer to be deleted only if he has no orders. Write the FOREIGN KEY definition that enforces this, then write the alternative definition that would instead delete all his orders automatically, and state which one you would choose for a real business and why. (Industry decision)
2. A HR table permits two employees with the same official email id and permits a blank department. Write the ALTER statements that fix both, and explain why UNIQUE allows NULL but PRIMARY KEY does not. (Open-book)
3. From a given DBA job advertisement, list any five responsibilities and state for each the exact SQL feature or Oracle component you have studied that supports it. (Application-oriented)

**Homework**

1. On the STUDENT table, retrieve records using IN, LIKE and BETWEEN predicates and add PRIMARY KEY, NOT NULL and UNIQUE constraints as specified in the original plan, then verify them.

---

## Session 13 (Module 2) - Database System Architecture, Data Abstraction, Data Independence, Operators IN, LIKE, BETWEEN

**Topics / Time / Teacher aid**

- Revision | 05 Min | Discussion
- Database system architecture | 20 Min | PPT, Smartboard
- Data abstraction | 15 Min | PPT, Smartboard
- Data independence (logical and physical) | 15 Min | PPT, Smartboard
- IN operator | 10 Min | PPT, Smartboard, SQL Plus
- LIKE operator | 10 Min | PPT, Smartboard, SQL Plus
- BETWEEN operator | 10 Min | PPT, Smartboard, SQL Plus
- Practical 7: Use foreign keys to establish relationships between tables | 15 Min | SQL Plus
- Practical 8: Implement Practical 1 again with referential constraint | 20 Min | SQL Plus

**1. Session Execution Plan**

Three-schema architecture is taught top-down using the college ERP that students use daily - the student login screen is the external view, the table design is the conceptual level and the data file on the server is the internal level. Data independence is demonstrated practically by adding a new column to a base table and showing that an existing application query continues to work, which makes an abstract concept concrete. Operators are then practised on a realistic customer dataset where pattern search (LIKE) is used as it is used in a real search box.

**2. Detailed SOP**

- Step 1 (05 min): Revision; outcome stated - 'student will map a real application to the three-schema architecture and will write production-style search queries using IN, LIKE and BETWEEN.'
- Step 2 (20 min): Three-level architecture explained using the college ERP screens; students identify which screen belongs to which level.
- Step 3 (15 min): Data abstraction levels explained with the same example; students write one real example of each level.
- Step 4 (15 min): Logical and physical data independence demonstrated live - a column is added to a base table and an existing view or query is re-run unchanged.
- Step 5 (30 min): IN, LIKE (with percent and underscore wildcards) and BETWEEN demonstrated on a 25-row customer table; faculty highlights the inclusive nature of BETWEEN and the date boundary trap.
- Step 6 (35 min): Students execute Practical 7 and Practical 8 implementing foreign keys; faculty verifies the referential behaviour on each machine.
- Deliverable: Three-schema mapping worksheet of the college ERP and a working two-table referential schema.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A search box on a travel portal must return all customers whose name starts with 'A', whose city is Ahmedabad, Surat or Rajkot, and whose booking amount is between 5,000 and 20,000. Write the single query, then state one reason why this query may become slow on 10 lakh rows. (Industry problem)
2. The development team added two new columns to the ORDERS table last night, yet none of the 40 existing reports failed. Name and explain the property of DBMS that made this possible, and describe one change that would have broken the reports. (Analytical)
3. Write a query using BETWEEN to fetch all transactions of March 2026 from a table where the column is of DATE type with a time component. Explain why the straightforward BETWEEN '01-MAR-2026' AND '31-MAR-2026' may silently miss rows. (Open-book, senior-level trap)

**Homework**

1. Create EMPLOYEE table with 10 records and write queries using IN, LIKE, BETWEEN and a combination of IN and BETWEEN as listed in the original plan.

---

## Session 14 (Module 2) - Flipped Classroom Activity (TPA Full Session)

**Topics / Time / Teacher aid**

- Flipped classroom - student-led teaching of assigned topics, TPA full session | 120 Min | Student presentation, Smartboard, SQL Plus

**1. Session Execution Plan**

Complete flipped classroom. Topics already covered in Module 1 and Module 2 (constraints, Oracle architecture, data independence, operators, aggregate functions) are distributed to student teams one week in advance. In this session students teach, demonstrate on SQL*Plus and set questions for their peers while the faculty only moderates, corrects conceptual errors and evaluates. A Topic Presentation Assessment (TPA) rubric is used for scoring and the session doubles as speaking-skill practice.

**2. Detailed SOP**

- Step 1 (10 min): Faculty announces the order of presentations, the TPA rubric (concept clarity 40, live demonstration 30, question handling 20, presentation 10) and appoints two student evaluators per team.
- Step 2 (80 min): Each team gets 8-10 minutes - 4 minutes concept, 3 minutes live SQL demonstration, 3 minutes handling questions from peers and faculty.
- Step 3 (15 min): Faculty gives a consolidated correction talk on every conceptual mistake observed, with the correct explanation.
- Step 4 (10 min): Peer evaluation sheets collected and marks consolidated with faculty marks.
- Step 5 (05 min): Faculty announces the best team and the common weak areas to be revised before Sessional-I.
- Deliverable: TPA score sheet per student, presentation files uploaded on ERP and a class-level weak-topic list.

**3. Real-Life / Unsolved / Open-Book Questions**

1. As the presenting team, demonstrate live why a CHECK constraint is better than validating the same rule in application code. Then answer: name one business rule that cannot be enforced by a CHECK constraint. (Demonstration-based)
2. A peer asks: 'if the application already validates input, why does the database need constraints at all'. Give a complete answer with one real incident-style example. (Viva-style, application-oriented)
3. Prepare and submit three examination-standard questions on your assigned topic along with the model answers, at the level expected in the PLM sessional examination. (Open-book question-setting task)

**Homework**

1. Upload the presentation and the three self-prepared examination questions with model answers.

---

## Session 15 (Module 2) - Types of DBMS, Aggregate Functions, Inbuilt Numeric Functions

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Types of DBMS - Centralized and Distributed | 30 Min | PPT, Smartboard
- Aggregate functions | 20 Min | PPT, Smartboard, SQL Plus
- Inbuilt functions: Numeric | 20 Min | PPT, Smartboard, SQL Plus
- Practical 10: Numeric functions - abs, ceil, power, mod, round, trunc, sqrt | 20 Min | SQL Plus
- Practical 13: Group functions - avg, min, max, sum, count | 15 Min | SQL Plus

**1. Session Execution Plan**

Centralized versus distributed DBMS is explained through two contrasting real systems - a single-branch college ERP versus UPI/IRCTC, which students use daily - and the discussion is driven by the question 'why can IRCTC not run on one server'. Numeric functions are taught as billing-engine building blocks: GST rounding, EMI computation and discount slabs are computed live in SQL so that students see functions solving money problems rather than textbook problems.

**2. Detailed SOP**

- Step 1 (15 min): Revision of previous session; outcome stated - 'student will choose between centralized and distributed architecture for a given business and will perform business calculations using numeric and group functions.'
- Step 2 (30 min): Centralized vs distributed DBMS compared on availability, cost, consistency and latency using the college ERP and IRCTC examples; students fill a comparison table.
- Step 3 (20 min): Aggregate functions revised and extended - COUNT(DISTINCT), handling of NULL, aggregate with GROUP BY.
- Step 4 (20 min): Numeric functions ROUND, TRUNC, MOD, CEIL, FLOOR, ABS, POWER, SQRT demonstrated through a GST and EMI calculation on a live SALES table.
- Step 5 (35 min): Students execute Practical 10 and Practical 13; faculty verifies that each student can explain the difference between ROUND and TRUNC with a negative precision example.
- Deliverable: A working billing query sheet computing net amount, GST and rounded payable amount, plus completed Practicals 10 and 13.

**3. Real-Life / Unsolved / Open-Book Questions**

1. An invoice must show amount, 18 percent GST and a final payable value rounded to the nearest rupee. Write a single query that produces all three columns for every row of a SALES table and explain the difference your choice of ROUND versus TRUNC makes to the company over 1 lakh invoices. (Industry problem)
2. IRCTC handles bookings from the entire country. Explain with two technical reasons why a centralized single-server design would fail, and name the distributed DBMS property that solves each. (Case-based)
3. Using MOD(), write a query that divides the employees into three equal batches for a training programme, and state how the result changes if an employee is deleted. (Open-book, application-oriented)

**Homework**

1. On the EMPLOYEE table, write the eight queries using ROUND, MOD, POWER, SQRT, ABS, CEIL, TRUNC, COUNT, SUM, AVG, MIN, MAX and department-wise GROUP BY as listed in the original plan.

---

## Session 16 (Module 2) - Build DBMS Model - Group Activity (Oracle Architecture 3D Model)

**Topics / Time / Teacher aid**

- Divide students into groups of 5-6; each group creates a 3D model, chart or poster of Oracle Database Architecture (Instance, Database, SGA, PGA, Background Processes, Data Files, Control Files, DBA) | 90 Min | 3D Model Creation
- Teams explain the role of each component as system architects | 30 Min | Presentation

**1. Session Execution Plan**

Experiential learning session. Groups of 5-6 build a physical 3D model or poster of the Oracle architecture using chart paper, thermocol and labels. Each member is assigned one component and must defend it as its 'owner' during the presentation. Faculty introduces failure scenarios during the presentation ('your LGWR process has died - explain what happens now') so that the activity tests understanding, not decoration.

**2. Detailed SOP**

- Step 1 (10 min): Groups formed, components allotted member-wise, rubric announced (technical accuracy 40, completeness 20, explanation 30, teamwork 10).
- Step 2 (70 min): Model or poster construction; faculty visits each group twice to verify that memory structures and background processes are correctly placed and labelled.
- Step 3 (10 min): Groups prepare the narration sequence - data flow of a SELECT and of an INSERT through their model.
- Step 4 (25 min): Presentations of 4-5 minutes per group; each member explains his own component; faculty throws one failure scenario at each group.
- Step 5 (05 min): Models displayed in the lab, photographs uploaded on ERP, marks recorded.
- Deliverable: Physical 3D model or poster, group photograph and a one-page component-wise role note uploaded on ERP.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Using your model, trace exactly what happens inside the SGA, redo log buffer and data files when a user executes an UPDATE followed by COMMIT. State which process writes to disk first and why. (Senior-level, application)
2. The LGWR background process of a production database stops responding. Predict the immediate impact on users and on committed transactions, and state the recovery route. (Real-time scenario)
3. Your group claims the database can run without a control file. Prove or disprove this with reasoning, and state what information the control file uniquely holds. (Analytical, open-book)

**Homework**

1. Upload model photographs and the component-wise role note; revise architecture for Sessional-I.

---

## Session 17 (Module 2) - Inbuilt Functions - Date Functions

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Inbuilt functions: Date | 35 Min | PPT, Smartboard, SQL Plus
- Practical 9: Date functions - add_months, months_between, round, next_day, trunc | 30 Min | SQL Plus
- Practical Assignment-3: Problem solving and practice (Q1-Q10) | 50 Min | SQL Plus

**1. Session Execution Plan**

Date functions are taught entirely through HR and banking use cases - probation completion date, retirement date, EMI due dates, number of months of service, next working day for cheque clearance. Faculty first asks students how they would compute each of these manually, then shows the single Oracle function that does it. Emphasis is placed on the industry pain point of date formats (NLS_DATE_FORMAT) because it is the most common cause of production errors.

**2. Detailed SOP**

- Step 1 (15 min): Revision of numeric functions; outcome stated - 'student will solve real HR and banking date problems using Oracle date functions.'
- Step 2 (10 min): SYSDATE, date arithmetic and NLS_DATE_FORMAT demonstrated; faculty shows how changing the format mask changes nothing in storage, only in display.
- Step 3 (25 min): ADD_MONTHS, MONTHS_BETWEEN, NEXT_DAY, LAST_DAY, ROUND and TRUNC on dates demonstrated, each tied to one HR or banking requirement.
- Step 4 (30 min): Practical 9 executed by all students; faculty verifies the output of MONTHS_BETWEEN including the fractional part and asks each bench to interpret it.
- Step 5 (50 min): Assignment-3 Q1-Q10 solved individually; faculty resolves doubts and gives a mid-way correction talk.
- Deliverable: An HR query sheet producing probation end date, completed service in months and retirement date for every employee.

**3. Real-Life / Unsolved / Open-Book Questions**

1. An HR policy states that probation ends exactly 6 months after joining and that the confirmation letter must be issued on the next Monday after that date. Write a single query producing employee name, probation end date and letter issue date. (Industry problem)
2. A bank must list all loan accounts whose EMI is due on the last day of the current month and must also show the number of completed months since disbursement. Write the query and explain which function handles month-end correctly for February. (Case-based)
3. Two queries on the same table give different results: one uses TRUNC(join_date) and the other does not. Explain with an example why the time component causes this and state the correct practice for date comparison. (Open-book, senior-level)

**Homework**

1. Write the four queries using ADD_MONTHS, MONTHS_BETWEEN, NEXT_DAY, ROUND and TRUNC on employee joining dates as listed in the original plan.

---

## Session 18 (Module 2) - Inbuilt Functions - String Functions

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Inbuilt functions: String | 30 Min | PPT, Smartboard, SQL Plus
- Practical 11: String functions - initcap, lower, upper, rtrim, replace, substr, instr | 35 Min | SQL Plus
- Practical Assignment-3: Problem solving and practice (Q11-Q25) | 40 Min | SQL Plus

**1. Session Execution Plan**

Executed as a data-cleaning workshop, which is exactly how string functions are used in industry. Faculty supplies a deliberately dirty dataset (names in mixed case with trailing spaces, phone numbers with +91 and dashes, email ids in capitals, addresses with double spaces) and students must clean it using string functions only. This converts a routine syntax topic into a real data-quality task and prepares students for case-based examination questions.

**2. Detailed SOP**

- Step 1 (15 min): Revision of date functions; faculty loads the dirty dataset script on all machines; outcome stated - 'student will clean and standardise real dirty data using Oracle string functions.'
- Step 2 (30 min): UPPER, LOWER, INITCAP, LENGTH, LTRIM, RTRIM, TRIM, SUBSTR, INSTR, REPLACE, CONCAT and LPAD demonstrated, each applied to one dirty column of the dataset.
- Step 3 (35 min): Practical 11 executed; students must produce a fully cleaned output of the dataset and get it verified.
- Step 4 (40 min): Assignment-3 Q11-Q25 solved; faculty picks two tricky questions and solves them on the smartboard after students attempt them.
- Deliverable: Before-and-after cleaned dataset output pasted in the lab file with the query used for each column.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A marketing database has names stored as '  rAHUL   patel ' and mobile numbers as '+91-98250-11223'. Write queries to produce a properly capitalised name without extra spaces and a clean 10-digit mobile number. (Real-life data cleaning)
2. From an email column, extract the username part and the domain part as two separate columns, and then count how many customers use gmail. Write all queries. (Industry-oriented, application)
3. Explain why LENGTH('RAHUL ') and LENGTH(TRIM('RAHUL ')) return different values and describe one real bug in a login system that this difference can cause. (Open-book, analytical)

**Homework**

1. Write the four queries using UPPER, LOWER, INITCAP, SUBSTR, INSTR, RTRIM and REPLACE on employee names and departments as listed in the original plan.

---

## Session 19 (Module 2) - Conversion Functions and Explanation of SEE-2 / ALA of Module 2

**Topics / Time / Teacher aid**

- Revision | 20 Min | Discussion
- Practical 12: Conversion functions - to_char, to_date, to_number | 35 Min | PPT, Smartboard, SQL Plus
- Practical Assignment-3: Problem solving and practice (Q26-Q50) | 50 Min | SQL Plus
- Explanation of SEE-2 and ALA of Module 2 - student instructions for performing and submitting the work | 15 Min | Explanation

**1. Session Execution Plan**

Conversion functions are introduced through the single most common industry requirement - report formatting. Faculty shows a real salary slip and an invoice and asks students to produce exactly that output from a table using TO_CHAR with format masks (currency, comma separator, date formats). TO_DATE is taught through the classic production bug of comparing a string with a date column. The last 15 minutes are used to formally brief SEE-2 and ALA-2 with the rubric and submission timeline.

**2. Detailed SOP**

- Step 1 (20 min): Revision of numeric, date and string functions through a 10-question rapid quiz; outcome stated - 'student will produce formatted, report-ready output and will convert safely between datatypes.'
- Step 2 (15 min): TO_CHAR with number masks (9,999.99, L, FM) and date masks (DD-MON-YYYY, DAY, MONTH, HH24:MI) demonstrated by reproducing a salary slip header.
- Step 3 (10 min): TO_DATE and TO_NUMBER demonstrated; faculty shows the ORA-01861 literal does not match format string error and corrects it.
- Step 4 (10 min): Practical 12 executed by students on their own data.
- Step 5 (50 min): Assignment-3 Q26-Q50 solved; faculty maintains a doubt register and addresses the three most repeated doubts on the board.
- Step 6 (15 min): SEE-2 and ALA-2 explained - problem statement, rubric, format, deadline and ERP submission steps; students note the checklist.
- Deliverable: A formatted report query output resembling a salary slip, Assignment-3 completed, SEE-2/ALA-2 instruction checklist noted.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Produce a payroll report showing employee name, joining date as '05 March 2024', and salary as 'Rs. 45,000.00' using a single query. State what will break if the server NLS settings change. (Industry reporting task)
2. A legacy system supplies dates as the text '15/08/2024' and amounts as the text '1,25,000'. Write the queries that convert both into proper DATE and NUMBER values for insertion, and explain the error that occurs if the format mask is omitted. (Real-life integration problem)
3. Explain with an example why WHERE join_date = '01-JAN-2024' may fail on one machine and work on another, and write the version of the condition that is safe everywhere. (Open-book, senior-level)

**Homework**

1. Write the five TO_CHAR, TO_DATE and TO_NUMBER queries on the EMPLOYEE table as listed in the original plan; begin ALA-2 work.

---

## Session 20 (Module 2) - Practice of Inbuilt Functions - Numeric, Date and String

**Topics / Time / Teacher aid**

- Revision | 20 Min | Discussion
- Practical 5: Practice with numeric, date and string inbuilt functions | 35 Min | SQL Plus
- Practical Assignment-4: Problem solving and practice (Q1-Q25) | 65 Min | SQL Plus

**1. Session Execution Plan**

Dedicated practice and consolidation lab before Sessional-I. Conducted in examination mode: questions are given on a printed sheet, time is announced per question block, and no ready-made solutions are shown until each block is over. Faculty uses this session to generate a personalised weak-area list for every student, which is the basis for remedial support.

**2. Detailed SOP**

- Step 1 (20 min): Revision of all three function families using a function-matching worksheet (requirement in column A, function in column B).
- Step 2 (35 min): Practical 5 executed in examination mode in three blocks of about 12 minutes; after each block the model solution is discussed for 2 minutes.
- Step 3 (65 min): Assignment-4 Q1-Q25 solved; faculty records for each student the question numbers attempted correctly.
- Step 4: Faculty prepares the weak-area list and announces remedial pairing (a strong student with a weak student) for the next lab.
- Deliverable: Assignment-4 solved sheet, per-student weak-area record for CCE and remedial action list.

**3. Real-Life / Unsolved / Open-Book Questions**

1. From a RETAIL(bill_no, customer_name, bill_date, amount) table, produce a single report showing customer name in proper case, bill date as 'DD-MON-YYYY', amount rounded to the nearest 10 rupees and the number of days since the bill was raised. (Integrated application)
2. A telecom company must mask customer mobile numbers so that only the last 4 digits are visible (XXXXXX1234) in a report. Write the query using string functions. (Industry problem, data privacy)
3. Given a table of 25 employees, write one query that returns for each employee: completed years of service, salary in words-free currency format, and a flag 'Eligible'/'Not Eligible' for a bonus if service exceeds 3 years. (Open-book, multi-function)

**Homework**

1. Complete Assignment-4 and revise Module 1 and Module 2 for Sessional-I.

---

## Session 21 (Module 2) - Database Integrity Detective Challenge (Activity)

**Topics / Time / Teacher aid**

- Provide faulty tables containing NULL values, duplicate IDs, invalid marks and missing foreign keys for data validation and error identification | 10 Min | Instructor Briefing
- Students identify violated constraints and propose corrective actions applying NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY and CHECK | 70 Min | Identifying Corrective Actions
- Students evaluate data inconsistencies and recommend solutions | 40 Min | Evaluation

**1. Session Execution Plan**

Investigation-style activity. Each team receives a deliberately corrupted schema script (duplicate roll numbers, NULL names, marks of 150 and -5, orphan foreign key rows, inconsistent department names). Teams act as 'data integrity auditors': they must detect every defect using SQL queries, document it in an audit sheet with evidence, clean the data and then alter the schema so that the defect can never recur. Faculty evaluates on detection, correction and prevention - the three-step model used in real data-quality audits.

**2. Detailed SOP**

- Step 1 (10 min): Faculty runs the corrupted schema script on all machines, forms teams of 3-4 and distributes the audit sheet format (defect, detection query, affected rows, corrective action, preventive constraint).
- Step 2 (30 min): Detection phase - teams write SQL to find duplicates (GROUP BY HAVING COUNT(*)>1), NULLs, out-of-range values and orphan child rows. Minimum six defects must be found.
- Step 3 (25 min): Correction phase - teams clean the data using UPDATE and DELETE, keeping a record of the rows changed.
- Step 4 (15 min): Prevention phase - teams write and execute the ALTER statements adding the correct constraints; faculty verifies that the dirty data can no longer be re-inserted.
- Step 5 (30 min): Each team presents its audit sheet in 3 minutes; the class cross-questions on any defect missed.
- Step 6 (10 min): Faculty reveals the complete defect list, teams self-score on how many they detected, sheets submitted on ERP.
- Deliverable: Completed data integrity audit sheet with detection queries, corrective statements and preventive ALTER statements.

**3. Real-Life / Unsolved / Open-Book Questions**

1. In the given faulty STUDENT table, write a single query to detect all duplicate enrolment numbers along with the number of occurrences, and then write the statements to retain only the earliest record of each duplicate. (Unsolved, real audit task)
2. The RESULT table contains marks of 150 and -5 out of 100 and the client refuses to delete those rows. Propose a correction strategy acceptable to the business and implement it with SQL, then prevent recurrence. (Case-based decision)
3. Twelve rows in ENROLMENT refer to a course_id that does not exist in COURSE. Write the query that finds them and explain in business terms what these orphan rows mean and what damage they cause in a report. (Analytical, industry-oriented)

**Homework**

1. Submit the audit sheet on ERP; complete remaining pending assignments; prepare for Sessional-I.

---

## Session 22 (Module 1 & 2) - Sessional Examination - I (Module 1 and Module 2)

**Topics / Time / Teacher aid**

- Sessional Examination - I (Module 1 and 2) as per institute examination schedule | 120 Min | Examination

**1. Session Execution Plan**

Formal sessional examination conducted as per the institute schedule and PLM examination pattern, including application-oriented, case-based and open-book style questions drawn from the session-wise question banks of Sessions 1 to 21. Seating, invigilation and question paper handling follow the examination cell SOP.

**2. Detailed SOP**

- Step 1: Question paper prepared jointly by all faculty teaching this subject (MCS, DPZ, YGL) to maintain a common standard, with a minimum of 50 percent application and case-based questions.
- Step 2: Examination conducted as per the examination cell seating plan and timing; open-book components, if any, are announced in advance with the permitted material.
- Step 3: Faculty invigilates and records attendance and any unfair-means case as per institute policy.
- Step 4: Answer sheets assessed against a common rubric prepared before evaluation so that all three faculty members mark identically.
- Step 5: Result shared with students, question-wise performance analysed and weak topics identified.
- Step 6: A remedial plan for the weak topics is announced and scheduled in the revision slots.
- Deliverable: Evaluated answer sheets, question-wise performance analysis and remedial plan.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Paper to include at least one full case-based question of the type: 'For the given hospital scenario, design the tables with appropriate constraints and write five queries required by the management.'
2. Paper to include at least one unsolved production-situation question of the type: 'An UPDATE without a WHERE clause has been executed - describe the recovery.'
3. Paper to include at least one open-book query-writing question based on a supplied dataset and schema diagram.

**Homework**

1. Review the evaluated answer sheet and submit a correction of every wrong answer.

---

## Session 23 (Module 3) - Advanced Joins - Inner, Outer and Self Join

**Topics / Time / Teacher aid**

- Advanced Joins: Inner, Outer, Self Join | 20 Min | PPT, Smartboard
- Advanced Joins examples | 25 Min | PPT, Smartboard, SQL Plus
- Displaying data from multiple tables (join) | 25 Min | PPT, Smartboard
- Practical 1: Implement inner join, outer join (left, right, full) and self join | 15 Min | PPT, Smartboard, SQL Plus
- Practical 2: Retrieve and display combined data from multiple tables using joins | 15 Min | SQL Plus
- Practical Assignment-5: Problem solving and practice on joins (Q1-Q10) | 20 Min | SQL Plus

**1. Session Execution Plan**

Joins are taught with a physical activity first - two sets of cards (employees and departments) are physically matched by students on the desk to build the mental model of inner, left, right and full outer join, and the rows that remain unmatched are kept visibly aside to represent NULL-extended rows. The self join is introduced through the employee-manager relationship which exists in the students' own college hierarchy. Each join type is then written in SQL and the row counts are compared, which is the practical way to verify a join in industry.

**2. Detailed SOP**

- Step 1 (05 min): Outcome stated - 'student will combine data from multiple related tables using the correct join type and will justify the choice of join from the business requirement.'
- Step 2 (20 min): Card-matching activity on the desk for inner, left, right and full outer join; students record the resulting row counts for each case.
- Step 3 (25 min): SQL implementation of each join type on the DEPARTMENT-EMPLOYEE schema; faculty compares row counts with the card activity to confirm the model.
- Step 4 (25 min): Self join demonstrated using employee-manager; faculty shows the alias requirement and the effect of using an outer self join for the top-most manager.
- Step 5 (30 min): Practical 1 and Practical 2 executed by students; faculty verifies that students can state, before running, how many rows the query should return.
- Step 6 (20 min): Assignment-5 Q1-Q10 solved.
- Deliverable: A join comparison table (join type, business question answered, row count obtained) and completed Practicals 1 and 2.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A manager asks for a report of all departments along with their employees, including departments that currently have no employees. State which join is required, write the query, and explain what the manager will do with the NULL rows. (Industry requirement)
2. Using a SELF JOIN on EMPLOYEE(emp_id, emp_name, manager_id, salary), list every employee who earns more than his own manager. Then explain, in one line, why this result is a red flag for an HR audit. (Case-based)
3. Two queries written by two developers on the same tables return 120 rows and 145 rows respectively. One used an INNER JOIN and the other a LEFT JOIN. Explain which rows account for the difference and how you would verify it with a single query. (Analytical, open-book)

**Homework**

1. On DEPARTMENT and EMPLOYEE, write the five join queries (inner, left outer, departments without employees, employee-manager self join, employees earning more than their manager) given in the original plan.

---

## Session 24 (Module 3) - Subqueries, Nested Queries and Correlated Subqueries, EXISTS / ANY / ALL

**Topics / Time / Teacher aid**

- Subqueries, Nested Queries, Correlated Subqueries | 20 Min | PPT, Smartboard
- Subqueries examples | 15 Min | PPT, Smartboard, SQL Plus
- Retrieve data from multiple tables using subqueries (multiple, nested, correlated) | 15 Min | SQL Plus
- SQL Queries: EXISTS, ANY, ALL | 10 Min | PPT, Smartboard, SQL Plus
- Practical 3: Multiple-row, nested and correlated subqueries | 20 Min | SQL Plus
- Practical 4: Solve complex SQL queries using single-row and multiple-row subqueries | 20 Min | SQL Plus
- Practical 5: Usage of EXISTS, ANY and ALL | 20 Min | SQL Plus

**1. Session Execution Plan**

Subqueries are taught by the 'question inside a question' method - faculty writes a business question that cannot be answered in one step (employees earning more than the company average) and makes students solve it in two manual steps first, then merges the two steps into a single subquery. The correlated subquery is explained by deliberately showing the row-by-row execution using a small 5-row table so that students see why it is slower. EXISTS, ANY and ALL are compared against the equivalent IN and join forms.

**2. Detailed SOP**

- Step 1 (05 min): Outcome stated - 'student will solve multi-step business questions using nested and correlated subqueries and will choose between IN, EXISTS and joins.'
- Step 2 (20 min): Two-step manual method demonstrated, then converted into a single-row subquery; rules for single-row vs multiple-row operators explained with the ORA-01427 error shown deliberately.
- Step 3 (15 min): Nested subquery in WHERE, FROM (inline view) and SELECT clauses demonstrated with one business example each.
- Step 4 (15 min): Correlated subquery traced row by row on a 5-row table on the board, then executed; performance implication discussed.
- Step 5 (10 min): EXISTS, ANY and ALL demonstrated and compared with the equivalent IN and join versions of the same question.
- Step 6 (60 min): Practicals 3, 4 and 5 executed; students must write, for each practical, the business question their query answers.
- Deliverable: A solved problem set in which each query is accompanied by the business question and the reason for choosing that subquery form.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A company wants the list of employees who earn more than the average salary of their own department. Write the correlated subquery, and then write an equivalent solution without a correlated subquery. State which you would use on a 10 lakh row table and why. (Industry performance problem)
2. List all customers who have never placed an order, using (i) NOT EXISTS and (ii) a LEFT JOIN with IS NULL. Explain which version is safe when the order table contains NULL customer ids. (Case-based trap)
3. Find the department whose total salary expense is the highest, without using ORDER BY and ROWNUM. Write the query using a subquery with ALL. (Unsolved, open-book)

**Homework**

1. On DEPARTMENT and EMPLOYEE, write the five subquery questions (nested, correlated, EXISTS, ANY, ALL) given in the original plan.

---

## Session 25 (Module 3) - SQL Escape Room Game - Joins and Subqueries (Activity)

**Topics / Time / Teacher aid**

- Students solve SQL puzzles - briefing | 10 Min | Instructor Briefing
- Level 1: INNER JOIN, Level 2: Subquery, Level 3: Correlated Subquery, Level 4: EXISTS - each correct query unlocks the next clue | 80 Min | Puzzle solving
- Students feedback and experience sharing | 30 Min | Experience Sharing

**1. Session Execution Plan**

Gamified assessment of Module 3 querying skills. Teams of 3-4 progress through four locked levels; the output value of a correct query is the password to the next level, so a wrong query cannot be bluffed. The dataset used is a realistic e-commerce schema (CUSTOMER, ORDERS, PRODUCT, ORDER_ITEM) so that every puzzle is a genuine business question. A leaderboard is maintained on the smartboard, and the debrief converts the game into learning by discussing the fastest correct approach for each level.

**2. Detailed SOP**

- Step 1 (10 min): Faculty loads the e-commerce dataset, forms teams, explains the unlock rule and the leaderboard, and distributes the Level-1 clue.
- Step 2 (15 min): Level 1 - INNER JOIN puzzle; the output value becomes the key to Level 2. Faculty verifies and hands over the next clue.
- Step 3 (20 min): Level 2 - subquery puzzle requiring an aggregate inside the condition.
- Step 4 (20 min): Level 3 - correlated subquery puzzle (per-group comparison).
- Step 5 (25 min): Level 4 - EXISTS / NOT EXISTS final puzzle combining three tables; first three teams to finish are recorded.
- Step 6 (30 min): Debrief - each level solved on the smartboard by the fastest team, alternative approaches discussed, students share what blocked them.
- Deliverable: Team query log of all four levels, leaderboard record and individual reflection note on the mistakes made.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Level-style question: identify the customer who has bought from every product category available in the store. Write the query. (Unsolved, division-type problem)
2. Level-style question: find products that have never been ordered in the last 90 days but are still held in stock, and state the business action the company should take. (Industry case)
3. Level-style question: for each city, display the customer with the highest total order value. Write the query and explain how you handled ties. (Open-book, senior-level)

**Homework**

1. Submit the team query log and a written note on the two queries that took the longest and why.

---

## Session 26 (Module 3) - Set Operations - UNION, INTERSECT and MINUS

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Set Operations: UNION, INTERSECT, MINUS | 35 Min | PPT, Smartboard
- Executing UNION, INTERSECT, MINUS | 15 Min | SQL Plus
- Practical 6: Implement set operators to combine results of multiple queries | 20 Min | SQL Plus
- Practical Assignment-5: Problem solving and practice on joins (Q11-Q20) | 35 Min | SQL Plus

**1. Session Execution Plan**

Set operations are introduced through a data-migration scenario that students can visualise - merging the current and former employee registers, or finding students who appear in the admission list but not in the fee-paid list. Venn diagrams are drawn on the board and immediately mapped to the SQL. The UNION versus UNION ALL performance difference and the column-compatibility rule are stressed because both are standard examination and interview points.

**2. Detailed SOP**

- Step 1 (15 min): Revision of joins and subqueries; outcome stated - 'student will combine and compare result sets of two queries using set operators and will distinguish them from joins.'
- Step 2 (20 min): Venn diagram explanation of UNION, UNION ALL, INTERSECT and MINUS with the admission list and fee-paid list example.
- Step 3 (15 min): Column count, datatype compatibility and ORDER BY placement rules demonstrated, including the deliberate error of mismatched columns.
- Step 4 (15 min): Live execution on CURRENT_EMPLOYEE and FORMER_EMPLOYEE tables; duplicate handling compared between UNION and UNION ALL with row counts.
- Step 5 (20 min): Practical 6 executed by students.
- Step 6 (35 min): Assignment-5 Q11-Q20 solved; faculty discusses one question where a set operator and a join both work and compares the two.
- Deliverable: A comparison sheet of UNION, UNION ALL, INTERSECT and MINUS with the row counts obtained on the live dataset.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A college has an ADMITTED list and a FEE_PAID list. Write queries to produce (i) all students in either list, (ii) students who have both admitted and paid, (iii) students admitted but not paid. State the business action for the third list. (Real-life case)
2. During a data migration, the old and the new employee tables must be merged into a single report with no duplicate employee appearing twice. Write the query, and state the performance consequence if you use UNION instead of UNION ALL on 50 lakh rows. (Industry problem)
3. Explain with an example why MINUS is not symmetric, that is, why A MINUS B is not the same as B MINUS A, and give one business question that needs each direction. (Analytical, open-book)

**Homework**

1. On CURRENT_EMPLOYEE and FORMER_EMPLOYEE, write the five UNION, INTERSECT and MINUS queries listed in the original plan.

---

## Session 27 (Module 3) - Views, Indexes, Sequences and Synonyms

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Views, Indexes, Sequences, Synonyms | 40 Min | PPT, Smartboard
- Creating and using Views, Indexes, Sequences | 25 Min | SQL Plus
- Practical 7: Creation and usage of views, indexes and sequences | 40 Min | SQL Plus

**1. Session Execution Plan**

Each object is introduced through the problem it solves rather than its syntax: a view is introduced as the answer to 'how do I let the accounts clerk see salary but not the bank account number', an index as the answer to 'why does this report take 40 seconds', a sequence as the answer to 'how do two users insert without duplicating the id'. The index portion includes a measurable demonstration - the same query is run on a large table with and without an index and the elapsed time is compared using SET TIMING ON.

**2. Detailed SOP**

- Step 1 (15 min): Revision; outcome stated - 'student will create and justify views, indexes, sequences and synonyms for stated business needs.'
- Step 2 (15 min): Views - simple and complex, read-only views, WITH CHECK OPTION; faculty demonstrates column-level security by creating a restricted view and granting access.
- Step 3 (15 min): Indexes - creation, when an index helps and when it hurts (heavy DML tables); demonstration with SET TIMING ON on a table of at least one lakh rows generated by a script.
- Step 4 (10 min): Sequences - NEXTVAL and CURRVAL, use in multi-user insert, gap behaviour after rollback demonstrated live.
- Step 5 (10 min): Synonyms - public and private, and their role in hiding schema names from application code.
- Step 6 (40 min): Practical 7 executed; each student must create one view, one index with a timing comparison, one sequence used in an insert, and one synonym.
- Deliverable: Script file containing the four objects created, with the before-and-after timing evidence for the index.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The accounts clerk must see employee name, department and salary but must never see the bank account number or PAN. Implement this requirement without changing the base table, and write the GRANT statement that completes the solution. (Industry security requirement)
2. A daily sales report takes 42 seconds on a 20 lakh row table filtered by sale_date. Propose a solution, implement it, and state one negative impact of your solution on the nightly data-load job. (Performance case study)
3. Two data-entry operators insert invoices at the same time and both get invoice number 1007. Explain the cause and implement the correct Oracle solution. Also explain why gaps may appear in the invoice numbers and whether that is acceptable to an auditor. (Real-time problem)

**Homework**

1. Create the EMP_DETAILS view, an index on Emp_Name, the EMP_SEQ sequence starting from 1001 and a synonym EMP, as specified in the original plan, and verify each.

---

## Session 28 (Module 3) - Transaction Control Commands - COMMIT, ROLLBACK, SAVEPOINT

**Topics / Time / Teacher aid**

- Revision | 05 Min | Discussion
- Transaction Control Commands: COMMIT, ROLLBACK, SAVEPOINT | 30 Min | PPT, Smartboard
- COMMIT, ROLLBACK, SAVEPOINT examples | 25 Min | PPT, Smartboard
- Practical 8: Demonstrating transactions - COMMIT, ROLLBACK, SAVEPOINT | 20 Min | SQL Plus
- Explanation of SEE-3 and ALA of Module 3 - student instructions | 10 Min | Explanation
- Practical Assignment-5: Problem solving and practice on subqueries (Q1-Q10) | 30 Min | SQL Plus

**1. Session Execution Plan**

Taught through the bank fund-transfer scenario executed live by two students on two SQL*Plus sessions. One student debits account A and does not commit; the other student queries the same row from a second session and sees the old value - this demonstrates atomicity, isolation and read consistency concretely. SAVEPOINT is demonstrated through a multi-step order-booking transaction where only part of the work must be undone.

**2. Detailed SOP**

- Step 1 (05 min): Revision; outcome stated - 'student will control transaction boundaries correctly and will explain atomicity and isolation from observed behaviour.'
- Step 2 (20 min): Two-session bank transfer demonstration performed by two students on the smartboard - debit without commit, read from the second session, then commit and re-read.
- Step 3 (15 min): COMMIT, ROLLBACK, implicit commit by DDL, and auto-commit behaviour explained from the demonstration.
- Step 4 (20 min): SAVEPOINT and ROLLBACK TO SAVEPOINT demonstrated through a four-step order booking where step 3 fails.
- Step 5 (20 min): Practical 8 executed by students in pairs so that both the transaction and the observing session are experienced.
- Step 6 (10 min): SEE-3 and ALA-3 explained with rubric and deadline.
- Step 7 (30 min): Assignment-5 subquery questions Q1-Q10 solved.
- Deliverable: Transaction log sheet recording the value seen by each session at each step, signed by both partners of the pair.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Write the complete transaction for transferring Rs. 10,000 from account A to account B including the failure case where account B does not exist. Show where COMMIT and ROLLBACK must be placed and explain what the account holder would see if the system crashed between the two UPDATE statements. (Banking scenario)
2. A clerk made four changes, realised that the third was wrong, and does not want to lose the first two. Write the exact statement sequence using SAVEPOINT that achieves this. (Practical situation)
3. Explain why executing a CREATE TABLE in the middle of an uncommitted transaction can make a later ROLLBACK ineffective. Demonstrate with a statement sequence. (Open-book, senior-level trap)

**Homework**

1. On the EMPLOYEE table, perform the three SAVEPOINT, COMMIT and ROLLBACK exercises listed in the original plan and record the output of each step.

---

## Session 29 (Module 3) - Introduction to Database Design, Functional Dependency and Normalization

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Introduction to database design | 15 Min | PPT, Smartboard
- Functional dependency | 15 Min | PPT, Smartboard
- Normalization: 1NF, 2NF, 3NF, BCNF | 40 Min | PPT, Smartboard
- Comparison of 3NF and BCNF | 20 Min | PPT, Smartboard
- Multivalued dependency: 4NF and 5NF (Project Join NF) | 15 Min | PPT, Smartboard, SQL Plus

**1. Session Execution Plan**

Normalization is taught entirely on one running real example - a single flat spreadsheet of student-course-faculty data that the college actually maintains. The same table is normalized live, one normal form per step, and after each step students are asked which specific anomaly (insert, update, delete) has just been removed. This anomaly-driven approach makes the abstract definitions usable in examination answers. BCNF is then introduced by showing a 3NF table that still has an anomaly, which is the standard examination discriminator.

**2. Detailed SOP**

- Step 1 (15 min): Revision; outcome stated - 'student will normalize a real unnormalized table up to BCNF and will justify each decomposition by the anomaly it removes.'
- Step 2 (15 min): The flat STUDENT_COURSE spreadsheet is projected; students list the redundancy they can see and the three anomaly types are defined from their observations.
- Step 3 (15 min): Functional dependency notation introduced; students write all FDs of the projected table and identify the candidate keys.
- Step 4 (40 min): Live decomposition into 1NF, 2NF and 3NF; after each step faculty asks which anomaly is now impossible and students record it.
- Step 5 (20 min): A 3NF-but-not-BCNF example shown and decomposed; the difference is tabulated with the dependency-preservation trade-off.
- Step 6 (15 min): Multivalued dependency shown with the student-skill-course example and decomposed to 4NF, with a note on 5NF.
- Deliverable: A worksheet showing the same table at 1NF, 2NF, 3NF and BCNF with the FD list and the anomaly removed at each stage.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The college keeps one flat sheet: Student_ID, Student_Name, Course_ID, Course_Name, Faculty_ID, Faculty_Name, Skill. Normalize it up to 3NF, listing every functional dependency, and state one specific business problem that exists before normalization and disappears after it. (Case-based)
2. Give a table that is in 3NF but not in BCNF from a real college or hospital context, decompose it, and state what is lost by that decomposition. (Senior-level, analytical)
3. A manager argues that a fully normalized design makes reports slow and wants the data kept in one table. Write a reasoned response of five lines stating when denormalization is professionally acceptable and what safeguard must accompany it. (Industry judgement, open-book)

**Homework**

1. Normalize the given STUDENT_COURSE table to 3NF, test it for BCNF, and decompose it to 4NF and 5NF as specified in the original plan.

---

## Session 30 (Module 3) - Transaction Processing, ACID Properties, Backup and Recovery, Oracle Import/Export

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Transaction processing - introduction | 20 Min | PPT, Smartboard
- ACID properties | 25 Min | Video, Explanation
- Serializability of scheduling | 10 Min | PPT, Smartboard
- Database backup and recovery | 15 Min | PPT, Smartboard
- ORACLE Utility - Import, Export | 20 Min | PPT, Smartboard
- Practical 9: Backup and recovery using export and import utilities | 20 Min | SQL Plus

**1. Session Execution Plan**

ACID is taught by failure demonstration: for each property the faculty shows what a system without it would do (a failed transfer leaving money nowhere for atomicity, two simultaneous bookings of the same seat for isolation). A short video reinforces concurrency. The backup portion is fully practical - students export their own schema using Data Pump, deliberately drop a table, and restore it, which gives them a genuine disaster-recovery experience.

**2. Detailed SOP**

- Step 1 (10 min): Revision; outcome stated - 'student will explain ACID from observed failures and will perform a schema-level backup and restore.'
- Step 2 (20 min): Transaction states and transaction processing explained with the order-booking life cycle.
- Step 3 (25 min): ACID properties, each introduced by its failure scenario, supported by a short video; students write one real-world failure example per property.
- Step 4 (10 min): Serializability explained with a two-transaction schedule drawn on the board; students determine whether it is serializable.
- Step 5 (15 min): Backup types (physical, logical, full, incremental) and recovery concepts explained with the college ERP as the example.
- Step 6 (40 min): Practical 9 - each student performs expdp of his own schema, drops one table, and performs impdp to restore it; the restored row count must match the original.
- Deliverable: Export dump file, screenshot of the drop, and proof of successful restore with matching row counts.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Two passengers book the last seat on the same train at the same instant. Name the ACID property involved, explain what the DBMS does internally, and state what the second passenger sees. (Real-time scenario)
2. A company's database server crashed at 3 pm; the last full backup was taken at 2 am and archive logs are available. Explain what can and cannot be recovered and outline the recovery sequence. (Industry case)
3. Perform a logical backup of your schema, drop any one table, and restore only that table. Write every command used and state one situation in which this approach would not be sufficient. (Open-book practical)

**Homework**

1. Watch the video links of the session uploaded on Google Classroom and submit a one-page note on any one real database failure incident and its recovery.

---

## Session 31 (Module 3) - Module-3 Practice Session - Assignment-6 Problem Solving

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Practical Assignment-6: Problem solving and practice (Q1-Q27) | 105 Min | SQL Plus

**1. Session Execution Plan**

Extended practice lab conducted in examination mode with progressive difficulty. The 27 questions are arranged in three levels - direct joins and subqueries, multi-table analytical queries, and open-ended business questions with no single correct query. Students work individually; peer review is used for the third level so that different correct approaches are compared, which is exactly how the PLM sessional expects students to think.

**2. Detailed SOP**

- Step 1 (15 min): Revision of joins, subqueries, set operators and views through a 10-question oral round.
- Step 2 (35 min): Level 1 - Q1 to Q10 solved individually in a timed block; solutions discussed for 3 minutes at the end of the block.
- Step 3 (35 min): Level 2 - Q11 to Q20, multi-table analytical queries; faculty circulates and records the approach used by each student.
- Step 4 (30 min): Level 3 - Q21 to Q27, open-ended business questions; students exchange machines and review a peer's query for correctness and efficiency.
- Step 5 (05 min): Faculty consolidates the best approaches seen in class and uploads them as a reference solution set.
- Deliverable: Assignment-6 fully solved with peer-review remarks on the Level-3 questions.

**3. Real-Life / Unsolved / Open-Book Questions**

1. For an e-commerce dataset, find the top three customers by revenue in each city. Write the query and state how you would verify that the result is correct. (Analytical)
2. Identify all products whose stock is below the average stock of their category and which have pending orders. Write the query and state the business action it triggers. (Industry problem)
3. Write any one business question of your own that needs at least two tables and a subquery, write the query, and give it to a peer to validate. (Open-book, question-setting)

**Homework**

1. Complete all pending assignment questions and prepare for the Module-3 activity.

---

## Session 32 (Module 3) - Design, Normalize and Query - Case Study Activity

**Topics / Time / Teacher aid**

- Form groups of 4; assign a real-world case study (Hospital Management, Library Management, College ERP) - analyse, design, identify functional dependencies, normalize up to BCNF | 20 Min | Explanation, Definition Finalization
- Design ER Diagram | 30 Min | Lucidchart
- Normalize up to BCNF | 20 Min | Microsoft Word
- Write 5 SQL Queries using Joins/Subqueries | 20 Min | SQL Plus
- Present findings | 30 Min | Presentation

**1. Session Execution Plan**

End-to-end mini project activity covering the full Module-3 cycle. Each group takes one real domain, draws the ER diagram in Lucidchart, normalizes the design up to BCNF with documented functional dependencies, implements the tables and writes five analytical queries that the management of that domain would actually ask. The deliverable is a complete design document, which is the format expected in industry and in the ALA submission.

**2. Detailed SOP**

- Step 1 (20 min): Groups formed, domains allotted so that no two adjacent groups share a domain; faculty finalises the scope and the list of five management questions each group must answer.
- Step 2 (30 min): ER diagram prepared in Lucidchart with entities, attributes, keys, relationships and cardinality; faculty approves each diagram before the group proceeds.
- Step 3 (20 min): Normalization up to BCNF documented in Word with the FD list and the justification of each decomposition.
- Step 4 (20 min): Tables implemented in Oracle and the five analytical queries written using joins and subqueries, with output captured.
- Step 5 (30 min): Each group presents for 4 minutes - domain, ER diagram, normalization decision and one query output; other groups cross-question.
- Step 6: Design document uploaded on ERP as the Module-3 ALA deliverable.
- Deliverable: Complete design document containing ER diagram, FD list, BCNF schema, DDL script and five analytical queries with output.

**3. Real-Life / Unsolved / Open-Book Questions**

1. For your allotted domain, state the five questions the management would ask the database every week and write the SQL for any three of them. (Industry-oriented)
2. In your normalized design, identify one place where you deliberately stopped at 3NF instead of BCNF and justify the decision in business terms. (Senior-level judgement)
3. Your ER diagram shows a many-to-many relationship. Show how it is implemented physically and write a query that uses the resulting bridge table meaningfully. (Open-book, application)

**Homework**

1. Complete and upload the Module-3 ALA design document with all group member contributions listed.

---

## Session 33 (Module 4) - Introduction to PL/SQL, Block Structure and Variables

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Introduction to PL/SQL | 15 Min | PPT, Smartboard
- PL/SQL block structure | 20 Min | PPT, Smartboard, SQL Plus
- Variables | 15 Min | PPT, Smartboard
- Practical 1: Implement basic PL/SQL blocks | 30 Min | SQL Plus
- Practical Assignment-7: Problem solving and practice (Q1-Q5) | 30 Min | SQL Plus

**1. Session Execution Plan**

The need for PL/SQL is established first by a problem SQL cannot solve - 'give a 10 percent raise only if the department budget allows it, otherwise 5 percent' - which requires logic. Faculty then builds the anonymous block incrementally on the smartboard: DECLARE, BEGIN, EXCEPTION, END, adding one part at a time with students typing along. Emphasis on SET SERVEROUTPUT ON, on the percent TYPE anchored declaration, and on SELECT INTO, since these three cause most beginner failures.

**2. Detailed SOP**

- Step 1 (10 min): Revision of SQL; the conditional-raise problem posed; students attempt it in pure SQL and realise the limitation. Outcome stated - 'student will write and execute PL/SQL blocks that implement business logic.'
- Step 2 (15 min): Difference between SQL and PL/SQL, and the advantage of reduced network traffic explained with a diagram of 10 separate statements versus one block.
- Step 3 (20 min): Block structure built live - the mandatory BEGIN-END, the optional DECLARE and EXCEPTION; SET SERVEROUTPUT ON demonstrated with and without, so students recognise the silent-output problem.
- Step 4 (15 min): Variable declaration, constants, percent TYPE anchoring and SELECT INTO demonstrated; faculty shows the error when SELECT INTO returns more than one row.
- Step 5 (30 min): Practical 1 executed; every student must run at least three blocks successfully.
- Step 6 (30 min): Assignment-7 Q1-Q5 solved.
- Deliverable: Three executed PL/SQL blocks with output, including one that reads a value from a table into a variable using percent TYPE.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Write a PL/SQL block that fetches the salary of a given employee and prints 'High', 'Medium' or 'Low'. Then state what happens if the employee id does not exist and how you would make the block safe. (Application + anticipation of exceptions)
2. A payroll job must apply a raise of 10 percent if the department budget is sufficient and 5 percent otherwise. Explain why this cannot be done in a single plain SQL UPDATE in a maintainable way, and write the PL/SQL block. (Industry problem)
3. Explain the practical advantage of declaring v_name EMPLOYEE.emp_name percent TYPE instead of VARCHAR2(50), using a real maintenance scenario where the column size changes. (Open-book, senior-level)

**Homework**

1. Write the five PL/SQL blocks on the EMPLOYEE table (welcome message, variable assignment, addition, fetch emp_name, count employees) listed in the original plan.

---

## Session 34 (Module 4) - Advantages of PL/SQL, Control Structures - IF, WHILE LOOP, CASE

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Control structures syntax | 10 Min | PPT, Smartboard
- Advantages of PL/SQL | 10 Min | PPT, Smartboard
- IF statement | 15 Min | PPT, Smartboard
- WHILE loop | 15 Min | PPT, Smartboard
- CASE | 15 Min | PPT, Smartboard
- Practical 2: PL/SQL programs using IF statement | 15 Min | SQL Plus
- Practical 3: PL/SQL programs using WHILE loop | 15 Min | SQL Plus
- Practical 4: PL/SQL programs using IF, CASE and loops | 15 Min | SQL Plus

**1. Session Execution Plan**

Control structures are taught through business rule implementation rather than number-printing exercises. IF is taught through a loan eligibility rule, CASE through a grade or bonus slab, and WHILE through an EMI schedule generation. Faculty writes the business rule in English on the board, students convert it into pseudo-code, and only then into PL/SQL - this three-step habit is what the sessional questions test.

**2. Detailed SOP**

- Step 1 (10 min): Revision of block structure; outcome stated - 'student will implement a written business rule as a PL/SQL control structure.'
- Step 2 (10 min): Advantages of PL/SQL consolidated (procedural capability, error handling, reusability, performance).
- Step 3 (15 min): IF, IF-ELSIF-ELSE demonstrated with a loan eligibility rule given in English and converted to code by the class.
- Step 4 (15 min): CASE statement and CASE expression compared with IF using a bonus slab rule; difference between the two forms demonstrated in SELECT.
- Step 5 (15 min): WHILE LOOP demonstrated by generating a 6-month EMI schedule; faculty deliberately writes an infinite loop and shows how to detect and stop it.
- Step 6 (45 min): Practicals 2, 3 and 4 executed; each student must implement at least one rule given verbally by the faculty on the spot.
- Deliverable: Three working PL/SQL programs implementing a loan eligibility rule, a slab-based bonus and a generated EMI schedule.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A bank sanctions a loan if income is above 30,000 and age is below 55, sanctions with conditions if income is between 20,000 and 30,000, and rejects otherwise. Implement this as a PL/SQL block and test it with three sample applicants. (Industry rule)
2. Generate and display a 12-month EMI schedule for a loan of Rs. 1,00,000 at 10 percent using a WHILE loop, showing month, interest, principal and closing balance. (Application-oriented)
3. Rewrite a given four-branch IF-ELSIF block using CASE and state one situation in which CASE cannot replace IF. (Open-book, analytical)

**Homework**

1. Write the five PL/SQL blocks using IF, WHILE and CASE on the EMPLOYEE table (salary category, even-odd, count check, salary classification, bonus category) listed in the original plan.

---

## Session 35 (Module 4) - Cursors and its Types

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Cursors: Implicit | 15 Min | PPT, Smartboard
- Cursors: Explicit | 15 Min | PPT, Smartboard
- Cursors: Cursor FOR Loop | 15 Min | PPT, Smartboard
- Cursors: Parameterized Cursor | 15 Min | PPT, Smartboard
- Practical 5: PL/SQL programs with cursor implementation (all types) | 30 Min | SQL Plus
- Practical Assignment-7: Problem solving and practice (Q6-Q10) | 20 Min | SQL Plus

**1. Session Execution Plan**

The need for a cursor is created by a failure first - students run a SELECT INTO that returns many rows and see the TOO_MANY_ROWS error, after which the explicit cursor is presented as the solution. Implicit cursor attributes (SQL percent ROWCOUNT, SQL percent FOUND) are demonstrated on an UPDATE, which is how they are used in real jobs. A salary-slip generation program is built end to end using a cursor FOR loop, and a parameterized cursor is used to make the same program department-wise.

**2. Detailed SOP**

- Step 1 (10 min): Revision; faculty makes students run a multi-row SELECT INTO to produce TOO_MANY_ROWS. Outcome stated - 'student will process multiple rows row-by-row using the appropriate cursor type.'
- Step 2 (15 min): Implicit cursor attributes demonstrated on an UPDATE that affects several rows; students print the affected count.
- Step 3 (15 min): Explicit cursor - DECLARE, OPEN, FETCH, close with EXIT WHEN NOT FOUND, written step by step with the class.
- Step 4 (15 min): Cursor FOR loop introduced as the compact form; the same program is rewritten and the reduction in code is highlighted.
- Step 5 (15 min): Parameterized cursor used to generate the salary slip department-wise; the parameter is supplied at run time.
- Step 6 (50 min): Practical 5 and Assignment-7 Q6-Q10 executed; each student must demonstrate all four cursor forms.
- Deliverable: A working salary-slip generator program in all three explicit forms (basic, FOR loop, parameterized) with output.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Generate a department-wise salary slip listing for a department supplied at run time, using a parameterized cursor. State why a parameterized cursor is better than declaring three separate cursors. (Industry program)
2. A batch job updated employee salaries and must log how many rows were actually changed. Write the block using implicit cursor attributes and explain where this count is used in a real production log. (Practical)
3. Rewrite a given explicit cursor program using a cursor FOR loop and list the three statements that become unnecessary. State one case where the explicit form must still be used. (Open-book, analytical)

**Homework**

1. Write the five cursor programs (implicit update count, explicit cursor listing, cursor FOR loop, parameterized cursor, salary filter) on the EMPLOYEE table listed in the original plan.

---

## Session 36 (Module 4) - Revision of PL/SQL Block, IF, WHILE, CASE and Cursor; SEE-4 and CCE Explanation

**Topics / Time / Teacher aid**

- Revision - PL/SQL block | 15 Min | Discussion
- Revision - IF | 15 Min | PPT, Smartboard
- Revision - WHILE | 15 Min | PPT, Smartboard
- Revision - CASE | 15 Min | PPT, Smartboard
- Revision - Cursor | 15 Min | PPT, Smartboard
- Practical Assignment-7: Problem solving and practice (Q11-Q15) | 30 Min | SQL Plus
- Explanation of SEE-4 and CCE of Module 4 - student instructions | 15 Min | Explanation

**1. Session Execution Plan**

Consolidation session run as a code-review clinic. Instead of re-teaching, faculty projects student-written programs collected from the previous sessions (anonymised) and the class reviews each one for correctness, efficiency and readability. Students then fix the defects on their own machines. The session ends with a formal briefing of SEE-4 and the CCE rubric for Module 4.

**2. Detailed SOP**

- Step 1 (15 min): Rapid revision of block structure through a fill-in-the-blanks skeleton on the smartboard completed by students.
- Step 2 (30 min): Code review clinic - four anonymised student programs (one each on IF, WHILE, CASE and cursor) are projected; the class identifies defects and suggests corrections; faculty records the top five recurring mistakes.
- Step 3 (15 min): Faculty demonstrates the corrected version of the weakest program line by line.
- Step 4 (30 min): Assignment-7 Q11-Q15 solved individually.
- Step 5 (15 min): SEE-4 problem statement, CCE rubric, submission format and deadline explained; students prepare their checklist.
- Deliverable: Corrected versions of the reviewed programs in each student's lab file and a personal error-checklist for PL/SQL.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Review the given PL/SQL program (supplied in the examination) and list every logical and syntactical defect with the corrected line. (Code-review question, unsolved)
2. Write a single PL/SQL block for a STUDENT table that classifies each student as Distinction, First Class, Pass or Fail using a cursor and CASE, and prints a class-wise count at the end. (Integrated application)
3. A program works correctly for 10 rows but takes 4 minutes for 1 lakh rows. Give two reasons related to cursor usage and state what you would change. (Senior-level, performance)

**Homework**

1. Write the six PL/SQL programs on the STUDENT table (fetch details, marks check, WHILE loop, result classification, cursor listing) listed in the original plan; start SEE-4 work.

---

## Session 37 (Module 4) - PL/SQL Debugging and Exception Handling Workshop (Activity)

**Topics / Time / Teacher aid**

- Form groups of 4; provide PL/SQL programs containing logical and runtime errors - briefing | 10 Min | Instructor Briefing
- Identify errors and classify them; implement predefined exception handlers; create user-defined exceptions for business rules | 80 Min | Activity Execution
- Present the corrected solutions | 30 Min | Presentation

**1. Session Execution Plan**

Workshop-style activity in which each group receives a set of five broken PL/SQL programs containing compile-time errors, runtime exceptions (NO_DATA_FOUND, TOO_MANY_ROWS, ZERO_DIVIDE, VALUE_ERROR, DUP_VAL_ON_INDEX) and silent logical errors. Groups must classify each error correctly, fix it, add the right exception handler and additionally raise a user-defined exception for a business rule supplied with the program. The emphasis is on classification, because identifying the error type is what the examination and real debugging both require.

**2. Detailed SOP**

- Step 1 (10 min): Faculty distributes the broken program set and the error classification sheet (error type, cause, fix, handler added), forms groups of 4 and allots roles - coder, reviewer, documenter, presenter.
- Step 2 (30 min): Groups compile each program, record the exact Oracle error number and message, and classify it as compile-time, runtime or logical.
- Step 3 (30 min): Groups fix the programs and attach the correct predefined exception handler to each runtime error, verifying that the program now fails gracefully.
- Step 4 (20 min): Groups implement a user-defined exception with RAISE and RAISE_APPLICATION_ERROR for the supplied business rule (for example salary below minimum wage).
- Step 5 (30 min): Each group presents one program - the original defect, the classification and the corrected code; the class verifies.
- Deliverable: Completed error classification sheet and five corrected, exception-safe programs uploaded on ERP.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The given program fails with ORA-01403 for some employee ids and works for others. Classify the error, explain the exact cause and rewrite the block so that it prints a clear business message instead of failing. (Unsolved debugging)
2. A payroll rule states that a salary below Rs. 10,000 must never be saved. Implement this with a user-defined exception and RAISE_APPLICATION_ERROR, and explain why doing this in the database is safer than doing it only in the application form. (Industry rule)
3. Distinguish, with one example each from the given programs, between a compile-time error, a runtime exception and a logical error that produces wrong output silently. State which is the most dangerous in production and why. (Analytical, open-book)

**Homework**

1. Upload the corrected programs and the classification sheet; revise exception handling for the next session.

---

## Session 38 (Module 4) - Exception Handling and SQL versus PL/SQL

**Topics / Time / Teacher aid**

- Revision | 15 Min | Discussion
- Exception handling - introduction | 15 Min | PPT, Smartboard
- Predefined exceptions | 15 Min | PPT, Smartboard
- User-defined exceptions | 15 Min | PPT, Smartboard
- Handling raised exceptions | 15 Min | PPT, Smartboard
- SQL vs PL/SQL | 15 Min | PPT, Smartboard
- Practical 6: PL/SQL programs using exception handling | 30 Min | SQL Plus

**1. Session Execution Plan**

Formal treatment of exception handling after the practical exposure of the previous workshop, so theory follows experience. Faculty demonstrates each predefined exception by deliberately triggering it on a live table, then adds the handler and re-runs. SQLCODE and SQLERRM are introduced as the mechanism used by real applications to write error logs, and students build a small ERROR_LOG table and write their errors into it, which is standard industry practice.

**2. Detailed SOP**

- Step 1 (15 min): Revision of the workshop findings; outcome stated - 'student will make any PL/SQL program production-safe using predefined and user-defined exception handling with error logging.'
- Step 2 (15 min): Exception architecture explained - declare, raise, handle; the EXCEPTION section position in the block.
- Step 3 (15 min): Predefined exceptions NO_DATA_FOUND, TOO_MANY_ROWS, ZERO_DIVIDE, DUP_VAL_ON_INDEX, INVALID_NUMBER triggered live one by one and then handled.
- Step 4 (15 min): User-defined exceptions with DECLARE, RAISE and RAISE_APPLICATION_ERROR demonstrated on a business rule.
- Step 5 (15 min): WHEN OTHERS with SQLCODE and SQLERRM demonstrated; students create an ERROR_LOG table and insert the error details from the handler.
- Step 6 (15 min): SQL vs PL/SQL compared in a tabulated form derived from the session experience.
- Step 7 (30 min): Practical 6 executed; every program submitted must contain a working EXCEPTION section and must log to ERROR_LOG.
- Deliverable: Exception-safe programs plus an ERROR_LOG table containing at least three logged error entries with code, message and timestamp.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Write a block that fetches an employee's salary for a given id and handles the cases of no such employee, duplicate records and any other unexpected error separately, writing each failure into an ERROR_LOG table. (Production-standard program)
2. A block contains WHEN OTHERS THEN NULL. Explain what business risk this single line creates and rewrite it correctly. (Senior-level, real code-review issue)
3. A banking procedure must reject a withdrawal exceeding the balance with the message 'Insufficient funds'. Implement it using a user-defined exception and state why the error number must be between -20000 and -20999. (Industry rule, open-book)

**Homework**

1. Write the five exception-handling programs on the EMPLOYEE table (no data found, salary fetch, user-defined exception below 10,000, existence check, custom exception above 1,00,000) listed in the original plan.

---

## Session 39 (Module 4) - Database Security - Authentication, Authorization, Access Control, DAC and MAC

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Database security: Authentication, Authorization and Access control | 30 Min | PPT, Smartboard
- DAC (Discretionary Access Control) | 25 Min | PPT, Smartboard
- MAC (Mandatory Access Control) | 25 Min | PPT, Smartboard
- Practical Assignment-7: Problem solving and practice (Q16-Q20) | 30 Min | SQL Plus

**1. Session Execution Plan**

Security is taught through a role-mapping exercise on a system students know - the college ERP. Students list who can do what (student, faculty, HOD, exam cell, accounts) and the class derives authentication versus authorization from their own list. DAC is demonstrated live with GRANT between two student schemas, and MAC is explained through a defence or hospital classification example where the owner cannot decide access. A recent data-breach news item is used to show the cost of weak access control.

**2. Detailed SOP**

- Step 1 (10 min): Revision; outcome stated - 'student will design an access control scheme for a real application and will distinguish DAC from MAC with examples.'
- Step 2 (15 min): Role-mapping exercise on the college ERP - students build a who-can-do-what matrix in pairs.
- Step 3 (15 min): Authentication, authorization and access control defined from the student matrix; a recent database breach news item is discussed for impact.
- Step 4 (25 min): DAC demonstrated live - two students pair up, one grants SELECT on his table to the other, the other verifies access and then access is revoked.
- Step 5 (25 min): MAC explained with the hospital and defence classification model; DAC, MAC and RBAC compared in a table.
- Step 6 (30 min): Assignment-7 Q16-Q20 solved.
- Deliverable: An access control matrix for the college ERP and a working DAC demonstration log between two schemas.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Prepare an access control matrix for a hospital database covering doctor, nurse, receptionist, lab technician and accounts, listing the tables and the operations each may perform. Identify the one role that must never have DELETE and justify it. (Case study)
2. A clinic allows the record owner to share patient data with anyone he chooses. Explain which access control model this is, state the specific risk under medical data privacy rules, and state which model should replace it. (Industry judgement)
3. A former employee's database account was never disabled and was used to download data after he left. Identify every control that failed and write the SQL statements that would have prevented the incident. (Real incident analysis, open-book)

**Homework**

1. Watch the video links on database security, DAC, MAC and RBAC shared in the original plan and submit a one-page comparison note.

---

## Session 40 (Module 4) - AI-Powered Database Security Audit (AI Activity)

**Topics / Time / Teacher aid**

- Provide a Hospital or College ERP database scenario - briefing | 10 Min | Instructor Briefing, ChatGPT, AI Assistants
- Use AI tools to suggest security policies and user roles; verify AI recommendations against database security principles; design an access-control matrix | 80 Min | Group Formation, Execution
- Present security risks and improvements | 30 Min | AI-assisted Research, Presentation

**1. Session Execution Plan**

AI-integrated activity in which groups use ChatGPT or similar assistants to generate a security policy and role design for a hospital or college ERP, and then critically verify every AI recommendation against the principles studied in Session 39. The key learning objective is AI literacy with verification - students must mark each AI suggestion as correct, incomplete or wrong and must justify the verdict with a reason and, where possible, with an executed SQL statement.

**2. Detailed SOP**

- Step 1 (10 min): Faculty gives the scenario and the AI-usage rules - every prompt and response must be recorded, and no recommendation may be accepted without verification.
- Step 2 (25 min): Groups prompt the AI tool to propose user roles, privileges and security policies for the scenario; prompts and outputs are pasted into the worksheet.
- Step 3 (30 min): Verification phase - each AI recommendation is marked correct, incomplete or wrong with a written justification; at least three recommendations must be tested as actual GRANT or REVOKE statements in Oracle.
- Step 4 (25 min): Groups design the final access-control matrix combining verified AI output with their own corrections, and list the residual security risks.
- Step 5 (30 min): Presentations of 4 minutes per group covering the matrix, the AI errors they caught and the improvements proposed.
- Deliverable: Prompt-and-response log, verification sheet with verdicts, final access control matrix and a residual risk list uploaded on ERP.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The AI suggested granting DBA privilege to the application user for convenience. Explain why this is unacceptable, state the specific principle violated, and write the minimum set of privileges that should be granted instead. (AI verification, industry-oriented)
2. Design and justify the roles for a hospital ERP where a nurse may update vitals but not billing, and the accounts clerk may read billing but not diagnosis. Write the CREATE ROLE and GRANT statements. (Practical implementation)
3. List any two security recommendations produced by the AI tool that you found incomplete, state what was missing, and give the corrected recommendation. (Critical thinking, open-book)

**Homework**

1. Upload the AI prompt log, verification sheet and final matrix; prepare the role scripts for execution in the DCL session.

---

## Session 41 (Module 4) - SQL Injection - Attack and Prevention

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- SQL injection | 30 Min | PPT, Smartboard
- SQL injection examples | 20 Min | SQL Plus
- Practical Assignment-7: Problem solving and practice (Q21-Q25) | 40 Min | SQL Plus
- Doubt solving of concept, assignment and practical questions | 20 Min | SQL Plus

**1. Session Execution Plan**

Conducted as an ethical demonstration session. Faculty builds a deliberately vulnerable login query on the smartboard, and students see the classic ' OR '1'='1 bypass succeed on a test table. The attack is then defeated in front of the class using bind variables and input validation, and the difference is shown at the generated-SQL level. Students are briefed on the legal and ethical boundary - the technique is demonstrated only on the lab test schema.

**2. Detailed SOP**

- Step 1 (10 min): Revision of database security; ethical-use declaration explained and the outcome stated - 'student will identify an injectable query and will rewrite it securely using bind variables.'
- Step 2 (15 min): How a login query is built by string concatenation in application code, shown step by step.
- Step 3 (15 min): Live demonstration of the authentication bypass with ' OR '1'='1 and of a UNION-based data extraction on the lab test table only.
- Step 4 (20 min): Prevention demonstrated - bind variables, parameterised statements, input validation, least privilege and avoidance of dynamic SQL; the same attack is re-run and fails.
- Step 5 (40 min): Assignment-7 Q21-Q25 solved, including the rewriting of given vulnerable queries into safe ones.
- Step 6 (20 min): Open doubt-solving slot before the module ends.
- Deliverable: A before-and-after document showing one vulnerable query, the successful attack output, the secured version and proof that the attack now fails.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Given the query SELECT * FROM USERS WHERE username = 'input1' AND password = 'input2' built by concatenation, show the exact input that bypasses the login, explain why it works, and rewrite the query securely. (Classic unsolved industry problem)
2. An online complaint form passes the complaint id directly into a query. Demonstrate how an attacker could read another user's complaint, and list three controls - at code level, at database privilege level and at monitoring level - that together prevent it. (Case-based, layered defence)
3. Explain why granting the application user only SELECT, INSERT and UPDATE on specific tables limits the damage of a successful injection, and write the GRANT statements for such a least-privilege application account. (Open-book, senior-level)

**Homework**

1. Write the two SQL injection questions from the original plan - demonstrate the bypass and propose the secure alternative for the given EMPLOYEE query.

---

## Session 42 (Module 4) - PL/SQL Practice and Doubt Solving

**Topics / Time / Teacher aid**

- PL/SQL programs practice | 60 Min | SQL Plus
- Practical Assignment-7: Problem solving and practice (Q26-Q30) | 40 Min | SQL Plus
- Doubt solving of concept, assignment and practical questions | 20 Min | Discussion

**1. Session Execution Plan**

Dedicated practice lab for Module 4 conducted in examination mode with a printed question set. Students write complete programs - including the exception section - within fixed time boxes, and faculty evaluates not only the output but also code structure and error handling, which is the standard applied in the PLM practical examination.

**2. Detailed SOP**

- Step 1 (05 min): Printed question set distributed; evaluation standard announced - correctness 50, exception handling 20, structure and readability 20, output presentation 10.
- Step 2 (60 min): Programs practised in three timed blocks of 20 minutes each (control structures, cursors, exceptions); a 2-minute model discussion after each block.
- Step 3 (40 min): Assignment-7 Q26-Q30 solved individually.
- Step 4 (20 min): Open doubt-solving; faculty records the unresolved doubts and uploads written answers on ERP the same day.
- Deliverable: Complete Assignment-7 submission and a per-student readiness score for the Module-4 practical examination.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Write a complete, production-standard PL/SQL program that processes all employees of a given department, applies a slab-based increment using CASE, logs the number of rows processed, and handles the case where the department does not exist. (Integrated, examination-level)
2. For a library system, write a block that marks a book as unavailable when issued, raises a user-defined exception if the book is already issued, and logs every failure. (Industry program)
3. You are given a program that compiles but produces wrong totals. List the three debugging steps you would perform in order, and state what you would print at each step. (Analytical, open-book)

**Homework**

1. Complete all pending Module-4 work and the SEE-4 submission.

---

## Session 43 (Module 4) - AI-Generated Mini Project Development (AI Activity)

**Topics / Time / Teacher aid**

- Assign a domain (Hospital, Library, Banking, College ERP) - briefing | 15 Min | Instructor Briefing
- Use AI tools to generate database schema, PL/SQL procedures, security policies and exception handling mechanisms | 55 Min | Activity Execution
- Validate all AI-generated content | 20 Min | Student Skill Enhancement
- Each group demonstrates the working solution and reflects on strengths and limitations of AI assistance | 30 Min | Presentation

**1. Session Execution Plan**

Project-based AI literacy activity. Groups use an AI assistant to generate a complete small database solution for an assigned domain, then must make it actually run in Oracle - which is where AI output typically fails (non-Oracle syntax, missing semicolons, invalid datatypes, logically wrong joins). Students record every correction they had to make, and the reflection on AI limitations is itself an assessed deliverable, supporting industry readiness and AI literacy.

**2. Detailed SOP**

- Step 1 (15 min): Domains allotted, deliverable defined (schema with at least 4 tables, 2 procedures, 1 trigger-ready rule, security policy, exception handling) and the correction log format explained.
- Step 2 (55 min): Groups generate the solution using AI tools, saving every prompt and output.
- Step 3 (20 min): Validation phase - all generated code is executed in Oracle; each error is corrected and recorded in the correction log with the reason the AI output was wrong.
- Step 4 (30 min): Each group demonstrates the running solution for 4 minutes and presents two strengths and two limitations of AI assistance observed first-hand.
- Step 5: Project files, prompt log and correction log uploaded on ERP as the Module-4 AI activity deliverable.
- Deliverable: A working mini database solution in Oracle, the AI prompt log and a correction log listing every AI error found and fixed.

**3. Real-Life / Unsolved / Open-Book Questions**

1. The AI generated a procedure using MySQL syntax (AUTO_INCREMENT and LIMIT). Rewrite it correctly for Oracle and list every change you made. (Real AI limitation, practical)
2. Validate the AI-generated schema for your domain against normalization rules and state at least one design flaw it contains, with the corrected design. (Analytical)
3. State two tasks in this activity where AI assistance clearly saved time and two where it introduced errors that only domain knowledge could catch. Support each with a concrete example from your own project. (Reflection, industry readiness)

**Homework**

1. Upload the mini project, prompt log and correction log; prepare the demonstration for evaluation.

---

## Session 44 (Module 5) - Stored Procedures and Stored Functions

**Topics / Time / Teacher aid**

- Revision | 10 Min | PPT, Smartboard
- Stored procedures | 20 Min | PPT, Smartboard
- Stored functions | 20 Min | PPT, Smartboard
- Stored procedures examples | 20 Min | SQL Plus
- Stored functions examples | 20 Min | SQL Plus
- Practical 1: Creating stored procedures and functions | 30 Min | SQL Plus

**1. Session Execution Plan**

Introduced through the reuse problem - the same salary calculation logic written in three different programs - which students have actually experienced in earlier sessions. The procedure is then presented as named, stored, reusable logic. IN, OUT and IN OUT parameters are demonstrated with a real requirement (pass employee id, return salary and grade). The function is distinguished by the fact that it can be called inside a SELECT, which is demonstrated live and is a standard examination point.

**2. Detailed SOP**

- Step 1 (10 min): Revision of anonymous blocks; the reuse problem posed; outcome stated - 'student will create, call and debug stored procedures and functions with correct parameter modes.'
- Step 2 (20 min): CREATE OR REPLACE PROCEDURE syntax, compilation, SHOW ERRORS and execution demonstrated; faculty deliberately introduces a compile error and uses SHOW ERRORS and USER_ERRORS to locate it.
- Step 3 (20 min): IN, OUT and IN OUT parameters demonstrated with a get-salary-and-grade requirement; calling from an anonymous block with host variables shown.
- Step 4 (20 min): Functions created and called from SELECT, WHERE and from a PL/SQL block; restrictions on functions used in SQL explained.
- Step 5 (20 min): Procedure versus function compared in a table built from the live examples.
- Step 6 (30 min): Practical 1 executed; each student creates at least one procedure with an OUT parameter and one function called from a SELECT.
- Deliverable: Two compiled database objects - one procedure with OUT parameter and one function used inside a SELECT, with execution output.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Create a function that returns the total salary payable for a given department, and use it inside a SELECT that lists every department with its payable amount. State why this cannot be done with a procedure. (Industry reporting requirement)
2. A procedure must return both the employee's salary and a computed grade to the calling program. Write it with the correct parameter modes and show the calling block. (Application-oriented)
3. A stored procedure compiled with errors and the developer cannot see why. List the exact steps and queries you would use to find the error, and state one common cause related to privileges. (Open-book, practical troubleshooting)

**Homework**

1. Create the PRODUCT and EMPLOYEE procedures and functions listed in the original plan - display product details, increase price by 10 percent with row count, cursor listing, employee salary procedure and total salary function.

---

## Session 45 (Module 5) - Stored Procedures and Stored Functions - Practice Session

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Practical Assignment-8: Problem solving and practice (Q1-Q20) | 110 Min | SQL Plus

**1. Session Execution Plan**

Extended hands-on lab on named program units. Students convert the anonymous blocks written in Module 4 into reusable procedures and functions, which makes the value of modularity concrete. Faculty enforces a coding standard - naming convention, parameter prefixes, mandatory exception section and a header comment - so that all three faculty members teaching this subject evaluate against the same standard.

**2. Detailed SOP**

- Step 1 (10 min): Revision and announcement of the common coding standard (p_ for parameters, v_ for variables, mandatory header comment and EXCEPTION section).
- Step 2 (40 min): Q1-Q7 - conversion of earlier anonymous blocks into procedures; faculty verifies compilation and naming standard.
- Step 3 (40 min): Q8-Q14 - functions returning computed business values, called from SELECT statements.
- Step 4 (30 min): Q15-Q20 - procedures with OUT parameters and exception handling; faculty conducts a 2-question viva for each student while they work.
- Deliverable: A compiled script library of at least 20 procedures and functions following the common coding standard, submitted on ERP.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Convert any three anonymous blocks written in Module 4 into stored procedures with proper parameters and exception sections, and explain one maintenance benefit gained. (Application)
2. Create a function that returns the number of days a library book is overdue for a given issue id, returning zero when it is not overdue, and use it in a SELECT listing all defaulters with the fine computed at Rs. 2 per day. (Industry problem)
3. Two procedures in your library have the same name but different parameters. Explain whether Oracle allows this at schema level, and how packages change the answer. (Open-book, senior-level)

**Homework**

1. Create the STUDENT procedure and function listed in the original plan - display student name and marks for a given id, and return average marks of all students.

---

## Session 46 (Module 5) - Packages

**Topics / Time / Teacher aid**

- Revision | 20 Min | Discussion
- Packages | 20 Min | PPT, Smartboard
- Packages example | 20 Min | SQL Plus
- Practical 2: Creating and using packages | 30 Min | SQL Plus
- Practical Assignment-8: Problem solving and practice (Q21-Q22) | 40 Min | SQL Plus

**1. Session Execution Plan**

The package is introduced as the industry answer to the script-library mess created in the previous session - 30 loose procedures with no organisation. Faculty groups the students' own procedures into a single HR_PKG with specification and body, demonstrating encapsulation, the public-private distinction and overloading. The practical benefit of a package - changing the body without invalidating dependent objects - is demonstrated live.

**2. Detailed SOP**

- Step 1 (20 min): Revision; the loose-procedure problem shown by listing USER_OBJECTS; outcome stated - 'student will organise related program units into a package and will use public and private subprograms correctly.'
- Step 2 (20 min): Package specification and body explained; the specification of HR_PKG is written with the class.
- Step 3 (20 min): Body implemented, including one private procedure not listed in the specification, and the resulting access error is demonstrated when it is called from outside.
- Step 4 (10 min): Overloading demonstrated with two subprograms of the same name and different parameters; dependency advantage shown by altering the body and verifying that dependent objects stay valid.
- Step 5 (30 min): Practical 2 executed - each student builds a package for his own domain with at least one procedure, one function and one private subprogram.
- Step 6 (40 min): Assignment-8 Q21-Q22 solved.
- Deliverable: A compiled package with specification and body containing at least three subprograms including one private, with execution output.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Build a PRODUCT_PKG containing a procedure to display product details, a function returning total stock and a private procedure that writes to an audit table. Demonstrate that the private procedure cannot be called from outside the package. (Industry design)
2. Explain, with the dependency scenario demonstrated in class, why changing a package body does not invalidate dependent objects while changing a standalone procedure can cause recompilation. (Senior-level, analytical)
3. Design the specification only of a package that a banking application would need for account operations, listing the subprograms and their parameters, without writing the body. Justify what you kept public and what you kept private. (Open-book design task)

**Homework**

1. Create the five PRODUCT package exercises listed in the original plan - product details procedure, total stock function, price update procedure, highest price function and the combined package.

---

## Session 47 (Module 5) - Cursor Implementation - Practice Session

**Topics / Time / Teacher aid**

- Revision | 20 Min | Discussion
- Practical 3: Implement cursor | 40 Min | SQL Plus
- Practical Assignment-8: Problem solving and practice (Q23-Q24) | 20 Min | SQL Plus
- Doubt solving of concept, assignment and practical questions | 40 Min | Discussion

**1. Session Execution Plan**

Advanced cursor practice at Module-5 level, where cursors are now used inside procedures, functions and packages rather than in loose blocks. Faculty introduces cursors with FOR UPDATE and WHERE CURRENT OF, which is the pattern used in real batch-update jobs, and discusses the performance consideration of row-by-row processing versus set-based SQL - a point frequently asked at senior level.

**2. Detailed SOP**

- Step 1 (20 min): Revision of all cursor types; outcome stated - 'student will implement cursors inside named program units and will justify row-by-row processing against set-based SQL.'
- Step 2 (15 min): Cursor with FOR UPDATE and WHERE CURRENT OF demonstrated on a batch salary revision.
- Step 3 (25 min): Practical 3 executed - students implement a cursor inside a stored procedure of their own package.
- Step 4 (20 min): Assignment-8 Q23-Q24 solved.
- Step 5 (40 min): Structured doubt-solving - students write their doubts on the board, doubts are grouped into themes and resolved theme by theme, with the solutions uploaded afterwards.
- Deliverable: A procedure containing a FOR UPDATE cursor performing a controlled batch update, with before-and-after data evidence.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Write a procedure that increases by 7 percent the salary of every employee of a given department using a cursor with FOR UPDATE and WHERE CURRENT OF, and explain what the lock protects against. (Industry batch job)
2. The same requirement can be done by a single UPDATE statement. Compare the two approaches on correctness, performance and locking, and state when the cursor version is genuinely justified. (Senior-level comparison)
3. A cursor-based job on 5 lakh rows takes 20 minutes and times out. Suggest two concrete changes and state the expected improvement from each. (Open-book, performance problem)

**Homework**

1. Write the three cursor programs on the EMPLOYEE table listed in the original plan - explicit cursor listing, cursor FOR loop for the IT department and a parameterized cursor.

---

## Session 48 (Module 5) - Triggers and Types of Triggers, Users - Create and Delete User

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Triggers introduction | 10 Min | PPT, Smartboard
- Types of triggers | 20 Min | PPT, Smartboard
- Users - Create user | 10 Min | PPT, Smartboard
- Users - Delete user | 10 Min | PPT, Smartboard
- Testing triggers: BEFORE, AFTER, INSTEAD OF (row/statement level) | 20 Min | PPT, Smartboard
- Practical 4: Implement trigger | 20 Min | SQL Plus
- Practical Assignment-8: Problem solving and practice (Q25-Q26) | 20 Min | SQL Plus

**1. Session Execution Plan**

Triggers are introduced through the audit requirement every organisation has - 'who changed this salary and when'. Faculty builds a salary audit trigger live, then shows it firing automatically on an UPDATE, which makes the concept of an event-driven program unit immediate. BEFORE versus AFTER and row versus statement level are demonstrated by printing messages from each, so students see the firing order. User creation is then performed practically, with each student creating a user for his own application.

**2. Detailed SOP**

- Step 1 (10 min): Revision; the audit requirement posed; outcome stated - 'student will implement auditing and business-rule enforcement using triggers and will create and manage database users.'
- Step 2 (20 min): Trigger concept, firing events and the classification into BEFORE, AFTER, row-level and statement-level explained; a trigger that prints a message at each of the four points is run once to show the firing order.
- Step 3 (20 min): A salary audit trigger built live using :OLD and :NEW, writing to an AUDIT_SALARY table; an UPDATE is executed and the audit row is shown.
- Step 4 (20 min): CREATE USER, ALTER USER, DROP USER and the required CREATE SESSION privilege demonstrated; each student creates one application user.
- Step 5 (20 min): Practical 4 executed - each student implements one audit trigger and one rule-enforcement trigger.
- Step 6 (20 min): Assignment-8 Q25-Q26 solved.
- Deliverable: A working audit trigger with populated audit table and a created application user with login verified.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A company must record who changed any employee's salary, the old value, the new value and the timestamp. Implement this with a trigger and show the audit table after two updates. (Compliance requirement)
2. A rule states that no employee record may be deleted from the EMPLOYEE table during working hours. Implement it with a trigger and state one disadvantage of enforcing such policy in a trigger rather than in the application. (Industry rule, judgement)
3. Explain the difference between a BEFORE INSERT row-level trigger and an AFTER INSERT statement-level trigger using the firing-order output observed in class, and state which one you would use to generate a primary key value and why. (Open-book, senior-level)

**Homework**

1. Create the three EMPLOYEE triggers listed in the original plan - BEFORE INSERT preventing salary below 10,000, AFTER UPDATE message on salary change, and BEFORE DELETE preventing deletion.

---

## Session 49 (Module 5) - Revision of Stored Procedures, Functions, Packages and Triggers; SEE-5 and ALA Explanation

**Topics / Time / Teacher aid**

- Revision - stored procedures and stored functions | 20 Min | Discussion
- Revision - packages | 10 Min | PPT, White Board
- Revision - trigger | 10 Min | PPT, White Board
- Practical 5: Writing and testing triggers - BEFORE, AFTER, INSTEAD OF (row/statement level) | 30 Min | SQL Plus
- Practical 6: Creating and managing users - CREATE and DELETE USER | 30 Min | SQL Plus
- Explanation of SEE-5 and ALA of Module 5 - student instructions | 20 Min | Explanation

**1. Session Execution Plan**

Consolidation session for Module 5 conducted as an integration exercise - students combine their procedures, functions, package and triggers into one coherent application schema for their chosen domain and demonstrate it end to end. INSTEAD OF triggers are covered here on a complex view, which completes the trigger topic. The session closes with the formal SEE-5 and ALA-5 briefing.

**2. Detailed SOP**

- Step 1 (40 min): Revision of procedures, functions, packages and triggers through a single integrated example built with class participation.
- Step 2 (30 min): Practical 5 - students write and test BEFORE, AFTER and INSTEAD OF triggers, the last one on a join-based view to demonstrate updatable views.
- Step 3 (30 min): Practical 6 - user creation, privilege assignment, password policy, locking and dropping of a user; each student verifies login from a second session.
- Step 4 (20 min): SEE-5 and ALA-5 explained - problem statement, deliverable format, rubric, deadline and ERP submission steps.
- Deliverable: An integrated application schema containing package, triggers and a dedicated application user, with a demonstration log.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A view joins EMPLOYEE and DEPARTMENT and the application needs to insert through it. Explain why a plain INSERT fails and implement the solution with an INSTEAD OF trigger. (Senior-level practical)
2. Create an application user with the minimum privileges required to run your package and nothing more, then verify from a second session that the user cannot query the base tables directly. (Industry least-privilege task)
3. For your domain application, list which business rules you implemented as constraints, which as triggers and which in PL/SQL procedures, and justify each placement. (Design judgement, open-book)

**Homework**

1. Complete the ALA-5 deliverable as instructed.

---

## Session 50 (Module 5) - SQL Escape Room - Advanced PL/SQL (Activity)

**Topics / Time / Teacher aid**

- Faculty gives SQL puzzles - briefing | 15 Min | Instructor Briefing
- Students solve SQL puzzles within a time limit; each query result unlocks the next room; the final challenge requires combining multiple SQL concepts | 90 Min | Solve puzzles
- Students feedback | 15 Min | Discussion

**1. Session Execution Plan**

Second gamified assessment, now at Module 4-5 level. The rooms require PL/SQL rather than plain SQL - a room is unlocked by the output of a function the team must write, by the audit row produced by a trigger they must create, and by the value returned by a package subprogram. The final room is an integrated challenge combining joins, a cursor, exception handling and a trigger, closely modelled on the standard of the PLM sessional practical examination.

**2. Detailed SOP**

- Step 1 (15 min): Faculty loads the puzzle schema, forms teams, explains the unlock mechanism and starts the timer; the leaderboard is displayed.
- Step 2 (20 min): Room 1 - write a function whose returned value is the key to Room 2.
- Step 3 (20 min): Room 2 - write a procedure with an OUT parameter and exception handling; the logged error message is the key to Room 3.
- Step 4 (20 min): Room 3 - create a trigger; the audit row generated is the key to Room 4.
- Step 5 (30 min): Room 4 - the integrated final challenge combining a multi-table query, a cursor and exception handling; completion times recorded.
- Step 6 (15 min): Feedback and debrief - the fastest team explains its approach, the faculty gives the model solution for every room.
- Deliverable: Team code log for all four rooms, leaderboard record and individual reflection on the concept that proved weakest.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Room-style question: write a function that returns the name of the customer with the highest total purchase in the last quarter; the returned name is your key. (Integrated application)
2. Room-style question: create a trigger that logs every attempt to delete a product that still has pending orders, and block the deletion; the logged message is your key. (Industry rule)
3. Final-room-style question: using a cursor, exception handling and a multi-table join, produce a defaulter report for a library with the fine computed per member, handling the case of a member with no issues. (Examination-standard integrated problem)

**Homework**

1. Submit the team code log and the individual reflection note.

---

## Session 51 (Module 5) - DCL Commands - GRANT and REVOKE; TPL - BEGIN TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT

**Topics / Time / Teacher aid**

- Data Control Language (DCL) commands | 10 Min | Discussion
- Grant and Revoke | 20 Min | PPT, Smartboard
- Transaction Processing Language (TPL) | 10 Min | PPT, Smartboard
- BEGIN TRANSACTION | 10 Min | PPT, Smartboard
- COMMIT, ROLLBACK and SAVEPOINT | 30 Min | PPT, Smartboard, SQL Plus
- ROLLBACK TO SAVEPOINT | 10 Min | PPT, Smartboard
- Practical 7: Using GRANT and REVOKE | 30 Min | SQL Plus

**1. Session Execution Plan**

Executed as a paired practical - students work in pairs as two different database users and grant, use and revoke privileges on each other's objects in real time, immediately seeing the ORA-00942 error when a privilege is missing or revoked. This makes access control tangible. The transaction control portion revisits COMMIT, ROLLBACK and SAVEPOINT now in the context of a banking application and connects back to the ACID discussion of Session 30.

**2. Detailed SOP**

- Step 1 (10 min): Outcome stated - 'student will grant and revoke object and system privileges correctly and will control transaction boundaries in a multi-user environment.'
- Step 2 (20 min): GRANT and REVOKE of object privileges (SELECT, INSERT, UPDATE, DELETE), WITH GRANT OPTION and the cascading effect of a revoke demonstrated live between two student schemas.
- Step 3 (20 min): TPL concepts revisited - implicit transaction start, COMMIT, ROLLBACK and SAVEPOINT, and the behaviour of a DDL in the middle of a transaction.
- Step 4 (20 min): ROLLBACK TO SAVEPOINT demonstrated on a multi-step banking transaction; students predict the final row count before the statement is run and then verify.
- Step 5 (30 min): Practical 7 executed in pairs; each pair records the error observed before the grant and after the revoke.
- Deliverable: A privilege log sheet per pair showing the statement, the user who ran it, and the result or error before and after each grant and revoke.

**3. Real-Life / Unsolved / Open-Book Questions**

1. A reporting team needs read-only access to two tables of your schema and must not be able to pass this access to anyone else. Write the exact statements, verify from the other session, and then revoke the access. (Industry task)
2. User A granted SELECT to user B with the grant option, and B granted it to C. A now revokes from B. State what happens to C's access and justify the Oracle behaviour. (Senior-level, analytical)
3. A bank transaction must insert three rows, and if the third fails, the first two must still be retained but a fourth corrective row must be added. Write the complete statement sequence using SAVEPOINT. (Open-book, application-oriented)

**Homework**

1. Create the ACCOUNT table and perform the SAVEPOINT, COMMIT and ROLLBACK exercises listed in the original plan, recording the output after each step.

---

## Session 52 (Module 5) - Locking Strategies - Implicit and Explicit Locking, LOCK TABLE Command

**Topics / Time / Teacher aid**

- Revision | 10 Min | Discussion
- Locking strategies - introduction | 10 Min | PPT, Smartboard
- Implicit locking | 20 Min | PPT, Smartboard
- Explicit locking | 20 Min | PPT, Smartboard
- LOCK TABLE command | 15 Min | SQL Plus
- Practical 8: Demonstrating transaction control with SAVEPOINT and rollback | 25 Min | SQL Plus
- Practical Assignment-8: Problem solving and practice (Q27-Q28) | 20 Min | SQL Plus

**1. Session Execution Plan**

Locking is demonstrated, not described. Two students update the same row from two sessions and the class watches the second session hang, which is a row-level lock experienced live. The lock is then released by a commit and the second session proceeds. A deadlock is created deliberately between two sessions to show Oracle's automatic detection and the ORA-00060 message. SELECT FOR UPDATE and LOCK TABLE are then introduced as the explicit controls used in booking systems.

**2. Detailed SOP**

- Step 1 (10 min): Revision of transactions; outcome stated - 'student will explain and demonstrate locking behaviour in a multi-user database and will use explicit locks appropriately.'
- Step 2 (20 min): Implicit row-level locking demonstrated by two students updating the same row from two sessions; the class observes the blocked session and the release on commit.
- Step 3 (15 min): Deadlock created deliberately between two sessions in reverse order; ORA-00060 shown and the prevention rule (consistent access order) derived.
- Step 4 (20 min): SELECT FOR UPDATE, NOWAIT and LOCK TABLE in various modes demonstrated with the seat-booking scenario.
- Step 5 (25 min): Practical 8 executed in pairs with an observation log of which session waited and for how long.
- Step 6 (20 min): Assignment-8 Q27-Q28 solved.
- Deliverable: A locking observation log recording the blocked session, the waiting time, the deadlock error number and the resolution.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Two counter clerks of a cinema try to book the same seat at the same instant. Explain the exact locking behaviour Oracle applies, write the SELECT FOR UPDATE statement that makes the booking safe, and state what the second clerk sees. (Real-time scenario)
2. A nightly batch job and an online user deadlocked at 2 am and the job aborted with ORA-00060. Explain how the deadlock arose and state the one design discipline that prevents such deadlocks. (Industry incident)
3. Explain the practical difference between SELECT FOR UPDATE and SELECT FOR UPDATE NOWAIT, and state which one a customer-facing booking screen should use and why. (Open-book, senior-level judgement)

**Homework**

1. Complete all pending practical and assignment work before the Module-5 evaluation.

---

## Session 53 (Module 5) - Oracle Database Privileges and Roles - System and Object Privileges, Assigning, Viewing, Revoking, Roles

**Topics / Time / Teacher aid**

- ORACLE database privileges and roles | 10 Min | Discussion
- System privileges | 10 Min | PPT, Smartboard
- Object privileges | 10 Min | PPT, Smartboard
- Assigning privileges | 10 Min | PPT, Smartboard
- Viewing privileges | 20 Min | PPT, Smartboard
- Revoking privileges | 20 Min | PPT, Smartboard
- Roles - create, grant, view and delete | 20 Min | PPT, Smartboard
- Practical Assignment-8: Problem solving and practice (Q29) | 20 Min | SQL Plus

**1. Session Execution Plan**

The final conceptual session implements the access control matrix that students designed in the Module-4 AI security activity. Roles are introduced as the solution to the unmanageable position of granting privileges to 50 individual users, and students implement the complete role structure of their own domain application, then verify it through the dictionary views USER_SYS_PRIVS, USER_TAB_PRIVS and USER_ROLE_PRIVS - which is exactly how an auditor verifies access in a real organisation.

**2. Detailed SOP**

- Step 1 (10 min): The 50-user problem posed; outcome stated - 'student will implement and audit a complete role-based access control scheme.'
- Step 2 (20 min): System versus object privileges distinguished with examples; the ANY privileges and their risk discussed.
- Step 3 (20 min): Roles created, privileges granted to roles, roles granted to users, default roles, and role removal demonstrated live.
- Step 4 (20 min): Viewing privileges through USER_SYS_PRIVS, USER_TAB_PRIVS, USER_ROLE_PRIVS and SESSION_PRIVS; students audit their own account.
- Step 5 (20 min): Revoking privileges and roles, and the effect on currently connected sessions, demonstrated.
- Step 6 (20 min): Assignment-8 Q29 solved - the full role implementation of the student's own domain application.
- Deliverable: Implemented role structure with a privilege audit report generated from the dictionary views, matching the access control matrix designed earlier.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Implement the access control matrix your group designed in the AI security activity using roles - create the roles, grant the privileges, assign them to users, and produce the audit report from the dictionary views that proves correct implementation. (Integrated industry task)
2. A developer has been granted SELECT ANY TABLE 'temporarily' on the production database. State the specific risk, the minimum alternative privilege set, and the statements to correct the position. (Real-life audit finding)
3. An auditor asks you to prove which users can modify the SALARY table. Write the queries you would run on the dictionary views and explain how a privilege granted through a role would appear in your output. (Open-book, senior-level)

**Homework**

1. Complete the three privilege and role exercises listed in the original plan - create a user with CREATE SESSION and CREATE TABLE, grant and revoke SELECT and UPDATE on EMPLOYEE, and create, assign and remove the EMP_ROLE role.

---

## Session 54 (Exam) (Module 3, 4 & 5) - Sessional Examination - II (Module 3, 4 and 5)

**Topics / Time / Teacher aid**

- Sessional Examination - II (Module 3, 4 and 5) as per institute examination schedule | 120 Min | Examination

**1. Session Execution Plan**

Formal second sessional examination covering Modules 3, 4 and 5, set to the PLM standard with a majority of application, case-based and open-book style questions drawn from the session-wise question banks of Sessions 23 to 53.

**2. Detailed SOP**

- Step 1: Common question paper prepared jointly by MCS, DPZ and YGL with a minimum of 50 percent application and case-based questions and at least one open-book query-writing question.
- Step 2: Examination conducted as per the examination cell seating and timing plan.
- Step 3: Evaluation against a common rubric agreed by all three faculty members before assessment begins.
- Step 4: Question-wise performance analysis prepared and shared.
- Step 5: Remedial sessions scheduled for the identified weak topics before the end-semester examination.
- Deliverable: Evaluated answer sheets, question-wise analysis and remedial plan.

**3. Real-Life / Unsolved / Open-Book Questions**

1. Paper to include a full case-based design and query question on a given business domain.
2. Paper to include a PL/SQL program-writing question with mandatory exception handling.
3. Paper to include an unsolved production-situation question on locking, privileges or recovery.

**Homework**

1. Review the evaluated paper and submit corrections of all wrong answers.

---

## Session 55 (Module 5) - Database Innovation Hackathon using AI (AI Activity)

**Topics / Time / Teacher aid**

- Develop a mini database solution collaboratively - briefing | 15 Min | Instructor Briefing
- Teams design and implement a complete database application | 60 Min | Implementation
- Include procedures, functions, triggers, security and reports | 15 Min | Discussion
- Present the final solution | 30 Min | Presentation

**1. Session Execution Plan**

Capstone activity of the subject. Teams build a complete working database application for a self-chosen problem within a fixed time, using AI assistance where useful but validating every generated artefact. The solution must include a normalized schema, constraints, a package of procedures and functions, at least two triggers, a role-based security scheme and three management reports - that is, every major outcome of the subject in one deliverable. Judging is done against an industry-style rubric and the best solutions are recommended for the departmental project showcase.

**2. Detailed SOP**

- Step 1 (15 min): Teams of 4 formed, problem statements approved by the faculty, rubric announced (schema and normalization 20, program units 20, triggers and security 20, reports 20, presentation and AI reflection 20).
- Step 2 (20 min): Design sprint - ER diagram, normalized schema and the list of three reports to be produced, approved by faculty before coding starts.
- Step 3 (40 min): Implementation sprint - tables with constraints, package with procedures and functions, triggers for audit and rule enforcement, roles and grants.
- Step 4 (15 min): Report sprint - three management queries executed and their output captured; AI-generated code validated and the correction log completed.
- Step 5 (30 min): Each team demonstrates the working solution for 5 minutes, answers cross-questions from the panel and states two limitations of its design.
- Step 6: Final submission on ERP - script file, design document, report output and AI reflection note.
- Deliverable: A complete working database application with script, design document, report output and AI usage reflection, evaluated against the hackathon rubric.

**3. Real-Life / Unsolved / Open-Book Questions**

1. For your hackathon problem, state the three reports the management of that organisation would need weekly and write the SQL that produces them. (Industry-oriented)
2. Identify one business rule in your solution that you enforced with a trigger and explain why a constraint could not have done it. (Design justification)
3. State one limitation of your solution that would appear only when the data grows to 10 lakh rows, and the change you would make to address it. (Senior-level, scalability)

**Homework**

1. Upload the final hackathon submission with all artefacts; complete any pending ALA and SEE deliverables.

---

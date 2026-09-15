PLM MESA Examination Portal - Paper A + Paper B

Examiner login: examiner / exam123

This version adds:
- Live student monitoring: submitted tasks and remaining tasks
- Per-student ENABLE / DISABLE exam access control
- Students cannot log in or open tasks while disabled
- Student completion PDF becomes available after all 3 tasks are submitted
- Examiner can download/review a readable PDF for each completed student
- Examiner can manually enter 0-10 marks for each task and optional notes
- Marks are saved in SQLite and included in regenerated PDFs
- Paper A and Paper B assignment remains automatic

Run:
1. Install dependencies: pip install -r requirements.txt
2. Run: python app.py
3. Open: http://127.0.0.1:5000

The database is created/migrated automatically in data/plm_exam.db.
Examiner password remains exam123.

STUDENT FINAL-SUBMISSION RULES
- SAVE stores the latest working answer and keeps the task editable.
- SUBMIT TASK permanently submits that task, locks all answers, and returns the student to the task dashboard.
- A submitted task cannot be opened again.
- FINAL SUBMIT PAPER permanently submits and locks all remaining saved answers for all three tasks.
- Empty answers/selections are normalized to NIL at final submission and included in the examiner PDF.
- The student dashboard includes an exam countdown; the configured exam duration is 120 minutes but the duration is not displayed as a total on the examiner dashboard.
- When the countdown reaches zero, the browser automatically performs the same final-paper submission using the latest SAVED answers.

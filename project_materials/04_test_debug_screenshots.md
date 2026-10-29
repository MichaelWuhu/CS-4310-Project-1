# Task 4: Test, Debug, and Capture Screenshots

Give the model all four program files and use this prompt:

```text
Act as a testing and debugging reviewer for my CPU scheduling project.

Review:
- fcfs.py
- sjf.py
- rr2.py
- rr5.py

Check that:
1. All programs correctly read job.txt.
2. FCFS uses input order.
3. SJF sorts by burst time and preserves input order for ties.
4. RR-2 uses quantum 2.
5. RR-5 uses quantum 5.
6. All jobs arrive at time 0.
7. Turnaround time equals completion time.
8. Average turnaround time is calculated correctly.
9. The execution schedule shows job name, start time, stop time, and burst used.
10. The output is readable.

Run all programs using these expected results:

5 jobs:
FCFS 31.40
SJF 24.00
RR-2 36.40
RR-5 36.00

10 jobs:
FCFS 54.10
SJF 38.90
RR-2 66.10
RR-5 66.70

15 jobs:
FCFS 79.07
SJF 54.47
RR-2 95.80
RR-5 94.87

Fix any errors you find. Then explain exactly how to run each program and which output should be captured for the four screenshots.
```

Capture four screenshots total: one for each program running successfully.

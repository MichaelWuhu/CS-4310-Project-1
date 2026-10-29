# Task 3: Implement RR-2 and RR-5

Give the following prompt to an AI model. Include the programs from Task 2 and the design file if available.

```text
Implement two separate Python programs for my CPU scheduling project.

Create:
1. rr2.py
2. rr5.py

Input:
- Read job.txt.
- The file contains alternating job names and burst times.
- All jobs arrive at time 0.
- Jobs enter the ready queue in input order.

Requirements:
- rr2.py uses a time quantum of 2.
- rr5.py uses a time quantum of 5.
- Use a FIFO ready queue.
- When a job uses its full quantum and still has remaining burst time, place it at the back of the queue.
- When a job finishes, record its completion time.
- Calculate each job's turnaround time.
- Calculate and display the average turnaround time.
- Display every execution segment with job name, start time, stop time, and amount executed.
- Include comments and documentation.
- Do not combine the programs into one file.
- Do not change the required input format.
- Test using the provided 5-, 10-, and 15-job cases.
```

Expected files: `rr2.py` and `rr5.py`.

Expected averages:

| Jobs | RR-2 | RR-5 |
|---:|---:|---:|
| 5 | 36.40 | 36.00 |
| 10 | 66.10 | 66.70 |
| 15 | 95.80 | 94.87 |

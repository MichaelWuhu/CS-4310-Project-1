# Task 2: Implement FCFS and SJF

Give the following prompt to an AI model. Include the design file from Task 1 if available.

```text
Implement two separate Python programs for my CPU scheduling project.

Create:
1. fcfs.py
2. sjf.py

Input:
- Read job.txt.
- The file contains alternating job names and burst times.

Requirements:
- All jobs arrive at time 0.
- FCFS must process jobs in input order.
- SJF must process jobs in ascending burst-time order.
- Preserve original order when burst times are tied.
- Calculate each job's completion time, which is also its turnaround time because all jobs arrive at time 0.
- Calculate and display the average turnaround time.
- Display a readable execution schedule showing job name, start time, stop time, and burst used.
- Include comments and documentation inside each file.
- Do not combine the programs into one file.
- Do not change the required input format.
- Test both programs using the provided 5-, 10-, and 15-job test cases and report the resulting averages.
```

Expected files: `fcfs.py`, `sjf.py`, and `job.txt`.

Expected averages:

| Jobs | FCFS | SJF |
|---:|---:|---:|
| 5 | 31.40 | 24.00 |
| 10 | 54.10 | 38.90 |
| 15 | 79.07 | 54.47 |

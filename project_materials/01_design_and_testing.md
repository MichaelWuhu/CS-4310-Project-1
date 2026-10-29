# Task 1: Design and Testing Plan

Give the following prompt to an AI model:

```text
I am completing a CS 4310 Operating Systems project about CPU scheduling.

The project requires four separate programs:
1. First-Come-First-Serve (FCFS)
2. Shortest-Job-First (SJF)
3. Round-Robin with quantum 2 (RR-2)
4. Round-Robin with quantum 5 (RR-5)

Requirements:
- Read jobs from job.txt.
- The file contains alternating job names and burst times.
- All jobs arrive at time 0.
- FCFS, RR-2, and RR-5 use the order in which jobs appear.
- SJF sorts jobs by shortest burst time.
- There are no more than 30 jobs.
- Calculate and display each job's completion/turnaround time.
- Calculate the average turnaround time.
- Show the execution order and time intervals.
- Create separate program files.
- Use Python.
- Keep tie-breaking deterministic: preserve original order when two jobs have equal burst times.

Do not write the implementation yet.

Create:
1. Clear pseudocode for FCFS.
2. Clear pseudocode for SJF.
3. Clear pseudocode for RR-2.
4. Clear pseudocode for RR-5.
5. A short explanation of how turnaround time is calculated.
6. A testing strategy for random inputs of 5, 10, and 15 jobs.
7. Explain why the same input set must be used for all four algorithms.

Keep the explanations appropriate for a student report.
```

Save the result as `design_and_testing.md`.

## Standard testing data

Use these three cases in Part 1(b).

### Case 1: 5 jobs

```text
Job1
7
Job2
18
Job3
10
Job4
4
Job5
12
```

Expected averages: FCFS `31.40`, SJF `24.00`, RR-2 `36.40`, RR-5 `36.00`.

### Case 2: 10 jobs

```text
Job1
7
Job2
18
Job3
10
Job4
4
Job5
12
Job6
6
Job7
15
Job8
3
Job9
11
Job10
8
```

Expected averages: FCFS `54.10`, SJF `38.90`, RR-2 `66.10`, RR-5 `66.70`.

### Case 3: 15 jobs

```text
Job1
7
Job2
18
Job3
10
Job4
4
Job5
12
Job6
6
Job7
15
Job8
3
Job9
11
Job10
8
Job11
20
Job12
5
Job13
14
Job14
2
Job15
9
```

Expected averages: FCFS `79.07`, SJF `54.47`, RR-2 `95.80`, RR-5 `94.87`.

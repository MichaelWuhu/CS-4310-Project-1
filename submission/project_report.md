# CS 4310 Project 1: CPU Scheduling and Performance Analysis

## Part 1: Design and Testing

### 1(a) Scheduling algorithms

Every job arrives at time 0 and is read as a job name followed by a positive
integer burst time. Since all arrival times are zero, a job's turnaround time
equals its completion time. The average turnaround time is the sum of all job
completion times divided by the number of jobs. Execution intervals are shown
with start and stop times.

**First-Come-First-Served (FCFS)**

```text
read jobs in input order
time = 0
for each job:
    start = time
    time = time + job burst
    record job completion time as time
    display job from start to time
average = sum of completion times / number of jobs
display each job's turnaround time and the average
```

**Shortest-Job-First (SJF), non-preemptive**

```text
read jobs and preserve their original positions
sort by burst time ascending; preserve input order for ties
time = 0
for each job in sorted order:
    start = time
    time = time + job burst
    record job completion time as time
    display job from start to time
average = sum of completion times / number of jobs
display each job's turnaround time and the average
```

**Round-Robin with quantum 2 (RR-2)**

```text
read jobs in input order and put them in a FIFO ready queue
time = 0
while the ready queue is not empty:
    remove the first job
    run it for the smaller of 2 or its remaining burst
    update time and the job's remaining burst
    display the job's execution interval
    if the job is finished:
        record its completion time as time
    otherwise:
        append it to the back of the queue
average = sum of completion times / number of jobs
display each job's turnaround time and the average
```

**Round-Robin with quantum 5 (RR-5)**

```text
read jobs in input order and put them in a FIFO ready queue
time = 0
while the ready queue is not empty:
    remove the first job
    run it for the smaller of 5 or its remaining burst
    update time and the job's remaining burst
    display the job's execution interval
    if the job is finished:
        record its completion time as time
    otherwise:
        append it to the back of the queue
average = sum of completion times / number of jobs
display each job's turnaround time and the average
```

### 1(b) Correctness test cases

The four programs were run using each of these same data sets. The expected
average turnaround times are shown below.

| Test | Jobs in input order (name: burst in ms) | FCFS (ms) | SJF (ms) | RR-2 (ms) | RR-5 (ms) |
|---|---|---:|---:|---:|---:|
| 1 (5 jobs) | Job1: 7, Job2: 18, Job3: 10, Job4: 4, Job5: 12 | 31.40 | 24.00 | 36.40 | 36.00 |
| 2 (10 jobs) | Job1: 7, Job2: 18, Job3: 10, Job4: 4, Job5: 12, Job6: 6, Job7: 15, Job8: 3, Job9: 11, Job10: 8 | 54.10 | 38.90 | 66.10 | 66.70 |
| 3 (15 jobs) | Job1: 7, Job2: 18, Job3: 10, Job4: 4, Job5: 12, Job6: 6, Job7: 15, Job8: 3, Job9: 11, Job10: 8, Job11: 20, Job12: 5, Job13: 14, Job14: 2, Job15: 9 | 79.07 | 54.47 | 95.80 | 94.87 |

### 1(c) Random-input testing strategy

The performance experiment uses 5, 10, and 15 jobs. For each size, it creates
20 different input files, for 60 files total. Every burst time is an integer
from 1 through 20 ms, meeting the assignment's requirement that the maximum
burst be at least 20 ms. A fixed random seed of 4310 makes the generated input
sets repeatable. Each generated file is given, unchanged, to all four
algorithms. The average turnaround time from every run is saved. The final
result for each algorithm and input size is the mean of that algorithm's 20
trial averages. The saved files are under `results/inputs/`.

## Part 2: Implementation and Correctness Testing

### 2(a) Program files

The four independent Python programs are [fcfs.py](./fcfs.py),
[sjf.py](./sjf.py), [rr2.py](./rr2.py), and [rr5.py](./rr5.py). Each reads the
alternating job-name/burst-time format from [job.txt](./job.txt), allows up to
30 jobs, and reports a readable execution schedule and turnaround results.

### 2(b) Program documentation

- **FCFS:** Reads jobs and runs each to completion in file order.
- **SJF:** Runs the shortest burst first; Python's stable sort retains file
  order when burst times tie.
- **RR-2:** Uses a FIFO ready queue and runs at most two time units per turn.
- **RR-5:** Uses a FIFO ready queue and runs at most five time units per turn.

Each program documents its scheduling method and reports job names, start and
stop times, burst used, completion/turnaround time, and the average. Invalid or
missing input is reported as an error rather than silently treated as a valid
run.

### 2(c) Correctness test results

All four programs were run on all three cases listed in Part 1(b). The measured
averages matched the provided expected values to two decimal places. Every run
also passed checks that the intervals were contiguous, burst used summed to
each job's original burst, reported completion times matched final execution
endpoints, and quantum limits and FCFS/SJF ordering were respected. An
additional equal-burst test confirmed that SJF preserves input order for ties.

| Test size | FCFS | SJF | RR-2 | RR-5 |
|---:|:---:|:---:|:---:|:---:|
| 5 jobs | ✓ | ✓ | ✓ | ✓ |
| 10 jobs | ✓ | ✓ | ✓ | ✓ |
| 15 jobs | ✓ | ✓ | ✓ | ✓ |

### 2(d) Program execution screenshots

The four screenshots show each program running with the included five-job
`job.txt` input:

1. [FCFS execution](./screenshots/fcfs_screenshot.png)
2. [SJF execution](./screenshots/sjf_screenshot.png)
3. [RR-2 execution](./screenshots/rr2_screenshot.png)
4. [RR-5 execution](./screenshots/rr5_screenshot.png)

## Part 3: Performance Analysis

### 3(a) Average of 20 trial averages

The values below are calculated from the program-generated
[summary_results.csv](./results/summary_results.csv). All values are in milliseconds.

| Number of jobs | FCFS | SJF | RR-2 | RR-5 |
|---:|---:|---:|---:|---:|
| 5 | 31.68 | 25.57 | 39.58 | 38.77 |
| 10 | 58.33 | 44.48 | 75.68 | 74.50 |
| 15 | 86.80 | 62.95 | 111.73 | 110.53 |

The individual trial outputs are in [raw_results.csv](./results/raw_results.csv). The
analysis was run with seed 4310 and includes 20 trials at each of the three
input sizes.

### 3(b) Graphs and comparison

**FCFS:** [FCFS graph](./results/graphs/fcfs_graph.png) shows that its mean average turnaround
time increases from 31.68 ms for 5 jobs to 86.80 ms for 15 jobs. In FCFS, a
later job must wait for all earlier jobs to finish.

**SJF:** [SJF graph](./results/graphs/sjf_graph.png) shows the lowest measured average at each
input size: 25.57, 44.48, and 62.95 ms. Short jobs tend to complete sooner
because jobs are scheduled in ascending burst order.

**RR-2:** [RR-2 graph](./results/graphs/rr2_graph.png) rises from 39.58 ms to 111.73 ms across
the tested sizes. The small quantum provides frequent turns, but jobs may
require many queue visits before completing.

**RR-5:** [RR-5 graph](./results/graphs/rr5_graph.png) rises from 38.77 ms to 110.53 ms. In
these trials it was slightly better than RR-2 at each input size, although
both Round-Robin results were higher than the measured FCFS and SJF results.

The [combined graph](./results/graphs/combined_graph.png) compares all four means. For each
tested input size, the measured ranking from lowest to highest average
turnaround time is **SJF, FCFS, RR-5, RR-2**. This describes this experiment's
20 generated data sets, not a guarantee for every possible workload. SJF
benefits from completing short jobs early; FCFS avoids repeated queue turns;
the Round-Robin algorithms trade prompt service to queued jobs for completion
times that can increase when many jobs need multiple slices.

### 3(c) Conclusion

This project implemented and tested four CPU scheduling algorithms as
independent programs. A strength of the work is that each program reports its
execution intervals as well as each job's completion and turnaround time,
which makes it possible to inspect the scheduling behavior, not just the final
average. The standard tests matched the expected averages, and the performance
experiment used the same 60 saved inputs for all four algorithms. A fixed
random seed also makes the results reproducible. In this experiment, SJF had
the lowest mean average turnaround time for each tested job count, while
Round-Robin had higher means on these inputs. The results are limited to
workloads with all jobs arriving at time zero, three input sizes, burst times
from 1 to 20, and 20 trials per size. Different arrival patterns or burst
distributions could change the comparison. If I repeated the project, I would
include more input sizes and trials, test different arrival times, and compare
the effect of more time quantum values. I would keep the fixed-seed inputs and
automated checks because they make comparisons easier to reproduce and verify.

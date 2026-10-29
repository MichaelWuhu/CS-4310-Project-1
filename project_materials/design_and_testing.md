# CPU Scheduling Design and Testing Plan

## Scheduling assumptions

- Every job arrives at time 0.
- Each job has a name, a positive integer burst time, and an original input position.
- FCFS and both round-robin schedulers use input order.
- SJF sorts by burst time in ascending order. Equal burst times retain input order.
- The input contains no more than 30 jobs.
- A job's turnaround time is its completion time because all jobs arrive at time 0.
- Each execution interval is shown as a half-open interval `[start, end)`.

## FCFS pseudocode

```text
read jobs in input order
current_time = 0
total_turnaround = 0

for each job in input order:
    start_time = current_time
    current_time = current_time + job.burst_time
    job.completion_time = current_time
    record (job.name, start_time, current_time) as an execution interval
    total_turnaround = total_turnaround + job.completion_time

average_turnaround = total_turnaround / number_of_jobs
display execution intervals, each job's completion time, and the average
```

## SJF pseudocode

```text
read jobs in input order and keep each job's original position
sort jobs by (burst_time ascending, original position ascending)
current_time = 0
total_turnaround = 0

for each job in sorted order:
    start_time = current_time
    current_time = current_time + job.burst_time
    job.completion_time = current_time
    record (job.name, start_time, current_time) as an execution interval
    total_turnaround = total_turnaround + job.completion_time

average_turnaround = total_turnaround / number_of_jobs
display execution intervals, each job's completion time, and the average
```

## RR-2 pseudocode

```text
read jobs in input order
put each job with its remaining burst time into a FIFO ready queue
current_time = 0
total_turnaround = 0

while the ready queue is not empty:
    remove the job at the front of the queue
    start_time = current_time
    run_time = minimum(2, job.remaining_time)
    current_time = current_time + run_time
    job.remaining_time = job.remaining_time - run_time
    record (job.name, start_time, current_time) as an execution interval

    if job.remaining_time is 0:
        job.completion_time = current_time
        total_turnaround = total_turnaround + job.completion_time
    else:
        append the job to the back of the ready queue

average_turnaround = total_turnaround / number_of_jobs
display execution intervals, each job's completion time, and the average
```

## RR-5 pseudocode

```text
read jobs in input order
put each job with its remaining burst time into a FIFO ready queue
current_time = 0
total_turnaround = 0

while the ready queue is not empty:
    remove the job at the front of the queue
    start_time = current_time
    run_time = minimum(5, job.remaining_time)
    current_time = current_time + run_time
    job.remaining_time = job.remaining_time - run_time
    record (job.name, start_time, current_time) as an execution interval

    if job.remaining_time is 0:
        job.completion_time = current_time
        total_turnaround = total_turnaround + job.completion_time
    else:
        append the job to the back of the ready queue

average_turnaround = total_turnaround / number_of_jobs
display execution intervals, each job's completion time, and the average
```

## Turnaround time

Turnaround time is the elapsed time from a job's arrival until its completion. Since all jobs arrive at time 0, each job's turnaround time is its completion time. The average turnaround time is the sum of all jobs' turnaround times divided by the number of jobs. Display the average to two decimal places.

## Testing strategy

Use the three standard data sets below to check correctness with 5, 10, and 15 jobs. Run each exact data set through all four programs. For each run, verify that every job appears in the output, execution intervals are contiguous and have lengths consistent with the algorithm, every job's reported completion time matches its final execution endpoint, and the displayed average matches the expected value to two decimal places.

Also test additional randomly generated inputs of 5, 10, and 15 jobs. Give each job a unique name and a positive integer burst time, preserve input order when writing the file, and use the exact same generated file for all four algorithms. Include inputs with equal burst times to verify SJF's stable tie-breaking, burst times shorter than the quantum, burst times equal to a quantum, and burst times longer than a quantum. For reproducible comparisons, record the generated input (or its random seed) and retain it for all four runs.

### Standard case 1: 5 jobs

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

Expected average turnaround times: FCFS `31.40`, SJF `24.00`, RR-2 `36.40`, RR-5 `36.00`.

### Standard case 2: 10 jobs

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

Expected average turnaround times: FCFS `54.10`, SJF `38.90`, RR-2 `66.10`, RR-5 `66.70`.

### Standard case 3: 15 jobs

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

Expected average turnaround times: FCFS `79.07`, SJF `54.47`, RR-2 `95.80`, RR-5 `94.87`.

## Why all algorithms must use the same input

Average turnaround time depends on both the scheduling algorithm and the jobs being scheduled. Comparing results from different inputs would mix the effect of the algorithm with differences in job count, input order, or burst times. Using the same input set makes the comparison fair: any change in execution order or average turnaround time is attributable to the scheduling policy.

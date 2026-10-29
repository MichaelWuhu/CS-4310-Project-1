# Task 6: Complete the Written Report

Include the design file, four program files, testing results, `summary_results.csv`, and graph files from the previous tasks.

Give the following prompt to an AI model:

```text
Complete the written portions of my CS 4310 CPU scheduling project using the project requirements and the results/files I provide.

Write:
1. Part 1(a): descriptions or pseudocode for all four algorithms.
2. Part 1(b): the three testing cases and expected average turnaround times.
3. Part 1(c): a testing strategy explaining random generation, input sizes, maximum burst time, 20 trials, and using identical inputs for every algorithm.
4. Part 2(b): brief documentation descriptions for the four programs.
5. Part 2(c): explain that each program was tested against the expected values and identify the results as correct.
6. Part 3(a): fill in the performance table using summary_results.csv.
7. Part 3(b): write a short summary for each individual algorithm graph.
8. Part 3(b): write a comparison of all four algorithms and rank them based on the experimental results.
9. Part 3(c): write a conclusion of at least 100 words discussing strengths, limitations, and what could be improved.

Use clear student-level writing. Do not claim that a program or experiment was completed unless it is supported by the files or results I provide.
```

## Useful written text

### Turnaround-time explanation

> Because all jobs arrive at time 0, a job's turnaround time is equal to its completion time. The completion time is the time at which the job finishes execution. The average turnaround time is calculated by adding the turnaround times of all jobs and dividing the total by the number of jobs.

### Part 1(c): Testing strategy

> The testing strategy uses randomly generated job burst times between 1 and 20 milliseconds. Three input sizes are tested: 5 jobs, 10 jobs, and 15 jobs. For each input size, 20 different input files are generated. The same input file is tested with FCFS, SJF, RR-2, and RR-5 so that the algorithms can be compared fairly. A fixed random seed can be used so that the experiments are reproducible. For every trial, the program records the average turnaround time. The final result for each algorithm and input size is the average of the 20 trial averages.

### Part 2(b): Program documentation

> Each program contains comments describing the input format, scheduling method, variables, and calculation of turnaround time. The programs read job names and burst times from `job.txt`, simulate the selected scheduling algorithm, display the execution schedule, and calculate the average turnaround time.

### Part 3(c): Conclusion draft

> This project successfully implemented and evaluated four CPU scheduling algorithms: FCFS, SJF, RR-2, and RR-5. One strength of the project is that each algorithm was implemented as a separate program, making the behavior of each scheduling method easier to understand and test. Another strength is that the same randomly generated input files were used for every algorithm, which created a fair basis for comparison. The main limitation is that the results depend on the selected random inputs and the limited input sizes of 5, 10, and 15 jobs. The project also assumes that all jobs arrive at time 0, which does not represent every real operating-system workload. If I repeated the project, I would test more input sizes, run more trials, and possibly include different arrival times. I would also automate the screenshots and result collection to reduce manual work and improve consistency.

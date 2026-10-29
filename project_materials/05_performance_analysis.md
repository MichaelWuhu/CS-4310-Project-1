# Task 5: Performance Analysis

Include the four completed programs from Tasks 2 and 3.

This session should generate 20 files containing 5 jobs, 20 files containing 10 jobs, and 20 files containing 15 jobs. Use burst values from 1 through 20. The same input file must be used by all four algorithms.

Give the following prompt to an AI model:

```text
Create a performance-analysis system for my CPU scheduling project.

I already have:
- fcfs.py
- sjf.py
- rr2.py
- rr5.py

Create a separate Python script called performance_analysis.py.

Requirements:
1. Generate 20 random test files containing 5 jobs each.
2. Generate 20 random test files containing 10 jobs each.
3. Generate 20 random test files containing 15 jobs each.
4. Use burst times from 1 through 20.
5. Use the exact same test file for FCFS, SJF, RR-2, and RR-5.
6. Run all four algorithms on every test file.
7. Extract the average turnaround time for each algorithm.
8. Calculate the average of the 20 average turnaround times for each input size.
9. Save all raw results to CSV.
10. Save a summary table containing the final results for 5, 10, and 15 jobs.
11. Create four separate graphs:
   - FCFS average turnaround time versus number of jobs
   - SJF average turnaround time versus number of jobs
   - RR-2 average turnaround time versus number of jobs
   - RR-5 average turnaround time versus number of jobs
12. Create one combined graph showing all four algorithms.
13. Label every graph clearly.
14. Use a fixed random seed so the results can be reproduced.
15. Do not overwrite the four scheduling programs.
```

Expected output files:

```text
performance_analysis.py
raw_results.csv
summary_results.csv
fcfs_graph.png
sjf_graph.png
rr2_graph.png
rr5_graph.png
combined_graph.png
```

Do not invent performance values before actually running the script.

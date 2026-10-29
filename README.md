# CS 4310 Project 1

The repository is arranged so that the completed, ready-to-submit work is
separate from the original assignment PDF and session/task guidance.

## Repository layout

```text
submission/
  fcfs.py, sjf.py, rr2.py, rr5.py
  job.txt
  performance_analysis.py
  requirements.txt
  project_report.md
  results/
    raw_results.csv
    summary_results.csv
    inputs/                 # 60 reproducible trial inputs
    graphs/                 # four individual graphs and one combined graph
  screenshots/              # one successful run per scheduler
project_materials/
  cs4310 project1_26Fall.pdf
  design_and_testing.md
  01_design_and_testing.md through 06_complete_written_report.md
```

## Run the schedulers

Open a terminal in `submission/`, then run:

```text
python3 fcfs.py
python3 sjf.py
python3 rr2.py
python3 rr5.py
```

The programs read `job.txt` in the current folder. It contains alternating job
names and positive integer burst times, with no more than 30 jobs. The included
file is the standard 5-job case.

## Reproduce the performance analysis

From `submission/`, install the graphing dependency and run the fixed-seed
20-trial-per-size experiment:

```text
python3 -m pip install -r requirements.txt
python3 performance_analysis.py
```

The script writes all trial averages and summary means under `results/`, saves
the 60 shared generated inputs in `results/inputs/`, and saves five labeled PNG
graphs in `results/graphs/`.

## What to submit

The ready-to-submit materials are in `submission/`: four scheduler programs,
`job.txt`, the completed [project report](submission/project_report.md), the
performance-analysis script and dependency file, the CSV results, graphs,
generated trial inputs, and four execution screenshots. Follow your instructor's
directions if the report must be copied into the original assignment document.

The assignment PDF and original task instructions are kept separately in
`project_materials/` for reference; they are not generated experiment output.

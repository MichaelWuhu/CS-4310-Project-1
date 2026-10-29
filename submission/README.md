# Submission Folder

This folder contains the completed scheduler programs, their sample input, the
written report, reproducible performance-analysis script, results, graphs, and
screenshots.

## Run a scheduler

Open a terminal in this folder and run any of:

```text
python3 fcfs.py
python3 sjf.py
python3 rr2.py
python3 rr5.py
```

Each program reads `job.txt` from this folder.

## Regenerate the experiment

Install the plotting dependency and run the fixed-seed experiment:

```text
python3 -m pip install -r requirements.txt
python3 performance_analysis.py
```

The script writes trial inputs to `results/inputs/`, CSV files to `results/`,
and five graphs to `results/graphs/`.

## Submission checklist

- Four scheduler scripts: `fcfs.py`, `sjf.py`, `rr2.py`, and `rr5.py`
- Input file: `job.txt`
- Written answers and analysis: `project_report.md`
- Reproducible analysis: `performance_analysis.py` and `requirements.txt`
- Performance results: `results/raw_results.csv` and
  `results/summary_results.csv`
- All generated inputs: `results/inputs/`
- Five performance graphs: `results/graphs/`
- Four successful-run screenshots: `screenshots/`

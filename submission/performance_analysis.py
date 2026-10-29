"""Run reproducible scheduling trials and create CSV summaries and graphs.

Install the plotting dependency with ``python3 -m pip install -r requirements.txt``
before running this script. It generates 20 inputs for each of 5, 10, and 15
jobs, runs all four independent scheduling programs on every input, and writes
the results under ``results/``.
"""

import csv
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from statistics import mean
from typing import Dict, List


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
INPUTS = RESULTS / "inputs"
GRAPHS = RESULTS / "graphs"
SEED = 4310
TRIALS_PER_SIZE = 20
JOB_COUNTS = (5, 10, 15)
BURST_MIN = 1
BURST_MAX = 20
PROGRAMS = {
    "FCFS": "fcfs.py",
    "SJF": "sjf.py",
    "RR-2": "rr2.py",
    "RR-5": "rr5.py",
}
AVERAGE_PATTERN = re.compile(
    r"Average Turnaround Time:\s*([0-9]+(?:\.[0-9]+)?)\s*ms"
)


def load_plotting_library():
    """Load matplotlib or report how to install the declared dependency."""
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as error:
        raise RuntimeError(
            "Matplotlib is required. Install project dependencies with "
            "'python3 -m pip install -r requirements.txt'."
        ) from error
    return plt


def write_job_file(path: Path, burst_times: List[int]) -> None:
    """Write jobs in the alternating name/burst format used by the simulators."""
    lines = []
    for job_number, burst_time in enumerate(burst_times, start=1):
        lines.extend((f"Job{job_number}", str(burst_time)))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_program(script_name: str, working_directory: Path) -> float:
    """Run one scheduler and return its reported average turnaround time."""
    script_path = ROOT / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=working_directory,
        capture_output=True,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed for {working_directory / 'job.txt'} "
            f"(exit {result.returncode}):\n{result.stderr.strip()}"
        )

    match = AVERAGE_PATTERN.search(result.stdout)
    if match is None:
        raise RuntimeError(
            f"Could not find the average turnaround time in {script_name}'s "
            f"output for {working_directory / 'job.txt'}:\n{result.stdout}"
        )
    return float(match.group(1))


def create_graphs(summary: List[Dict[str, float]]) -> None:
    """Save one graph per algorithm and a combined comparison graph."""
    plt = load_plotting_library()
    sizes = [int(row["Number of Jobs"]) for row in summary]
    colors = {
        "FCFS": "#1f77b4",
        "SJF": "#2ca02c",
        "RR-2": "#d62728",
        "RR-5": "#9467bd",
    }

    for algorithm, filename in (
        ("FCFS", "fcfs_graph.png"),
        ("SJF", "sjf_graph.png"),
        ("RR-2", "rr2_graph.png"),
        ("RR-5", "rr5_graph.png"),
    ):
        values = [float(row[algorithm]) for row in summary]
        figure, axis = plt.subplots(figsize=(7, 5))
        axis.plot(
            sizes,
            values,
            marker="o",
            linewidth=2,
            color=colors[algorithm],
            label=algorithm,
        )
        axis.set(
            title=f"{algorithm} Average Turnaround Time",
            xlabel="Number of Jobs",
            ylabel="Average Turnaround Time (ms)",
            xticks=sizes,
        )
        axis.grid(True, linestyle="--", alpha=0.45)
        axis.legend()
        figure.tight_layout()
        figure.savefig(GRAPHS / filename, dpi=160)
        plt.close(figure)

    figure, axis = plt.subplots(figsize=(8, 5.5))
    for algorithm in PROGRAMS:
        values = [float(row[algorithm]) for row in summary]
        axis.plot(
            sizes,
            values,
            marker="o",
            linewidth=2,
            color=colors[algorithm],
            label=algorithm,
        )
    axis.set(
        title="Average Turnaround Time by Scheduling Algorithm",
        xlabel="Number of Jobs",
        ylabel="Average Turnaround Time (ms)",
        xticks=sizes,
    )
    axis.grid(True, linestyle="--", alpha=0.45)
    axis.legend()
    figure.tight_layout()
    figure.savefig(GRAPHS / "combined_graph.png", dpi=160)
    plt.close(figure)


def main() -> int:
    """Generate all trials, save the CSV files, and create the graphs."""
    try:
        load_plotting_library()
        rng = random.Random(SEED)
        INPUTS.mkdir(parents=True, exist_ok=True)
        GRAPHS.mkdir(parents=True, exist_ok=True)
        raw_rows: List[Dict[str, object]] = []

        with tempfile.TemporaryDirectory(prefix="scheduling-trials-") as temp:
            working_directory = Path(temp)
            for job_count in JOB_COUNTS:
                size_directory = INPUTS / f"{job_count}_jobs"
                size_directory.mkdir(parents=True, exist_ok=True)

                for trial in range(1, TRIALS_PER_SIZE + 1):
                    burst_times = [
                        rng.randint(BURST_MIN, BURST_MAX)
                        for _ in range(job_count)
                    ]
                    input_path = size_directory / f"trial_{trial:02d}.txt"
                    write_job_file(input_path, burst_times)

                    # Stage the exact same generated input for each algorithm.
                    staged_input = working_directory / "job.txt"
                    staged_input.write_bytes(input_path.read_bytes())
                    row: Dict[str, object] = {
                        "Number of Jobs": job_count,
                        "Trial": trial,
                        "Input File": input_path.relative_to(ROOT).as_posix(),
                    }
                    for algorithm, script_name in PROGRAMS.items():
                        row[algorithm] = run_program(
                            script_name, working_directory
                        )
                    raw_rows.append(row)

        raw_fields = ["Number of Jobs", "Trial", "Input File", *PROGRAMS]
        with (RESULTS / "raw_results.csv").open(
            "w", newline="", encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=raw_fields)
            writer.writeheader()
            writer.writerows(raw_rows)

        summary: List[Dict[str, float]] = []
        for job_count in JOB_COUNTS:
            rows_for_size = [
                row for row in raw_rows if row["Number of Jobs"] == job_count
            ]
            summary_row: Dict[str, float] = {
                "Number of Jobs": float(job_count)
            }
            for algorithm in PROGRAMS:
                summary_row[algorithm] = mean(
                    float(row[algorithm]) for row in rows_for_size
                )
            summary.append(summary_row)

        summary_fields = ["Number of Jobs", *PROGRAMS]
        with (RESULTS / "summary_results.csv").open(
            "w", newline="", encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=summary_fields)
            writer.writeheader()
            for row in summary:
                writer.writerow(
                    {
                        "Number of Jobs": int(row["Number of Jobs"]),
                        **{
                            algorithm: f"{row[algorithm]:.2f}"
                            for algorithm in PROGRAMS
                        },
                    }
                )

        create_graphs(summary)
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Random seed: {SEED}")
    print(f"Trials per job count: {TRIALS_PER_SIZE}")
    print(f"Raw results: {RESULTS / 'raw_results.csv'}")
    print(f"Summary results: {RESULTS / 'summary_results.csv'}")
    print(f"Generated inputs: {INPUTS}")
    print(f"Graphs: {GRAPHS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

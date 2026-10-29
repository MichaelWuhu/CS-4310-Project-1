"""Simulate First-Come-First-Served CPU scheduling using jobs from job.txt."""

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import List, Tuple


@dataclass
class Job:
    """A job read from the input file."""

    name: str
    burst_time: int
    completion_time: int = 0


def read_jobs(filename: str = "job.txt") -> List[Job]:
    """Read alternating job-name and positive burst-time lines."""
    try:
        lines = [
            line.strip()
            for line in Path(filename).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    except OSError as error:
        raise OSError(f"Cannot read {filename}: {error}") from error

    if not lines:
        raise ValueError(f"{filename} contains no jobs.")
    if len(lines) % 2:
        raise ValueError(
            f"{filename} must contain alternating job names and burst times."
        )
    if len(lines) // 2 > 30:
        raise ValueError(f"{filename} cannot contain more than 30 jobs.")

    jobs = []
    for index in range(0, len(lines), 2):
        name = lines[index]
        try:
            burst_time = int(lines[index + 1])
        except ValueError as error:
            raise ValueError(
                f"Burst time for {name} must be a positive integer."
            ) from error
        if burst_time <= 0:
            raise ValueError(f"Burst time for {name} must be a positive integer.")
        jobs.append(Job(name=name, burst_time=burst_time))
    return jobs


def schedule_fcfs(jobs: List[Job]) -> List[Tuple[Job, int, int, int]]:
    """Run each job to completion in its original input order."""
    current_time = 0
    schedule = []
    for job in jobs:
        start_time = current_time
        current_time += job.burst_time
        job.completion_time = current_time
        schedule.append((job, start_time, current_time, job.burst_time))
    return schedule


def display_results(
    jobs: List[Job], schedule: List[Tuple[Job, int, int, int]]
) -> None:
    """Print execution intervals and each job's turnaround time."""
    print("FCFS CPU Scheduling")
    print("\nExecution Schedule:")
    print(f"{'Job':<12}{'Start':>10}{'Stop':>10}{'Burst Used':>14}")
    for job, start, stop, burst_used in schedule:
        print(f"{job.name:<12}{start:>10}{stop:>10}{burst_used:>14}")

    print("\nCompletion / Turnaround Times:")
    print(f"{'Job':<12}{'Completion':>14}{'Turnaround':>14}")
    for job in jobs:
        print(
            f"{job.name:<12}{job.completion_time:>14}"
            f"{job.completion_time:>14}"
        )
    average = sum(job.completion_time for job in jobs) / len(jobs)
    print(f"\nAverage Turnaround Time: {average:.2f} ms")


def main() -> int:
    """Load job.txt, run FCFS, and report input errors clearly."""
    try:
        jobs = read_jobs()
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    display_results(jobs, schedule_fcfs(jobs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

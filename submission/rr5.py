"""Simulate Round-Robin CPU scheduling with a time quantum of 5."""

from collections import deque
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Deque, List, Tuple


@dataclass
class Job:
    """A job and its state during the scheduling simulation."""

    name: str
    burst_time: int
    remaining_time: int
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
        jobs.append(Job(name, burst_time, burst_time))
    return jobs


def schedule_round_robin(
    jobs: List[Job], quantum: int = 5
) -> List[Tuple[Job, int, int, int]]:
    """Run FIFO time slices until all jobs finish."""
    ready_queue: Deque[Job] = deque(jobs)
    current_time = 0
    schedule = []

    while ready_queue:
        job = ready_queue.popleft()
        start_time = current_time
        burst_used = min(quantum, job.remaining_time)
        current_time += burst_used
        job.remaining_time -= burst_used
        schedule.append((job, start_time, current_time, burst_used))

        if job.remaining_time == 0:
            job.completion_time = current_time
        else:
            ready_queue.append(job)

    return schedule


def display_results(
    jobs: List[Job], schedule: List[Tuple[Job, int, int, int]]
) -> None:
    """Print execution intervals and each job's turnaround time."""
    print("RR-5 CPU Scheduling (Time Quantum = 5)")
    print("\nExecution Schedule:")
    print(f"{'Job':<12}{'Start':>10}{'Stop':>10}{'Burst Used':>14}")
    for job, start, stop, burst_used in schedule:
        print(f"{job.name:<12}{start:>10}{stop:>10}{burst_used:>14}")

    print("\nCompletion / Turnaround Times:")
    print(f"{'Job':<12}{'Completion':>14}{'Turnaround':>14}")
    for job in jobs:
        completion_time = job.completion_time
        print(f"{job.name:<12}{completion_time:>14}{completion_time:>14}")
    average = sum(job.completion_time for job in jobs) / len(jobs)
    print(f"\nAverage Turnaround Time: {average:.2f} ms")


def main() -> int:
    """Load job.txt, run RR-5, and report input errors clearly."""
    try:
        jobs = read_jobs()
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    display_results(jobs, schedule_round_robin(jobs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

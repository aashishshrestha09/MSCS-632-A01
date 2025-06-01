# Employee Shift Scheduler — MSCS-632-A01 Assignment 4

This directory contains the implementation of Assignment 4 for the 2025 Summer course _Advanced Programming Languages_ (MSCS-632-A01).

## Project Overview

This project implements an employee shift scheduling application that manages employee shift preferences and assignments for a 7-day week with three shifts per day: `Morning`, `Afternoon`, and `Evening`.

The application ensures:

- No employee works more than one shift per day.
- Employees work a maximum of 5 days per week.
- Each shift has at least 2 employees assigned.
- Shift conflicts and overflows are resolved by reassigning employees to available shifts.
- Employee shift preferences are prioritized where possible.

## Implementations

### Python Implementation (`python/` folder)

- Written in Python
- Features an **intuitive GUI built with [PyQt6](https://pypi.org/project/PyQt6/)** for easy input of employee names and shift preferences
- Includes logic to handle shift assignments and conflict resolution
- Refer to the [`python/README.md`](./python/README.md) for setup and usage details

### Go Implementation (`go/` folder)

- Written in Go
- Command-line based application for managing employee schedules and assignments
- Refer to the [`go/README.md`](./go/README.md) for setup and usage details

## Running the Applications

Please check the respective README files inside each folder for instructions on how to run the applications and dependencies.

## Output

Both implementations generate a readable weekly schedule that shows assigned employees per shift each day, respecting the business constraints and preferences.

Screenshots and sample output can be found in each language folder.

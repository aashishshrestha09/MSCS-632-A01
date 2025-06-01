# Employee Shift Scheduler

A Python application to automate scheduling of employee shifts based on user-defined constraints and preferences.

## Features

- Intuitive GUI built with [PyQt6](https://pypi.org/project/PyQt6/) for easy employee and shift input
- Automatically assigns shifts while ensuring:
  - Maximum one shift per employee per day
  - Maximum 5 working days per employee per week
  - Minimum number of employees per shift
- Schedule output displayed in an HTML format for easy sharing and printing
- Configuration through environment variables for shift types and working days
- Designed to simplify shift planning and improve workforce management

## Installation

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

## Development

### Setup

1. Clone this repository

   ```bash
    git clone https://github.com/aashishshrestha09/MSCS-632-A01.git
    cd MSCS-632-A01/week-4/assignment-4/python
   ```

2. Create virtual environment for this project: `python3 -m venv .venv`.
3. Activate the virtual environment: `. .venv/bin/activate`.
4. Install as editable with "dev" packages: `pip install --editable ".[dev]"`.

### Running the program

```sh
python main.py
```

## Project Structure

```
.
├── main.py
├── pyproject.toml
├── README.md
└── src
    ├── config.py
    ├── gui.py
    ├── helpers.py
    ├── models.py
    ├── scheduler.py
    └── templates
        └── schedule_template.html
```

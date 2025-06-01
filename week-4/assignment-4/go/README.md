# Employee Shift Scheduler (Go)

A Go application to automate scheduling of employee shifts based on user-defined preferences.

## Features

- Command-line interface for adding employees and their preferred shifts
- Automatically assigns shifts respecting preferences
- Displays the schedule in a neat table format with preference legends
- Modular design with config, scheduler, models, and helpers packages

## Installation

### Prerequisites

- Install [Go](https://go.dev/) (version 1.22+ recommended)

## Development

### Setup

- Clone this repository

  ```bash
  git clone https://github.com/aashishshrestha09/MSCS-632-A01.git
  cd MSCS-632-A01/week-4/assignment-4/go
  ```

## Running the program

```bash
go run main.go
```

## Project Structure

```go
.
├── config
│   └── config.go
├── go.mod
├── go.sum
├── helpers
│   └── helpers.go
├── main.go
├── models
│   └── employee.go
├── README.md
└── scheduler
    └── scheduler.go
```

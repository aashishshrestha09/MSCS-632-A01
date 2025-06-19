# Go Ride Sharing Data Processing System 🚗

A concurrent ride-sharing task processing system built in Go, simulating multiple workers retrieving tasks from a shared queue, processing them, and writing results to a shared file.

## Requirements

- ✔️ Concurrency management with goroutines and channels
- ✔️ Mutex-protected shared results slice
- ✔️ Error handling via explicit error checks and `defer`
- ✔️ Centralized logging to `outputs/ride.log`
- ✔️ Clean, modular package structure using `cmd/` and `pkg/`
- ✔️ Industry-standard Makefile for workflow management

## Project Structure

```bash
.
├── cmd
│   └── rideshare
│       └── main.go
├── go.mod
├── Makefile
├── outputs
│   ├── ride_results.txt
│   └── ride.log
├── pkg
│   ├── fileutils
│   │   └── fileutils.go
│   ├── logger
│   │   └── logger.go
│   ├── taskqueue
│   │   └── queue.go
│   └── worker
│       └── worker.go
├── README.md
```

## Prerequisites

- Install [Go](https://go.dev/) (version 1.22+ recommended)

## Setup

- Clone this repository

  ```bash
  git clone https://github.com/aashishshrestha09/MSCS-632-A01.git
  cd MSCS-632-A01/week-7/assignment-7/go-ride-sharing-system
  ```

## 🛠️ Usage

Use the provided `Makefile` to build, run, and clean the project:

| Command      | Description                                   |
| :----------- | :-------------------------------------------- |
| `make`       | Build and run the program                     |
| `make build` | Compile the Go binary `rideshare`             |
| `make run`   | Run the program using `go run`                |
| `make clean` | Remove compiled binary, result, and log files |
| `make fmt`   | Format all Go source files                    |
| `make tidy`  | Tidy Go modules and dependencies              |

## 📄 Output Files (in outputs/ folder)

- `outputs/ride_results.txt` — Processed task results
- `outputs/ride.log` — Execution logs and worker activity

The `outputs/` folder is automatically created at runtime or by `make`.

## Run

### (Optional) Clean previous build and outputs

```bash
make clean
```

### Build and run the program

```bash
make
```

### If you prefer to run manually

Run directly:

```bash
go run ./cmd/rideshare
```

Or build and run:

```bash
go build -o rideshare ./cmd/rideshare
./rideshare
```

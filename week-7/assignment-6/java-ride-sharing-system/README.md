# Java Ride Sharing Data Processing System

## Overview

A concurrent ride-sharing task processing system built in Java, simulating multiple threads retrieving tasks from a shared queue, processing them, and writing results to a shared file.

## Features

- ✔️ Concurrency management with `ExecutorService` and `ReentrantLock`
- ✔️ Synchronized task queue and result list
- ✔️ Exception handling using `try-catch` blocks
- ✔️ Centralized logging with `java.util.logging` to `outputs/ride.log`
- ✔️ Clean, modular package structure under `src/`
- ✔️ Industry-standard Makefile for workflow management

## Project Structure

```bash
.
├── go-ride-sharing-system
├── java-ride-sharing-system
└── README.md
```

## Prerequisites

- [Java JDK 21+](https://www.oracle.com/java/technologies/downloads/) installed

## Setup

- Clone this repository

  ```bash
  git clone https://github.com/aashishshrestha09/MSCS-632-A01.git
  cd MSCS-632-A01/week-7/assignment-7/java-ride-sharing-system
  ```

## Usage

Use the provided `Makefile` to build, run, and clean the project:

| Command      | Description                                         |
| :----------- | :-------------------------------------------------- |
| `make`       | Build and run the program                           |
| `make build` | Compile Java source files into the `out/` directory |
| `make run`   | Run the program using the compiled classes          |
| `make clean` | Remove compiled binary, result, and log files       |

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

### If you prefer to compile and run manually

Compile the source files:

```bash
javac -d out src/com/rideshare/*.java
```

Run the program:

```bash
java -cp out com.rideshare.Main
```

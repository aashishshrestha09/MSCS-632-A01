# Ride Sharing Data Processing System

## Overview

This project implements a concurrent Ride Sharing Data Processing System in both **Java** and **Go**. The system simulates multiple worker threads (Java) and goroutines (Go) processing ride tasks from a shared queue, with appropriate concurrency management and error handling to avoid deadlocks and safely manage shared resources.

## Technologies

- **Java 21**
- **Go 1.22**

## Features

- Shared task queue for ride requests
- Concurrent workers (Java Threads, Go Goroutines)
- Safe, concurrency-protected resource access using:
  - `ReentrantLock` (Java)
  - Channels and Mutex (Go)
- Robust error handling with centralized logs
- Graceful termination of all worker processes
- Comparative concurrency analysis report (APA 7 format)

## Project Structure

```bash
.
├── go-ride-sharing-system
│   ├── cmd
│   │   └── rideshare
│   │       └── main.go
│   ├── go.mod
│   ├── Makefile
│   ├── outputs
│   │   ├── ride_results.txt
│   │   └── ride.log
│   ├── pkg
│   │   ├── fileutils
│   │   │   └── fileutils.go
│   │   ├── logger
│   │   │   └── logger.go
│   │   ├── taskqueue
│   │   │   └── queue.go
│   │   └── worker
│   │       └── worker.go
│   ├── README.md
│   └── rideshare
├── java-ride-sharing-system
│   ├── Makefile
│   ├── outputs
│   │   ├── ride_results.txt
│   │   └── ride.log
│   ├── README.md
│   └── src
│       └── com
│           └── rideshare
│               ├── FileUtils.java
│               ├── LoggerConfig.java
│               ├── Main.java
│               ├── TaskQueue.java
│               └── Worker.java
└── README.md
```

## Setup

### Pre-requisites

- Install [Go (v1.22+)](https://go.dev/doc/install)
- Install [Java JDK 21+](https://www.oracle.com/java/technologies/downloads/)

## How to Run

Refer to the individual implementation READMEs for detailed instructions:

- [📄 Java Ride Sharing System](./java-ride-sharing-system/README.md)

- [📄 Go Ride Sharing System](./go-ride-sharing-system/README.md)

Each project includes a Makefile for streamlined build, run, and clean operations.

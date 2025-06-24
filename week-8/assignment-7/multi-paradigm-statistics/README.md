# Multi-Paradigm Statistics Calculator

## 📖 Overview

This project implements a statistics calculator capable of computing:

- Mean
- Median
- Mode (with multi-mode support)

across three different programming paradigms:

- **Procedural Programming** in C
- **Functional Programming** in OCaml
- **Object-Oriented Programming** in Python

This project was completed for **Advanced Programming Languages (MSCS-632-A01)**.

## 📁 Project Structure

```bash
.
├── C
│   ├── Makefile                 # Build instructions for C implementation
│   └── statistics.c             # Procedural C program
├── Makefile                     # Root Makefile to build/run all implementations
├── OCaml
│   └── statistics.ml            # Functional OCaml program
├── Python
│   └── statistics_calculator.py # OOP Python program
├── README.md                    # Project documentation and instructions
└── screenshots                  # Screenshots of program outputs and cleanup process
    ├── c_output.png
    ├── cleanup_output.png
    ├── ocaml_output.png
    └── python_output.png
```

## Prerequisites

Before running the programs, ensure you have the following installed:

- **C Compiler:**  
  Install a C compiler such as [GCC](https://gcc.gnu.org/install/) or [Clang](https://clang.llvm.org/get_started.html).  
  (Alternatively, visit [installc.org](https://installc.org/) for setup guides.)

- **OCaml:**  
  Recommended installation via [OPAM](https://opam.ocaml.org/doc/Install.html).  
  See the official OCaml install page for your platform:

  - [Linux/macOS](https://ocaml.org/install#linux_mac_bsd)
  - [Windows](https://ocaml.org/install#windows)

- **Python 3:**  
  Install Python 3 from the official source: [python.org/downloads](https://www.python.org/downloads/)
  Ensure the `venv` module is available for virtual environment support.

## Setup and Usage

You can build and run each implementation individually or all together via the Makefile:

### Build and run all

```bash
make all
```

### Build and run C implementation

```bash
make c
```

### Build and run OCaml implementation

```bash
make ocaml
```

**_Note: The first time you run make ocaml, opam will initialize and may take time to install the OCaml compiler._**

### Run Python implementation

```bash
make python
```

## Cleaning Build Artifacts

To remove all build outputs and the Python virtual environment, run:

```bash
make clean
```

### Additional Features

Besides mean, median, and mode, the implementations also calculate:

- Min
- Max
- Range
- Standard Deviation

These additions showcase further statistical computations and provide a richer comparison across paradigms.

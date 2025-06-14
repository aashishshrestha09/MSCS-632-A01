# Ride Sharing System in C++

## Overview

This project implements a Ride Sharing System in C++ demonstrating core Object-Oriented Programming (OOP) principles:

- **Encapsulation**
- **Inheritance**
- **Polymorphism**

The system models a ride-sharing service with rides of different types, drivers, and riders.

## Project Structure

```makefile
.
├── include                 # Header files for all classes
│   ├── Driver.h
│   ├── PremiumRide.h
│   ├── Ride.h
│   ├── Rider.h
│   └── StandardRide.h
├── main.cpp                # Main entry point to run the system
├── README.md
├── run.sh                  # Shell script to build and run the program
└── src                     # Source files for class implementations
    ├── Driver.cpp
    ├── PremiumRide.cpp
    ├── Ride.cpp
    ├── Rider.cpp
    └── StandardRide.cpp

3 directories, 13 files

```

## Features

- **Ride Class (Base Class)**: Contains basic ride information and methods for fare calculation and displaying ride details.
- **StandardRide & PremiumRide (Derived Classes)**: Override fare calculation to reflect different pricing models.
- **Driver Class**: Holds driver details and list of assigned rides, with proper encapsulation.
- **Rider Class**: Holds rider details and list of requested rides.
- **Polymorphism**: Demonstrated by storing multiple ride types in a single collection and invoking overridden methods.

## How to Build and Run

## Using the shell script (recommended)

- Make sure you have g++ installed (supports C++11 or later).
- Run the shell script to build and execute the program:

```bash
chmod +x run.sh
./run.sh
```

## Manually via terminal

Compile the program with:

```bash
g++ -std=c++11 -Iinclude -o RideSharingSystem main.cpp src/Ride.cpp src/Driver.cpp src/StandardRide.cpp src/PremiumRide.cpp src/Rider.cpp
```

Run the program:

```bash
./RideSharingSystem
```

### Sample Output

```text
Ride Sharing System Started 🚗
Ride ID: 1, From: Downtown, To: Airport, Distance: 10 miles, Fare: $20
Ride ID: 2, From: Hotel, To: Stadium, Distance: 8 miles, Fare: $28

========== Driver Information ==========
Driver ID: 101, Name: Aashish Shrestha, Rating: 4.9
Assigned Rides (2):
[1] Ride ID: 1, From: Downtown, To: Airport, Distance: 10 miles, Fare: $20
[2] Ride ID: 2, From: Hotel, To: Stadium, Distance: 8 miles, Fare: $28
========================================

========== Rider Information ==========
Rider ID: 201, Name: Ashmin Shrestha
Requested Rides (2):
[1] Ride ID: 1, From: Downtown, To: Airport, Distance: 10 miles, Fare: $20
[2] Ride ID: 2, From: Hotel, To: Stadium, Distance: 8 miles, Fare: $28
========================================
```

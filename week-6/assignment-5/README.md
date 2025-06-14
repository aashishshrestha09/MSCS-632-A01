# Assignment 5: Developing a Class-Based Ride Sharing System

## Overview

This assignment involves implementing a Ride Sharing System as part of the Object-Oriented Programming topic in the Advanced Programming Languages (MSCS-632-A01) course. The primary goal is to demonstrate key OOP principles, including:

- Encapsulation
- Inheritance
- Polymorphism

The system is implemented in two different programming languages to showcase how these concepts can be expressed across language paradigms:

- C++
- Smalltalk

## Project Structure

```makefile
.
├── README.md
├── RideSharingSystem_Cpp
│   ├── img
│   │   └── output.png
│   ├── include
│   │   ├── Driver.h
│   │   ├── PremiumRide.h
│   │   ├── Ride.h
│   │   ├── Rider.h
│   │   └── StandardRide.h
│   ├── main.cpp
│   ├── README.md
│   ├── run.sh
│   └── src
│       ├── Driver.cpp
│       ├── PremiumRide.cpp
│       ├── Ride.cpp
│       ├── Rider.cpp
│       └── StandardRide.cpp
└── RideSharingSystem_Smalltalk
    ├── img
    │   └── output.png
    ├── README.md
    └── RideSharingSystem.st
```

## About the Assignment

The Ride Sharing System simulates basic functionalities of a ride-sharing platform, including:

- Managing rides of different types (standard, premium)
- Handling drivers and riders with appropriate data and behaviors
- Calculating fares with polymorphic methods
- Encapsulating attributes and providing clean class interfaces

The C++ and Smalltalk implementations demonstrate how these OOP concepts are applied differently in each language while achieving consistent design goals.

## How to Use

- For C++, please refer to the [RideSharingSystem_Cpp/README.md](./RideSharingSystem_Cpp/README.md) for build and run instructions.
- For Smalltalk, please refer to the [Smalltalk/README.md](./RideSharingSystem_Smalltalk/README.md) for setup and usage details.

#!/bin/bash

# Compile the program
g++ -std=c++11 -Iinclude -o RideSharingSystem main.cpp src/Ride.cpp src/Driver.cpp src/StandardRide.cpp src/PremiumRide.cpp src/Rider.cpp

# Check if compilation succeeded
if [ $? -eq 0 ]; then
    echo "Compilation succeeded. Running the program..."
    ./RideSharingSystem
    echo "Program finished. Cleaning up..."
    rm RideSharingSystem
else
    echo "Compilation failed. Exiting."
    exit 1
fi

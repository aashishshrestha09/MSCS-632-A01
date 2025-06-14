#include "Driver.h"
#include "Ride.h"
#include <iostream>

Driver::Driver(int id, std::string n, double r)
    : driverID(id), name(n), rating(r) {}

void Driver::addRide(Ride* ride) {
    assignedRides.push_back(ride);
}

void Driver::getDriverInfo() const {
    std::cout << "\n========== Driver Information ==========\n";
    std::cout << "Driver ID: " << driverID 
              << ", Name: " << name 
              << ", Rating: " << rating 
              << std::endl;

    if (assignedRides.empty()) {
        std::cout << "No assigned rides.\n";
    } else {
        std::cout << "Assigned Rides (" << assignedRides.size() << "):\n";
        int count = 1;
        for (auto ride : assignedRides) {
            std::cout << "[" << count++ << "] ";
            ride->rideDetails();
        }
    }

    std::cout << "========================================\n";
}

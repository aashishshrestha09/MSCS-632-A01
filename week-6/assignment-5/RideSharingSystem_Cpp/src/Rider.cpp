#include "Rider.h"
#include "Ride.h"
#include <iostream>

Rider::Rider(int id, std::string n)
    : riderID(id), name(n) {}

void Rider::requestRide(Ride* ride) {
    requestedRides.push_back(ride);
}

void Rider::viewRides() const {
    std::cout << "\n========== Rider Information ==========\n";
    std::cout << "Rider ID: " << riderID << ", Name: " << name << std::endl;

    if (requestedRides.empty()) {
        std::cout << "No requested rides.\n";
    } else {
        std::cout << "Requested Rides (" << requestedRides.size() << "):\n";
        int count = 1;
        for (auto ride : requestedRides) {
            std::cout << "[" << count++ << "] ";
            ride->rideDetails();
        }
    }

    std::cout << "========================================\n";
}

#include "Ride.h"
#include <iostream>

Ride::Ride(int id, std::string pickup, std::string dropoff, double dist)
    : rideID(id), pickupLocation(pickup), dropoffLocation(dropoff), distance(dist) {}

double Ride::fare() const {
    return distance * 1.5;
}

void Ride::rideDetails() const {
    std::cout << "Ride ID: " << rideID
              << ", From: " << pickupLocation
              << ", To: " << dropoffLocation
              << ", Distance: " << distance << " miles"
              << ", Fare: $" << fare() << std::endl;
}
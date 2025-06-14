#include "StandardRide.h"
#include <iostream>

StandardRide::StandardRide(int id, std::string pickup, std::string dropoff, double dist)
    : Ride(id, pickup, dropoff, dist) {}

double StandardRide::fare() const {
    return distance * 2.0;
}
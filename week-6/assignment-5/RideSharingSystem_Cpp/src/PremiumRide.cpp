#include "PremiumRide.h"
#include <iostream>

PremiumRide::PremiumRide(int id, std::string pickup, std::string dropoff, double dist)
    : Ride(id, pickup, dropoff, dist) {}

double PremiumRide::fare() const {
    return distance * 3.5;
}

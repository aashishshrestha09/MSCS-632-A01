#ifndef PREMIUMRIDE_H
#define PREMIUMRIDE_H

#include "Ride.h"

class PremiumRide : public Ride {
public:
    PremiumRide(int id, std::string pickup, std::string dropoff, double dist);
    double fare() const override;
};

#endif
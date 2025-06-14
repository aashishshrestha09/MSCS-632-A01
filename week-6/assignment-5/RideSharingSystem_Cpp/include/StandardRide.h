#ifndef STANDARDRIDE_H
#define STANDARDRIDE_H

#include "Ride.h"

class StandardRide : public Ride {
public:
    StandardRide(int id, std::string pickup, std::string dropoff, double dist);
    double fare() const override;
};

#endif
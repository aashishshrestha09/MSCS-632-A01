#ifndef RIDE_H
#define RIDE_H

#include <string>

class Ride {
protected:
    int rideID;
    std::string pickupLocation;
    std::string dropoffLocation;
    double distance;

public:
    Ride(int id, std::string pickup, std::string dropoff, double dist);
    virtual double fare() const;
    virtual void rideDetails() const;
    virtual ~Ride() {}
};

#endif
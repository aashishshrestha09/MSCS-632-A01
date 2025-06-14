#ifndef DRIVER_H
#define DRIVER_H

#include <string>
#include <vector>
#include "Ride.h"

class Driver {
protected:
    int driverID;
    std::string name;
    double rating;
    std::vector<Ride*> assignedRides;

public:
    Driver(int id, std::string n, double r);
    void addRide(Ride* ride);
    void getDriverInfo() const;
};

#endif
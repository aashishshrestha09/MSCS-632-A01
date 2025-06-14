#ifndef RIDER_H
#define RIDER_H

#include <string>
#include <vector>
#include "Ride.h"

class Rider {
protected:
    int riderID;
    std::string name;
    std::vector<Ride*> requestedRides;

public:
    Rider(int id, std::string n);
    void requestRide(Ride* ride);
    void viewRides() const;
};

#endif
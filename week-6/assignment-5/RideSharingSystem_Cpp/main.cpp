#include <iostream>
#include <vector>
#include "Driver.h"
#include "PremiumRide.h"
#include "Rider.h"
#include "StandardRide.h"

int main() {
    std::cout << "Ride Sharing System Started 🚗\n";

    StandardRide* sRide = new StandardRide(1, "Downtown", "Airport", 10);
    PremiumRide* pRide = new PremiumRide(2, "Hotel", "Stadium", 8);

    std::vector<Ride*> rides = {sRide, pRide};
    for (auto ride : rides) {
        ride->rideDetails();
    }

    Driver driver(101, "Aashish Shrestha", 4.9);
    driver.addRide(sRide);
    driver.addRide(pRide);
    driver.getDriverInfo();

    Rider rider(201, "Ashmin Shrestha");
    rider.requestRide(sRide);
    rider.requestRide(pRide);
    rider.viewRides();

    delete sRide;
    delete pRide;

    return 0;
}
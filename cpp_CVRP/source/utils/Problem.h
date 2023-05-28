#ifndef CVRP_PROBLEM_H
#define CVRP_PROBLEM_H

#include "LocationNode.h"
#include "LocationsContainer.h"

class Problem{
public:
    Problem();
    Problem(LocationsContainer& locations,
            int vehicleCapacity);

    int VehicleCapacity() const;
    LocationsContainer& Locations();

private:
    LocationsContainer _locations;
    int _vehicleCapacity;
};

#endif //CVRP_PROBLEM_H

#ifndef CVRP_ROUTE_H
#define CVRP_ROUTE_H

#include <vector>
#include <iostream>
#include "LocationNode.h"

class Route{
public:
    // constructors
    Route();
    Route(int distance, int demand, int id);

    // getters
    int GetID() const;
    int GetTotalDistance() const;
    int GetTotalDemand() const;
    bool DemandIsInCapacity(int capacity) const;

private:
    int ID;
    int totalCost;
    int totalDemand;
    int capacity;
    int load;
    std::vector<LocationNode> customers;
};

#endif //CVRP_ROUTE_H

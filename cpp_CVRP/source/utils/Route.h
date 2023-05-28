#ifndef CVRP_ROUTE_H
#define CVRP_ROUTE_H

#include <vector>
#include <iostream>
#include "LocationNode.h"
#include "../includes/math/MathUtil.h"

class Route{
public:
    // constructors
    Route();
    Route(int distance, int demand, int id);
    Route(int capacity, int id);

    // getters
    int GetID() const;
    int GetTotalDistance() const;
    int GetTotalDemand() const;
    int Load() const;
    bool DemandIsInCapacity(int capacity) const;

    void AddLocation(LocationNode node);

    void PrintRoute() const;

private:
    int ID;
    int totalCost;
    int totalDemand;
    int capacity;
    int _load;
    std::vector<LocationNode> _customers;
};

#endif //CVRP_ROUTE_H

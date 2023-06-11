#ifndef CVRP_ROUTE_H
#define CVRP_ROUTE_H

#include <vector>
#include <iostream>
#include "LocationNode.h"
#include "../../includes/math/MathUtil.h"

class Route{
public:
    // constructors
    Route();
    Route(int id);
    Route(int capacity, int id);
    Route(int distance, int demand, int id);

    // getters
    int GetID() const;
    int GetTotalDistance() const;
    int GetTotalDemand() const;
    int Load() const;
    bool DemandIsInCapacity(int capacity) const;

    void AddLocation(LocationNode node);

    void PrintRoute() const;

private:
    int _routeID;
    int _routeCost;
    int _routeDemand;
    int _vehicleCapacity;
    int _cargo;
    std::vector<LocationNode> _customers;
};

#endif //CVRP_ROUTE_H

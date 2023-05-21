#ifndef CVRP_LOCATIONSCONTAINER_H
#define CVRP_LOCATIONSCONTAINER_H

#include <vector>
#include <iostream>
#include "LocationNode.h"
#include "Route.h"
#include "MathUtil.h"

class LocationsContainer{
public:
    LocationsContainer();

    void AddLocation(LocationNode& location);
    void RemoveLocation(LocationNode& locNode);
    Route CreateRoute(const std::vector<int>& locationIDs, int ID);
    LocationNode GetDepot();
    void AddDemandToLocation(int locID, int demand);
    static int GetDistanceBetweenLocations(const LocationNode& loc1, const LocationNode& loc2);

    bool CheckVisitedOnce();

private:
    std::vector<LocationNode> locations;
};

#endif //CVRP_LOCATIONSCONTAINER_H

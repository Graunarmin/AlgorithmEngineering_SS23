#ifndef CVRP_LOCATIONSCONTAINER_H
#define CVRP_LOCATIONSCONTAINER_H

#include <vector>
#include <iostream>
#include "LocationNode.h"
#include "Route.h"
#include "../includes/math/MathUtil.h"

class LocationsContainer{
public:
    LocationsContainer();

    void AddLocation(LocationNode& location);
    void RemoveLocation(LocationNode& locNode);
    Route CreateRoute(const std::vector<int>& locationIDs, int ID);
    LocationNode& GetDepot();
    void AddDemandToLocation(int locID, int demand);
    static int LocationDistance(const LocationNode& loc1, const LocationNode& loc2);

    bool CheckVisitedOnce();

    void CreateDistanceMatrix();
    std::vector<std::vector<int>> DistanceMatrix();

    bool AnyNodeUnvisited();
    std::tuple<bool, LocationNode&> FindNearestUnvisited(LocationNode& node, int maxDemand);

private:
    std::vector<LocationNode> _locations;
    std::vector<std::vector<int>> _distanceMatrix;
};

#endif //CVRP_LOCATIONSCONTAINER_H

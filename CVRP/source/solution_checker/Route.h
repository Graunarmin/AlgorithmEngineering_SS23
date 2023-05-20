#ifndef CVRP_ROUTE_H
#define CVRP_ROUTE_H

#include <vector>
#include "LocationNode.h"
#include "VrpData.h"

class Route{
public:
    // constructors
    Route(const std::vector<int>& customers, VrpData vrp);

    // getters
    int GetTotalDistance();
    int GetTotalDemand();

private:
    std::vector<LocationNode> routeNodes;

    void AddLocationToRoute(LocationNode location);
};

#endif //CVRP_ROUTE_H

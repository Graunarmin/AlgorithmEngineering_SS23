#include "Route.h"
#include "MathUtil.h"

#include <utility>

Route::Route(const std::vector<int>& customers, VrpData vrp)
{
    LocationNode depot = vrp.GetLocation(1);
    AddLocationToRoute(depot);
    for(int id : customers)
    {
        AddLocationToRoute(vrp.GetLocation(id+1));
    }
    AddLocationToRoute(depot);
}

int Route::GetTotalDistance()
{
    int totalDistance = 0;
    for(int i = 0; i < routeNodes.size()-1; ++i)
    {
        int x1 = routeNodes.at(i).GetX();
        int y1 = routeNodes.at(i).GetY();

        int x2 = routeNodes.at(i+1).GetX();
        int y2 = routeNodes.at(i+1).GetY();

        totalDistance += MathUtil::DistanceBetweenTwoPoints(x1,y1,x2,y2);
    }
}

void Route::AddLocationToRoute(LocationNode location)
{
    routeNodes.push_back(location);
}
#include "Route.h"

Route::Route() = default;

Route::Route(int id)
{
    _routeID = id;
}

Route::Route(int distance, int demand, int id)
{
    _routeID = id;
    _routeCost = distance;
    _routeDemand = demand;
}

Route::Route(int capacity, int id)
{
    _cargo = capacity;
    _routeID = id;
}

int Route::GetID() const
{
    return _routeID;
}

int Route::GetTotalDistance() const
{
    return _routeCost;
}

int Route::GetTotalDemand() const
{
    return _routeDemand;
}

bool Route::DemandIsInCapacity(int capacity) const
{
    if(_routeDemand > capacity)
    {
        std::cout << "Demand on Tour " << _routeID << " is bigger than vehicle _vehicleCapacity of " << capacity << std::endl;
        return false;
    }
    return true;
}

void Route::AddLocation(LocationNode node)
{
    if(!_customers.empty())
    {
        int x1 = _customers.back().X();
        int y1 = _customers.back().Y();

        int x2 = node.X();
        int y2 = node.Y();

        // increase to total distance of the route
        _routeCost += MathUtil::Distance(x1, y1, x2, y2);
    }
    // Add node to route
    _customers.push_back(node);

    // increase total demand on this route
    _routeDemand += node.GetDemand();

    // decrease the loaded resources
    _cargo -= node.GetDemand();
}

int Route::Load() const
{
    return _cargo;
}

void Route::PrintRoute() const
{
    std::cout << "Route #" << _routeID << ": ";
    for(const auto& c : _customers)
    {

        std::cout << c.GetID() << " ";
    }
    std::cout << std::endl;
}


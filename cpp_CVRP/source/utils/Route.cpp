#include "Route.h"

Route::Route() = default;

Route::Route(int distance, int demand, int id)
{
    ID = id;
    totalCost = distance;
    totalDemand = demand;
}

Route::Route(int capacity, int id)
{
    _load = capacity;
    ID = id;
}

int Route::GetID() const
{
    return ID;
}

int Route::GetTotalDistance() const
{
    return totalCost;
}

int Route::GetTotalDemand() const
{
    return totalDemand;
}

bool Route::DemandIsInCapacity(int capacity) const
{
    if(totalDemand > capacity)
    {
        std::cout << "Demand on Tour " << ID << " is bigger than vehicle capacity of " << capacity << std::endl;
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
        totalCost += MathUtil::Distance(x1,y1,x2,y2);
    }
    // Add node to route
    _customers.push_back(node);

    // increase total demand on this route
    totalDemand += node.GetDemand();

    // decrease the loaded resources
    _load -= node.GetDemand();
}

int Route::Load() const
{
    return _load;
}

void Route::PrintRoute() const
{
    std::cout << "Route #" << ID << ": ";
    for(const auto& c : _customers)
    {

        std::cout << c.GetID() << " ";
    }
    std::cout << std::endl;
}


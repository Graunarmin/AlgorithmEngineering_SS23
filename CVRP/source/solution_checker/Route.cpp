#include "Route.h"

Route::Route() = default;

Route::Route(int distance, int demand, int id)
{
    ID = id;
    totalCost = distance;
    totalDemand = demand;
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
        std::cout << "Demand on Tour " << ID << " is bigger than vehicle capacity of "
                  << capacity <<". Invalid Solution!" << std::endl;
        return false;
    }
    return true;
}


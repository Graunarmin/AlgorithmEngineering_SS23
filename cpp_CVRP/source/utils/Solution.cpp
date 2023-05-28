#include "Solution.h"

Solution::Solution() = default;

Solution::Solution(std::vector<Route>& routes)
{
    _routes = routes;
}

Solution::Solution(std::vector<Route> &routes, LocationsContainer& locations, int solFileCosts)
{
    _routes = routes;
    _locations = locations;
    _solFileCosts = solFileCosts;
}

bool Solution::CheckSolution(Problem& problem)
{
    if(!TotalCostMatches())
    {
        std::cout << "Due to Brain-Error" << std::endl;
    }
    if(CapacityConditionValid(problem) && OneVisitConditionValid(problem))
    {
        std::cout << "Solution is VALID for given Problem." << std::endl;
        return true;
    }
    std::cout << "Solution is NOT VALID for given Problem." << std::endl;
    return false;
}

bool Solution::CapacityConditionValid(Problem& problem)
{
    for(auto& route : _routes)
    {
        if(!route.DemandIsInCapacity(problem.VehicleCapacity()))
        {
            return false;
        }
    }
    std::cout << "The demand on all routes is less or equal to the maximum vehicle capacity of " <<  problem.VehicleCapacity() << std::endl;
    return true;
}

bool Solution::OneVisitConditionValid(Problem& problem)
{
    if(!_locations.CheckVisitedOnce())
    {
        return false;
    }
    return true;
}

bool Solution::TotalCostMatches()
{
    int totalDist = 0;
    for(auto& route : _routes)
    {
        totalDist += route.GetTotalDistance();
    }

    if(_solFileCosts != totalDist)
    {
        std::cout << "The solution-costs of " << _solFileCosts << " for the Tour do not match the calculated costs of "
                  << totalDist << " (but this is probably due to our rounding or calculation)." << std::endl;
        return false;
    }
    std::cout << "The solution-costs of " << _solFileCosts << " for the Tour match the calculated costs." << std::endl;
    return true;
}

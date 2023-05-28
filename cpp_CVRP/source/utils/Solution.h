#ifndef CVRP_SOLUTION_H
#define CVRP_SOLUTION_H

#include "Route.h"
#include "Problem.h"
#include <vector>

class Solution{
public:
    Solution();
    Solution(std::vector<Route>& routes);
    Solution(std::vector<Route>& routes, LocationsContainer& locations, int solFileCosts);

    bool CheckSolution(Problem& problem);


private:
    std::vector<Route> _routes;
    int _solFileCosts;
    LocationsContainer _locations;

    bool CapacityConditionValid(Problem& problem);
    bool OneVisitConditionValid(Problem& problem);
    bool TotalCostMatches();
};

#endif //CVRP_SOLUTION_H

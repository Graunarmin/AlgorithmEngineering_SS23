#include "GreedySolver.h"

GreedySolver::GreedySolver() = default;

GreedySolver::GreedySolver(LocationsContainer &locations, int capacity)
{
    _locations = locations;
    _vehicleCapacity = capacity;
}

void GreedySolver::Solve()
{
    std::vector <Route> routes{};
    int routeID = 0;

    while(_locations.AnyNodeUnvisited())
    {
        routeID += 1;
        // Start new Route at Depot
        Route route{_vehicleCapacity, routeID};
        LocationNode current = _locations.GetDepot();
        route.AddLocation(current);

        while (true)
        {
            //Then find the nearest unvisited node for which the _cargo is still enough
            const auto [found, nearest] = _locations.FindNearestUnvisited(current, route.Load());

            // If we did find a next node and the vehicle can satisfy its demand
            if(found && route.Load() - nearest.GetDemand() >= 0)
            {
                // add that node to the route
                route.AddLocation(nearest);

                // then mark the node as visited
                nearest.Visit();
            }
                // if we could not find a node that fulfills the conditions, we return to the depot
            else
            {
                current = _locations.GetDepot();
                route.AddLocation(current);

                // add the route to the solutions
                routes.push_back(route);

                // then start a new route
                break;
            }
        }
        int totalCost = 0;
        for(const auto& r : routes)
        {
            totalCost += r.GetTotalDistance();
            r.PrintRoute();
        }
        std::cout << "Cost " << totalCost << std::endl;

        bool visitedOnce = _locations.CheckVisitedOnce();
        if(visitedOnce)
        {
            std::cout << "In this Solution every Customer was visited exactly once." << std::endl;
        }
        else
        {
            std::cout << "There are customers missing from the Tour or some were visited multiple times." << std::endl;
        }

    }
}


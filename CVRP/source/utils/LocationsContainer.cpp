#include "LocationsContainer.h"

LocationsContainer::LocationsContainer() = default;

void LocationsContainer::AddLocation(LocationNode& location)
{
    locations.push_back(location);
}

void LocationsContainer::RemoveLocation(LocationNode& locNode)
{
    // go over the _locations-vector, find the one with the matching ID and remove it
    locations.erase(std::remove_if(
            locations.begin(), locations.end(),
            [&locNode](LocationNode loc){return loc.GetID() == locNode.GetID();}),
                    locations.end());
}

/// Returns the Depot from the List of Locations
/// \return
LocationNode LocationsContainer::GetDepot()
{
    if(locations.empty()){
        std::cout << "No _locations added yet." << std::endl;
        return LocationNode{};
    }
    return locations.at(0);
}


Route LocationsContainer::CreateRoute(const std::vector<int>& locationIDs, int ID)
{
    int totalDistance = 0;
    int totalDemand = 0;

    // all routes start at depot
    LocationNode start = GetDepot();

    // go ove the locations-vector
    for(LocationNode& loc : locations)
    {
        // if the ID of an element is in the locationIDs vector,
        if(std::find(locationIDs.begin(), locationIDs.end(), loc.GetID()) != locationIDs.end())
        {
            // mark this node as visited
            loc.Visit();

            //compute distance between start and loc
            totalDistance += GetDistanceBetweenLocations(start, loc);

            // increase Route-Demand by Location-Demand
            totalDemand += loc.GetDemand();

            // set start to loc
            // ToDo: Check for possible Error when setting start-Node to next node (important for computing the correct distance)
            start = loc;
        }
    }

    // all routes end at depot
    LocationNode end = GetDepot();
    totalDistance += GetDistanceBetweenLocations(start, end);

    // Create Route Object
    Route route{totalDistance, totalDemand, ID};

    return route;
}

void LocationsContainer::AddDemandToLocation(int locID, int demand)
{
    std::find_if(locations.begin(), locations.end(),
                 [&locID](LocationNode loc){return loc.GetID() == locID;})->SetDemand(demand);
}

int LocationsContainer::GetDistanceBetweenLocations(const LocationNode& loc1, const LocationNode& loc2)
{
    int x1 = loc1.GetX();
    int y1 = loc1.GetY();

    int x2 = loc2.GetX();
    int y2 = loc2.GetY();

    return MathUtil::DistanceBetweenTwoPoints(x1,y1,x2,y2);
}

bool LocationsContainer::CheckVisitedOnce()
{
    for(LocationNode& loc : locations)
    {
        if(loc.TimesVisited() != 1 && loc.GetID() != 1)
        {
            std::cout << "Node " << loc.GetID() << " was visited " << loc.TimesVisited() << " times." << std::endl;
            return false;
        }
    }
    std::cout << "Every Customer was visited exactly once." << std::endl;
    return true;
}
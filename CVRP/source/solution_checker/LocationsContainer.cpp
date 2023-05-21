#include "LocationsContainer.h"

LocationsContainer::LocationsContainer() = default;

void LocationsContainer::AddLocation(LocationNode location)
{
    locations.push_back(location);
}

void LocationsContainer::RemoveLocation(LocationNode locNode)
{
    // go over the locations-vector, find the one with the matching ID and remove it
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
        std::cout << "No locations added yet." << std::endl;
        return LocationNode{};
    }
    return locations.at(0);
}


Route LocationsContainer::CreateRoute(std::vector<int> locationIDs, int ID)
{
    int totalDistance = 0;
    int totalDemand = 0;

    // all routes start at depot
    LocationNode start = GetDepot();

    // go ove the locations-vector
    for(LocationNode& loc : locations)
    {
        // if the ID-1 of an element is in the locationIDs vector,
        if(std::find(locationIDs.begin(), locationIDs.end(), loc.GetID()) != locationIDs.end())
        {
            // mark this node as visited
            loc.Visit();
            //compute distance between start and loc
            totalDistance += GetDistanceBetweenLocations(start, loc);
            totalDemand += loc.GetDemand();

            // set start to loc
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

int LocationsContainer::GetDistanceBetweenLocations(LocationNode loc1, LocationNode loc2)
{
    int x1 = loc1.GetX();
    int y1 = loc1.GetY();

    int x2 = loc2.GetX();
    int y2 = loc2.GetY();

    return MathUtil::DistanceBetweenTwoPoints(x1,y1,x2,y2);
}

bool LocationsContainer::CheckVisitedOnce()
{
    for(auto& loc : locations)
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
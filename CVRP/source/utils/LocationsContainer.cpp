#include "LocationsContainer.h"

LocationsContainer::LocationsContainer() = default;

void LocationsContainer::AddLocation(LocationNode& location)
{
    _locations.push_back(location);
}

void LocationsContainer::RemoveLocation(LocationNode& locNode)
{
    // go over the _locations-vector, find the one with the matching ID and remove it
    _locations.erase(std::remove_if(
                             _locations.begin(), _locations.end(),
                             [&locNode](LocationNode loc){return loc.GetID() == locNode.GetID();}),
                     _locations.end());
}

/// Returns the Depot from the List of Locations
/// \return
LocationNode LocationsContainer::GetDepot()
{
    if(_locations.empty()){
        std::cout << "No _locations added yet." << std::endl;
        return LocationNode{};
    }
    return _locations.at(0);
}


Route LocationsContainer::CreateRoute(const std::vector<int>& locationIDs, int ID)
{
    int totalDistance = 0;
    int totalDemand = 0;

    // all routes start at depot
    LocationNode start = GetDepot();

    // go ove the _locations-vector
    for(LocationNode& loc : _locations)
    {
        // if the ID of an element is in the locationIDs vector,
        if(std::find(locationIDs.begin(), locationIDs.end(), loc.GetID()) != locationIDs.end())
        {
            // mark this node as visited
            loc.Visit();

            //compute distance between start and loc
            totalDistance += LocationDistance(start, loc);

            // increase Route-Demand by Location-Demand
            totalDemand += loc.GetDemand();

            // set start to loc
            // ToDo: Check for possible Error when setting start-Node to next node (important for computing the correct distance)
            start = loc;
        }
    }

    // all routes end at depot
    LocationNode end = GetDepot();
    totalDistance += LocationDistance(start, end);

    // Create Route Object
    Route route{totalDistance, totalDemand, ID};

    return route;
}

void LocationsContainer::AddDemandToLocation(int locID, int demand)
{
    std::find_if(_locations.begin(), _locations.end(),
                 [&locID](LocationNode loc){return loc.GetID() == locID;})->SetDemand(demand);
}

int LocationsContainer::LocationDistance(const LocationNode& loc1, const LocationNode& loc2)
{
    int x1 = loc1.X();
    int y1 = loc1.Y();

    int x2 = loc2.X();
    int y2 = loc2.Y();

    return MathUtil::Distance(x1, y1, x2, y2);
}

bool LocationsContainer::CheckVisitedOnce()
{
    for(LocationNode& loc : _locations)
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

void LocationsContainer::CreateDistanceMatrix()
{
    std::vector<int> tmp(_locations.size());
    for(int i = 0; i < _locations.size(); ++i)
    {
        _distanceMatrix.push_back(tmp);
    }
    for(int i = 0; i < _locations.size(); ++i)
    {
        for(int j = i; j < _locations.size(); ++j)
        {
            _distanceMatrix[i][j] = LocationDistance(_locations.at(i), _locations.at(j));
            _distanceMatrix[j][i] = _distanceMatrix[i][j];
        }
    }
}

std::vector<std::vector<int>> LocationsContainer::DistanceMatrix()
{
    return _distanceMatrix;
}
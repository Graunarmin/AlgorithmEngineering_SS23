#include "LocationsContainer.h"

LocationsContainer::LocationsContainer() = default;

void LocationsContainer::AddLocation(LocationNode& location)
{
    _locations.push_back(location);
}

void LocationsContainer::RemoveLocation(LocationNode& locNode)
{
    // go over the _AllLocations-vector, find the one with the matching _routeID and remove it
    _locations.erase(std::remove_if(
                             _locations.begin(), _locations.end(),
                             [&locNode](LocationNode loc){return loc.GetID() == locNode.GetID();}),
                     _locations.end());
}

/// Returns the Depot from the List of Locations
/// \return
LocationNode& LocationsContainer::GetDepot()
{
    LocationNode n{};
    if(_locations.empty()){
        std::cout << "No Locations added yet." << std::endl;
        //return n;
    }
    return _locations.at(0);
}

LocationNode &LocationsContainer::GetLocationNode(int nodeID)
{
    for(auto & loc : _locations)
    {
        if(loc.GetID() == nodeID)
        {
            return loc;
        }
    }
    LocationNode emptyNode{};
    return emptyNode;
}


Route LocationsContainer::CreateRoute(const std::vector<int>& customerIDs, int routeID)
{
    Route route{routeID};

    // all routes start at depot
    route.AddLocation(GetDepot());

    for(int customerId : customerIDs)
    {
        // ad next stop to route
        LocationNode customerNode = GetLocationNode(customerId);
        route.AddLocation(customerNode);
        // if the routeID of an element is in the customerIDs vector,
    }
    // all routes end at depot
    route.AddLocation(GetDepot());
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

// see https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L178
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

bool LocationsContainer::AnyNodeUnvisited()
{
    return std::any_of(_locations.begin(), _locations.end(),
                       [](LocationNode node){return node.TimesVisited() == 0;});
}

// Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L96
// Todo: The IDs probably don't match. This is a hot mess.
std::tuple<bool, LocationNode&> LocationsContainer::FindNearestUnvisited(LocationNode &node, int maxDemand)
{
    double cost = std::numeric_limits<double>::max();
    int closest_id = 0;

    bool found = false;
    for(int j = 0; j < _distanceMatrix[0].size(); j++)
    {
        if(_locations.at(j).TimesVisited() > 0
        && _locations.at(j).GetDemand() <= maxDemand
        && _distanceMatrix[node.GetID()][j] < cost)
        {
            cost = _distanceMatrix[node.GetID()][j];
            closest_id = j;
            found = true;
        }
    }
    if(found)
    {
        return {found, _locations.at(closest_id)};
    }
    LocationNode n{};
    return {false, n};
}
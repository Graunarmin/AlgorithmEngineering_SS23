#include "LocationNode.h"

LocationNode::LocationNode() = default;

LocationNode::LocationNode(int ID, int demand)
{
    locationID = ID;
    locationDemand = demand;
    xCoord = 0;
    yCoord = 0;
    visited = 0;
}

LocationNode::LocationNode(int ID, int x, int y)
{
    locationID = ID;
    xCoord = x;
    yCoord = y;
    locationDemand = 0;
    visited = 0;
}

LocationNode::LocationNode(int ID, int x, int y, int demand)
{
    locationID = ID;
    xCoord = x;
    yCoord = y;
    locationDemand = demand;
    visited = 0;
}

int LocationNode::GetID() const
{
    return locationID;
}

int LocationNode::GetDemand() const
{
    return locationDemand;
}

int LocationNode::GetX() const
{
    return xCoord;
}

int LocationNode::GetY() const
{
    return yCoord;
}

int LocationNode::TimesVisited()
{
    return visited;
}

void LocationNode::SetDemand(int demand)
{
    locationDemand = demand;
}

void LocationNode::SetCoordinates(int x, int y)
{
    xCoord = x;
    yCoord = y;
}

void LocationNode::Visit()
{
    visited += 1;
    //std::cout << "Visited Node " << locationID << ": visit no. " << visited << std::endl;
}


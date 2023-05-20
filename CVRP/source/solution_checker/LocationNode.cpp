#include "LocationNode.h"

LocationNode::LocationNode() {}

LocationNode::LocationNode(int ID, int demand)
{
    locationID = ID;
    locationDemand = demand;
}

LocationNode::LocationNode(int ID, int x, int y)
{
    locationID = ID;
    xCoord = x;
    yCoord = y;
}

LocationNode::LocationNode(int ID, int x, int y, int demand)
{
    locationID = ID;
    xCoord = x;
    yCoord = y;
    locationDemand = demand;
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

void LocationNode::SetDemand(int demand)
{
    locationDemand = demand;
}

void LocationNode::SetCoordinates(int x, int y)
{
    xCoord = x;
    yCoord = y;
}


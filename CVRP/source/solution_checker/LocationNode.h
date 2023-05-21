#ifndef CVRP_LOCATIONNODE_H
#define CVRP_LOCATIONNODE_H

#include <iostream>

class LocationNode{
public:
    // constructors
    LocationNode();
    LocationNode(int ID, int x, int y);
    LocationNode(int ID, int x, int y, int demand);
    LocationNode(int ID, int demand);

    // getter
    int GetID() const;
    int GetX() const;
    int GetY() const;
    int GetDemand() const;
    int TimesVisited();

    // setter
    void SetDemand(int demand);
    void SetCoordinates(int x, int y);
    void Visit();

private:
    // member
    int locationID;
    int xCoord;
    int yCoord;
    int locationDemand;
    int visited;

    // functions
};
#endif //CVRP_LOCATIONNODE_H

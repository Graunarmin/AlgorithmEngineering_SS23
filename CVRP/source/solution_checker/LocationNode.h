#ifndef CVRP_LOCATIONNODE_H
#define CVRP_LOCATIONNODE_H

#include <array>

class LocationNode{
public:
    LocationNode();

    LocationNode(int ID, int x, int y);

    LocationNode(int ID, int x, int y, int demand);

    LocationNode(int ID, int demand);

    // getter
    int GetID() const;
    int GetX() const;
    int GetY() const;
    int GetDemand() const;

    // setter

    void SetDemand(int demand);
    void SetCoordinates(int x, int y);


private:
    int locationID;
    int xCoord;
    int yCoord;
    int locationDemand;
};
#endif //CVRP_LOCATIONNODE_H

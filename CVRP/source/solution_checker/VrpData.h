#ifndef CVRP_VRPDATA_H
#define CVRP_VRPDATA_H

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "LocationNode.h"
#include "LocationsContainer.h"

class VrpData{
public:
    // constructors
    VrpData(std::string const& filePath);

    // getters
    int GetVehicleCapacity();
    LocationsContainer GetLocations();

private:
    // members
    LocationsContainer locs;
    //std::map<int, LocationNode> locations;
    int vehicleCapacity;
    int dimension;

    // functions
    void ReadData(std::string const& filePath);
};

#endif //CVRP_VRPDATA_H

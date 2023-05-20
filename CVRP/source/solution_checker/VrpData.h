#ifndef CVRP_VRPDATA_H
#define CVRP_VRPDATA_H

#include <string>
#include <array>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include "LocationNode.h"

class VrpData{
public:
    // constructors
    VrpData(std::string const& filePath);

    // getters
    int GetVehicleCapacity();
    int GetDemandForTour(std::vector<int> customers);
    LocationNode GetLocation(int id);

private:
    // members
    std::map<int, LocationNode> locations;
    int vehicleCapacity;
    int dimension;

    // functions
    void ReadData(std::string const& filePath);
};

#endif //CVRP_VRPDATA_H

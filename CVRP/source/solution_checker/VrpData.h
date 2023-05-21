#ifndef CVRP_VRPDATA_H
#define CVRP_VRPDATA_H

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "../utils/LocationNode.h"
#include "../utils/LocationsContainer.h"
#include "../utils/Problem.h"

class VrpData{
public:
    VrpData();

    Problem ReadData(std::string const& filePath);

};

#endif //CVRP_VRPDATA_H

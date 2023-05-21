#ifndef CVRP_SOLDATA_H
#define CVRP_SOLDATA_H

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include "Route.h"
#include "VrpData.h"

class SolData{

public:
    SolData(std::string const& filePath, VrpData vrp);

    bool IsValidFile();

private:
    // members
    std::vector<Route> routesData;
    std::map<int, std::vector<int>> routes;
    int solCost;
    bool fileIsValid = true;

    // functions
    bool ReadData(std::string const& filePath, VrpData vrp);
    bool TotalCostsMatch();
    bool CheckCapacityBound(int capacity);

};

#endif //CVRP_SOLDATA_H

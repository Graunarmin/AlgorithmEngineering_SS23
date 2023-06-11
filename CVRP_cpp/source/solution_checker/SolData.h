#ifndef CVRP_SOLDATA_H
#define CVRP_SOLDATA_H

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include "../utils/Route.h"
#include "../utils/Solution.h"
#include "VrpData.h"

class SolData{

public:
    SolData();

    Solution ReadData(std::string const& filePath, Problem& prbl);

};

#endif //CVRP_SOLDATA_H

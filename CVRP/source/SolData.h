#ifndef CVRP_SOLDATA_H
#define CVRP_SOLDATA_H

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

class SolData{

public:
    SolData();
    SolData(std::string const& filePath);

    // Getters


    // Setters

private:
    // members
    std::map<int, std::vector<int>> routes;
    int totalCost;
    std::vector<std::string> keywords{"Route", "Cost"};

    // functions
    void ReadData(std::string const& filePath);

};

#endif //CVRP_SOLDATA_H

#include "VrpData.h"

VrpData::VrpData() = default;

Problem VrpData::ReadData(const std::string &filePath)
{
    std::ifstream vrpFile;
    std::string line;

    LocationsContainer locations{};
    int vehicleCapacity = 0;

    vrpFile.open(filePath);

    if(vrpFile.is_open())
    {
        int section = 0;
        // Read in the file line by line:
        while(std::getline(vrpFile,line))
        {
            std::stringstream ss;
            std::string word;
            std::vector<std::string> tokens;

            ss << line;

            // The >> operator reads a string only until it encounters a white space character
            while (ss >> word)
            {
                tokens.push_back(word);
            }

            std::string keyword = tokens.at(0);

            if(keyword == "DIMENSION")
            {
                section = 1;
            }
            else if(keyword == "CAPACITY")
            {
                section = 1;
                vehicleCapacity = std::stoi(tokens.at(2));
            }
            else if(keyword == "NODE_COORD_SECTION")
            {
                section = 2;
                continue;
            }
            else if(keyword == "DEMAND_SECTION")
            {
                section = 3;
                continue;
            }
            else if(keyword == "DEPOT_SECTION")
            {
                section = 4;
                continue;
            }
            else if(keyword == "EOF")
            {
                break;
            }

            if(section == 2)
            {
                int id = std::stoi(keyword);
                int x = std::stoi(tokens.at(1));
                int y = std::stoi(tokens.at(2));
                LocationNode tmpNode{id, x, y};
                locations.AddLocation(tmpNode);
            }
            else if(section == 3)
            {
                int id = std::stoi(keyword);
                int demand = std::stoi(tokens.at(1));
                locations.AddDemandToLocation(id, demand);
            }
        }
    }
    Problem problem(locations, vehicleCapacity);
    return problem;
}
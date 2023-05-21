#include "VrpData.h"

VrpData::VrpData(const std::string &filePath)
{
    vehicleCapacity = 0;
    dimension = 0;
    ReadData(filePath);
    std::cout << "Vrp File is valid, Vehicle Capacity is " << vehicleCapacity << std::endl;
}

void VrpData::ReadData(const std::string &filePath)
{
    std::ifstream vrpFile;
    std::string line;

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
            //std::cout << keyword << std::endl;

            if(keyword == "DIMENSION")
            {
                section = 1;
                dimension = std::stoi(tokens.at(2));
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
                locs.AddLocation(LocationNode(id, x, y));
                //locations.insert({id, LocationNode(id, x, y)});
            }
            else if(section == 3)
            {
                int id = std::stoi(keyword);
                int demand = std::stoi(tokens.at(1));
                locs.AddDemandToLocation(id, demand);
                //locations.at(id).SetDemand(demand);
            }
        }
    }
}

int VrpData::GetVehicleCapacity()
{
    return vehicleCapacity;
}

LocationsContainer VrpData::GetLocations()
{
    return locs;
}
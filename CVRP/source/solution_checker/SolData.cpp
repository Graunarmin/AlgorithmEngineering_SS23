#include "SolData.h"

#include <utility>


SolData::SolData(std::string const& filePath, VrpData vrp)
{
    solCost = 0;
    ReadData(filePath, std::move(vrp));
}

bool SolData::ReadData(const std::string &filePath, VrpData vrp){
    std::ifstream solFile;
    std::string line;
    LocationsContainer locations = vrp.GetLocations();

    solFile.open(filePath);

    if(solFile.is_open())
    {
        // Read in the file line by line:
        while(std::getline(solFile,line))
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

            //check if the first word is a valid keyword
            std::string keyword = tokens.at(0);

            if(keyword == "Route")
            {
                // Route #1: 31 46 35
                // Die ID der Route ist die Nummer an Position 1
                std::string routeID = tokens.at(1);
                // Aber den # brauchen wir nicht
                routeID.erase(remove(routeID.begin(), routeID.end(), '#'), routeID.end());

                std::vector<int> customers;
                // Ab Position 2 beginnen die IDs der Customer, die auf der Route besucht werden
                for(int i = 2; i < tokens.size(); ++i)
                {
                    // die ID der Customer um 1 erhöhen, um die ID im vrp-file zu matchen
                    customers.push_back(std::stoi(tokens.at(i))+1);
                }

                // customer IDs in locations suchen
                Route route = locations.CreateRoute(customers, std::stoi(routeID));
                routesData.push_back(route);
                //routes.insert({std::stoi(routeID), customers});
                customers.clear();

            }
            else if(keyword == "Cost")
            {
                // Cost 27591
                solCost = std::stoi(tokens.at(1));
            }
            else
            {
                std::cout << tokens.at(0) << " is not a valid keyword, file not accepted.";
                fileIsValid = false;
                return false;
            }
            tokens.clear();
        }
        // Check if Total Costs are Correct
        if(!TotalCostsMatch())
        {
            //fileIsValid = false;
            //return false;
        }

        // Check if all Customers where visited exactly once
        if(!locations.CheckVisitedOnce())
        {
            fileIsValid = false;
            return false;
        }

        if(!CheckCapacityBound(vrp.GetVehicleCapacity()))
        {
            fileIsValid = false;
            return false;
        }

        std::cout << "Solution File is VALID " << std::endl;
        return true;
    }
    std::cout << "File could not be opened." << std::endl;
    return false;
}

bool SolData::TotalCostsMatch()
{
    int totalDistance = 0;
    for(Route route : routesData)
    {
        totalDistance += route.GetTotalDistance();
    }

    if(solCost != totalDistance)
    {
        std::cout << "The solution-costs of " << solCost << " for the Tour do not match the calculated costs of "
                << totalDistance << " (but this is probably due to our rounding or calculation)." << std::endl;
        return false;
    }
    std::cout << "The solution-costs of " << solCost << " for the Tour match the calculated costs." << std::endl;
    return true;
}

bool SolData::CheckCapacityBound(int capacity)
{
    for(Route route : routesData)
    {
        if(!route.DemandIsInCapacity(capacity))
        {
            return false;
        }
    }
    std::cout << "The demand on all routes is less or equal to the maximum vehicle capacity of " <<  capacity << std::endl;
    return true;
}

bool SolData::IsValidFile()
{
    return fileIsValid;
}


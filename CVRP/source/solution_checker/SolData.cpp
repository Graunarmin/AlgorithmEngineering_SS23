#include "SolData.h"


SolData::SolData() = default;

Solution SolData::ReadData(const std::string &filePath, Problem& prbl){
    std::ifstream solFile;
    std::string line;
    int solFileCosts;
    std::vector<Route> routes;
    LocationsContainer locations = prbl.Locations();

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
                // Route-ID is the number at pos 1
                std::string routeID = tokens.at(1);

                // we don't need the "#"
                routeID.erase(remove(routeID.begin(), routeID.end(), '#'), routeID.end());

                std::vector<int> customers;

                // Customer-IDs start from pos 2
                for(int i = 2; i < tokens.size(); ++i)
                {
                    // increase Customer-ID by one to match location-IDs from vrp-file
                    customers.push_back(std::stoi(tokens.at(i))+1);
                }

                // search for customer IDs in _AllLocations
                Route route = locations.CreateRoute(customers, std::stoi(routeID));
                routes.push_back(route);
                customers.clear();

            }
            else if(keyword == "Cost")
            {
                // Cost 27591
                solFileCosts = std::stoi(tokens.at(1));
            }
            else
            {
                std::cout << tokens.at(0) << " is not a valid keyword, file not accepted.";
            }
            tokens.clear();
        }
        std::cout << "Solution File is VALID." << std::endl;

        Solution solution{routes, locations, solFileCosts};
        return solution;
    }
    std::cout << "File could not be opened." << std::endl;
    Solution solution{};
    return solution;
}

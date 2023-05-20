#include "SolData.h"


SolData::SolData(std::string const& filePath){

    ReadData(filePath);
    std::cout << "Valid File, Costs are " << totalCost;

}

void SolData::ReadData(const std::string &filePath){
    std::ifstream solFile;
    std::string line;

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
                std::string routeID = tokens.at(1);
                routeID.erase(remove(routeID.begin(), routeID.end(), '#'), routeID.end());

                std::vector<int> customers;
                for(int i = 2; i < tokens.size(); ++i)
                {
                    customers.push_back(std::stoi(tokens.at(i)));
                }

                routes.insert({std::stoi(routeID), customers});
                customers.clear();

            }
            else if(keyword == "Cost")
            {
                totalCost = std::stoi(tokens.at(1));

            }
            else
            {
                std::cout << tokens.at(0) << " is not a valid keyword, file not accepted.";
            }
        }

    }
}
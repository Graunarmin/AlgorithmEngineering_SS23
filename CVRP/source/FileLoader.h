#ifndef CVRP_FILELOADER_H
#define CVRP_FILELOADER_H

#include <string>
#include <array>

class FileLoader{
    public:

        //Constructors
        FileLoader();

        //Getter

        //Setter


    private:
        void LoadVrpFile(std::string filepath);
        void LoadSolFile(std::string filePath);

        //Member (VRP)
        std::array<int,3> coordinates;
        std::array<int,2> demands;
        int vehicleCapacity;
};


#endif //CVRP_FILELOADER_H

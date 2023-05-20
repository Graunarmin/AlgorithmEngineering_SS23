#include <iostream>
#include <fstream>
#include <string>
#include "solution_checker/SolData.h"
#include "solution_checker/VrpData.h"

int main(int argc, char* argv[]) {

    std::string vrpPath = argv[1];
    std::string solPath = argv[2];

    VrpData vrp = VrpData(vrpPath);
    SolData solution = SolData(solPath);

    //check if the sum of all demands on a route is smaller than the vehicle capacity:


    return 0;
}

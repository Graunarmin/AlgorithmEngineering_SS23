#include <iostream>
#include <fstream>
#include <string>
#include "solution_checker/SolData.h"
#include "solution_checker/VrpData.h"

int main(int argc, char* argv[]) {

    std::string vrpPath = argv[1];
    std::string solPath = argv[2];

    VrpData vrp = VrpData(vrpPath);
    SolData solution = SolData(solPath, vrp);

    if(!solution.IsValidFile())
    {
        exit(0);
    }
    return 0;
}
#include <iostream>
#include <fstream>
#include <string>
#include "SolData.h"

int main(int argc, char* argv[]) {
    //std::cout << "Hello, World!" << std::endl;

    std::string vrpPath = argv[1];
    std::string solPath = argv[1];

    SolData solution = SolData(solPath);

    //check if the sum of all demands on a tour is smaller than the vehicle capacity:


    return 0;
}

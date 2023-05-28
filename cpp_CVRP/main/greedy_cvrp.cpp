#include <iostream>

#include "../source/solution_checker/VrpData.h"
#include "../source/greedy/GreedySolver.h"


int main(int argc, char* argv[]) {
    std::string vrpPath = argv[1];

    VrpData vrp{};
    Problem problem = vrp.ReadData(vrpPath);

    GreedySolver greedy{problem.Locations(), problem.VehicleCapacity()};
    greedy.Solve();

    return 0;
}

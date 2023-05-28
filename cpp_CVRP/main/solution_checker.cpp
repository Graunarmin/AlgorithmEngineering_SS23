#include <string>
#include "../source/solution_checker/SolData.h"
#include "../source/solution_checker/VrpData.h"

int main(int argc, char* argv[]) {

    std::string vrpPath = argv[1];
    std::string solPath = argv[2];

    VrpData vrp{};
    Problem problem = vrp.ReadData(vrpPath);

    SolData sol{};
    Solution solution = sol.ReadData(solPath, problem);

    solution.CheckSolution(problem);

    return 0;
}
cmake_minimum_required(VERSION 3.25)
project(CVRP)

set(CMAKE_CXX_STANDARD 17)

# Executable Solution Checker for Problem 1
add_executable(cvrp_SolutionChecker main/solution_checker.cpp
        source/solution_checker/VrpData.cpp source/solution_checker/VrpData.h
        source/solution_checker/SolData.cpp source/solution_checker/SolData.h
        source/utils/Problem.cpp source/utils/Problem.h
        source/utils/Solution.cpp source/utils/Solution.h
        source/utils/Route.cpp source/utils/Route.h
        source/utils/LocationNode.cpp source/utils/LocationNode.h
        source/utils/LocationsContainer.cpp source/utils/LocationsContainer.h
        includes/math/MathUtil.cpp includes/math/MathUtil.h
        )

target_include_directories(cvrp_SolutionChecker PUBLIC data/)
target_include_directories(cvrp_SolutionChecker PUBLIC includes/math/)

# Executable Greedy Heuristics for Problem 2
add_executable(greedy_cvrp main/greedy_cvrp.cpp
        source/greedy/GreedySolver.cpp source/greedy/GreedySolver.h source/utils/Problem.cpp source/utils/Problem.h source/utils/Solution.cpp source/utils/Solution.h)

target_include_directories(greedy_cvrp PUBLIC data/)
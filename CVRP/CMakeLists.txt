cmake_minimum_required(VERSION 3.25)
project(CVRP)

set(CMAKE_CXX_STANDARD 17)

add_executable(cvrp_SolutionChecker source/solution_checker.cpp source/solution_checker/VrpData.cpp source/solution_checker/VrpData.h source/solution_checker/SolData.cpp source/solution_checker/SolData.h source/solution_checker/LocationNode.cpp source/solution_checker/LocationNode.h)

target_include_directories(cvrp_SolutionChecker PUBLIC data/)

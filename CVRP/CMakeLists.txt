cmake_minimum_required(VERSION 3.25)
project(CVRP)

set(CMAKE_CXX_STANDARD 17)

add_executable(cvrp_SolutionChecker source/solution_checker.cpp source/VrpData.cpp source/VrpData.h source/SolData.cpp source/SolData.h)

target_include_directories(cvrp_SolutionChecker PUBLIC data/)

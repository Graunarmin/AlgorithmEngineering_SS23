#ifndef CVRP_GREEDYSOLVER_H
#define CVRP_GREEDYSOLVER_H

#include "../utils/LocationsContainer.h"
using namespace std;

class GreedySolver{
public:
    // constructors
    GreedySolver();
    GreedySolver(LocationsContainer& locations, int capacity);

    // solver
    void Solve();

    LocationsContainer _locations;
    int _vehicleCapacity;
};

#endif //CVRP_GREEDYSOLVER_H

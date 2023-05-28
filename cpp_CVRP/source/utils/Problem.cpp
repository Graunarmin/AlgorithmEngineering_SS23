#include "Problem.h"

Problem::Problem() = default;

Problem::Problem(LocationsContainer& locations, int vehicleCapacity)
{
    _locations = locations;
    _vehicleCapacity = vehicleCapacity;
}

int Problem::VehicleCapacity() const
{
    return _vehicleCapacity;
}

LocationsContainer& Problem::Locations()
{
    return _locations;
}
#include "MathUtil.h"
#include <utility>

int MathUtil::Distance(int x1, int y1, int x2, int y2)
{
    double distance = std::sqrt(
            std::pow((x2 - x1), 2) +
            std::pow((y2 - y1), 2));

    return std::floor(distance + 0.5);
}

#include "MathUtil.h"
#include <utility>

int MathUtil::DistanceBetweenTwoPoints(int x1, int y1, int x2, int y2)
{
    float distance = std::sqrt(
            std::pow(x2 - x1, 2) +
            std::pow(y2 - y1, 2) * 1.0
            );

    return std::floor(distance + 0.5f);
}

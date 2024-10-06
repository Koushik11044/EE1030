#include <stdio.h>

void find_x_intercept(float n[], float c, float *x_intercept, float *y_intercept) {
    *x_intercept = c / n[0];  // n[0] is the slope (m)
    *y_intercept = 0;           // The y-coordinate is always 0 on the x-axis
}

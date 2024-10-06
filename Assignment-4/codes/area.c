#include <stdio.h>
#include <math.h>

// Function to be integrated
double f(double x) {
    return 3 * x + 2;
}

// Function to find the area using the trapezoidal rule
double trapezoidalRule(double a, double b, int n) {
    double h = (b - a) / n;
    double area = 0.0;
    double x;

    // Sum up areas of each trapezoid
    for (int i = 0; i < n; i++) {
        x = a + i * h;
        double y1 = fabs(f(x));
        double y2 = fabs(f(x + h));
        area += (y1 + y2) * h / 2;
    }

    return area;
}

int main() {
    double x1 = -2.0;
    double x2 = 1.0;
    int n = 1000; // Number of trapezoids

    // Calculate area
    double area = trapezoidalRule(x1, x2, n);

    // Output the result
    printf("The area of the region is: %lf\n", area);

    return 0;
}


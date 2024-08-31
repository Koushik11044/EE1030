// midpoint.c
#include <stdio.h>

// Structure to represent a point
typedef struct {
    double x;
    double y;
} Point;

// Function to calculate the midpoint of two points
Point calculate_midpoint(Point p1, Point p2) {
    Point midpoint;
    midpoint.x = (p1.x + p2.x) / 2;
    midpoint.y = (p1.y + p2.y) / 2;
    return midpoint;
}


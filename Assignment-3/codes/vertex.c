#include <stdio.h>

// Function to calculate the C vertex
void find_c_vertex(double O[2], double A[2], double B[2], double C[2]) {
    C[0] = A[0] + B[0] - O[0];
    C[1] = A[1] + B[1] - O[1];
}


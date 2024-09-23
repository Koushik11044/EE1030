
#include <stdio.h>
#include <math.h>

double calculate_diagonal(double x1, double y1, double x2, double y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main() {
    double O[] = {0, 0};
    double B[] = {5, 0};
    double A[] = {0, 3};
    double C[2];
    C[0]=A[0]+B[0]-O[0];
    C[1]=A[1]+B[1]-O[1];
    double diagonal_OC = calculate_diagonal(O[0], O[1], C[0], C[1]);
    double diagonal_AB = calculate_diagonal(A[0], A[1], B[0], B[1]);

    FILE *file = fopen("output.dat", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    } 
   fprintf(file, "%.lf\n%.lf",C[0],C[1]); 
    fclose(file);

    printf("The Diagonal AB=%.2lf\n",diagonal_AB);
    return 0;
}


#include "../ctypes/matrix_mul.c"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random matrix
int* generate_random_matrix(int rows, int cols) {
    int* matrix = (int*)malloc(rows * cols * sizeof(int));
    if (!matrix) {
        return NULL;  // Memory allocation failure
    }

    for (int i = 0; i < rows * cols; i++) {
        matrix[i] = rand() % 10;  // Random values between 0 and 9
    }

    return matrix;
}

// Function to print a matrix (for debugging, optional)
void print_matrix(int* matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i * cols + j]);
        }
        printf("\n");
    }
}

int main() {
    const int size = 1000;

    // Seed the random number generator
    srand(time(NULL));

    // Generate two random 1000x1000 matrices
    int* mat1 = generate_random_matrix(size, size);
    int* mat2 = generate_random_matrix(size, size);

    if (!mat1 || !mat2) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    // Start the timer
    clock_t start = clock();

    // Perform matrix multiplication
    int* result = matrix_mul(mat1, size, size, mat2, size, size);
    
    // Stop the timer
    clock_t end = clock();

    if (!result) {
        fprintf(stderr, "Matrix multiplication failed.\n");
        free_matrix(mat1);
        free_matrix(mat2);
        return 1;
    }

    // Calculate the elapsed time in seconds
    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%02.2fs\n", time_taken);

    // Free allocated memory
    free_matrix(mat1);
    free_matrix(mat2);
    free_matrix(result);

    return 0;
}

#include <stdlib.h>

// Function to perform matrix multiplication
int* mul(int* mat1, int rows1, int cols1, int* mat2, int rows2, int cols2) {
    if (cols1 != rows2) {
        return NULL;  // Dimension mismatch
    }

    // Allocate memory for the result matrix
    int* result = (int*)malloc(rows1 * cols2 * sizeof(int));
    if (!result) {
        return NULL;  // Memory allocation failure
    }

    // Initialize the result matrix
    for (int i = 0; i < rows1 * cols2; i++) {
        result[i] = 0;
    }

    // Perform matrix multiplication
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            for (int k = 0; k < cols1; k++) {
                result[i * cols2 + j] += mat1[i * cols1 + k] * mat2[k * cols2 + j];
            }
        }
    }

    return result;
}

// Function to free allocated memory
void free_matrix(int* matrix) {
    free(matrix);
}


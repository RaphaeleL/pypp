#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

// Matrix multiplication function
static PyObject* matrix_mul_v3(PyObject* self, PyObject* args) {
    PyObject *mat1, *mat2;
    if (!PyArg_ParseTuple(args, "OO", &mat1, &mat2)) {
        return NULL;  // Error parsing arguments
    }

    if (!PyList_Check(mat1) || !PyList_Check(mat2)) {
        PyErr_SetString(PyExc_TypeError, "Both arguments must be lists.");
        return NULL;
    }

    Py_ssize_t rows1 = PyList_Size(mat1);
    Py_ssize_t cols1 = PyList_Size(PyList_GetItem(mat1, 0));
    Py_ssize_t rows2 = PyList_Size(mat2);
    Py_ssize_t cols2 = PyList_Size(PyList_GetItem(mat2, 0));

    if (cols1 != rows2) {
        PyErr_SetString(PyExc_ValueError, "Invalid matrix dimensions for multiplication.");
        return NULL;
    }

    // Initialize the result matrix
    PyObject* result = PyList_New(rows1);
    for (Py_ssize_t i = 0; i < rows1; i++) {
        PyObject* row = PyList_New(cols2);
        for (Py_ssize_t j = 0; j < cols2; j++) {
            PyList_SetItem(row, j, PyLong_FromLong(0));
        }
        PyList_SetItem(result, i, row);
    }

    // Perform matrix multiplication
    for (Py_ssize_t i = 0; i < rows1; i++) {
        for (Py_ssize_t j = 0; j < cols2; j++) {
            long sum = 0;
            for (Py_ssize_t k = 0; k < cols1; k++) {
                PyObject* val1 = PyList_GetItem(PyList_GetItem(mat1, i), k);
                PyObject* val2 = PyList_GetItem(PyList_GetItem(mat2, k), j);
                sum += PyLong_AsLong(val1) * PyLong_AsLong(val2);
            }
            PyList_SetItem(PyList_GetItem(result, i), j, PyLong_FromLong(sum));
        }
    }

    return result;
}

// Define module methods
static PyMethodDef MatrixMethods[] = {
    {"matrix_mul_v3", matrix_mul_v3, METH_VARARGS, "Perform matrix multiplication."},
    {NULL, NULL, 0, NULL}
};

// Define the module
static struct PyModuleDef matrixmodule = {
    PyModuleDef_HEAD_INIT,
    "matrix_mul_v3",  // Name of the module
    NULL,          // Optional documentation string
    -1,            // State (-1 means global state)
    MatrixMethods
};

// Initialize the module
PyMODINIT_FUNC PyInit_matrix_mul_v3(void) {
    return PyModule_Create(&matrixmodule);
}


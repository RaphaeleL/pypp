package main

/*
#include <stdlib.h>
*/
import "C"
import (
	"sync"
	"unsafe"
)

//export mul
func mul(mat1 *C.int, rows1, cols1 C.int, mat2 *C.int, rows2, cols2 C.int) *C.int {
	if cols1 != rows2 {
		return nil
	}

	result := C.malloc(C.size_t(rows1*cols2) * C.size_t(C.sizeof_int))
	if result == nil {
		return nil
	}

	res := (*[1 << 30]C.int)(result)[: rows1*cols2 : rows1*cols2]
	m1 := (*[1 << 30]C.int)(unsafe.Pointer(mat1))[: rows1*cols1 : rows1*cols1]
	m2 := (*[1 << 30]C.int)(unsafe.Pointer(mat2))[: rows2*cols2 : rows2*cols2]

	var wg sync.WaitGroup
	for i := 0; i < int(rows1); i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			for j := 0; j < int(cols2); j++ {
				sum := C.int(0)
				for k := 0; k < int(cols1); k++ {
					sum += m1[i*int(cols1)+k] * m2[k*int(cols2)+j]
				}
				res[i*int(cols2)+j] = sum
			}
		}(i)
	}

	wg.Wait()
	return (*C.int)(result)
}

//export free_matrix
func free_matrix(ptr *C.int) {
	C.free(unsafe.Pointer(ptr))
}

func main() {}

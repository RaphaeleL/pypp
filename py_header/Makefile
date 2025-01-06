PYTHON_CONFIG = python3-config
CFLAGS = -I$(shell $(PYTHON_CONFIG) --includes) -fPIC -arch arm64
LDFLAGS = $(shell $(PYTHON_CONFIG) --ldflags) -shared -arch arm64
LIBS = -lpython3.13
TARGET = matrix_mul_v3.so

all: build run clean

build:
	@gcc $(CFLAGS) matrix_mul_v3.c $(LDFLAGS) $(LIBS) -o $(TARGET)

run:
	@python3 main.py

clean:
	@rm -rf build module_matrix_mul.cpython-313-darwin.so $(TARGET)

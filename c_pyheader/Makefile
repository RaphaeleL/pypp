PYTHON_CONFIG = python3-config
CFLAGS = -I$(shell $(PYTHON_CONFIG) --includes) -fPIC #-arch arm64
LDFLAGS = $(shell $(PYTHON_CONFIG) --ldflags) -shared #-arch arm64
LIBS = -lpython3.13
TARGET = ccms_ccore_matrix.so

all: build run clean

build:
	@gcc $(CFLAGS) ccms_ccore_matrix.c $(LDFLAGS) $(LIBS) -o $(TARGET)

run:
	@python3 main.py

clean:
	@rm -rf build $(TARGET)

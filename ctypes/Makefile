all: build run clean

build: 
	@gcc -shared -o ccms_ccore_matrix.so -fPIC ccms_ccore_matrix.c

run:
	@python3 main.py

clean:
	@rm -rf ccms_ccore_matrix.so

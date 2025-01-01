all: build run clean

build: 
	@gcc -shared -o matrix_mul.so -fPIC matrix_mul.c

run:
	@python3 main.py

clean:
	@rm -rf matrix_mul.so

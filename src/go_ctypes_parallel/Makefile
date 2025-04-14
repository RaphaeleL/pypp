all: build run clean

build: 
	@go build -o main.so -buildmode=c-shared main.go

run:
	@python3 main.py

clean:
	@rm -rf main.so main.h

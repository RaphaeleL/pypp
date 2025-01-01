v1_create: 
	make -C v1 create

v2_create:
	make -C v2 create

v1_run:
	make -C v1 run 

v2_run:
	make -C v2 run 

plain_run:
	python3 plain.py

v1_compare: 
	make -C v1 compare 

v2_compare: 
	make -C v2 compare 

clean:
	make -C v2 clean 

help:
	@echo "v1_create: 	Create the Shared Libs for V1"
	@echo "v2_create: 	Create the Shared Libs for V2"
	@echo "v1_run:		Run C in Python V1" 
	@echo "v2_run:		Run C in Python V2" 
	@echo "plain_run: 	Run Plain Python"
	@echo "v1_compare: 	Compare V1 to Python" 
	@echo "v2_compare: 	Compare V2 to Python3" 
	@echo "clean: 		Cleanup Junk" 

all:
	g++-8 -std=c++1z a.cpp 2>&1 | tee build.log
run:
	cat a.txt | ./a.out | tee  b.txt
output:
	cat ouput.cpp | pbcopy
init:
	cp b.cpp a.cpp
test:
	diff b.txt c.txt
random:
	g++-7 -std=c++1z random.cpp 2>&1 | tee build.log

all:
	javac Main.java 2>&1 | tee build.log
run:
	cat a.txt | java Main | tee  b.txt
copy:
	cat Main.java | pbcopy
init:
	cp template.java Main.java
test:
	diff b.txt c.txt

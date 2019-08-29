all:
	cat a.txt | python3 a.py 2>&1 | tee  b.txt
copy:
	cat a.py | pbcopy
init:
	cp b.py a.py
test:
	diff b.txt c.txt

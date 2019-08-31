all:
	cat a.txt | ruby a.rb 2>&1 | tee  b.txt
copy:
	cat a.rb | pbcopy
init:
	cp b.rb a.rb
test:
	diff b.txt c.txt

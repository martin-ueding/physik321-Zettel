# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

physik321-08-Martin.pdf: H3.py.txt H3.c.txt

H3.py.txt: H3.py
	bash -c "/usr/bin/time -p ./$< &> $@"

H3.c.txt: H3-c
	bash -c "/usr/bin/time -p ./$< &> $@"

H3.java.txt: H3.class
	bash -c "/usr/bin/time -p java $< &> $@"

%.class: %.java
	javac $^

H3-c: H3.c
	gcc -Wall --pedantic -o $@ -O3 $^ -lm

%.pdf: %.tex
	pdflatex -shell-escape $<

.PHONY: clean
clean:
	latexmk -C
	$(RM) *.txt
	$(RM) *.class

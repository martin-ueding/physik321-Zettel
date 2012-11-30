# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

physik321-08-Martin.pdf: H3.py H3.txt H3-c.txt

H3.txt: H3.py
	"./$<" > "$@"

H3-c.txt: H3-c
	"./$<" > "$@"

H3-c: H3.c
	gcc -o $@ -O3 $^ -lm

%.pdf: %.tex
	pdflatex -shell-escape $<

.PHONY: clean
clean:
	latexmk -C

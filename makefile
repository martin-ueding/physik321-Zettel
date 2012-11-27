# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

physik321-08-Martin.pdf: H3.py H3.txt

H3.txt: H3.py
	"./$<" > "$@"

%.pdf: %.tex
	pdflatex -shell-escape $<

.PHONY: clean
clean:
	latexmk -C

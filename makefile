all:
	python mathquiz
	xelatex -shell-escape answer.tex
	xelatex -shell-escape question.tex

clean:
	rm -rf *.aux *.log *.out *.pdf *.tex _minted-*

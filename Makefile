LATEX = pdflatex -interaction=nonstopmode

MAIN_TEX = wolf_prize.tex
MAIN_PDF = wolf_prize.pdf

CHAPTERS = chapters/chapter_*.tex

.PHONY: all main clean cleanall quick

all: main

main: $(MAIN_PDF)

$(MAIN_PDF): $(MAIN_TEX) $(CHAPTERS)
	$(LATEX) $(MAIN_TEX)
	makeindex wolf_prize
	$(LATEX) $(MAIN_TEX)
	$(LATEX) $(MAIN_TEX)
	@echo "---"
	@echo "Output: $(MAIN_PDF)"
	@echo "Pages: $$(grep -c '\/Type\/Page' $(MAIN_PDF) 2>/dev/null || echo '?')"

quick:
	$(LATEX) $(MAIN_TEX)

clean:
	rm -f *.aux *.log *.out *.toc *.idx *.ilg *.ind chapters/*.aux chapters/*.log

cleanall: clean
	rm -f $(MAIN_PDF)

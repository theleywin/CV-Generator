NAME=cv

# Default target - compile the main CV
all:
	latexmk -pdf ${NAME}.tex

# Generate bilingual CVs with interactive color selection
generate:
	@python3 generate_cv.py

# Generate CVs with specific colors
cv-blue:
	@echo "Generating CVs with blue color..."
	@python3 generate_cv.py blue

cv-red:
	@echo "Generating CVs with red color..."
	@python3 generate_cv.py red

cv-green:
	@echo "Generating CVs with green color..."
	@python3 generate_cv.py green

cv-purple:
	@echo "Generating CVs with purple color..."
	@python3 generate_cv.py purple

cv-gray:
	@echo "Generating CVs with gray color..."
	@python3 generate_cv.py gray

cv-black:
	@echo "Generating CVs with black color..."
	@python3 generate_cv.py black

# Generate all color variations (English and Spanish)
all-colors:
	@for color in blue red green purple gray black; do \
		echo "Generating CVs with $$color color..."; \
		python3 generate_cv.py $$color || true; \
	done

# Clean auxiliary files
clean:
	@rm -f ${NAME}.aux ${NAME}.bbl ${NAME}.bcf ${NAME}.fdb_latexmk ${NAME}.fls ${NAME}.log ${NAME}.out ${NAME}.run.xml ${NAME}.blg ${NAME}.toc *\~
	@rm -f cv_en_*.aux cv_en_*.log cv_en_*.out cv_en_*.fdb_latexmk cv_en_*.fls cv_en_*.synctex.gz
	@rm -f cv_es_*.aux cv_es_*.log cv_es_*.out cv_es_*.fdb_latexmk cv_es_*.fls cv_es_*.synctex.gz
	@echo "Cleaned auxiliary files"

# Clean all generated PDFs
clean-pdfs:
	@rm -f cv_en_*.pdf cv_es_*.pdf
	@echo "Removed generated CV PDFs"

# Complete cleanup
distclean: clean clean-pdfs
	@rm -f ${NAME}.pdf
	@echo "Complete cleanup done"

# Show help
help:
	@echo "CV Generator - Available commands:"
	@echo ""
	@echo "  make all         - Compile the main cv.tex file"
	@echo "  make generate    - Generate bilingual CVs with interactive color selection"
	@echo "  make cv-blue     - Generate CVs with blue color"
	@echo "  make cv-red      - Generate CVs with red color"
	@echo "  make cv-green    - Generate CVs with green color"
	@echo "  make cv-purple   - Generate CVs with purple color"
	@echo "  make cv-gray     - Generate CVs with gray color"
	@echo "  make cv-black    - Generate CVs with black color"
	@echo "  make all-colors  - Generate CVs in all available colors"
	@echo "  make clean       - Remove auxiliary files"
	@echo "  make clean-pdfs  - Remove generated CV PDFs"
	@echo "  make distclean   - Complete cleanup (aux files + PDFs)"
	@echo "  make help        - Show this help message"
	@echo ""

.PHONY: all generate cv-blue cv-red cv-green cv-purple cv-gray cv-black all-colors clean clean-pdfs distclean help

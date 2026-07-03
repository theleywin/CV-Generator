#!/usr/bin/env python3
"""
CV Generator - Automated bilingual CV generation with customizable colors
Author: Pablo Gómez
Date: 2026-07-03

This script generates two versions of the CV (English and Spanish) with a selected color scheme.
Supported colors: blue, red, green, purple, gray, black
"""

import os
import subprocess
import sys
from pathlib import Path

# Color definitions
COLORS = {
    '1': ('blue', 'Azul'),
    '2': ('red', 'Rojo'),
    '3': ('green', 'Verde'),
    '4': ('purple', 'Morado'),
    '5': ('gray', 'Gris'),
    '6': ('black', 'Negro')
}

# ANSI color codes for terminal output
class Colors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    GRAY = '\033[90m'
    BLACK = '\033[90m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    """Print a fancy header"""
    print(f"\n{Colors.BOLD}{'='*60}")
    print("  📄 CV Generator - Bilingual Resume Builder")
    print(f"{'='*60}{Colors.END}\n")

def select_color():
    """Interactive color selection"""
    print(f"{Colors.BOLD}Selecciona el color del CV / Select CV color:{Colors.END}\n")
    for key, (color_en, color_es) in COLORS.items():
        color_code = getattr(Colors, color_en.upper(), '')
        print(f"  {color_code}{key}. {color_en.capitalize()} / {color_es}{Colors.END}")
    
    while True:
        choice = input(f"\n{Colors.BOLD}Ingresa el número (1-6): {Colors.END}").strip()
        if choice in COLORS:
            return COLORS[choice][0]
        print(f"{Colors.RED}Opción inválida. Por favor selecciona un número del 1 al 6.{Colors.END}")

def generate_tex_file(language, color):
    """Generate a temporary .tex file with the specified language and color"""
    # Map language codes to folder names
    language_folder = 'ingles' if language == 'en' else 'español'
    
    template = f"""\\documentclass[a4paper,12pt]{{article}}

%----------------------------------------------------------------------------------------
%	PACKAGES
%----------------------------------------------------------------------------------------
\\usepackage{{url}}
\\usepackage{{parskip}}
\\usepackage[none]{{hyphenat}}

%other packages for formatting
\\RequirePackage{{color}}
\\RequirePackage{{graphicx}}
\\usepackage[usenames,dvipsnames]{{xcolor}}
\\usepackage[scale=0.85]{{geometry}}

%tabularx environment
\\usepackage{{tabularx}}

%for lists within experience section
\\usepackage{{enumitem}}

% centered version of 'X' col. type
\\newcolumntype{{C}}{{>{{\\centering\\arraybackslash}}X}}

%to prevent spillover of tabular into next pages
\\usepackage{{supertabular}}
\\usepackage{{tabularx}}
\\newlength{{\\fullcollw}}
\\setlength{{\\fullcollw}}{{0.47\\textwidth}}

%custom \\section
\\usepackage{{titlesec}}
\\usepackage{{multicol}}
\\usepackage{{multirow}}

%for publications
\\usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{{biblatex}}

%Setup hyperref package, and colours for links
\\usepackage[unicode, draft=false]{{hyperref}}
\\addbibresource{{citations.bib}}
\\setlength\\bibitemsep{{1em}}

%for social icons
\\usepackage{{fontawesome5}}

%for ifthen
\\usepackage{{ifthen}}

%----------------------------------------------------------------------------------------
%	COLOR SCHEME
%----------------------------------------------------------------------------------------
\\def\\cvcolor{{{color}}}
\\input{{colors.tex}}

%CV Sections inspired by:
%http://stefano.italians.nl/archives/26
\\titleformat{{\\section}}{{\\Large\\scshape\\raggedright\\color{{primary}}}}{{}}{{0em}}{{}}[{{\\color{{primary}}\\titlerule[0.8pt]}}]
\\titlespacing{{\\section}}{{0pt}}{{12pt}}{{8pt}}

% Use accent color for links instead of fixed blue
\\hypersetup{{colorlinks,breaklinks,urlcolor=accent,linkcolor=accent}}

%----------------------------------------------------------------------------------------
%	JOB ENVIRONMENTS
%----------------------------------------------------------------------------------------
\\newenvironment{{jobshort}}[2]
    {{
    \\begin{{tabularx}}{{\\linewidth}}{{@{{}}l X r@{{}}}}
    \\textbf{{#1}} & \\hfill &  #2 \\\\[3.75pt]
    \\end{{tabularx}}
    }}
    {{
    }}

\\newenvironment{{joblong}}[2]
    {{
    \\begin{{tabularx}}{{\\linewidth}}{{@{{}}l X r@{{}}}}
    \\textbf{{#1}} & \\hfill & {{\\color{{secondary}}\\textit{{#2}}}} \\\\[3.75pt]
    \\end{{tabularx}}
    \\begin{{minipage}}[t]{{\\linewidth}}
    \\begin{{itemize}}[nosep,after=\\strut, leftmargin=1em, itemsep=2.5pt,label={{\\color{{primary}}$\\bullet$}}]
    }}
    {{
    \\end{{itemize}}
    \\end{{minipage}}
    }}

%----------------------------------------------------------------------------------------
%	BEGIN DOCUMENT
%----------------------------------------------------------------------------------------
\\begin{{document}}

% non-numbered pages
\\pagestyle{{empty}}

%----------------------------------------------------------------------------------------
%	CONTENT
%----------------------------------------------------------------------------------------
\\input{{{language_folder}/main.tex}}

\\end{{document}}
"""
    
    filename = f"cv_{language}_{color}.tex"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return filename

def compile_pdf(tex_file, language, color):
    """Compile the .tex file to PDF using pdflatex"""
    print(f"\n{Colors.BOLD}Compilando CV en {language.upper()} con color {color}...{Colors.END}")
    
    try:
        # Run pdflatex twice for proper rendering
        for i in range(2):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode != 0:
                print(f"{Colors.RED}Error al compilar {tex_file}{Colors.END}")
                print(result.stdout)
                return False
        
        output_pdf = tex_file.replace('.tex', '.pdf')
        if os.path.exists(output_pdf):
            print(f"{Colors.GREEN}✓ CV generado exitosamente: {output_pdf}{Colors.END}")
            return True
        else:
            print(f"{Colors.RED}✗ No se pudo generar el PDF{Colors.END}")
            return False
            
    except FileNotFoundError:
        print(f"{Colors.RED}Error: pdflatex no está instalado o no está en el PATH{Colors.END}")
        print("Por favor instala TeX Live o MiKTeX")
        return False
    except Exception as e:
        print(f"{Colors.RED}Error inesperado: {e}{Colors.END}")
        return False

def cleanup_temp_files(base_name):
    """Clean up auxiliary files generated by LaTeX"""
    extensions = ['.aux', '.log', '.out', '.fdb_latexmk', '.fls', '.synctex.gz', '.bcf', '.run.xml', '.bbl', '.blg']
    for ext in extensions:
        file = f"{base_name}{ext}"
        if os.path.exists(file):
            os.remove(file)

def main():
    """Main execution flow"""
    print_header()
    
    # Check if color is provided as command line argument
    if len(sys.argv) > 1:
        # Get color from command line argument
        color_input = sys.argv[1].lower().strip()
        # Validate that it's a valid color
        valid_colors = [color_en for _, (color_en, _) in COLORS.items()]
        if color_input in valid_colors:
            color = color_input
        else:
            print(f"{Colors.RED}Error: '{color_input}' no es un color válido.{Colors.END}")
            print(f"{Colors.BOLD}Colores válidos:{Colors.END} {', '.join(valid_colors)}")
            return 1
    else:
        # Interactive color selection
        color = select_color()
    
    print(f"\n{Colors.BOLD}Generando CVs en Inglés y Español con el color: {color.upper()}{Colors.END}")
    print(f"{Colors.GRAY}{'─'*60}{Colors.END}")
    
    success_count = 0
    
    # Generate both language versions
    for language in ['en', 'es']:
        # Generate temporary .tex file
        tex_file = generate_tex_file(language, color)
        
        # Compile to PDF
        if compile_pdf(tex_file, language, color):
            success_count += 1
        
        # Cleanup temporary .tex file
        if os.path.exists(tex_file):
            os.remove(tex_file)
        
        # Cleanup auxiliary files
        base_name = f"cv_{language}_{color}"
        cleanup_temp_files(base_name)
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*60}")
    if success_count == 2:
        print(f"{Colors.GREEN}✓ ¡Generación completada exitosamente!{Colors.END}")
        print(f"\n{Colors.BOLD}Archivos generados:{Colors.END}")
        print(f"  • cv_en_{color}.pdf (English)")
        print(f"  • cv_es_{color}.pdf (Español)")
    else:
        print(f"{Colors.RED}✗ Algunos CVs no pudieron ser generados{Colors.END}")
    
    print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")
    
    return 0 if success_count == 2 else 1

if __name__ == "__main__":
    sys.exit(main())

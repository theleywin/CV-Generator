#!/bin/bash
# Quick demo - Generate one CV in each color to showcase the system

echo "🎨 Generando CVs de demostración en todos los colores..."
echo ""

colors=("1" "2" "3" "4" "5" "6")
color_names=("blue" "red" "green" "purple" "gray" "black")

for i in "${!colors[@]}"; do
    echo "▶ Generando CV en color: ${color_names[$i]}..."
    echo "${colors[$i]}" | python3 generate_cv.py > /dev/null 2>&1
done

echo ""
echo "✓ ¡Demostración completada!"
echo ""
echo "📁 Archivos generados:"
ls -1 cv_*.pdf 2>/dev/null | sort

echo ""
echo "💡 Puedes abrir cualquiera de estos PDFs para ver los diferentes estilos."

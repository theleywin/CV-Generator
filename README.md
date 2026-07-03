# 📄 CV Generator - Sistema de Generación Automatizada de CV Bilingüe

Sistema automatizado para generar currículums profesionales en **inglés y español** con **esquemas de color personalizables**.

## 🎨 Colores Disponibles

- **Azul** (Blue) - Profesional y corporativo
- **Rojo** (Red) - Audaz y llamativo
- **Verde** (Green) - Fresco y moderno
- **Morado** (Purple) - Creativo y único
- **Gris** (Gray) - Minimalista y elegante
- **Negro** (Black) - Clásico y sobrio

## 🚀 Uso Rápido

### Generación Interactiva (Recomendado)

```bash
python3 generate_cv.py
```

o usando Make:

```bash
make generate
```

El script te pedirá que selecciones un color y generará automáticamente:
- `cv_en_[color].pdf` - Versión en inglés
- `cv_es_[color].pdf` - Versión en español

### Generación con Color Específico

Usando Make:

```bash
make cv-blue      # CV azul
make cv-red       # CV rojo
make cv-green     # CV verde
make cv-purple    # CV morado
make cv-gray      # CV gris
make cv-black     # CV negro
```

### Generar Todas las Variaciones de Color

```bash
make all-colors
```

Esto generará 12 PDFs (6 colores × 2 idiomas).

## 📁 Estructura del Proyecto

```
Pablo_CV/
├── generate_cv.py       # Script principal de generación
├── colors.tex           # Definiciones de esquemas de color
├── ingles               # Contenido en inglés
├── español              # Contenido en español
├── Makefile             # Comandos de automatización
└── README.md            # Esta documentación
```

## 🛠️ Requisitos

- **LaTeX** (TeX Live o MiKTeX)
  - Paquetes necesarios: fontawesome5, biblatex, xcolor, geometry, titlesec
- **Python 3.x**
- **Make** (opcional, para usar comandos simplificados)

### Instalación de LaTeX en macOS

```bash
brew install --cask mactex
```

### Verificar instalación

```bash
pdflatex --version
python3 --version
```

### Ajustar Colores

Edita `colors.tex` para modificar los valores RGB de cada esquema de color.

Ejemplo:
```latex
\ifthenelse{\equal{#1}{blue}}{
  \definecolor{primary}{rgb}{0.1,0.2,0.5}      % Color principal
  \definecolor{secondary}{rgb}{0.3,0.3,0.3}    % Color secundario
  \definecolor{accent}{rgb}{0.0,0.3,0.6}       % Color de acento
}{}
```

### Agregar Nuevos Colores

1. Edita `colors.tex` y agrega un nuevo bloque `\ifthenelse`
2. Actualiza el diccionario `COLORS` en `generate_cv.py`
3. (Opcional) Agrega un comando en el `Makefile`

## 🧹 Limpieza

```bash
make clean          # Eliminar archivos auxiliares (.aux, .log, etc.)
make clean-pdfs     # Eliminar PDFs generados
make distclean      # Limpieza completa
```

## 📊 Comandos Disponibles

```bash
make help           # Ver todos los comandos disponibles
```

## 💡 Consejos

1. **Primera vez**: Usa `make generate` para familiarizarte con el proceso
2. **Producción**: Genera solo los colores que necesitas con `make cv-[color]`
3. **Experimentación**: Usa `make all-colors` para ver todas las variaciones
4. **Mantenimiento**: Ejecuta `make clean` regularmente para liberar espacio

## 🐛 Solución de Problemas

### Error: "pdflatex not found"
- Instala TeX Live o MiKTeX
- Verifica que `pdflatex` esté en tu PATH

### Error al compilar LaTeX
- Revisa el contenido de los archivos `.tex`
- Asegúrate de que todos los paquetes estén instalados
- Ejecuta `make clean` y vuelve a intentar

### Los colores no se aplican correctamente
- Verifica que `colors.tex` exista y tenga la sintaxis correcta
- Revisa que el nombre del color sea exactamente uno de los definidos

## 📄 Licencia

MIT License - Puedes usar, modificar y distribuir libremente.

## 👤 Autor

**Pablo Gómez**
- GitHub: [@theleywin](https://github.com/theleywin)
- Email: pgomezvidal034@gmail.com

---

**¡Éxito con tus aplicaciones! 🎉**

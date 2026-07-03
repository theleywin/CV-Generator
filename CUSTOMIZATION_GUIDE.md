# 🎯 Guía de Personalización del CV

Este documento te guía para personalizar tu CV con tu propia información.

## 📝 Información Personal

### 1. Editar Datos de Contacto

Abre `content_en.tex` y `content_es.tex` y modifica:

```latex
{\fontsize{32}{38}\selectfont\color{primary}\textbf{TU NOMBRE}}
```

Y los enlaces:
```latex
\href{https://github.com/tu-usuario}{\raisebox{-0.05\height}{\Large\faGithub}\ tu-usuario}
\href{mailto:tu-email@ejemplo.com}{\raisebox{-0.05\height}{\Large\faEnvelope} \ tu-email@ejemplo.com}
\href{tel:+1234567890}{\raisebox{-0.05\height}{\Large\faMobile} \ (+12) 34567890}
```

### 2. Modificar el Resumen

Busca la sección `\section{Summary}` o `\section{Resumen}` y actualiza el texto descriptivo con tu perfil profesional.

### 3. Actualizar Experiencia Laboral

Cada trabajo usa el formato:

```latex
\begin{joblong}{Empresa --- Puesto}{Fecha inicio - Fecha fin}
\item Descripción de responsabilidad 1
\item Descripción de responsabilidad 2
\item Descripción de responsabilidad 3
\end{joblong}
```

**Para agregar más trabajos:** Copia un bloque completo y pégalo donde quieras.
**Para eliminar trabajos:** Borra el bloque completo desde `\begin{joblong}` hasta `\end{joblong}`.

### 4. Actualizar Educación

Modifica la sección:

```latex
\section{Education}  % o \section{Educación} en español
\begin{tabularx}{\linewidth}{@{}l X@{}}	
Fecha inicio - Fecha fin & Título en \textbf{Universidad}, Ciudad, País \\
\end{tabularx}
```

### 5. Actualizar Habilidades

En la sección `\section{Skills}` o `\section{Habilidades}`:

```latex
\begin{multicols}{2}
\begin{itemize}[nosep,after=\strut, leftmargin=1em, itemsep=3pt,label={\color{primary}$\bullet$}]
\item \textbf{Categoría:} Tecnología1, Tecnología2, Tecnología3
\item \textbf{Otra categoría:} Herramienta1, Herramienta2
\end{itemize}
\end{multicols}
```

## 🎨 Personalizar Colores

### Modificar Colores Existentes

Edita `colors.tex` y ajusta los valores RGB (rango: 0.0 a 1.0):

```latex
\ifthenelse{\equal{#1}{blue}}{
  \definecolor{primary}{rgb}{0.1,0.2,0.5}      % Color principal (títulos, nombre)
  \definecolor{secondary}{rgb}{0.3,0.3,0.3}    % Color secundario (fechas)
  \definecolor{accent}{rgb}{0.0,0.3,0.6}       % Color de acento (enlaces)
}{}
```

### Agregar un Nuevo Color

1. En `colors.tex`, agrega un nuevo bloque:

```latex
\ifthenelse{\equal{#1}{orange}}{
  \definecolor{primary}{rgb}{0.8,0.4,0.0}
  \definecolor{secondary}{rgb}{0.3,0.3,0.3}
  \definecolor{accent}{rgb}{0.9,0.5,0.0}
}{}
```

2. En `generate_cv.py`, actualiza el diccionario `COLORS`:

```python
COLORS = {
    '1': ('blue', 'Azul'),
    '2': ('red', 'Rojo'),
    '3': ('green', 'Verde'),
    '4': ('purple', 'Morado'),
    '5': ('gray', 'Gris'),
    '6': ('black', 'Negro'),
    '7': ('orange', 'Naranja'),  # ⬅️ Nuevo color
}
```

3. (Opcional) En el `Makefile`, agrega:

```makefile
cv-orange:
	@echo "Generating CVs with orange color..."
	@python3 -c "exec(open('generate_cv.py').read().replace('select_color()', '\"orange\"'))"
```

## 📐 Ajustes de Formato

### Cambiar Tamaño de Márgenes

En `generate_cv.py`, busca:

```latex
\usepackage[scale=0.85]{geometry}
```

- `scale=0.85` = márgenes estándar
- `scale=0.90` = márgenes más amplios (menos contenido)
- `scale=0.80` = márgenes más pequeños (más contenido)

### Cambiar Tamaño del Nombre

En `content_en.tex` y `content_es.tex`:

```latex
{\fontsize{32}{38}\selectfont...}  % Tamaño actual
{\fontsize{36}{42}\selectfont...}  % Más grande
{\fontsize{28}{34}\selectfont...}  # Más pequeño
```

### Ajustar Espaciado entre Secciones

En el script `generate_cv.py`, busca:

```latex
\titlespacing{\section}{0pt}{12pt}{8pt}
```

- Primer número: espacio izquierdo
- Segundo número: espacio antes del título
- Tercer número: espacio después del título

## 🌐 Agregar Más Idiomas

Para agregar un tercer idioma (por ejemplo, francés):

1. Crea `content_fr.tex` con el contenido traducido
2. En `generate_cv.py`, modifica el loop principal:

```python
for language in ['en', 'es', 'fr']:  # Agrega 'fr'
    # ... resto del código
```

## 🔧 Troubleshooting Común

### El PDF no refleja mis cambios
- Asegúrate de editar el archivo correcto (`content_en.tex` o `content_es.tex`)
- Ejecuta `make clean` antes de regenerar
- Verifica que no haya errores de sintaxis LaTeX

### Los acentos no aparecen correctamente
- Verifica que los archivos estén guardados en codificación UTF-8
- LaTeX debería manejar automáticamente los caracteres especiales

### El texto se sale de la página
- Reduce el tamaño de letra en secciones específicas
- Ajusta el `scale` en geometry
- Divide textos largos en múltiples líneas

## 💡 Mejores Prácticas

1. **Mantén respaldo**: Haz copia de tu versión original antes de cambios grandes
2. **Prueba incremental**: Regenera el CV después de cada cambio importante
3. **Consistencia**: Usa el mismo formato para todas las secciones similares
4. **Brevedad**: Los CVs de 1-2 páginas son ideales
5. **Legibilidad**: No uses tamaños de letra menores a 10pt

## 📚 Recursos Adicionales

- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [ShareLaTeX Guides](https://www.overleaf.com/learn)
- [FontAwesome Icons](https://fontawesome.com/v5/search)

---

**¿Necesitas más ayuda?** Abre un issue en el repositorio o contacta al autor.

# 📂 Estructura Modular del CV

## 🎯 Visión General

El CV ahora está organizado en una **estructura modular** que facilita agregar, quitar o modificar secciones independientemente. Cada sección está en su propio archivo `.tex`, lo que hace el sistema más mantenible y escalable.

## 📁 Estructura de Carpetas

```
Pablo_CV/
├── ingles/                  # 🇬🇧 English version
│   ├── main.tex             # Main file that loads all sections
│   ├── header.tex           # Name and contact information
│   ├── summary.tex          # Professional summary
│   ├── experience.tex       # Work experience
│   ├── education.tex        # Education
│   ├── skills.tex           # Technical skills and languages
│   ├── publications.tex     # 📄 Optional: Publications
│   ├── projects.tex         # 💻 Optional: Notable projects
│   ├── certifications.tex   # 🎓 Optional: Certifications
│   └── awards.tex           # 🏆 Optional: Awards & honors
│
├── español/                 # 🇪🇸 Spanish version
│   ├── main.tex             # Archivo principal que carga todas las secciones
│   ├── header.tex           # Nombre e información de contacto
│   ├── summary.tex          # Resumen profesional
│   ├── experience.tex       # Experiencia laboral
│   ├── education.tex        # Educación
│   ├── skills.tex           # Habilidades técnicas e idiomas
│   ├── publications.tex     # 📄 Opcional: Publicaciones
│   ├── projects.tex         # 💻 Opcional: Proyectos destacados
│   ├── certifications.tex   # 🎓 Opcional: Certificaciones
│   └── awards.tex           # 🏆 Opcional: Premios y reconocimientos
│
├── generate_cv.py           # Script de generación
├── colors.tex               # Esquemas de color
└── ... (otros archivos)
```

## 🔧 Cómo Funciona

### main.tex - El Archivo Orquestador

Cada idioma tiene un archivo `main.tex` que **carga todas las secciones** usando `\input{}`:

```latex
% ingles/main.tex o español/main.tex

\input{ingles/header.tex}
\input{ingles/summary.tex}
\input{ingles/experience.tex}
\input{ingles/education.tex}
\input{ingles/skills.tex}

% Secciones opcionales (comentadas por defecto)
% \input{ingles/publications.tex}
% \input{ingles/projects.tex}
% \input{ingles/certifications.tex}
% \input{ingles/awards.tex}
```

## ✅ Ventajas de esta Estructura

1. **🔀 Modularidad**: Cada sección es independiente
2. **➕ Fácil agregar secciones**: Solo crea el archivo y agrégalo en `main.tex`
3. **➖ Fácil quitar secciones**: Comenta o elimina la línea en `main.tex`
4. **🔄 Fácil reordenar**: Cambia el orden de las líneas `\input{}`
5. **📝 Mantenimiento simplificado**: Edita solo la sección que necesitas
6. **🌐 Sincronización multiidioma**: Estructura paralela en inglés/español

---

## 📖 Guía de Uso

### ✏️ Editar una Sección Existente

Simplemente edita el archivo correspondiente:

```bash
# Editar experiencia en inglés
nano ingles/experience.tex

# Editar habilidades en español
nano español/skills.tex
```

No necesitas tocar ningún otro archivo. Los cambios se reflejarán automáticamente.

---

### ➕ Agregar una Nueva Sección

**Ejemplo: Agregar sección de "Publicaciones"**

#### Paso 1: Descomentar la plantilla existente

Ya incluimos plantillas para secciones comunes. Simplemente descomenta el contenido:

```bash
# Editar la plantilla
nano ingles/publications.tex
```

Descomenta y personaliza:

```latex
\section{Publications}

\begin{itemize}[nosep,after=\strut, leftmargin=1em, itemsep=3pt,label={\color{primary}$\bullet$}]

\item \textbf{Tu Nombre}, Co-Autor. (2026). "Título de tu Artículo." 
      \textit{Conference Name}. DOI: 10.xxxx/xxxxx

\end{itemize}
```

#### Paso 2: Activar la sección en main.tex

```bash
nano ingles/main.tex
```

Descomenta la línea:

```latex
\input{ingles/skills.tex}

% DESCOMENTA ESTA LÍNEA ⬇️
\input{ingles/publications.tex}
```

#### Paso 3: Repetir en español

```bash
nano español/publications.tex
nano español/main.tex
```

#### Paso 4: Generar CV

```bash
make generate
```

¡Listo! Tu CV ahora incluye la sección de publicaciones.

---

### ➕ Crear una Sección Completamente Nueva

**Ejemplo: Agregar sección de "Idiomas"**

#### Paso 1: Crear el archivo de la sección

```bash
# Versión en inglés
cat > ingles/languages.tex << 'EOF'
%----------------------------------------------------------------------------------------
%	LANGUAGES
%----------------------------------------------------------------------------------------
\section{Languages}

\begin{tabularx}{\linewidth}{@{}l X@{}}
\textbf{Spanish} & Native \\
\textbf{English} & Fluent (C1) \\
\textbf{French} & Intermediate (B1) \\
\end{tabularx}
EOF

# Versión en español
cat > español/languages.tex << 'EOF'
%----------------------------------------------------------------------------------------
%	IDIOMAS
%----------------------------------------------------------------------------------------
\section{Idiomas}

\begin{tabularx}{\linewidth}{@{}l X@{}}
\textbf{Español} & Nativo \\
\textbf{Inglés} & Fluido (C1) \\
\textbf{Francés} & Intermedio (B1) \\
\end{tabularx}
EOF
```

#### Paso 2: Agregar a main.tex

```bash
# Inglés
echo "\input{ingles/languages.tex}" >> ingles/main.tex

# Español
echo "\input{español/languages.tex}" >> español/main.tex
```

#### Paso 3: Generar

```bash
make generate
```

---

### ➖ Quitar una Sección

**Opción 1: Comentar (temporal)**

```latex
% En main.tex
\input{ingles/summary.tex}
% \input{ingles/publications.tex}  ← Comentada, no aparecerá
\input{ingles/experience.tex}
```

**Opción 2: Eliminar (permanente)**

Simplemente borra la línea `\input{}` de `main.tex`.

---

### 🔄 Reordenar Secciones

Cambia el orden de las líneas `\input{}` en `main.tex`:

**Antes:**
```latex
\input{ingles/summary.tex}
\input{ingles/experience.tex}
\input{ingles/education.tex}
\input{ingles/skills.tex}
```

**Después** (Education antes que Experience):
```latex
\input{ingles/summary.tex}
\input{ingles/education.tex}
\input{ingles/experience.tex}
\input{ingles/skills.tex}
```

---

## 🎨 Secciones Opcionales Incluidas

### 📄 Publications (Publicaciones)

Para académicos o investigadores:

```bash
# Activar
nano ingles/publications.tex     # Descomenta y edita
nano ingles/main.tex              # Descomenta \input{ingles/publications.tex}
```

### 💻 Projects (Proyectos)

Para mostrar proyectos personales o open-source:

```bash
nano ingles/projects.tex
nano ingles/main.tex
```

### 🎓 Certifications (Certificaciones)

Para mostrar certificaciones profesionales:

```bash
nano ingles/certifications.tex
nano ingles/main.tex
```

### 🏆 Awards (Premios)

Para reconocimientos y honores:

```bash
nano ingles/awards.tex
nano ingles/main.tex
```

---

## 💡 Mejores Prácticas

### ✅ DO (Hacer)

1. **Mantén sincronizados inglés y español**: Si agregas una sección en inglés, agrégala también en español
2. **Usa nombres descriptivos**: Si creas nuevas secciones, usa nombres claros
3. **Comenta en lugar de eliminar**: Si no estás seguro, comenta la línea en `main.tex`
4. **Ordena lógicamente**: Coloca las secciones más importantes primero
5. **Prueba después de cambios**: Regenera el CV después de cada modificación

### ❌ DON'T (No hacer)

1. **No mezcles idiomas**: Cada carpeta debe tener contenido en su idioma
2. **No dupliques información**: Cada dato debe estar en una sola sección
3. **No sobrecargues**: Un CV debe ser 1-2 páginas máximo
4. **No olvides comentarios**: Documenta cambios importantes en los archivos
5. **No edites archivos generados**: Edita solo los archivos fuente en `ingles/` y `español/`

---

## 🔍 Ejemplos de Casos de Uso

### Para Desarrollador Junior

```latex
% main.tex - Orden recomendado
\input{ingles/header.tex}
\input{ingles/summary.tex}
\input{ingles/skills.tex}        % Skills primero (menos experiencia)
\input{ingles/projects.tex}      % Proyectos personales
\input{ingles/education.tex}
\input{ingles/experience.tex}    % Experiencia al final
```

### Para Desarrollador Senior

```latex
% main.tex - Orden recomendado
\input{ingles/header.tex}
\input{ingles/summary.tex}
\input{ingles/experience.tex}    % Experiencia primero
\input{ingles/skills.tex}
\input{ingles/education.tex}     % Educación al final
```

### Para Investigador/Académico

```latex
% main.tex - Orden recomendado
\input{ingles/header.tex}
\input{ingles/summary.tex}
\input{ingles/education.tex}      % Educación primero
\input{ingles/publications.tex}   % Publicaciones destacadas
\input{ingles/experience.tex}
\input{ingles/awards.tex}         % Premios académicos
\input{ingles/skills.tex}
```

### Para Freelancer/Consultor

```latex
% main.tex - Orden recomendado
\input{ingles/header.tex}
\input{ingles/summary.tex}
\input{ingles/skills.tex}         % Skills primero
\input{ingles/projects.tex}       % Proyectos destacados
\input{ingles/experience.tex}
\input{ingles/certifications.tex} % Certificaciones
\input{ingles/education.tex}
```

---

## 🛠️ Solución de Problemas

### Error: "File not found"

```bash
! LaTeX Error: File `ingles/newsection.tex' not found.
```

**Solución:**
- Verifica que el archivo existe: `ls ingles/newsection.tex`
- Revisa que el nombre en `main.tex` coincida exactamente
- Asegúrate de usar la ruta correcta (`ingles/` o `español/`)

### Una sección no aparece

**Checklist:**
1. ¿Está descomentado el contenido en el archivo de la sección?
2. ¿Está descomentado el `\input{}` en `main.tex`?
3. ¿Está antes de `\end{document}` en el flujo?
4. ¿Regeneraste el CV después del cambio?

### Sección aparece en blanco

**Causa:** El contenido está comentado en el archivo de la sección

**Solución:** Edita el archivo y descomenta el contenido

---

## 📚 Recursos Adicionales

- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Guía de personalización completa
- [PRACTICAL_EXAMPLES.md](PRACTICAL_EXAMPLES.md) - Ejemplos prácticos de uso
- [README_GENERATOR.md](README_GENERATOR.md) - Documentación del sistema

---

## 🎉 Resumen Rápido

```bash
# 1. Editar una sección
nano ingles/experience.tex

# 2. Agregar nueva sección
nano ingles/newsection.tex
echo "\input{ingles/newsection.tex}" >> ingles/main.tex

# 3. Quitar una sección
# Comenta la línea en main.tex

# 4. Reordenar secciones
# Cambia el orden de \input{} en main.tex

# 5. Generar CV
make generate
```

---

**Estructura modular = Máxima flexibilidad** 🚀

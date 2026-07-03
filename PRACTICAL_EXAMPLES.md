# 💼 Ejemplos Prácticos de Uso del Sistema de CV

Este documento contiene ejemplos del mundo real para usar tu sistema de generación de CV.

---

## 📋 Escenario 1: Primera vez usando el sistema

**Situación:** Acabas de instalar el sistema y quieres generar tu primer CV.

```bash
# Paso 1: Personaliza tu información
open content_en.tex content_es.tex
# Edita tu nombre, experiencia, educación, etc.

# Paso 2: Genera tu CV con modo interactivo
python3 generate_cv.py
# Selecciona: 1 (azul) para un estilo profesional

# Paso 3: Revisa el resultado
open cv_en_blue.pdf cv_es_blue.pdf
```

**Resultado:** Tienes 2 CVs profesionales listos para enviar.

---

## 📋 Escenario 2: Aplicar a diferentes tipos de empresas

**Situación:** Quieres adaptar el estilo de tu CV según el tipo de empresa.

### Para Tech Startup (Creativo)
```bash
make cv-purple
# o
make cv-green
```

### Para Corporación (Profesional)
```bash
make cv-blue
# o
make cv-gray
```

### Para Agencia Creativa (Audaz)
```bash
make cv-red
```

### Para Posición Senior/Ejecutiva (Clásico)
```bash
make cv-black
# o
make cv-gray
```

---

## 📋 Escenario 3: Prepararse para feria de empleo

**Situación:** Tienes una feria de empleo mañana y quieres tener opciones.

```bash
# Genera todas las versiones
make all-colors

# Resultado: 12 PDFs diferentes
# Imprime 2-3 versiones que más te gusten
open cv_en_blue.pdf cv_en_gray.pdf cv_en_green.pdf
```

---

## 📋 Escenario 4: Actualización rutinaria del CV

**Situación:** Acabas de terminar un proyecto o cambiar de trabajo.

```bash
# 1. Actualiza el contenido
nano content_en.tex content_es.tex
# Agrega tu nueva experiencia/habilidades

# 2. Regenera tu versión favorita
make cv-blue

# 3. Limpia archivos viejos
make clean

# 4. Guarda en tu carpeta de documentos importantes
cp cv_en_blue.pdf ~/Documents/CV_2026_Actualizado.pdf
```

---

## 📋 Escenario 5: Aplicar a empresa internacional

**Situación:** La empresa acepta CVs en inglés o español.

```bash
# Genera solo el color que quieres
echo "1" | python3 generate_cv.py

# Envía ambas versiones
# - cv_en_blue.pdf → Para el recruiter internacional
# - cv_es_blue.pdf → Para el manager local
```

**Email sugerido:**
> Adjunto mi CV en ambos idiomas para su conveniencia:
> - CV_English.pdf
> - CV_Spanish.pdf

---

## 📋 Escenario 6: Experimentar con estilos

**Situación:** No estás seguro de qué color usar.

```bash
# Opción A: Genera todos y compara
./demo.sh

# Opción B: Genera tus 3 favoritos
make cv-blue cv-gray cv-purple

# Opción C: Pide opinión
# Genera varios y pregunta a amigos/mentores cuál prefieren
```

---

## 📋 Escenario 7: Portfolio para Freelancer

**Situación:** Necesitas múltiples versiones para diferentes clientes.

```bash
# Crea estructura organizada
mkdir -p ~/CV_Portfolio/{tech,creative,corporate}

# Genera versiones específicas
make cv-blue      # Para tech
make cv-purple    # Para creativos
make cv-black     # Para corporate

# Organiza
cp cv_en_blue.pdf ~/CV_Portfolio/tech/
cp cv_en_purple.pdf ~/CV_Portfolio/creative/
cp cv_en_black.pdf ~/CV_Portfolio/corporate/
```

---

## 📋 Escenario 8: Mantener múltiples versiones

**Situación:** Tienes experiencia en diferentes áreas (ej: Frontend y Data Science).

### Paso 1: Crea versiones de contenido
```bash
# Duplica los archivos de contenido
cp content_en.tex content_en_frontend.tex
cp content_en.tex content_en_datascience.tex
cp content_es.tex content_es_frontend.tex
cp content_es.tex content_es_datascience.tex
```

### Paso 2: Personaliza cada versión
```bash
# Edita content_en_frontend.tex
# - Enfatiza experiencia en React, Angular, etc.
# - Skills de frontend primero

# Edita content_en_datascience.tex
# - Enfatiza proyectos de ML/AI
# - Skills de Python, TensorFlow primero
```

### Paso 3: Genera manualmente
```bash
# Modifica temporalmente el script o los nombres
# O genera y renombra:
make cv-blue
mv cv_en_blue.pdf cv_frontend_blue.pdf

# Cambia content y regenera
make cv-purple
mv cv_en_purple.pdf cv_datascience_purple.pdf
```

---

## 📋 Escenario 9: Envío por email profesional

**Situación:** Quieres enviar tu CV con nombre profesional.

```bash
# Genera tu CV favorito
make cv-blue

# Renombra para envío profesional
cp cv_en_blue.pdf "Pablo_Gomez_Software_Developer_CV.pdf"
cp cv_es_blue.pdf "Pablo_Gomez_Desarrollador_Software_CV.pdf"

# Verifica el tamaño (debe ser < 2MB)
ls -lh Pablo_Gomez*.pdf
```

---

## 📋 Escenario 10: Integración con GitHub/Portfolio

**Situación:** Quieres que tu CV esté siempre disponible online.

```bash
# 1. Genera tu versión principal
make cv-blue

# 2. Crea/actualiza repositorio
git add cv_en_blue.pdf cv_es_blue.pdf
git commit -m "Update CV - $(date +%Y-%m-%d)"
git push

# 3. En tu README.md del portfolio
echo "📄 [Download my CV (English)](cv_en_blue.pdf)" >> README.md
echo "📄 [Descargar mi CV (Español)](cv_es_blue.pdf)" >> README.md
```

---

## 📋 Escenario 11: Automatización con Cron

**Situación:** Quieres generar tu CV automáticamente cada mes.

```bash
# Crea un script de actualización
cat > update_cv.sh << 'EOF'
#!/bin/bash
cd /Users/theleywin/Documents/Pablo_CV
make cv-blue
cp cv_en_blue.pdf ~/Dropbox/CV_Latest.pdf
echo "CV updated on $(date)" >> cv_update_log.txt
EOF

chmod +x update_cv.sh

# Programa tarea mensual (opcional)
# crontab -e
# 0 0 1 * * /Users/theleywin/Documents/Pablo_CV/update_cv.sh
```

---

## 📋 Escenario 12: Limpieza y mantenimiento

**Situación:** Tienes muchos archivos temporales.

```bash
# Ver espacio usado
du -sh .

# Limpieza ligera (mantiene PDFs)
make clean

# Limpieza de PDFs de prueba (mantiene tu favorito)
rm cv_en_{red,green,purple,gray,black}.pdf
rm cv_es_{red,green,purple,gray,black}.pdf

# Limpieza completa (cuidado!)
make distclean
```

---

## 🎯 Mejores Prácticas

### ✅ DO (Hacer)

1. **Mantén backups:** Guarda copias de tu CV en múltiples lugares
2. **Fecha tus archivos:** Usa nombres como `CV_2026_06.pdf`
3. **Versión de control:** Usa Git para trackear cambios en content_*.tex
4. **Prueba antes de enviar:** Abre y revisa cada PDF generado
5. **Personaliza por aplicación:** Ajusta contenido según la posición

### ❌ DON'T (No hacer)

1. **No uses imágenes grandes:** Mantén el CV en texto
2. **No exageres con colores:** Elige uno y úsalo consistentemente
3. **No olvides actualizar ambos idiomas:** Mantén sincronizados
4. **No envíes sin revisar:** Siempre revisa el PDF final
5. **No uses colores muy brillantes:** Mantén profesionalismo

---

## 💡 Tips Profesionales

### Para Desarrolladores
```bash
make cv-blue     # Más profesional
make cv-gray     # Minimalista
```

### Para Diseñadores/Creativos
```bash
make cv-purple   # Creativo pero profesional
make cv-green    # Fresco y moderno
```

### Para Ejecutivos/Management
```bash
make cv-black    # Clásico y serio
make cv-gray     # Elegante
```

### Para Startups/Tech
```bash
make cv-blue     # Confiable
make cv-green    # Innovador
```

---

## 🔧 Troubleshooting por Escenario

### "Mi CV se ve diferente en cada computadora"
```bash
# Asegúrate de usar las mismas fuentes
# Verifica que pdflatex esté actualizado
pdflatex --version

# Regenera desde cero
make distclean
make cv-blue
```

### "El PDF es muy grande"
```bash
# Verifica el tamaño
ls -lh cv_*.pdf

# Si es > 1MB, optimiza:
# Usa Acrobat o herramientas online para comprimir
```

### "Los acentos no se ven bien"
```bash
# Asegúrate que los archivos estén en UTF-8
file content_es.tex
# Debe decir: UTF-8 Unicode text
```

---

**¿Tienes otro escenario?** ¡Agrega tu propio ejemplo aquí! 🚀

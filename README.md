# Proyecto de Cuentos Educativos para Niños 🎨📚

Proyecto para crear cuentos ilustrados educativos usando Google Gemini API.

## 📁 Estructura del Proyecto

### Scripts Funcionales

- **`generar_imagen_con_gemini.py`** ⭐ **RECOMENDADO**
  - Usa el modelo `gemini-2.5-flash-image` (mismo que el chat de Gemini en el navegador)
  - Genera imágenes basándose en una imagen de referencia
  - **Ventajas:** Mejor calidad, mantiene estilo de referencia, más similar a Gemini web
  - **Uso:** Para generar escenas manteniendo consistencia del personaje Mateo

- **`generar_imagen_con_imagen4.py`**
  - Usa el modelo oficial `imagen-4.0-generate-001` de Imagen 4
  - Genera imágenes sin referencia
  - **Ventajas:** API específica de Imagen, más parámetros de configuración
  - **Uso:** Para generar imágenes simples sin necesidad de referencia

### Imágenes

- **`mateo.png`** - Imagen de referencia del personaje Mateo (8 años)
- **`mateo_gemini_dragon.png`** - Ejemplo generado con Gemini (Mateo vs dragón) ✅
- **`imagen_generada_1.png`** - Ejemplo generado con Imagen 4

## 🔑 API Key

Actualmente configurada: `AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk`

## 🚀 Cómo Usar

### Opción 1: Con Gemini (Recomendado)

```bash
python generar_imagen_con_gemini.py
```

Este script:
1. Analiza la imagen de referencia `mateo.png`
2. Genera una nueva escena manteniendo el estilo y características
3. Guarda el resultado como `mateo_gemini_dragon.png`

### Opción 2: Con Imagen 4

```bash
python generar_imagen_con_imagen4.py
```

Este script genera imágenes directamente con Imagen 4.

## 📝 Próximos Pasos

1. ✅ Generar imágenes con referencia de personaje
2. ✅ Mantener consistencia visual del personaje
3. ⏳ Crear sistema completo de generación de cuentos
4. ⏳ Integrar generación de audio/voz
5. ⏳ Crear videos a partir de las imágenes

## 🎯 Objetivo del Proyecto

Crear cuentos educativos ilustrados para enseñar a los niños sobre seguridad y buenos hábitos, con:
- Texto narrativo generado por Gemini
- Ilustraciones consistentes del personaje
- Voces/audio generado
- Video final del cuento

## 📦 Dependencias

```bash
pip install google-generativeai google-genai Pillow
```

## 🌟 Mejores Prácticas

- Usa `generar_imagen_con_gemini.py` para mantener consistencia del personaje
- Los prompts deben estar en **inglés** para mejores resultados
- La imagen de referencia ayuda a mantener el estilo visual
- Gemini 2.5 Flash Image produce resultados más similares al chat web

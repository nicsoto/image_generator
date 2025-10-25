# Generador de Imágenes para Cuentos Educativos Infantiles 🎨📚

Sistema para crear ilustraciones personalizadas y consistentes para cuentos infantiles usando Google Gemini API.

## 🎯 Objetivo

Generar imágenes para cuentos educativos infantiles manteniendo **consistencia visual** de los personajes a lo largo de toda la historia.

## 📁 Archivos del Proyecto

- **`generar_imagen_con_gemini.py`** - Generador principal (único archivo necesario)
- **`README.md`** - Esta documentación
- **`.gitignore`** - Configuración de Git

## 🚀 Cómo Usar

### Instalación

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate  # Windows

# Instalar dependencias
pip install google-generativeai google-genai Pillow
```

### Ejecución

```bash
.venv/bin/python generar_imagen_con_gemini.py
```

## 💡 Flujo de Trabajo Recomendado

### Para un CUENTO NUEVO:

1. **Primera escena (crear personaje nuevo):**
   - Selecciona opción `2` (sin referencia)
   - Describe detalladamente tu personaje y escena
   - Ejemplo: "Una niña de 7 años llamada Ana con trenzas rojas, vestido amarillo con flores, explorando un bosque mágico"
   - Guarda esta imagen (será tu referencia)

2. **Resto de escenas del MISMO cuento:**
   - Selecciona opción `1` (con referencia)
   - Usa la primera imagen como referencia
   - Describe solo las nuevas escenas
   - El personaje se mantendrá consistente

3. **NUEVO cuento:**
   - Vuelve al paso 1
   - Crea nuevos personajes desde cero

## � Ejemplos Prácticos

### Ejemplo 1: Cuento sobre lavarse las manos

**Escena 1 (sin referencia):**
```
Opción: 2
Descripción: Un niño de 6 años llamado Pedro con pelo negro corto, 
camiseta azul y pantalón verde, con las manos sucias de tierra, 
en un baño colorido y limpio
Archivo: pedro_manos_sucias.png
```

**Escena 2 (con referencia de pedro_manos_sucias.png):**
```
Opción: 1
Referencia: pedro_manos_sucias.png
Descripción: El mismo niño lavándose las manos con jabón, 
burbujas de colores, sonriendo
Archivo: pedro_lavando_manos.png
```

**Escena 3 (con referencia):**
```
Opción: 1
Referencia: pedro_manos_sucias.png
Descripción: El mismo niño mostrando sus manos limpias, 
muy feliz, con brillos alrededor
Archivo: pedro_manos_limpias.png
```

### Ejemplo 2: Cuento sobre no tocar enchufes

**Primera escena:**
```
Opción: 2
Descripción: Una niña curiosa de 5 años llamada Sofía con pelo rizado 
castaño, vestido rosa, acercándose a un enchufe en la pared
Archivo: sofia_enchufe_peligro.png
```

**Segunda escena:**
```
Opción: 1
Referencia: sofia_enchufe_peligro.png
Descripción: La misma niña alejándose del enchufe, su mamá 
explicándole con cariño el peligro
Archivo: sofia_aprende.png
```

## 🔑 Configuración API

La API Key está incluida en el código. Para cambiarla, edita la variable `API_KEY` en `generar_imagen_con_gemini.py`.

## 🌟 Tips para Mejores Resultados

1. **Sé específico:** Describe edad, colores de ropa, peinado, accesorios
2. **Mantén coherencia:** Usa la misma imagen de referencia para todo un cuento
3. **Detalles del escenario:** Describe el ambiente, colores, iluminación
4. **Emociones:** Menciona la expresión del personaje (feliz, triste, curioso)

## 📦 Dependencias

- `google-generativeai` - Cliente de Gemini
- `google-genai` - API adicional de Google
- `Pillow` - Procesamiento de imágenes

## 📝 Próximos Pasos

- ✅ Generador flexible de imágenes con/sin referencia
- ✅ Personalización completa de personajes
- ⏳ Sistema de generación de cuentos completos (texto + imágenes)
- ⏳ Integración de audio/voz narrativa
- ⏳ Exportación a video o PDF

## 🎯 Casos de Uso

Este generador es ideal para:

1. **Cuentos Educativos:** Enseñar hábitos, seguridad, valores
2. **Historias Personalizadas:** Crear cuentos con el nombre y características del niño
3. **Material Didáctico:** Ilustraciones para explicar conceptos
4. **Series de Personajes:** Mantener consistencia visual en múltiples escenas

## 📦 Dependencias

```bash
pip install google-generativeai google-genai Pillow
```

## 🌟 Mejores Prácticas

### Para Mejores Resultados:

1. **Sé específico en las descripciones:**
   - ✅ "Niña de 5 años con coletas negras, vestido amarillo con flores, zapatos rojos"
   - ❌ "Una niña bonita"

2. **Incluye detalles del escenario:**
   - ✅ "En un jardín soleado con mariposas azules y flores de colores"
   - ❌ "Afuera"

3. **Especifica el mood/tono:**
   - ✅ "Ambiente alegre y acogedor, colores cálidos"
   - ❌ Solo describir objetos

4. **Para consistencia de personajes:**
   - Usa modo con referencia (opción 1)
   - Guarda la primera imagen generada como referencia
   - Úsala para todas las escenas del mismo cuento

### Tips Técnicos:

- Los prompts pueden estar en español o inglés
- Imagen de referencia ayuda enormemente con la consistencia
- Gemini 2.5 Flash Image da mejores resultados que Imagen 4 para este uso
- Las imágenes generadas incluyen marca de agua SynthID de Google

## 🤝 Contribuciones

Este es un proyecto abierto. Siéntete libre de:
- Reportar bugs
- Sugerir mejoras
- Agregar nuevas funcionalidades
- Compartir ejemplos de cuentos creados

# Generador de Imágenes para Cuentos Educativos Infantiles 🎨📚

Sistema para crear ilustraciones personalizadas para cuentos infantiles usando Google Gemini API.

## 🎯 Características

- **Generación flexible:** Crea cualquier personaje o escena que necesites
- **Modo con referencia:** Mantiene consistencia visual usando una imagen de ejemplo
- **Modo libre:** Genera escenas basándose solo en tu descripción
- **Interactivo:** Simple interfaz de línea de comandos

## 📁 Estructura del Proyecto

### Scripts Principales

- **`generar_imagen_con_gemini.py`** ⭐ **RECOMENDADO**
  - Generador interactivo y flexible
  - Permite usar imagen de referencia opcional
  - Personaliza completamente los personajes y escenas
  - Usa `gemini-2.5-flash-image` (mismo que Gemini web)

- **`generar_imagen_con_imagen4.py`**
  - Generador usando Imagen 4 API directa
  - Solo descripción de texto (sin referencia)
  - Más opciones de configuración técnica

### Ejemplos Incluidos

- **`mateo.png`** - Ejemplo de imagen de referencia
- **`mateo_gemini_dragon.png`** - Ejemplo generado con referencia
- **`mateo_cueva.png`** - Otro ejemplo
- **`imagen_generada_1.png`** - Ejemplo con Imagen 4

## 🚀 Cómo Usar

### Ejecución Simple

```bash
.venv/bin/python generar_imagen_con_gemini.py
```

### Flujo de Uso

1. **Seleccionar modo:**
   - Opción 1: Con imagen de referencia (para mantener estilo/personaje consistente)
   - Opción 2: Sin referencia (descripción libre)

2. **Si elegiste opción 1:**
   - Proporciona la ruta a tu imagen de referencia
   - Ejemplo: `/home/usuario/mi_personaje.png`

3. **Describir la escena:**
   - Sé específico con personajes, colores, acciones, escenario
   - Ejemplo: "Una niña valiente de 7 años con trenzas rojas explorando un bosque mágico lleno de hongos luminosos, llevando una mochila amarilla"

4. **Nombre del archivo:**
   - Ejemplo: `nina_bosque.png`

5. **¡Listo!** La imagen se guarda en la carpeta del proyecto

## 💡 Ejemplos de Uso

### Ejemplo 1: Crear personaje nuevo sin referencia

```
Opción: 2
Descripción: Un niño de 6 años llamado Lucas con pelo rubio rizado, 
             pecas, usando overol azul y botas rojas, jugando con 
             un perro golden retriever en un parque al atardecer
Archivo: lucas_parque.png
```

### Ejemplo 2: Mantener consistencia con referencia

```
Opción: 1
Imagen de referencia: ./sofia.png
Descripción: La misma niña nadando en el océano con tortugas marinas, 
             burbujas de colores, corales al fondo
Archivo: sofia_oceano.png
```

### Ejemplo 3: Escena educativa

```
Descripción: Un grupo de niños diversos (asiático, africano, latino) 
             lavándose las manos correctamente con jabón, gotas de agua 
             brillantes, ambiente de baño colorido y limpio
Archivo: cuento_higiene.png
```

## 🔑 API Key

Actualmente configurada en el código. Para cambiarla, edita la variable `API_KEY` en los scripts.

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

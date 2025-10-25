# 🎭 Sistema de Personajes Consistentes

## 🎯 Concepto

Este proyecto usa un **sistema de personajes fijos** que aparecen en **múltiples cuentos**. Los niños reconocerán a los mismos personajes en diferentes historias, creando familiaridad y conexión.

## 👥 Los 5 Personajes Principales

### ✅ Definidos:
1. **Lucas** - Niño de 7 años (camisa azul)
2. **Sofia** - Niña de 7 años (vestido rosa)
3. **Dr. Muelitas** - Dentista de 40 años (bata blanca)

### 🔜 Por definir:
4. Personaje 4 (puedes agregar: maestro/a, bombero, policía, etc.)
5. Personaje 5 (puedes agregar: familiar, otro niño, etc.)

## 📁 Estructura del Sistema

```
personajes/
├── README_PERSONAJES.md          # Documentación de personajes
│
├── lucas/
│   ├── lucas_referencia.png      # ← IMAGEN OFICIAL (se usa en TODOS los cuentos)
│   └── lucas_descripcion.txt     # ← Backup en texto
│
├── sofia/
│   ├── sofia_referencia.png      # ← IMAGEN OFICIAL
│   └── sofia_descripcion.txt     # ← Backup en texto
│
└── dr_muelitas/
    ├── dr_muelitas_referencia.png # ← IMAGEN OFICIAL
    └── dr_muelitas_descripcion.txt # ← Backup en texto
```

## 🔄 Cómo Funciona

### 1️⃣ Definir personajes (una sola vez)
- Crea la carpeta del personaje en `personajes/`
- Genera su imagen de referencia oficial
- Escribe su descripción en el archivo `.txt`

### 2️⃣ Crear un nuevo cuento
- Abre `generar_cuento_con_personajes.py`
- Define las escenas de tu cuento
- Especifica qué personajes aparecen en cada escena
- ¡El script usa automáticamente sus referencias!

### 3️⃣ Coherencia garantizada
- Los personajes se ven **IGUALES** en todos los cuentos
- Misma ropa, mismo pelo, misma cara
- Los niños los reconocen de inmediato

## 📝 Ejemplo: Crear un Nuevo Cuento

```python
# En generar_cuento_con_personajes.py

TITULO_CUENTO = "Sofia Aprende a Cruzar la Calle"

ESCENAS = [
    {
        "numero": 1,
        "personajes_en_escena": ["sofia", "lucas"],  # ← Especifica personajes
        "descripcion": "Sofia y Lucas frente a un cruce peatonal...",
        "archivo": "cruce_01.png"
    },
    {
        "numero": 2,
        "personajes_en_escena": ["sofia", "lucas"],
        "descripcion": "Lucas enseñando a Sofia a mirar a ambos lados...",
        "archivo": "cruce_02.png"
    }
    # ... más escenas
]
```

**Resultado**: Sofia y Lucas se verán **exactamente igual** que en el cuento anterior de los dientes.

## ✅ Ventajas de Este Sistema

### Para el Desarrollo:
- ✅ **No redefinir personajes** cada vez
- ✅ **Reutilización** de referencias visuales
- ✅ **Escalable** - fácil agregar más personajes
- ✅ **Mantenible** - cambiar un personaje = cambiar 1 imagen

### Para los Niños:
- ✅ **Reconocimiento** - "¡Es Lucas otra vez!"
- ✅ **Familiaridad** - personajes conocidos = más confianza
- ✅ **Conexión** - desarrollan apego a los personajes
- ✅ **Consistencia** - mismo aspecto = menos confusión

### Para el Contenido:
- ✅ **Coherencia visual** total entre cuentos
- ✅ **Identidad de marca** - tus personajes únicos
- ✅ **Series de cuentos** con los mismos protagonistas
- ✅ **Universo compartido** - todos los cuentos conectados

## 🚀 Workflow Completo

### Primer Cuento (establecer personajes):
```bash
# 1. Generar primer cuento
python generar_cuento_con_personajes.py

# 2. Las imágenes se guardan en personajes/*/
# 3. ¡Referencias establecidas!
```

### Cuentos Siguientes (usar personajes existentes):
```bash
# 1. Editar SOLO la sección ESCENAS en el script
# 2. Ejecutar
python generar_cuento_con_personajes.py

# 3. ¡Personajes se ven idénticos automáticamente!
```

## 🎨 Agregar un Nuevo Personaje

### Paso 1: Crear estructura
```bash
mkdir -p personajes/nuevo_personaje
```

### Paso 2: Descripción en texto
Crea `personajes/nuevo_personaje/descripcion.txt`:
```
NOMBRE - Tipo de Personaje

EDAD: X años

CARACTERÍSTICAS FÍSICAS:
- Cabello: ...
- Ojos: ...
- Ropa: ...

PERSONALIDAD:
...
```

### Paso 3: Generar imagen de referencia
Usa `generar_imagen_con_gemini.py` o genera en el primer cuento donde aparezca.

### Paso 4: Agregar al diccionario
En `generar_cuento_con_personajes.py`:
```python
PERSONAJES = {
    # ... personajes existentes ...
    
    "nuevo_personaje": {
        "nombre": "Nombre del Personaje",
        "descripcion": "descripción breve",
        "referencia": "personajes/nuevo_personaje/referencia.png",
        "descripcion_file": "personajes/nuevo_personaje/descripcion.txt"
    }
}
```

### Paso 5: ¡Listo!
Ahora puedes usar `"nuevo_personaje"` en `personajes_en_escena`.

## 📊 Casos de Uso

### 1. Serie de Cuentos de Seguridad
- **Cuento 1**: Lucas y los enchufes
- **Cuento 2**: Sofia cruza la calle
- **Cuento 3**: Dr. Muelitas y la comida saludable
- **Resultado**: Los niños ven a los **mismos personajes** en diferentes situaciones

### 2. Personajes Temáticos
- **Lucas**: Niño responsable (ejemplo a seguir)
- **Sofia**: Niña curiosa (hace las preguntas que los niños harían)
- **Dr. Muelitas**: Figura de autoridad amigable (enseña)
- **Personaje 4**: Podría ser un adulto más (bombero, policía)
- **Personaje 5**: Podría ser hermano/a menor o mascota

### 3. Múltiples Idiomas
- Genera el cuento en español
- Las **imágenes son las mismas**
- Solo cambias el audio
- Los niños reconocen a los personajes en cualquier idioma

## ⚠️ Reglas Importantes

### ❌ NUNCA hagas esto:
1. Modificar las imágenes de referencia una vez establecidas
2. Cambiar la descripción física de un personaje
3. Usar diferentes estilos de ilustración

### ✅ SIEMPRE haz esto:
1. Usar las referencias en `generar_cuento_con_personajes.py`
2. Mantener coherencia de ropa/colores
3. Especificar personajes en cada escena
4. Guardar backups de las referencias

## 🔧 Solución de Problemas

### "El personaje se ve diferente"
- Verifica que la referencia existe: `ls personajes/lucas/lucas_referencia.png`
- Asegúrate de usar `generar_cuento_con_personajes.py` (no el script viejo)
- Revisa que el ID del personaje coincida en `PERSONAJES` y `personajes_en_escena`

### "Quiero cambiar la ropa de un personaje"
- Si el personaje ya aparece en cuentos publicados: **NO** lo cambies
- Si es nuevo: Genera nueva referencia y reemplaza
- Considera: ¿Los niños lo reconocerán con ropa diferente?

### "Necesito más de 5 personajes"
- ¡Adelante! No hay límite
- Agrega carpetas en `personajes/`
- Actualiza el diccionario `PERSONAJES`
- Los 5 son solo los principales, puedes tener secundarios

## 📈 Próximos Pasos

1. **Definir personajes 4 y 5** - ¿Qué roles faltan? ¿Maestro? ¿Familiar?
2. **Generar más cuentos** - Usa los 3 personajes existentes
3. **Crear biblioteca** - Organiza cuentos por tema
4. **Exportar a video** - Combina imágenes + audio
5. **Múltiples idiomas** - Mismas imágenes, diferentes audios

---

**🎯 Resumen**: Un sistema donde los personajes son **actores** que aparecen en **diferentes historias**, creando un universo cohesivo y familiar para los niños.

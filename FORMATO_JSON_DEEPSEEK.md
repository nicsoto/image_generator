## 📋 Formato JSON para DeepSeek

Este documento especifica cómo DeepSeek debe formatear el JSON del cuento para que sea procesado correctamente.

## ✅ Formato Obligatorio

```json
{
  "metadata": {
    "titulo": "Título del Cuento",
    "leccion": "Lección que enseña el cuento"
  },
  "escenas": [
    {
      "numero_escena": 1,
      "imagen_descripcion": "Descripción visual de la escena para generar la imagen",
      "dialogo": {
        "personaje": "Nombre del Personaje",
        "texto": "Lo que dice el personaje",
        "emocion": "alegre/triste/curioso/etc"
      }
    }
  ]
}
```

## 🎭 Personajes Disponibles (IMPORTANTE)

DeepSeek **DEBE usar SOLO estos personajes**:

- **Lucas** - Niño de 7 años
- **Sofia** - Niña de 7 años  
- **Dr. Muelitas** - Dentista adulto

### ⚠️ Nombres EXACTOS

Los nombres en `dialogo.personaje` deben ser **exactamente**:
- ✅ `"Lucas"` 
- ✅ `"Sofia"`
- ✅ `"Dr. Muelitas"`

❌ NO usar variaciones como:
- "El niño Lucas"
- "La doctora"
- "Sofía" (con tilde)

## 📝 Campos Explicados

### metadata (requerido)
```json
"metadata": {
  "titulo": "Nombre descriptivo del cuento",
  "leccion": "La lección moral/educativa que enseña"
}
```

### escenas (requerido, array)

Cada escena debe tener:

#### numero_escena (requerido)
```json
"numero_escena": 1
```
- Número secuencial empezando en 1
- Tipo: número entero

#### imagen_descripcion (requerido)
```json
"imagen_descripcion": "Lucas y Sofia jugando en el parque, Lucas en el columpio sonriendo mostrando sus dientes blancos, Sofia mirándolo curiosa. Día soleado con árboles verdes al fondo."
```
- Descripción DETALLADA de la escena visual
- Incluir: ubicación, acciones, expresiones faciales, ambiente
- NO incluir texto que deba aparecer en la imagen
- Tipo: string largo y descriptivo

**Ejemplos buenos**:
- ✅ "Lucas y Sofia caminando por la acera, Lucas señalando el semáforo en rojo, ambos detenidos. Calle urbana con edificios al fondo."
- ✅ "Dr. Muelitas en su consultorio dental, sosteniendo un cepillo de dientes gigante, Lucas y Sofia sentados frente a él escuchando atentos. Consultorio colorido con posters de dientes."

**Ejemplos malos**:
- ❌ "Los niños en el parque" (muy vago)
- ❌ "Lucas dice algo importante" (no es visual)

#### dialogo (requerido)
```json
"dialogo": {
  "personaje": "Sofia",
  "texto": "¿Por qué debemos mirar a ambos lados antes de cruzar?",
  "emocion": "curiosa"
}
```

- **personaje**: Uno de los 3 nombres exactos (Lucas/Sofia/Dr. Muelitas)
- **texto**: Lo que dice el personaje (para el audio)
- **emocion**: Emoción/tono (alegre, triste, curioso, educativo, etc.)

### sonido_fondo (opcional)
```json
"sonido_fondo": "sonidos de parque, niños jugando, pájaros"
```
- Descripción de sonidos ambientales
- Opcional, para el equipo de audio

## 📊 Ejemplo Completo

```json
{
  "metadata": {
    "titulo": "Sofia Aprende a Cruzar la Calle",
    "leccion": "Importancia de mirar a ambos lados antes de cruzar"
  },
  "escenas": [
    {
      "numero_escena": 1,
      "sonido_fondo": "sonidos de ciudad, autos pasando",
      "imagen_descripcion": "Sofia y Lucas parados frente a un cruce peatonal con semáforo en rojo. Sofia señalando al otro lado de la calle con expresión ansiosa. Lucas sosteniéndola del brazo con gesto de precaución. Calle urbana con autos a lo lejos.",
      "dialogo": {
        "personaje": "Sofia",
        "texto": "¡Lucas, quiero cruzar ya! ¡Veo la tienda de dulces al otro lado!",
        "emocion": "ansiosa"
      }
    },
    {
      "numero_escena": 2,
      "sonido_fondo": "sonidos de ciudad, semáforo cambiando",
      "imagen_descripcion": "Lucas mirando a ambos lados de la calle con expresión seria, Sofia observándolo. Semáforo aún en rojo. Perspectiva de la calle vacía.",
      "dialogo": {
        "personaje": "Lucas",
        "texto": "¡Espera, Sofia! Primero debemos mirar a ambos lados y esperar el semáforo verde",
        "emocion": "educativo"
      }
    },
    {
      "numero_escena": 3,
      "sonido_fondo": "sonido de semáforo cambiando, autos deteniéndose",
      "imagen_descripcion": "Sofia mirando cuidadosamente a la izquierda y derecha, Lucas a su lado asintiendo con aprobación. Semáforo ahora en verde para peatones. La calle sin autos.",
      "dialogo": {
        "personaje": "Sofia",
        "texto": "¡Ahora entiendo! Miro a la izquierda, a la derecha, y espero la luz verde",
        "emocion": "comprensiva"
      }
    },
    {
      "numero_escena": 4,
      "sonido_fondo": "pasos en la calle, música alegre suave",
      "imagen_descripcion": "Lucas y Sofia cruzando la calle tomados de la mano, ambos sonriendo. Semáforo verde para peatones visible. Al fondo la tienda de dulces.",
      "dialogo": {
        "personaje": "Lucas",
        "texto": "¡Muy bien, Sofia! Ahora ya sabes cruzar la calle de forma segura",
        "emocion": "orgulloso"
      }
    }
  ]
}
```

## ✅ Checklist para DeepSeek

Antes de enviar el JSON, verificar:

- [ ] El JSON es válido (sin comas extra, comillas correctas)
- [ ] Tiene campos `metadata` y `escenas`
- [ ] Cada escena tiene `numero_escena`, `imagen_descripcion` y `dialogo`
- [ ] Los nombres de personajes son exactos: Lucas/Sofia/Dr. Muelitas
- [ ] Las descripciones de imagen son DETALLADAS (no vagas)
- [ ] El número de escenas es entre 4 y 8 (ideal para cuentos cortos)
- [ ] La lección educativa está clara en el cuento

## 🎯 Consejos para DeepSeek

### Descripciones de Imagen

**Incluir siempre**:
1. Qué personajes están presentes
2. Qué están haciendo (acciones específicas)
3. Expresiones faciales
4. Ubicación/escenario
5. Elementos importantes del fondo

**Evitar**:
- Descripciones genéricas ("Los niños están felices")
- Referencias al diálogo ("Lucas dice lo que piensa")
- Texto que debe aparecer en la imagen

### Número de Escenas

- **Mínimo**: 4 escenas (muy corto pero funcional)
- **Ideal**: 6-8 escenas (buen balance)
- **Máximo**: 10 escenas (puede ser largo)

### Estructura del Cuento

Seguir estructura clásica:
1. **Planteamiento** (1-2 escenas): Presentar situación/problema
2. **Desarrollo** (3-5 escenas): Mostrar la lección
3. **Desenlace** (1-2 escenas): Resolver y reforzar la lección

## 🔧 Validación del JSON

El JSON será validado automáticamente. Si hay errores, la API devolverá:

```json
{
  "exito": false,
  "error": "Descripción del error"
}
```

Errores comunes:
- JSON inválido (sintaxis)
- Falta campo requerido
- Nombre de personaje no reconocido
- Array de escenas vacío

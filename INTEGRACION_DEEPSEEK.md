# 🔄 Integración DeepSeek → API → Imágenes

## 📊 Flujo Completo del Sistema

```
┌─────────────┐      ┌──────────┐      ┌────────────┐      ┌──────────┐
│   Página    │─────▶│ DeepSeek │─────▶│  API REST  │─────▶│ Imágenes │
│     Web     │      │   (LLM)  │      │  (Python)  │      │   PNG    │
└─────────────┘      └──────────┘      └────────────┘      └──────────┘
     ▲                                                             │
     │                                                             │
     └─────────────────────────────────────────────────────────────┘
                         (Devuelve URLs de imágenes)
```

## 🎯 Pasos del Proceso

### 1️⃣ Usuario en la Página Web
```
Usuario escribe: "Quiero una historia sobre la importancia de la amistad"
```

### 2️⃣ Página Web → DeepSeek
```javascript
// Tu página envía esto a DeepSeek
{
  "solicitud": "historia sobre la importancia de la amistad",
  "personajes_disponibles": ["Lucas", "Sofia", "Dr. Muelitas"],
  "num_escenas": 6
}
```

### 3️⃣ DeepSeek Genera el Cuento (JSON)
DeepSeek crea un JSON estructurado:
```json
{
  "metadata": {
    "titulo": "Lucas y Sofia: Mejores Amigos",
    "leccion": "La amistad nos ayuda en momentos difíciles"
  },
  "escenas": [
    {
      "numero_escena": 1,
      "imagen_descripcion": "Lucas solo en el parque...",
      "dialogo": {
        "personaje": "Lucas",
        "texto": "...",
        "emocion": "triste"
      }
    }
    // ... más escenas
  ]
}
```

### 4️⃣ Página Web → API Python (este proyecto)
```javascript
// Tu página envía el JSON de DeepSeek a tu API
fetch('http://tu-servidor:5000/generar-cuento', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify(cuentoDesdeDeepSeek)
})
```

### 5️⃣ API Python Genera las Imágenes
- Lee el JSON
- Identifica personajes
- Carga sus referencias visuales
- Genera cada imagen con Gemini
- Guarda las imágenes

### 6️⃣ API Devuelve las URLs
```json
{
  "exito": true,
  "titulo": "Lucas y Sofia: Mejores Amigos",
  "total_escenas": 6,
  "escenas_exitosas": 6,
  "imagenes": [
    {
      "numero_escena": 1,
      "url": "/imagenes/20251025_143022_Lucas_y_Sofia/escena_01.png",
      "exito": true
    },
    // ... más imágenes
  ]
}
```

### 7️⃣ Página Web Muestra las Imágenes
```javascript
// Tu página muestra las imágenes al usuario
resultado.imagenes.forEach(img => {
  document.getElementById('cuento').innerHTML += 
    `<img src="${img.url}" alt="Escena ${img.numero_escena}">`;
});
```

## 🛠️ Componentes del Sistema

### A. Scripts de Generación (Local/Desarrollo)
- `generar_imagen_con_gemini.py` - Generador manual interactivo
- `generar_cuento_con_personajes.py` - Generador con referencias
- `api_generar_cuento.py` - Procesador de JSON (sin web)

### B. API REST (Producción/Web)
- `api_rest_cuento.py` - **Servidor web que recibe el JSON**

### C. Sistema de Personajes
- `personajes/` - Carpeta con referencias visuales
- 3 personajes definidos (Lucas, Sofia, Dr. Muelitas)

## 🚀 Cómo Poner en Marcha

### Opción 1: Desarrollo Local (sin web)

```bash
# Editar el JSON en api_generar_cuento.py
python api_generar_cuento.py
```

### Opción 2: API REST (con conexión web)

```bash
# Instalar dependencias
pip install flask flask-cors

# Iniciar servidor
python api_rest_cuento.py

# El servidor corre en http://localhost:5000
```

#### Probar la API con curl:

```bash
curl -X POST http://localhost:5000/generar-cuento \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {"titulo": "Test", "leccion": "Test"},
    "escenas": [
      {
        "numero_escena": 1,
        "imagen_descripcion": "Lucas sonriendo en el parque",
        "dialogo": {"personaje": "Lucas", "texto": "Hola", "emocion": "alegre"}
      }
    ]
  }'
```

## 📋 Formato que DeepSeek Debe Enviar

Ver documento completo: **[FORMATO_JSON_DEEPSEEK.md](FORMATO_JSON_DEEPSEEK.md)**

### Resumen rápido:

```json
{
  "metadata": {
    "titulo": "Título",
    "leccion": "Lección"
  },
  "escenas": [
    {
      "numero_escena": 1,
      "imagen_descripcion": "Descripción DETALLADA de la imagen",
      "dialogo": {
        "personaje": "Lucas",  // Solo: Lucas, Sofia, Dr. Muelitas
        "texto": "Diálogo del personaje",
        "emocion": "alegre"
      }
    }
  ]
}
```

## ⚙️ Configuración de la API

### Variables importantes en `api_rest_cuento.py`:

```python
# Puerto del servidor
app.run(port=5000)  # Cambiar si necesitas otro puerto

# Carpeta de imágenes
IMAGENES_DIR = "cuentos_generados"  # Donde se guardan las imágenes

# API Key de Gemini
API_KEY = "AIzaSyD..."  # Ya está configurada
```

### CORS (Cross-Origin)

La API ya tiene CORS habilitado para permitir requests desde tu página web:

```python
CORS(app)  # Permite requests desde cualquier dominio
```

Si quieres restringir a tu dominio específico:
```python
CORS(app, origins=["https://tu-pagina.com"])
```

## 🔌 Endpoints de la API

### POST `/generar-cuento`
Genera imágenes del cuento

**Request**:
```json
{
  "metadata": {...},
  "escenas": [...]
}
```

**Response**:
```json
{
  "exito": true,
  "titulo": "...",
  "total_escenas": 6,
  "escenas_exitosas": 6,
  "imagenes": [...]
}
```

### GET `/imagenes/<path>`
Obtiene una imagen generada

**Ejemplo**: `/imagenes/20251025_143022_Cuento/escena_01.png`

### GET `/personajes`
Lista personajes disponibles

**Response**:
```json
{
  "personajes": {
    "lucas": {"nombre": "Lucas", "descripcion": "..."},
    "sofia": {"nombre": "Sofia", "descripcion": "..."},
    "dr_muelitas": {"nombre": "Dr. Muelitas", "descripcion": "..."}
  }
}
```

### GET `/health`
Verifica que la API esté funcionando

**Response**:
```json
{
  "status": "OK",
  "mensaje": "API de cuentos funcionando"
}
```

## 🌐 Conectar desde tu Página Web

### Ejemplo con JavaScript (Fetch):

```javascript
async function generarCuento(solicitudUsuario) {
  // 1. Enviar solicitud a DeepSeek
  const cuentoJSON = await fetch('https://api-deepseek.com/generar', {
    method: 'POST',
    body: JSON.stringify({
      solicitud: solicitudUsuario,
      personajes: ["Lucas", "Sofia", "Dr. Muelitas"]
    })
  }).then(r => r.json());
  
  // 2. Enviar JSON de DeepSeek a tu API de imágenes
  const resultado = await fetch('http://tu-servidor:5000/generar-cuento', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(cuentoJSON)
  }).then(r => r.json());
  
  // 3. Mostrar imágenes
  if (resultado.exito) {
    resultado.imagenes.forEach(img => {
      const imgElement = document.createElement('img');
      imgElement.src = `http://tu-servidor:5000${img.url}`;
      document.getElementById('cuento').appendChild(imgElement);
    });
  }
}

// Usar
generarCuento("historia sobre la importancia de lavarse las manos");
```

### Ejemplo con Python (requests):

```python
import requests

# 1. JSON desde DeepSeek
cuento_json = {
    "metadata": {...},
    "escenas": [...]
}

# 2. Enviar a tu API
response = requests.post(
    'http://localhost:5000/generar-cuento',
    json=cuento_json
)

# 3. Obtener resultado
resultado = response.json()
print(f"Se generaron {resultado['escenas_exitosas']} imágenes")
```

## 📂 Estructura de Archivos Generados

```
cuentos_generados/
└── 20251025_143022_Lucas_y_Sofia_Mejores_Amigos/
    ├── escena_01.png
    ├── escena_02.png
    ├── escena_03.png
    ├── escena_04.png
    ├── escena_05.png
    └── escena_06.png
```

Cada cuento se guarda en su propia carpeta con timestamp.

## 🔧 Solución de Problemas

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask flask-cors
```

### "CORS error" en el navegador
- Verifica que `CORS(app)` esté en `api_rest_cuento.py`
- O configura tu navegador para desarrollo

### "Personaje no reconocido"
- DeepSeek debe usar EXACTAMENTE: "Lucas", "Sofia", "Dr. Muelitas"
- Mayúsculas y minúsculas importan
- Sin tildes ni variaciones

### Imágenes no se generan
- Verifica que existan las referencias en `personajes/*/referencia.png`
- Revisa que la API key de Gemini sea válida
- Mira los logs del servidor para errores específicos

## 📊 Monitoreo

El servidor imprime logs en tiempo real:

```
📖 Generando: Lucas y Sofia: Mejores Amigos
🎬 Escenas: 6
👥 Personajes: ['lucas', 'sofia']
   Generando escena 1...
   ✅ Escena 1 guardada
   Generando escena 2...
   ✅ Escena 2 guardada
   ...
✅ Cuento 'Lucas y Sofia: Mejores Amigos' completado
```

## 🚀 Próximos Pasos

1. **Conectar DeepSeek** - Integrar la generación de texto
2. **Audio** - Sistema de síntesis de voz (ya tienes los diálogos en el JSON)
3. **Video** - Combinar imágenes + audio en video
4. **Deploy** - Subir a servidor (Heroku, DigitalOcean, AWS, etc.)

## 📝 Notas Importantes

- ✅ Las imágenes **NO tienen texto** (el diálogo es audio)
- ✅ Los personajes son **consistentes** (usan referencias)
- ✅ El sistema es **escalable** (fácil agregar personajes)
- ✅ El JSON es **el estándar** (fácil de integrar con cualquier sistema)

---

**Sistema listo para recibir cuentos desde DeepSeek y generar imágenes automáticamente** 🎨✨

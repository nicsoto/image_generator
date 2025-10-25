"""
EJEMPLO: Cómo usar el generador de imágenes en tu proyecto
===========================================================

Este archivo muestra cómo integrar el generador de imágenes
con el resto de tu proyecto (página web, audio, etc.)
"""

# ============================================================================
# CASO 1: Desde tu backend principal
# ============================================================================

from generar_imagenes_cuento import generar_imagenes_cuento

def procesar_solicitud_usuario(solicitud):
    """
    Función principal que conecta todo:
    Usuario → DeepSeek → Imágenes → Audio → Video
    """
    
    print("1️⃣ Usuario pidió:", solicitud)
    
    # 2. DeepSeek genera el JSON del cuento
    # (aquí pondrías tu llamada real a DeepSeek)
    cuento_json = llamar_deepseek(solicitud)  # ← Tu función
    
    # 3. Generar las imágenes
    resultado_imagenes = generar_imagenes_cuento(cuento_json)
    
    if not resultado_imagenes['exito']:
        print("❌ Error generando imágenes")
        return None
    
    print(f"✅ Generadas {resultado_imagenes['escenas_exitosas']} imágenes")
    
    # 4. Generar audios (tu código de audio)
    audios = generar_audios(cuento_json)  # ← Tu función
    
    # 5. Combinar en video (tu código de video)
    video_final = combinar_imagenes_y_audio(
        resultado_imagenes['imagenes'],
        audios
    )
    
    return video_final

# ============================================================================
# CASO 2: Llamada directa con JSON
# ============================================================================

def ejemplo_directo():
    """Uso más simple: ya tienes el JSON"""
    
    # Tu JSON (puede venir de DeepSeek, archivo, base de datos, etc.)
    cuento = {
        "metadata": {
            "titulo": "La Amistad de Lucas y Sofia",
            "leccion": "Importancia de ayudar a los amigos"
        },
        "escenas": [
            {
                "numero_escena": 1,
                "imagen_descripcion": "Lucas y Sofia jugando en el parque...",
                "dialogo": {
                    "personaje": "Lucas",
                    "texto": "Sofia, ¿quieres jugar conmigo?",
                    "emocion": "alegre"
                }
            },
            {
                "numero_escena": 2,
                "imagen_descripcion": "Sofia tropezando, Lucas ayudándola...",
                "dialogo": {
                    "personaje": "Sofia",
                    "texto": "¡Ay! Me caí",
                    "emocion": "triste"
                }
            }
        ]
    }
    
    # Generar imágenes
    resultado = generar_imagenes_cuento(cuento, carpeta_salida="mi_cuento")
    
    # Usar las imágenes
    for img in resultado['imagenes']:
        if img['exito']:
            print(f"Imagen lista: {img['archivo']}")
            # Aquí haces lo que necesites con la imagen

# ============================================================================
# CASO 3: En tu servidor web (Flask, FastAPI, etc.)
# ============================================================================

# Si usas Flask:
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/crear-cuento', methods=['POST'])
def crear_cuento():
    """Endpoint que recibe la solicitud del usuario"""
    
    data = request.get_json()
    solicitud = data.get('solicitud')  # "cuento sobre amistad"
    
    # 1. DeepSeek genera el JSON
    cuento_json = llamar_deepseek(solicitud)
    
    # 2. Generar imágenes
    resultado = generar_imagenes_cuento(cuento_json)
    
    # 3. Devolver info al frontend
    return jsonify({
        "titulo": resultado['titulo'],
        "imagenes": [img['archivo'] for img in resultado['imagenes'] if img['exito']],
        "total": resultado['escenas_exitosas']
    })

# ============================================================================
# CASO 4: Script standalone (generar de un archivo JSON)
# ============================================================================

import json

def generar_desde_archivo(archivo_json):
    """Lee un JSON y genera las imágenes"""
    
    with open(archivo_json, 'r', encoding='utf-8') as f:
        cuento = json.load(f)
    
    resultado = generar_imagenes_cuento(cuento)
    
    print(f"\n✅ Cuento generado:")
    print(f"   Título: {resultado['titulo']}")
    print(f"   Imágenes: {resultado['escenas_exitosas']}")
    print(f"   Carpeta: {resultado['carpeta']}")

# ============================================================================
# FUNCIONES AUXILIARES (ejemplos - tú tendrías las reales)
# ============================================================================

def llamar_deepseek(solicitud):
    """
    Aquí iría tu llamada real a DeepSeek
    Por ahora retorna un JSON de ejemplo
    """
    # Ejemplo de lo que DeepSeek devolvería
    return {
        "metadata": {
            "titulo": f"Cuento sobre {solicitud}",
            "leccion": "Lección educativa"
        },
        "escenas": [
            {
                "numero_escena": 1,
                "imagen_descripcion": "...",
                "dialogo": {"personaje": "Lucas", "texto": "...", "emocion": "alegre"}
            }
        ]
    }

def generar_audios(cuento_json):
    """Tu función de generación de audio"""
    pass

def combinar_imagenes_y_audio(imagenes, audios):
    """Tu función de combinación"""
    pass

# ============================================================================
# EJECUTAR EJEMPLO
# ============================================================================

if __name__ == "__main__":
    print("Ejemplo de uso del generador de imágenes\n")
    ejemplo_directo()

"""
API REST para Recibir Cuentos y Generar Imágenes
=================================================

Esta es la API web que recibirá el JSON desde tu página.

INSTALACIÓN:
pip install flask flask-cors

EJECUCIÓN:
python api_rest_cuento.py

ENDPOINT:
POST http://localhost:5000/generar-cuento

EJEMPLO DE REQUEST (desde tu página web):
{
    "metadata": {
        "titulo": "El Secreto de los Dientes Felices",
        "leccion": "Importancia de cepillarse los dientes"
    },
    "escenas": [
        {
            "numero_escena": 1,
            "imagen_descripcion": "Lucas en el columpio...",
            "dialogo": {
                "personaje": "Sofia",
                "texto": "...",
                "emocion": "curiosa"
            }
        }
    ]
}

RESPONSE:
{
    "exito": true,
    "titulo": "El Secreto de los Dientes Felices",
    "total_escenas": 8,
    "escenas_exitosas": 8,
    "imagenes": [
        {"numero_escena": 1, "url": "/imagenes/escena_01.png", "exito": true},
        ...
    ]
}
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from google import genai
from PIL import Image
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir requests desde tu página web

# Configurar API de Gemini
API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
client = genai.Client(api_key=API_KEY)

# Carpeta para guardar imágenes generadas
IMAGENES_DIR = "cuentos_generados"
os.makedirs(IMAGENES_DIR, exist_ok=True)

# Personajes disponibles
PERSONAJES = {
    "lucas": {
        "nombre": "Lucas",
        "descripcion": "niño de 7 años, cabello castaño corto, camisa azul celeste, sonrisa brillante",
        "referencia": "personajes/lucas/lucas_referencia.png"
    },
    "sofia": {
        "nombre": "Sofia",
        "descripcion": "niña de 7 años, cabello rizado castaño oscuro, vestido rosa intenso, expresión curiosa",
        "referencia": "personajes/sofia/sofia_referencia.png"
    },
    "dr_muelitas": {
        "nombre": "Dr. Muelitas",
        "descripcion": "dentista de 40 años, bata blanca, bigote, gafas redondas, sonrisa amplia",
        "referencia": "personajes/dr_muelitas/dr_muelitas_referencia.png"
    }
}

def mapear_nombre_a_id(nombre):
    """Convierte nombre de personaje a ID"""
    return nombre.lower().replace(" ", "_").replace(".", "")

def obtener_personajes_de_cuento(escenas):
    """Extrae qué personajes aparecen en el cuento"""
    personajes = set()
    for escena in escenas:
        nombre_personaje = escena.get("dialogo", {}).get("personaje", "")
        pid = mapear_nombre_a_id(nombre_personaje)
        if pid in PERSONAJES:
            personajes.add(pid)
    return list(personajes)

def generar_imagen(descripcion, personajes_ids):
    """Genera imagen usando referencias de personajes"""
    
    # Descripciones de personajes
    desc_personajes = "\n".join([
        f"- {PERSONAJES[p]['nombre']}: {PERSONAJES[p]['descripcion']}"
        for p in personajes_ids if p in PERSONAJES
    ])
    
    # Cargar referencias
    referencias = [
        Image.open(PERSONAJES[p]["referencia"])
        for p in personajes_ids
        if p in PERSONAJES and os.path.exists(PERSONAJES[p]["referencia"])
    ]
    
    # Prompt
    prompt = f"""PERSONAJES:
{desc_personajes}

ESCENA:
{descripcion}

INSTRUCCIONES:
- MANTÉN características EXACTAS de los personajes de las referencias
- NO incluir texto, diálogos ni viñetas
- Ilustración infantil colorida, amigable, educativa
- Colores brillantes
"""
    
    # Generar
    contenido = [prompt] + referencias
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=contenido
    )
    
    # Extraer imagen
    for part in response.parts:
        if hasattr(part, 'inline_data') and part.inline_data:
            return part.inline_data.data
    
    if hasattr(response, 'candidates') and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        return part.inline_data.data
    
    return None

@app.route('/generar-cuento', methods=['POST'])
def generar_cuento():
    """
    Endpoint principal que recibe el JSON de DeepSeek y genera las imágenes
    """
    try:
        # Recibir JSON
        cuento_json = request.get_json()
        
        if not cuento_json:
            return jsonify({"exito": False, "error": "No se recibió JSON"}), 400
        
        # Extraer datos
        metadata = cuento_json.get("metadata", {})
        titulo = metadata.get("titulo", "Cuento sin título")
        escenas = cuento_json.get("escenas", [])
        
        if not escenas:
            return jsonify({"exito": False, "error": "No hay escenas en el cuento"}), 400
        
        # Crear carpeta para este cuento
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        cuento_dir = os.path.join(IMAGENES_DIR, f"{timestamp}_{titulo.replace(' ', '_')}")
        os.makedirs(cuento_dir, exist_ok=True)
        
        # Identificar personajes
        personajes_cuento = obtener_personajes_de_cuento(escenas)
        
        print(f"📖 Generando: {titulo}")
        print(f"🎬 Escenas: {len(escenas)}")
        print(f"👥 Personajes: {personajes_cuento}")
        
        # Generar imágenes
        imagenes_resultado = []
        
        for escena in escenas:
            num = escena.get("numero_escena", 0)
            descripcion = escena.get("imagen_descripcion", "")
            
            print(f"   Generando escena {num}...")
            
            # Generar imagen
            imagen_data = generar_imagen(descripcion, personajes_cuento)
            
            if imagen_data:
                # Guardar
                filename = f"escena_{num:02d}.png"
                filepath = os.path.join(cuento_dir, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(imagen_data)
                
                imagenes_resultado.append({
                    "numero_escena": num,
                    "archivo": filename,
                    "url": f"/imagenes/{timestamp}_{titulo.replace(' ', '_')}/{filename}",
                    "exito": True
                })
                print(f"   ✅ Escena {num} guardada")
            else:
                imagenes_resultado.append({
                    "numero_escena": num,
                    "archivo": None,
                    "url": None,
                    "exito": False
                })
                print(f"   ❌ Error en escena {num}")
        
        # Respuesta
        resultado = {
            "exito": True,
            "titulo": titulo,
            "total_escenas": len(escenas),
            "escenas_exitosas": sum(1 for img in imagenes_resultado if img["exito"]),
            "imagenes": imagenes_resultado,
            "carpeta": cuento_dir
        }
        
        print(f"✅ Cuento '{titulo}' completado")
        
        return jsonify(resultado), 200
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"exito": False, "error": str(e)}), 500

@app.route('/imagenes/<path:filename>')
def servir_imagen(filename):
    """Sirve las imágenes generadas"""
    filepath = os.path.join(IMAGENES_DIR, filename)
    if os.path.exists(filepath):
        return send_file(filepath, mimetype='image/png')
    return jsonify({"error": "Imagen no encontrada"}), 404

@app.route('/personajes', methods=['GET'])
def listar_personajes():
    """Lista los personajes disponibles"""
    personajes_info = {
        pid: {
            "nombre": p["nombre"],
            "descripcion": p["descripcion"]
        }
        for pid, p in PERSONAJES.items()
    }
    return jsonify({"personajes": personajes_info}), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Verifica que la API esté funcionando"""
    return jsonify({"status": "OK", "mensaje": "API de cuentos funcionando"}), 200

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 API DE GENERACIÓN DE CUENTOS")
    print("=" * 70)
    print("\n📡 Endpoints disponibles:")
    print("  POST   /generar-cuento  - Genera imágenes del cuento")
    print("  GET    /imagenes/<path> - Obtiene una imagen generada")
    print("  GET    /personajes      - Lista personajes disponibles")
    print("  GET    /health          - Verifica estado de la API")
    print("\n🌐 Servidor corriendo en: http://localhost:5000")
    print("=" * 70)
    print()
    
    # Iniciar servidor
    app.run(host='0.0.0.0', port=5000, debug=True)

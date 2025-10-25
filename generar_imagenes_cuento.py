"""
Generador de Imágenes para Cuentos
===================================

Recibe un JSON del cuento (desde DeepSeek) y genera las imágenes.

USO SIMPLE:
    from generar_imagenes_cuento import generar_imagenes_cuento
    
    # Tu JSON desde DeepSeek
    cuento = {
        "metadata": {"titulo": "...", "leccion": "..."},
        "escenas": [...]
    }
    
    # Generar imágenes
    resultado = generar_imagenes_cuento(cuento)
    
    # Ver resultado
    print(f"Generadas: {resultado['escenas_exitosas']} imágenes")
    for img in resultado['imagenes']:
        print(f"  - {img['archivo']}")
"""

from google import genai
from PIL import Image
import os

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
client = genai.Client(api_key=API_KEY)

# Personajes disponibles (con sus referencias visuales)
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

# ============================================================================
# FUNCIONES INTERNAS
# ============================================================================

def _mapear_nombre_a_id(nombre):
    """Convierte nombre de personaje a ID"""
    return nombre.lower().replace(" ", "_").replace(".", "")

def _obtener_personajes_del_cuento(escenas):
    """Identifica qué personajes aparecen en el cuento"""
    personajes = set()
    for escena in escenas:
        nombre = escena.get("dialogo", {}).get("personaje", "")
        pid = _mapear_nombre_a_id(nombre)
        if pid in PERSONAJES:
            personajes.add(pid)
    return list(personajes)

def _generar_imagen(descripcion, personajes_ids):
    """Genera una imagen usando las referencias de personajes"""
    
    # Descripciones de personajes
    desc_personajes = "\n".join([
        f"- {PERSONAJES[p]['nombre']}: {PERSONAJES[p]['descripcion']}"
        for p in personajes_ids if p in PERSONAJES
    ])
    
    # Cargar imágenes de referencia
    referencias = []
    for pid in personajes_ids:
        if pid in PERSONAJES:
            ref_path = PERSONAJES[pid]["referencia"]
            if os.path.exists(ref_path):
                referencias.append(Image.open(ref_path))
    
    # Construir prompt
    prompt = f"""PERSONAJES:
{desc_personajes}

ESCENA:
{descripcion}

INSTRUCCIONES:
- MANTÉN las características EXACTAS de los personajes de las referencias
- NO incluir texto, diálogos ni viñetas en la imagen
- Estilo: ilustración infantil colorida, amigable, educativa
- Colores brillantes y alegres
"""
    
    # Generar imagen
    contenido = [prompt] + referencias
    
    try:
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
    except Exception as e:
        print(f"   ⚠️  Error: {str(e)}")
        return None
    
    return None

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def generar_imagenes_cuento(cuento_json, carpeta_salida="imagenes_cuento"):
    """
    Genera las imágenes de un cuento manteniendo coherencia visual.
    
    Args:
        cuento_json (dict): JSON con metadata y escenas del cuento
        carpeta_salida (str): Carpeta donde guardar las imágenes
        
    Returns:
        dict: Resultado con información de las imágenes generadas
    """
    
    print("=" * 70)
    print("🎨 GENERANDO IMÁGENES DEL CUENTO")
    print("=" * 70)
    
    # Extraer información
    metadata = cuento_json.get("metadata", {})
    titulo = metadata.get("titulo", "Cuento sin título")
    escenas = cuento_json.get("escenas", [])
    
    if not escenas:
        return {
            "exito": False,
            "error": "No hay escenas en el cuento",
            "titulo": titulo,
            "total_escenas": 0,
            "escenas_exitosas": 0,
            "imagenes": []
        }
    
    print(f"\n📖 Título: {titulo}")
    print(f"🎬 Escenas: {len(escenas)}")
    
    # Crear carpeta de salida
    os.makedirs(carpeta_salida, exist_ok=True)
    
    # Identificar personajes del cuento
    personajes_cuento = _obtener_personajes_del_cuento(escenas)
    print(f"👥 Personajes: {', '.join([PERSONAJES[p]['nombre'] for p in personajes_cuento if p in PERSONAJES])}")
    print()
    
    # Generar cada imagen
    imagenes_resultado = []
    
    for escena in escenas:
        num = escena.get("numero_escena", 0)
        descripcion = escena.get("imagen_descripcion", "")
        
        print(f"🎬 Escena {num}...")
        print(f"   {descripcion[:60]}...")
        
        # Generar imagen
        imagen_data = _generar_imagen(descripcion, personajes_cuento)
        
        if imagen_data:
            # Guardar
            filename = f"escena_{num:02d}.png"
            filepath = os.path.join(carpeta_salida, filename)
            
            with open(filepath, 'wb') as f:
                f.write(imagen_data)
            
            imagenes_resultado.append({
                "numero_escena": num,
                "archivo": filepath,
                "exito": True
            })
            print(f"   ✅ Guardada: {filepath}")
        else:
            imagenes_resultado.append({
                "numero_escena": num,
                "archivo": None,
                "exito": False
            })
            print(f"   ❌ Error en escena {num}")
    
    print(f"\n{'=' * 70}")
    print("✅ GENERACIÓN COMPLETA")
    print(f"{'=' * 70}")
    
    # Resultado
    escenas_exitosas = sum(1 for img in imagenes_resultado if img["exito"])
    
    resultado = {
        "exito": escenas_exitosas > 0,
        "titulo": titulo,
        "total_escenas": len(escenas),
        "escenas_exitosas": escenas_exitosas,
        "imagenes": imagenes_resultado,
        "carpeta": carpeta_salida
    }
    
    return resultado

# ============================================================================
# EJEMPLO DE USO (si ejecutas este archivo directamente)
# ============================================================================

if __name__ == "__main__":
    # Ejemplo de JSON desde DeepSeek
    cuento_ejemplo = {
        "metadata": {
            "titulo": "El Secreto de los Dientes Felices",
            "leccion": "Importancia de cepillarse los dientes"
        },
        "escenas": [
            {
                "numero_escena": 1,
                "imagen_descripcion": "Lucas sonriendo en el columpio del parque, mostrando sus dientes blancos. Sofia mirándolo curiosa. Parque soleado con árboles.",
                "dialogo": {
                    "personaje": "Sofia",
                    "texto": "Lucas, ¿cómo tienes los dientes tan blancos?",
                    "emocion": "curiosa"
                }
            },
            {
                "numero_escena": 2,
                "imagen_descripcion": "Lucas bajándose del columpio señalando hacia la distancia. Sofia escuchándolo atenta. Mismo parque.",
                "dialogo": {
                    "personaje": "Lucas",
                    "texto": "¡Es mi secreto! Vamos donde el Dr. Muelitas",
                    "emocion": "entusiasmado"
                }
            }
        ]
    }
    
    # Generar imágenes
    resultado = generar_imagenes_cuento(cuento_ejemplo)
    
    # Mostrar resultado
    print(f"\n📊 RESULTADO:")
    print(f"   Título: {resultado['titulo']}")
    print(f"   Exitosas: {resultado['escenas_exitosas']}/{resultado['total_escenas']}")
    print(f"   Carpeta: {resultado['carpeta']}")

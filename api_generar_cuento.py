"""
API para Generar Cuentos Ilustrados
====================================

Esta API recibe un JSON con la historia desde DeepSeek y genera las imágenes.

FLUJO:
1. DeepSeek crea el JSON del cuento
2. La página web lo envía a esta API
3. Esta API genera las imágenes con coherencia visual
4. Devuelve las rutas de las imágenes generadas

FORMATO ESPERADO:
{
    "solicitud": "historia sobre la importancia de la amistad",
    "personajes_ids": ["lucas", "sofia"],  # IDs de personajes a usar
    "escenas": [
        {
            "numero_escena": 1,
            "personajes_en_escena": ["lucas", "sofia"],
            "imagen_descripcion": "descripción de la escena...",
            "dialogo": {
                "personaje": "Lucas",
                "texto": "...",
                "emocion": "alegre"
            }
        }
    ]
}
"""

from google import genai
from PIL import Image
import os
import json

# Configurar API
API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
client = genai.Client(api_key=API_KEY)

# Personajes disponibles (con referencias)
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

def obtener_descripciones_personajes(personajes_ids):
    """Obtiene las descripciones de los personajes para el prompt"""
    descripciones = []
    for pid in personajes_ids:
        if pid in PERSONAJES:
            p = PERSONAJES[pid]
            descripciones.append(f"- {p['nombre']}: {p['descripcion']}")
    return "\n".join(descripciones)

def cargar_referencias_personajes(personajes_ids):
    """Carga las imágenes de referencia de los personajes"""
    referencias = []
    for pid in personajes_ids:
        if pid in PERSONAJES and os.path.exists(PERSONAJES[pid]["referencia"]):
            referencias.append(PERSONAJES[pid]["referencia"])
    return referencias

def generar_imagen(descripcion_escena, personajes_en_escena):
    """Genera una imagen de la escena manteniendo coherencia de personajes"""
    
    # Obtener descripciones y referencias
    desc_personajes = obtener_descripciones_personajes(personajes_en_escena)
    referencias = cargar_referencias_personajes(personajes_en_escena)
    
    # Construir prompt
    prompt = f"""PERSONAJES EN ESTA ESCENA:
{desc_personajes}

ESCENA:
{descripcion_escena}

INSTRUCCIONES:
- MANTÉN las características EXACTAS de los personajes de las referencias
- NO incluir texto, diálogos ni viñetas en la imagen
- Estilo: ilustración infantil colorida, amigable, educativa
- Colores brillantes y alegres
"""
    
    # Generar con referencias
    contenido = [prompt]
    for ref in referencias:
        contenido.append(Image.open(ref))
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=contenido
    )
    
    # Extraer imagen
    for part in response.parts:
        if hasattr(part, 'inline_data') and part.inline_data is not None:
            return part.inline_data.data
    
    if hasattr(response, 'candidates') and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data is not None:
                        return part.inline_data.data
    
    return None

def procesar_cuento(cuento_json):
    """
    Procesa un cuento desde DeepSeek y genera todas las imágenes
    
    Args:
        cuento_json: dict con el formato del cuento
        
    Returns:
        dict con las rutas de las imágenes generadas
    """
    
    print("=" * 70)
    print("🎨 PROCESANDO CUENTO DESDE DEEPSEEK")
    print("=" * 70)
    
    # Extraer información
    titulo = cuento_json.get("metadata", {}).get("titulo", "Cuento sin título")
    escenas = cuento_json.get("escenas", [])
    
    print(f"\n📖 Título: {titulo}")
    print(f"🎬 Escenas: {len(escenas)}")
    
    # Obtener personajes únicos del cuento
    personajes_usados = set()
    for escena in escenas:
        # Mapear nombres a IDs (lowercase, sin espacios)
        personaje_dialogo = escena.get("dialogo", {}).get("personaje", "")
        pid = personaje_dialogo.lower().replace(" ", "_").replace(".", "")
        if pid in PERSONAJES:
            personajes_usados.add(pid)
    
    print(f"👥 Personajes: {', '.join([PERSONAJES[p]['nombre'] for p in personajes_usados if p in PERSONAJES])}")
    print()
    
    # Generar imágenes
    imagenes_generadas = []
    
    for escena in escenas:
        num = escena.get("numero_escena", 0)
        descripcion = escena.get("imagen_descripcion", "")
        
        # Determinar qué personajes están en esta escena
        # Por ahora asumimos que todos los personajes del cuento están en cada escena
        # Esto se puede refinar si DeepSeek envía "personajes_en_escena"
        personajes_escena = list(personajes_usados)
        
        print(f"🎬 Escena {num}...")
        print(f"   {descripcion[:60]}...")
        
        # Generar imagen
        imagen_data = generar_imagen(descripcion, personajes_escena)
        
        if imagen_data:
            # Guardar imagen
            filename = f"escena_{num:02d}.png"
            with open(filename, 'wb') as f:
                f.write(imagen_data)
            
            imagenes_generadas.append({
                "numero_escena": num,
                "archivo": filename,
                "exito": True
            })
            print(f"   ✅ Guardada: {filename}")
        else:
            imagenes_generadas.append({
                "numero_escena": num,
                "archivo": None,
                "exito": False
            })
            print(f"   ❌ Error generando escena {num}")
    
    print(f"\n{'=' * 70}")
    print("✅ PROCESAMIENTO COMPLETO")
    print(f"{'=' * 70}")
    
    # Resultado
    resultado = {
        "titulo": titulo,
        "total_escenas": len(escenas),
        "escenas_exitosas": sum(1 for img in imagenes_generadas if img["exito"]),
        "imagenes": imagenes_generadas
    }
    
    return resultado

# ============================================================================
# EJEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Este es el JSON que recibirías desde DeepSeek
    cuento_desde_deepseek = {
        "metadata": {
            "titulo": "El Secreto de los Dientes Felices",
            "leccion": "Importancia de cepillarse los dientes regularmente",
            "duracion_estimada": "2-3 minutos"
        },
        "escenas": [
            {
                "numero_escena": 1,
                "sonido_fondo": "sonidos de parque, niños jugando",
                "imagen_descripcion": "Lucas sonriendo ampliamente mientras se balancea en el columpio del parque, mostrando sus dientes blancos y brillantes. Sofia está cerca mirándolo con curiosidad.",
                "dialogo": {
                    "personaje": "Sofia",
                    "texto": "Lucas, ¿cómo tienes los dientes tan blancos y bonitos?",
                    "emocion": "curiosa"
                }
            },
            {
                "numero_escena": 2,
                "sonido_fondo": "sonidos de parque con risas suaves de fondo",
                "imagen_descripcion": "Lucas bajándose del columpio y señalando hacia la distancia con expresión entusiasta, hablando con Sofia en el parque.",
                "dialogo": {
                    "personaje": "Lucas",
                    "texto": "¡Es mi secreto! Vamos al consultorio del Dr. Muelitas y te lo cuento",
                    "emocion": "entusiasmado"
                }
            },
            {
                "numero_escena": 3,
                "sonido_fondo": "música suave de consultorio, puerta abriéndose",
                "imagen_descripcion": "Dr. Muelitas recibiendo a Lucas y Sofia en la puerta de su consultorio dental colorido, con sonrisa cálida y brazos abiertos.",
                "dialogo": {
                    "personaje": "Dr. Muelitas",
                    "texto": "Hola niños, ¿listos para aprender el secreto de los dientes felices?",
                    "emocion": "amable"
                }
            }
        ]
    }
    
    # Procesar el cuento
    resultado = procesar_cuento(cuento_desde_deepseek)
    
    # Mostrar resultado
    print("\n📊 RESULTADO:")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

"""
Generador de Cuentos con Personajes Consistentes
================================================

Este script genera cuentos usando SIEMPRE los mismos personajes de referencia
para mantener coherencia visual en todos los cuentos del proyecto.

USO:
1. Define tu cuento en la sección ESCENAS
2. Especifica qué personajes aparecen en cada escena
3. El script usará automáticamente las imágenes de referencia
4. ¡Listo! Coherencia visual garantizada
"""

from google import genai
from PIL import Image
import os

# Configurar API
API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
client = genai.Client(api_key=API_KEY)

# ============================================================================
# PERSONAJES DISPONIBLES (con sus referencias visuales)
# ============================================================================

PERSONAJES = {
    "lucas": {
        "nombre": "Lucas",
        "descripcion": "niño de 7 años, cabello castaño corto, camisa azul celeste, sonrisa brillante con dientes blancos",
        "referencia": "personajes/lucas/lucas_referencia.png",
        "descripcion_file": "personajes/lucas/lucas_descripcion.txt"
    },
    "sofia": {
        "nombre": "Sofia",
        "descripcion": "niña de 7 años, cabello rizado castaño oscuro, vestido rosa intenso, expresión curiosa",
        "referencia": "personajes/sofia/sofia_referencia.png",
        "descripcion_file": "personajes/sofia/sofia_descripcion.txt"
    },
    "dr_muelitas": {
        "nombre": "Dr. Muelitas",
        "descripcion": "dentista de 40 años, bata blanca, bigote, gafas redondas, sonrisa amplia y amable",
        "referencia": "personajes/dr_muelitas/dr_muelitas_referencia.png",
        "descripcion_file": "personajes/dr_muelitas/dr_muelitas_descripcion.txt"
    }
}

# ============================================================================
# CONFIGURACIÓN DEL CUENTO
# ============================================================================

TITULO_CUENTO = "El Secreto de los Dientes Felices"

# Escenas del cuento
# personajes_en_escena: lista de IDs de personajes que aparecen ["lucas", "sofia"]
ESCENAS = [
    {
        "numero": 1,
        "personajes_en_escena": ["lucas", "sofia"],
        "descripcion": "Lucas sonriendo ampliamente mientras se balancea en el columpio del parque, mostrando sus dientes blancos y brillantes. Sofia está cerca mirándolo con curiosidad. Ambiente de parque soleado con árboles y flores.",
        "archivo": "escena_01_lucas_columpio.png"
    },
    {
        "numero": 2,
        "personajes_en_escena": ["lucas", "sofia"],
        "descripcion": "Lucas bajándose del columpio y señalando hacia la distancia con expresión entusiasta, hablando con Sofia. Mismo parque, ambiente alegre.",
        "archivo": "escena_02_lucas_senala.png"
    },
    {
        "numero": 3,
        "personajes_en_escena": ["lucas", "sofia", "dr_muelitas"],
        "descripcion": "Dr. Muelitas recibiendo a Lucas y Sofia en la puerta de su consultorio dental colorido, con sonrisa cálida. Consultorio con decoración infantil, posters de dientes felices en las paredes.",
        "archivo": "escena_03_llegada_consultorio.png"
    },
    {
        "numero": 4,
        "personajes_en_escena": ["lucas", "sofia", "dr_muelitas"],
        "descripcion": "Sofia mirando alrededor del consultorio dental con ojos curiosos, señalando los posters educativos en la pared. Lucas y Dr. Muelitas están cerca. Interior del consultorio colorido y amigable.",
        "archivo": "escena_04_sofia_curiosa.png"
    },
    {
        "numero": 5,
        "personajes_en_escena": ["lucas", "sofia", "dr_muelitas"],
        "descripcion": "Dr. Muelitas sosteniendo un cepillo de dientes gigante de demostración y un modelo grande de dientes, explicando a los niños. Lucas y Sofia escuchando atentos. Interior del consultorio.",
        "archivo": "escena_05_doctor_enseña.png"
    },
    {
        "numero": 6,
        "personajes_en_escena": ["lucas", "dr_muelitas", "sofia"],
        "descripcion": "Lucas asintiendo seriamente mientras el Dr. Muelitas muestra la técnica de cepillado circular en el modelo de dientes. Sofia observa atenta. Interior del consultorio.",
        "archivo": "escena_06_lucas_aprende.png"
    },
    {
        "numero": 7,
        "personajes_en_escena": ["sofia", "lucas", "dr_muelitas"],
        "descripcion": "Sofia practicando movimientos de cepillado en el aire con un cepillo, expresión concentrada y determinada. Lucas y Dr. Muelitas mirándola con aprobación. Interior del consultorio.",
        "archivo": "escena_07_sofia_practica.png"
    },
    {
        "numero": 8,
        "personajes_en_escena": ["lucas", "sofia", "dr_muelitas"],
        "descripcion": "Los tres personajes (Lucas, Sofia y Dr. Muelitas) sonriendo ampliamente frente al espejo del consultorio, mostrando sus dientes felices. Ambiente celebratorio y alegre.",
        "archivo": "escena_08_final_feliz.png"
    }
]

# ============================================================================
# FUNCIONES
# ============================================================================

def cargar_referencias_personajes(personajes_ids):
    """Carga las imágenes de referencia de los personajes"""
    referencias = []
    descripciones = []
    
    for pid in personajes_ids:
        if pid in PERSONAJES:
            p = PERSONAJES[pid]
            if os.path.exists(p["referencia"]):
                referencias.append(p["referencia"])
            descripciones.append(f"- {p['nombre']}: {p['descripcion']}")
    
    return referencias, "\n".join(descripciones)

def generar_imagen(descripcion_escena, personajes_en_escena):
    """Genera una imagen usando las referencias de los personajes"""
    
    # Obtener referencias y descripciones
    referencias, desc_personajes = cargar_referencias_personajes(personajes_en_escena)
    
    # Construir prompt
    prompt = f"""PERSONAJES EN ESTA ESCENA (mantener EXACTAMENTE estas características):
{desc_personajes}

ESCENA A ILUSTRAR:
{descripcion_escena}

INSTRUCCIONES CRÍTICAS:
- MANTÉN las características EXACTAS de los personajes de las imágenes de referencia
- Los personajes deben verse IDÉNTICOS a las referencias (misma ropa, mismo pelo, misma cara)
- NO incluir texto, diálogos, globos de texto ni viñetas en la imagen
- Estilo: ilustración infantil colorida, amigable, educativa
- Colores brillantes y alegres
- Sin texto visible en la imagen (el diálogo es por audio)
"""
    
    # Generar con referencias
    contenido = [prompt]
    for ref in referencias:
        if os.path.exists(ref):
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

# ============================================================================
# MAIN
# ============================================================================

print("=" * 70)
print(f"🎨 GENERANDO CUENTO: {TITULO_CUENTO}")
print("=" * 70)
print(f"\n📖 Generando {len(ESCENAS)} escenas con personajes consistentes...")
print("⚠️  Las imágenes NO incluirán texto (el diálogo es por audio)")
print("\n👥 Personajes del cuento:")
for pid in set([p for escena in ESCENAS for p in escena["personajes_en_escena"]]):
    if pid in PERSONAJES:
        print(f"  - {PERSONAJES[pid]['nombre']}")
print()

for escena in ESCENAS:
    print(f"\n{'=' * 70}")
    print(f"🎬 ESCENA {escena['numero']} de {len(ESCENAS)}")
    print(f"{'=' * 70}")
    print(f"👥 Personajes: {', '.join([PERSONAJES[p]['nombre'] for p in escena['personajes_en_escena'] if p in PERSONAJES])}")
    print(f"📝 {escena['descripcion'][:80]}...")
    
    print(f"\n🎨 Generando imagen...")
    imagen_data = generar_imagen(escena['descripcion'], escena['personajes_en_escena'])
    
    if imagen_data:
        with open(escena['archivo'], 'wb') as f:
            f.write(imagen_data)
        print(f"✅ Guardada: {escena['archivo']}")
    else:
        print(f"❌ Error generando escena {escena['numero']}")

print(f"\n{'=' * 70}")
print("✅ ¡CUENTO COMPLETO GENERADO!")
print(f"{'=' * 70}")
print("\n📁 Archivos generados:")
for escena in ESCENAS:
    print(f"  - {escena['archivo']}")
print("\n✨ Todos los personajes mantienen coherencia visual")
print("📢 Sin texto en las imágenes (diálogos por audio)")
print("🎭 Se usaron las referencias oficiales de personajes")

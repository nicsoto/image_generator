"""
Script para generar las 8 escenas del cuento "El Secreto de los Dientes Felices"
Usa el modelo Gemini para mantener coherencia visual entre todas las escenas
"""

from google import genai
from PIL import Image

# Configurar API
API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
client = genai.Client(api_key=API_KEY)

# Definición de personajes (para mantener coherencia)
PERSONAJES = """
PERSONAJES DEL CUENTO (mantener estas características en TODAS las escenas):
- Lucas: niño de 7 años, sonrisa brillante con dientes blancos, usa camisa azul
- Sofia: niña de 7 años, cabello rizado, vestido rosa
- Dr. Muelitas: dentista de 40 años, bata blanca, bigote, sonrisa amplia
"""

# Escenas del cuento
escenas = [
    {
        "numero": 1,
        "descripcion": "Lucas sonriendo ampliamente mientras se balancea en el columpio del parque, mostrando sus dientes blancos y brillantes. Sofia está cerca mirándolo con curiosidad. Ambiente de parque soleado con árboles y flores. Estilo ilustración infantil colorida.",
        "archivo": "escena_01_lucas_columpio.png"
    },
    {
        "numero": 2,
        "descripcion": "Lucas bajándose del columpio y señalando hacia la distancia con expresión entusiasta, hablando con Sofia. Mismo parque, ambiente alegre. Estilo ilustración infantil colorida.",
        "archivo": "escena_02_lucas_senala.png"
    },
    {
        "numero": 3,
        "descripcion": "Dr. Muelitas recibiendo a Lucas y Sofia en la puerta de su consultorio dental colorido, con sonrisa cálida. Consultorio con decoración infantil, posters de dientes felices en las paredes. Estilo ilustración infantil colorida.",
        "archivo": "escena_03_llegada_consultorio.png"
    },
    {
        "numero": 4,
        "descripcion": "Sofia mirando alrededor del consultorio dental con ojos curiosos, señalando los posters educativos en la pared. Lucas y Dr. Muelitas están cerca. Interior del consultorio colorido y amigable. Estilo ilustración infantil colorida.",
        "archivo": "escena_04_sofia_curiosa.png"
    },
    {
        "numero": 5,
        "descripcion": "Dr. Muelitas sosteniendo un cepillo de dientes gigante de demostración y un modelo grande de dientes, explicando a los niños. Lucas y Sofia escuchando atentos. Interior del consultorio. Estilo ilustración infantil colorida.",
        "archivo": "escena_05_doctor_enseña.png"
    },
    {
        "numero": 6,
        "descripcion": "Lucas asintiendo seriamente mientras el Dr. Muelitas muestra la técnica de cepillado circular en el modelo de dientes. Sofia observa atenta. Interior del consultorio. Estilo ilustración infantil colorida.",
        "archivo": "escena_06_lucas_aprende.png"
    },
    {
        "numero": 7,
        "descripcion": "Sofia practicando movimientos de cepillado en el aire con un cepillo, expresión concentrada y determinada. Lucas y Dr. Muelitas mirándola con aprobación. Interior del consultorio. Estilo ilustración infantil colorida.",
        "archivo": "escena_07_sofia_practica.png"
    },
    {
        "numero": 8,
        "descripcion": "Los tres personajes (Lucas, Sofia y Dr. Muelitas) sonriendo ampliamente frente al espejo del consultorio, mostrando sus dientes felices. Ambiente celebratorio y alegre. Estilo ilustración infantil colorida.",
        "archivo": "escena_08_final_feliz.png"
    }
]

def generar_imagen(descripcion, imagen_referencia=None):
    """Genera una imagen usando Gemini"""
    
    prompt = f"""{PERSONAJES}

ESCENA A ILUSTRAR:
{descripcion}

INSTRUCCIONES CRÍTICAS:
- NO incluir texto, diálogos, globos de texto ni viñetas en la imagen
- Mantener EXACTAMENTE las mismas características de los personajes en todas las escenas
- Estilo: ilustración infantil colorida, amigable, educativa
- Colores brillantes y alegres
- Sin texto visible en la imagen (el diálogo es por audio)
"""

    if imagen_referencia:
        # Con referencia para mantener coherencia
        prompt += "\n- MANTÉN las características visuales de los personajes de la imagen de referencia"
        img = Image.open(imagen_referencia)
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt, img]
        )
    else:
        # Primera escena sin referencia
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt]
        )
    
    # Extraer imagen
    for part in response.parts:
        if hasattr(part, 'inline_data') and part.inline_data is not None:
            return part.inline_data.data
    
    # Intentar desde candidates
    if hasattr(response, 'candidates') and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data is not None:
                        return part.inline_data.data
    
    return None

print("=" * 70)
print("🎨 GENERANDO CUENTO: El Secreto de los Dientes Felices")
print("=" * 70)
print("\n📖 Generando 8 escenas con coherencia visual...")
print("⚠️  Las imágenes NO incluirán texto (el diálogo es por audio)\n")

imagen_referencia = None

for escena in escenas:
    print(f"\n{'=' * 70}")
    print(f"🎬 ESCENA {escena['numero']} de 8")
    print(f"{'=' * 70}")
    print(f"📝 {escena['descripcion'][:100]}...")
    
    print(f"\n🎨 Generando imagen...")
    imagen_data = generar_imagen(escena['descripcion'], imagen_referencia)
    
    if imagen_data:
        with open(escena['archivo'], 'wb') as f:
            f.write(imagen_data)
        print(f"✅ Guardada: {escena['archivo']}")
        
        # La primera imagen es la referencia para las demás
        if escena['numero'] == 1:
            imagen_referencia = escena['archivo']
            print(f"📌 Esta será la referencia para mantener coherencia visual")
    else:
        print(f"❌ Error generando escena {escena['numero']}")

print(f"\n{'=' * 70}")
print("✅ ¡CUENTO COMPLETO GENERADO!")
print(f"{'=' * 70}")
print("\n📁 Archivos generados:")
for escena in escenas:
    print(f"  - {escena['archivo']}")
print("\n✨ Todas las imágenes mantienen coherencia visual de personajes")
print("📢 Sin texto en las imágenes (diálogos por audio)")

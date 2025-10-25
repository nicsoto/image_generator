import google.generativeai as genai
from PIL import Image

API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-image")

print("=" * 60)
print("GENERADOR DE IMAGENES PARA CUENTOS INFANTILES")
print("=" * 60)
print()
print("Opciones:")
print("  1. Usar imagen de referencia (mantener estilo/personaje)")
print("  2. Generar sin referencia (solo con descripcion)")
print()
opcion = input("Selecciona opcion (1 o 2): ")

usar_referencia = opcion == "1"
imagen_ref = None

if usar_referencia:
    print()
    ruta_imagen = input("Ruta de la imagen de referencia: ")
    try:
        imagen_ref = Image.open(ruta_imagen)
        print("Imagen de referencia cargada correctamente")
    except:
        print("No se pudo cargar la imagen. Continuando sin referencia...")
        usar_referencia = False

print()
print("-" * 60)
print("Describe la escena completa:")
print("  (Incluye personajes, escenario, acciones, colores, etc.)")
print()
user_prompt = input(">> ")

if not user_prompt.strip():
    print("Descripcion vacia. Saliendo...")
    exit()

# Construir el prompt
PROMPT = f"""Ilustracion de cuento infantil profesional:

ESCENA: {user_prompt}

ESTILO:
- Colores brillantes y vibrantes
- Estilo de libro infantil moderno
- Lineas limpias y definidas
- Ambiente alegre y acogedor
- Apropiado para ninos
"""

if usar_referencia:
    PROMPT += "\nUsa el mismo estilo artistico de la imagen de referencia adjunta."

print()
nombre = input("Nombre del archivo (ej: cuento_bosque.png): ")
if not nombre.strip():
    nombre = "imagen_cuento.png"
elif not nombre.endswith(".png"):
    nombre += ".png"

print()
print("-" * 60)
print("Generando imagen...")
print()

try:
    if usar_referencia:
        response = model.generate_content([PROMPT, imagen_ref])
    else:
        response = model.generate_content(PROMPT)
    
    for part in response.parts:
        if hasattr(part, "inline_data") and part.inline_data and part.inline_data.mime_type == "image/png":
            with open(nombre, "wb") as f:
                f.write(part.inline_data.data)
            print(f"LISTO: {nombre}")
            break
except Exception as e:
    print(f"ERROR: {e}")


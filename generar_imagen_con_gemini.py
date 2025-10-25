import google.generativeai as genai
from PIL import Image

API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-image")

print("GENERADOR DE IMAGENES")
print()
user_prompt = input("Describe la escena: ")

PROMPT = f"Ilustracion infantil: {user_prompt}. MATEO: nino 8 anos, camiseta azul con estrella amarilla, shorts, tenis rojos. Estilo colorido."

nombre = input("Nombre archivo: ")
if not nombre.endswith(".png"):
    nombre += ".png"

print("Generando...")

try:
    img = Image.open("/home/nico/Escritorio/hackaton/mateo.png")
    response = model.generate_content([PROMPT, img])
    
    for part in response.parts:
        if hasattr(part, "inline_data") and part.inline_data and part.inline_data.mime_type == "image/png":
            with open(nombre, "wb") as f:
                f.write(part.inline_data.data)
            print(f"LISTO: {nombre}")
            break
except Exception as e:
    print(f"ERROR: {e}")


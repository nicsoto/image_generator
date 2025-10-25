from google import genai
from google.genai import types

# Configurar la API Key
API_KEY = "AIzaSyD6B6z-Q8En35eLWd401WDH6Rcvy5zkNZk"

# Crear el cliente
client = genai.Client(api_key=API_KEY)

# El prompt (debe estar en inglés)
prompt = """A full body illustration of an 8-year-old boy named Mateo in children's book style. 
He has warm light brown skin (golden undertone), dark brown straight hair in a messy bowl cut with a lock 
falling over his right eyebrow. Large curious honey-colored eyes with long eyelashes, straight thick eyebrows 
giving a surprised expression. Small nose, thin lips in a half-smile. Tiny mole under left cheekbone. 
He's wearing a white t-shirt with a red rocket print, blue denim shorts with big pockets, worn white sneakers 
with red laces, and ankle socks with red stripe. Multicolored woven bracelet on left wrist. 
Friendly, curious expression. Children's book illustration style, bright colors, warm and cheerful."""

print(f"Generando imagen con Imagen 4...\n")
print(f"Prompt: {prompt}\n")

try:
    # Generar imágenes con el modelo Imagen 4
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',  # Modelo estándar de Imagen 4
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,  # Generar 1 imagen (puedes poner hasta 4)
            aspect_ratio="1:1",   # Relación de aspecto cuadrada
            # person_generation="allow_adult"  # Por defecto ya permite adultos
        )
    )
    
    # Guardar las imágenes generadas
    for i, generated_image in enumerate(response.generated_images):
        filename = f"imagen_generada_{i+1}.png"
        
        # Guardar la imagen
        generated_image.image.save(filename)
        
        print(f"✓ Imagen {i+1} guardada como: {filename}")
    
    print("\n¡Listo! Revisa las imágenes generadas.")
    print("Nota: Todas las imágenes generadas incluyen marca de agua SynthID")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nSi el error es sobre el módulo 'genai', instala la biblioteca correcta:")
    print("pip install google-genai")

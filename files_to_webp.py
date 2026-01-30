import os
from PIL import Image

EXTENSIONES = (".jpg", ".JPG", ".png")

def convertir_directorio(directorio, calidad=80):
    for archivo in os.listdir(directorio):
        if archivo.endswith(EXTENSIONES):
            ruta_origen = os.path.join(directorio, archivo)
            nombre = os.path.splitext(archivo)[0]
            ruta_webp = os.path.join(directorio, nombre + ".webp")

            try:
                with Image.open(ruta_origen) as img:
                    img = img.convert("RGB")
                    img.save(ruta_webp, "WEBP", quality=calidad)
                    print(f"Convertido: {archivo}")
            except Exception as e:
                print(f"Error con {archivo}: {e}")

if __name__ == "__main__":
    directorio = input("Ruta del directorio: ").strip()
    convertir_directorio(directorio)


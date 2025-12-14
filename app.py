from flask import Flask, send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PLANTILLA = os.path.join(BASE_DIR, "static", "plantilla.jpg")
CARPETA_CARNETS = os.path.join(BASE_DIR, "static", "carnets")
FONT_PATH = os.path.join(BASE_DIR, "fonts", "Montserrat-Regular.ttf")

os.makedirs(CARPETA_CARNETS, exist_ok=True)

@app.route("/generar/<nombre>/<documento>/<cargo>")
def generar_carnet(nombre, documento, cargo):

    img = Image.open(PLANTILLA).convert("RGB")
    draw = ImageDraw.Draw(img)

    # 🔥 FUENTES GRANDES (AQUÍ CAMBIAS TAMAÑO)
    font_nombre = ImageFont.truetype(FONT_PATH, 120)
    font_datos = ImageFont.truetype(FONT_PATH, 90)

    color = (46, 77, 46)

    # 📍 POSICIONES (AJUSTA SI QUIERES)
    draw.text((600, 520), f"Nombre: {nombre}", fill=color, font=font_nombre)
    draw.text((600, 660), f"Documento: {documento}", fill=color, font=font_datos)
    draw.text((600, 780), f"Cargo: {cargo}", fill=color, font=font_datos)

    nombre_archivo = f"{nombre}_{documento}.jpg"
    ruta_salida = os.path.join(CARPETA_CARNETS, nombre_archivo)

    img.save(ruta_salida, quality=95)

    return send_from_directory(CARPETA_CARNETS, nombre_archivo)


@app.route("/")
def home():
    return "Servidor activo"


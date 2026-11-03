import streamlit as st
import os
import json
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="BOSTO", page_icon=":camera:", layout="wide")

UPLOAD_FOLDER = "fotos"
DATA_FILE = "datos.json"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def cargar_datos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
def guardar_datos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

datos = cargar_datos()

st.title("BOSTO - Galeria Social")
st.write("Sube fotos, dale like y mira las vistas")

# --- AQUI ESTA EL BOTON VISIBLE ---
st.divider()
st.subheader("Subir foto desde tu celular")
uploaded_file = st.file_uploader("Elige de tu almacenamiento", type=["jpg","jpeg","png","webp","mp
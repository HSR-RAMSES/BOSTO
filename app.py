import streamlit as st
import os
import json
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="BOSTO", page_icon="📸", layout="wide")

# --- Carpetas y datos ---
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

st.title("📸 BOSTO - Galería Social")
st.write("Sube fotos, dale like y mira las vistas")

# --- Subir foto ---
with st.sidebar:
    st.header("Subir nueva foto")
    uploaded_file = st.file_uploader("Elige una foto", type=["jpg","jpeg","png","webp"])
    nombre = st.text_input("Tu nombre (opcional)")
    if st.button("Publicar foto"):
        if uploaded_file:
            filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_file.name}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            datos[filename] = {
                "likes": 0,
                "views": 0,
                "
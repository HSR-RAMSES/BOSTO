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

with st.sidebar:
    st.header("Subir nueva foto")
    uploaded_file = st.file_uploader("Elige una foto", type=["jpg","jpeg","png","webp"])
    nombre = st.text_input("Tu nombre")
    if st.button("Publicar foto"):
        if uploaded_file:
            filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_file.name}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())
            datos[filename] = {
                "likes": 0,
                "views": 0,
                "uploader": nombre if nombre else "Anonimo",
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            guardar_datos(datos)
            st.success("Foto subida!")
            st.rerun()

if not datos:
    st.info("Aun no hay fotos. Se el primero!")
else:
    fotos_ordenadas = sorted(datos.items(), key=lambda x: x[1]['fecha'], reverse=True)
    cols = st.columns(3)
    for i, (filename, info) in enumerate(fotos_ordenadas):
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        if not os.path.exists(filepath):
            continue
        datos[filename]["views"] += 1
        with cols[i % 3]:
            image = Image.open(filepath)
            st.image(image, use_container_width=True)
            st.caption(f"Por: {info['uploader']} - {info['fecha']}")
            if st.button(f"Like {info['likes']}", key=f"like_{filename}"):
                datos[filename]["likes"] += 1
                guardar_datos(datos)
                st.rerun()
            st.write(f"Vistas: {info['views']}")
            st.divider()
    guardar_datos(datos)
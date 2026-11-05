uploaded.nameimport streamlit as st
import os
import json
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="BOSTO", layout="wide")

os.makedirs("fotos", exist_ok=True)
if not os.path.exists("datos.json"):
    with open("datos.json", "w") as f:
        json.dump({}, f)

def cargar():
    with open("datos.json", "r") as f:
        return json.load(f)

def guardar(d):
    with open("datos.json", "w") as f:
        json.dump(d, f)

datos = cargar()
st.title("BOSTO - Galeria Social")

st.subheader("Subir foto desde tu almacenamiento")
uploaded = st.file_uploader("Toca aqui y elige de tu galeria")
nombre = st.text_input("Tu nombre")

if st.button("Publicar foto"):
    if uploaded:
        fname = datetime.now().strftime("%H%M%S_") + uploaded.name
        with open(os.path.join("fotos", fname), "wb") as out:
            out.write(uploaded.getbuffer())
        datos[fname] = {"likes":0,"views":0,"uploader":nombre,"fecha":datetime.now().strftime("%d/%m %H:%M")}
        guardar(datos)
        st.success("Subida!")
        st.rerun()

if not datos:
    st.info("Aun no hay fotos")
else:
    for fname, info in datos.items():
        path = os.path.join("fotos", fname)
        if not os.path.exists(path):
            continue
        st.image(Image.open(path), use_container_width=True)
        st.write(f"Por {info['uploader']} - Vistas {info['views']} - Likes {info['likes']}")
        if st.button("Dar like", key=fname):
            datos[fname]["likes"] += 1
            datos[fname]["views"] += 1
            guardar(datos)
            st.rerun()
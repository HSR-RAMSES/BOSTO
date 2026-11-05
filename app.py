import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(page_title="Carta para Jaz", layout="centered")

os.makedirs("respuestas", exist_ok=True)
if not os.path.exists("respuestas.json"):
    with open("respuestas.json", "w") as f:
        json.dump({}, f)

def cargar():
    with open("respuestas.json", "r") as f:
        return json.load(f)

def guardar(d):
    with open("respuestas.json", "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

datos = cargar()

# ESTILOS CORAZONES Y OSITOS
st.markdown("""
<style>
.stApp { background: linear-gradient(#1a0b1a, #3a1040); }
h1 { color: #ff2e8b; text-align:center; }
.pregunta { background:#fff0f5; padding:15px; border-radius:15px; border-left:5px solid #ff2e8b; color:#333; margin:10px 0; font-weight:bold; }
.ositos { text-align:center; font-size:40px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="ositos">💌 🧸 💖 🧸 💌</div>', unsafe_allow_html=True)
st.title("ABRE LA CARTA JAZ 💖")
st.markdown('<div class="ositos">🧸 💕 🧸 💕 🧸</div>', unsafe_allow_html=True)

st.subheader("De: H3ND3R_404 con mucho amor")

nombre = st.text_input("Tu nombre es Jaz? Escribe tu nombre 💗")
st.write("---")

preguntas = [
    "💗 1. ¿Qué sientes cuando estás conmigo?",
    "💗 2. ¿Crees que tú y yo tenemos algo especial?",
    "💗 3. ¿Qué es lo que más te gusta de mí?",
    "💗 4. ¿Te gustaría que estemos juntos para siempre?",
    "💗 5. ¿Me extrañas cuando no me ves? 🥺",
    "💗 6. ¿Quieres ser mi persona favorita? 💑"
]

respuestas = []
for i, p in enumerate(preguntas):
    st.markdown(f'<div class="pregunta">{p}</div>', unsafe_allow_html=True)
    r = st.text_area("", key=f"p{i}", placeholder="Escribe tu respuesta aquí... 🧸")
    respuestas.append(r)

st.write("---")
st.markdown('<div class="ositos">💖 🧸 💖 🧸 💖</div>', unsafe_allow_html=True)

if st.button("Enviar mis respuestas 💌💖"):
    if nombre:
        id_resp = datetime.now().strftime("%d-%m-%Y_%H%M%S_") + nombre
        datos[id_resp] = {
            "nombre": nombre,
            "respuestas": respuestas,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        guardar(datos)
        st.balloons()
        st.success(f"¡Gracias {nombre}! Tus respuestas se guardaron con mucho amor 🧸💕")
        st.snow()
    else:
        st.warning("Escribe tu nombre primero 💗")

if datos:
    st.write("---")
    st.subheader("Respuestas guardadas 🧸💌")
    for k, v in reversed(list(datos.items())):
        st.write(f"**{v['nombre']}** - {v['fecha']}")
        for idx, resp in enumerate(v['respuestas']):
            if resp:
                st.write(f"{preguntas[idx]} -> {resp}")
        st.write("---")
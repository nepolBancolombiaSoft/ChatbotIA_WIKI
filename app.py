import os
import streamlit as st
from chatbot import generar_respuesta  # ✅ Importar la función correcta

# Obtener el puerto asignado por Railway
def obtener_puerto():
    return int(os.getenv("PORT", 8501))

# Obtener y almacenar el puerto al iniciar la aplicación
port = obtener_puerto()

# Configuración de la interfaz con Streamlit
st.set_page_config(page_title="Chatbot Wiki - Entra ID", layout="wide")
st.title("🤖 Chatbot Wiki - Entra ID")
st.write("Consulta sobre la Wiki de Azure y Entra ID.")

# Entrada del usuario
pregunta = st.text_input("Escribe tu pregunta aquí:", "")

if pregunta:
    respuesta, documentos = generar_respuesta(pregunta)  # ✅ Ahora también obtenemos los documentos relevantes
    st.write(f"🤖 **Respuesta:** {respuesta}")

    # 📌 Mostrar documentos relevantes
    if documentos:
        st.write("📄 **Documentos relevantes encontrados:**")
        for idx, doc in enumerate(documentos, 1):
            with st.expander(f"📄 Documento {idx}"):
                st.write(f"📝 **Extracto:** {doc['contenido']}...")
                st.markdown(f"[🔗 Ver en la Wiki]({doc['url']})")
    else:
        st.write("⚠️ No encontré documentos relevantes en la base de datos.")

# 🚀 Ejecutar la aplicación en el puerto correcto
st.write(f"🚀 Ejecutando en el puerto {port}")


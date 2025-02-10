import streamlit as st
from chatbot import generar_respuesta  # ✅ Importar la función correcta

# Configuración de la interfaz con Streamlit
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



import os
import cohere
import langdetect
import mtranslate
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from config import COHERE_API_KEY  # ✅ Asegúrate de tener tu clave en config.py

# 📌 Configurar API de Cohere
co = cohere.Client(COHERE_API_KEY)

# 📌 Configuración de la Base de Datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wiki_db")

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small")
)
retriever = db.as_retriever()
print(f"📂 Base de datos guardada en: {DB_PATH}")

# 📌 Historial de conversación
historial = []

# 📌 Prompt optimizado para Cohere
qa_prompt = PromptTemplate(
    input_variables=["context", "question", "history"],
    template=(
        "Responde de manera clara y precisa usando la información de la Wiki.\n\n"
        "**Historial de conversación:**\n{history}\n\n"
        "**Información relevante:**\n{context}\n\n"
        "**Pregunta:** {question}\n\n"
        "📌 **Explicación clara y estructurada:**"
    )
)

# 📌 Función para actualizar el historial de conversación
def actualizar_historial(pregunta, respuesta):
    historial.append(f"Usuario: {pregunta}\nChatbot: {respuesta}")
    if len(historial) > 5:  # Mantiene las últimas 5 interacciones
        historial.pop(0)

# 📌 Función para generar respuesta con Cohere API
def generar_respuesta(pregunta):
    # 📌 Buscar documentos relevantes
    documentos = retriever.invoke(pregunta)
    print(f"🔍 Debug: {len(documentos)} documentos encontrados para '{pregunta}'")

    documentos_relevantes = []
    
    if documentos:
        print(f"\n📄 {len(documentos)} documentos relevantes encontrados.")

        # 📌 Evitar documentos duplicados
        documentos_unicos = {}
        for idx, doc in enumerate(documentos, 1):
            url = doc.metadata.get("source", "⚠️ No disponible")
            contenido = doc.page_content[:400]  # Muestra los primeros 400 caracteres del contenido
            
            documentos_relevantes.append({"url": url, "contenido": contenido})

            # Guardar solo documentos únicos basados en la URL
            if url not in documentos_unicos:
                documentos_unicos[url] = contenido

        print("✅ Los documentos fueron encontrados e impresos correctamente.")

        # 📌 Generar respuesta con Cohere API
        print("\n🤔 Estoy pensando en la respuesta...")  # ✅ Mensaje mientras se genera la IA

        query = qa_prompt.format(
            question=pregunta,
            context="\n\n".join(documentos_unicos.values()),
            history="\n".join(historial)
        )

        respuesta = co.generate(
            model="command",
            prompt=query,
            max_tokens=800,  # ✅ Permite respuestas más largas
            temperature=0.3,  # ✅ Hace que la respuesta sea más precisa y menos aleatoria
            frequency_penalty=0.4,  # ✅ Reduce repeticiones
            presence_penalty=0.5,  # ✅ Asegura que la IA no invente información
            stop_sequences=["\n"]
        )

        respuesta_texto = respuesta.generations[0].text.strip()

        # 📌 Si la respuesta está en inglés, traducir automáticamente
        if langdetect.detect(respuesta_texto) == "en":
            print("🌍 Detecté que la respuesta está en inglés. Traduciendo al español...")
            respuesta_texto = mtranslate.translate(respuesta_texto, "es", "auto")

        # 📌 Guardar en el historial
        actualizar_historial(pregunta, respuesta_texto)

        return respuesta_texto, documentos_relevantes

    else:
        return "⚠️ No encontré información relevante.", []


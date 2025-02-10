import os
import cohere
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from config import COHERE_API_KEY

# 📌 Configurar API de Cohere
co = cohere.Client(COHERE_API_KEY)

# 📌 Configuración de la Base de Datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wiki_db")

db = Chroma(persist_directory=DB_PATH, embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
retriever = db.as_retriever()
print(f"📂 Base de datos guardada en: {DB_PATH}")

# 📌 Historial de conversación
historial = []

# 📌 Prompt optimizado para Cohere
qa_prompt = PromptTemplate(
    input_variables=["context", "question", "history"],
    template=(
        "Responde en **español** de manera clara y precisa usando la información de la Wiki.\n\n"
        "**Historial de conversación:**\n{history}\n\n"
        "**Información relevante:**\n{context}\n\n"
        "**Pregunta:** {question}\n\n"
        "📌 **Explicación clara y estructurada en español:**"
    )
)

# 📌 Función para actualizar el historial de conversación
def actualizar_historial(pregunta, respuesta):
    historial.append(f"Usuario: {pregunta}\nChatbot: {respuesta}")
    if len(historial) > 5:
        historial.pop(0)

# 📌 Interfaz del chatbot en consola
while True:
    pregunta = input("\n🔹 Pregunta: ")
    if pregunta.lower() == "salir":
        print("👋 ¡Hasta luego! Si necesitas más ayuda, aquí estaré. 🚀")
        break

    # 📌 Buscar documentos relevantes
    documentos = retriever.invoke(pregunta)
    
    if documentos:
        print(f"📄 {len(documentos)} documentos relevantes encontrados.")

        # ✅ Mostrar los documentos encontrados
        for idx, doc in enumerate(documentos[:3], 1):
            print(f"\n📄 **Documento {idx}:**")
            print(f"📝 **Extracto:** {doc.page_content[:400]}...")  # 🔹 Solo mostramos los primeros 400 caracteres
            print(f"🔗 **URL:** {doc.metadata.get('source', '⚠️ No disponible')}\n")

        # 📌 Generar respuesta con Cohere API
        query = qa_prompt.format(
            question=pregunta,
            context="\n\n".join([doc.page_content[:300] for doc in documentos]),  
            history="\n".join(historial)
        )

        respuesta = co.generate(
            model="command",
            prompt=query,
            max_tokens=300,
            temperature=0.6,
            stop_sequences=["\n"]
            
        )

        respuesta_texto = respuesta.generations[0].text.strip()

        # 📌 Guardar en el historial
        actualizar_historial(pregunta, respuesta_texto)

        # 📌 Mostrar respuesta generada
        print(f"\n🤖 **Respuesta generada:**\n{respuesta_texto}\n")

    else:
        print("⚠️ No encontré información relevante. Intenta con otra pregunta.")

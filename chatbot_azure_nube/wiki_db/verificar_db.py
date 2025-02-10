import os
from langchain_chroma import Chroma

# 📌 Configuración de la Base de Datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wiki_db")

# 📌 Inicializar ChromaDB
db = Chroma(persist_directory=DB_PATH)

# 📌 Obtener documentos indexados
datos = db.get()

# 📌 Mostrar cuántos documentos hay en la base de datos
num_docs = len(datos["documents"])
print(f"\n📂 Número de documentos en la base de datos: {num_docs}")

# 📌 Mostrar los primeros 3 documentos (para evitar que la salida sea muy larga)
if num_docs > 0:
    print("\n🔍 **Primeros documentos indexados:**")
    for i, doc in enumerate(datos["documents"][:3], 1):
        print(f"\n📄 **Documento {i}:**")
        print(f"📝 **Extracto:** {doc[:300]}...")  # 🔹 Mostramos solo los primeros 300 caracteres
        print(f"🔗 **URL:** {datos['metadatas'][i-1].get('source', '⚠️ No disponible')}\n")

else:
    print("⚠️ No hay documentos en la base de datos.")


import os
import glob
from langchain_core.documents import Document  # ✅ Importamos Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 📌 Ruta donde se guarda la Wiki clonada
WIKI_DIR = os.path.expanduser("~/wiki_git")

# 📌 Configuración de la Base de Datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wiki_db")

# 📌 Inicializar ChromaDB
db = Chroma(persist_directory=DB_PATH, embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

# 📌 Reinicializar ChromaDB correctamente
print("🚨 Eliminando y reinicializando la base de datos...")
db.reset_collection()  # ✅ Se usa `reset_collection()` para evitar errores

# 📌 Leer archivos Markdown de la Wiki y convertirlos en objetos `Document`
documentos = []
for filepath in glob.glob(os.path.join(WIKI_DIR, "**/*.md"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        contenido = f.read()

    # 🔹 Obtener nombre del archivo como URL de referencia
    nombre_archivo = os.path.basename(filepath).replace(".md", "")
    source_url = f"https://dev.azure.com/npolo/BancolombiaTEST/_wiki/wikis/BancolombiaTEST.wiki/{nombre_archivo}"

    # ✅ Convertimos el diccionario en un objeto Document
    doc = Document(page_content=contenido, metadata={"source": source_url})
    documentos.append(doc)

# 📌 Verificar si hay documentos antes de agregarlos
if documentos:
    db.add_documents(documentos)  # ✅ Se agregan los documentos correctamente
    print(f"✅ Se han indexado {len(documentos)} documentos en la base de datos.")
else:
    print("⚠️ No se encontraron documentos en la Wiki.")

print("✅ Base de datos reconstruida con la Wiki actualizada 🚀")

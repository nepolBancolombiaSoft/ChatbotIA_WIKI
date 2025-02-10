import cohere
from config import COHERE_API_KEY  # ✅ Usa tu clave API almacenada en `config.py`

# 📌 Configurar API de Cohere
co = cohere.Client(COHERE_API_KEY)

# 📌 Pregunta de prueba
pregunta = "¿Cómo configuro una aplicación OAuth en Entra ID?"

# 📌 Tokenizar la pregunta correctamente especificando el modelo
tokens = co.tokenize(text=pregunta, model="command")

# 📌 Mostrar el número de tokens utilizados
print(f"🔍 Número de tokens en la consulta: {len(tokens.tokens)}")

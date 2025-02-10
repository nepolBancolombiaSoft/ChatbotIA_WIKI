# Proyecto IA Wiki

Este proyecto es un sistema de chatbot basado en inteligencia artificial con integración a una base de datos y una interfaz de aplicación. A continuación, se describe la estructura del proyecto y la funcionalidad de cada archivo.

## Estructura del Proyecto

```
proyectoIAwiki_extracted/
    algunos comandos.txt  # Archivo de comandos útiles o referencias
    app.py  # Archivo principal que ejecuta la aplicación
    chatbot.py  # Módulo del chatbot principal
    config.py  # Archivo de configuración de variables y credenciales
    indexa_db.py  # Script para indexar la base de datos
    requirements.txt  # Lista de dependencias necesarias para el proyecto
    sync_wiki.ps1  # Script PowerShell para sincronizar la base de datos de la wiki
    token_verifi.py  # Verificación de autenticación basada en tokens
    verificar_db.py  # Script para verificar la integridad de la base de datos
    __pycache__/  # Caché de Python
        chatbot.cpython-310.pyc  # Versión compilada de chatbot.py
        config.cpython-310.pyc  # Versión compilada de config.py
        token.cpython-310.pyc  # Versión compilada de token_verifi.py
    backup_chat/
        chatbot_bk.py  # Copia de seguridad del código del chatbot
    wiki_db/
        chroma.sqlite3  # Base de datos SQLite con el contenido de la wiki
        85ab03e3-b59c-430c-b421-c225b6e1e915/
            data_level0.bin  # Datos binarios de la base de datos
            header.bin  # Encabezado de la base de datos
            length.bin  # Longitudes de datos indexados
            link_lists.bin  # Listas de enlaces indexados
```

## Descripción de Archivos Clave

### 1. `app.py`
Este archivo es el punto de entrada de la aplicación. Se encarga de iniciar el chatbot y gestionar las interacciones con el usuario.

### 2. `chatbot.py`
Este módulo contiene la lógica principal del chatbot, incluyendo el procesamiento de mensajes, la integración con la base de datos y la generación de respuestas.

### 3. `config.py`
Archivo de configuración donde se almacenan las variables necesarias para la ejecución del proyecto, como claves API, configuraciones de conexión y parámetros globales.

### 4. `indexa_db.py`
Script que indexa la base de datos, permitiendo que la información sea buscada y recuperada de manera eficiente.

### 5. `requirements.txt`
Lista de bibliotecas y dependencias necesarias para ejecutar el proyecto. Se recomienda instalar las dependencias con:
```sh
pip install -r requirements.txt
```

### 6. `sync_wiki.ps1`
Script de PowerShell utilizado para sincronizar la base de datos de la wiki, asegurando que siempre esté actualizada.

### 7. `token_verifi.py`
Este script se encarga de la verificación de tokens para garantizar la autenticación segura de los usuarios.

### 8. `verificar_db.py`
Herramienta para verificar la integridad y estructura de la base de datos utilizada por el chatbot.

### 9. `backup_chat/chatbot_bk.py`
Copia de seguridad del chatbot principal, útil en caso de que se necesite restaurar código anterior.

### 10. `wiki_db/`
Directorio que contiene la base de datos en formato SQLite junto con archivos binarios utilizados para la indexación y almacenamiento eficiente de datos.

## Instalación y Uso

### Instalación de Dependencias
Ejecuta el siguiente comando para instalar todas las dependencias requeridas:
```sh
pip install -r requirements.txt
```

### Ejecución del Proyecto
Para iniciar la aplicación, ejecuta:
```sh
python app.py
```

Si deseas sincronizar la base de datos de la wiki manualmente, ejecuta:
```sh
powershell -ExecutionPolicy Bypass -File sync_wiki.ps1
```

## Notas Adicionales
- Asegúrate de tener Python instalado (versión 3.10 o superior recomendada).
- Si necesitas modificar las configuraciones, edita el archivo `config.py`.
- La base de datos se actualiza automáticamente al ejecutar el script de sincronización.

---

Este proyecto está en constante desarrollo. Si tienes sugerencias o encuentras algún error, no dudes en contribuir o reportarlo.


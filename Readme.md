# Proyecto IA Wiki

## Descripción

Proyecto IA Wiki es un sistema de chatbot basado en inteligencia artificial con integración a una base de datos. Su objetivo es proporcionar respuestas basadas en información indexada de una wiki, mejorando el acceso a la documentación de manera automatizada.

Este proyecto es Open Source, por lo que cualquier persona puede contribuir con mejoras y nuevas funcionalidades.

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
    backup_chat/
    wiki_db/
```

## Instalación

### 1. Requisitos Previos
- Python 3.10 o superior
- pip instalado
- PowerShell (para sincronización de la wiki en Windows)

### 2. Clonar el Repositorio
```sh
git clone https://github.com/tuusuario/proyectoIAwiki.git
cd proyectoIAwiki
```

### 3. Instalar Dependencias
```sh
pip install -r requirements.txt
```

### 4. Configurar Variables
Modifica `config.py` con tus credenciales y configuraciones necesarias.

## Uso

### Ejecutar la Aplicación
```sh
python app.py
```

### Sincronizar la Base de Datos de la Wiki
```sh
powershell -ExecutionPolicy Bypass -File sync_wiki.ps1
```

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:
1. Realiza un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y súbelos (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía un pull request para revisión.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo libremente para cualquier propósito.

## Contacto

Si tienes dudas o sugerencias, puedes abrir un issue en el repositorio o contactarme a través de [correo electrónico](polosoft1@gmail.com).


![2025-02-10_11-01](https://github.com/user-attachments/assets/76f5c53d-108a-45e0-83e9-3bc916641e66)
![2025-02-10_11-03](https://github.com/user-attachments/assets/ef09cb67-f35c-4427-950c-12a2b357359c)
![2025-02-10_11-06](https://github.com/user-attachments/assets/1fbc3a87-9343-42d2-b8d8-20ae477a44b2)
![2025-02-10_11-10](https://github.com/user-attachments/assets/817b1342-867e-4b36-a11f-952166fe4aa8)

GUI:
![imagen (1)](https://github.com/user-attachments/assets/5b4e5e82-6fe7-493b-8954-5c0dfd159fa6)
![imagen](https://github.com/user-attachments/assets/604d9cf4-31df-4327-a921-ce2067b7851f)

# Proyecto: Transcripción y Resumen de Audios/Videos con Whisper

Este proyecto permite transcribir audios o videos (incluyendo enlaces de YouTube o archivos locales) utilizando OpenAI Whisper, generando automáticamente subtítulos en formato `.ass` y facilitando la creación de resúmenes mediante un sistema de prompts.

## Características principales

- Transcripción automática de archivos de audio y video usando modelos Whisper de diferentes tamaños.
- Soporte para múltiples formatos: mp3, mp4, mpga, m4a, wav, webm, mpeg.
- Descarga directa desde YouTube (solo necesitas pegar el enlace).
- Generación de subtítulos en formato `.ass` editable.
- Edición/traducción manual de la transcripción antes de crear los subtítulos finales.
- Integración con prompts de resumen: tras la transcripción, puedes enviar el texto a un sistema de generación de resúmenes para obtener un análisis del contenido.

## Instalación

1. Clona el repositorio y accede a la carpeta.
2. Instala las dependencias necesarias: torch, openai-whisper, yt-dlp, pyperclip.
3. (Opcional) Crea una carpeta llamada `modelos` para almacenar los modelos descargados de Whisper y evitar descargas repetidas.

## Uso

1. Ejecuta el script principal: `python voz.py`
2. Selecciona la fuente: puedes ingresar la URL de un video de YouTube o la ruta de un archivo local.
3. Elige el idioma (automático o manual).
4. Se realiza la transcripción automática.
5. Opcional: puedes editar y/o traducir la transcripción antes de generar los subtítulos.
6. Se generan subtítulos en formato `.ass`.
7. Opcional: puedes enviar la transcripción a un sistema de resumen vía prompt personalizado.

## Flujo de trabajo

- Transcribe automáticamente el audio de un video de YouTube o de un archivo local.
- Permite edición manual del texto antes de generar los subtítulos.
- Genera subtítulos `.ass` para el video.
- Permite obtener un resumen utilizando el prompt incluido.

## Estructura del código

- `transcriptor.py`: Script principal que gestiona todo el flujo (descarga, transcripción, generación de subtítulos y gestión de resúmenes).
- `prompts/resumenes_youtube.py`: Funciones de apoyo para crear prompts de resumen (personalizable).

## Ventajas

- Ahorra tiempo en la transcripción y generación de subtítulos.
- Facilita la generación de resúmenes para estudios, actas o análisis.
- Admite traducción manual previa a la generación de subtítulos.

## Créditos

- OpenAI Whisper
- yt-dlp
- PyTorch

---

Desarrollado por Erick Pinargote

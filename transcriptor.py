import os
import re
import warnings
import importlib
import time
import json

warnings.filterwarnings("ignore")

tamano_modelo = ["tiny", "base", "small", "medium", "large","large-v3", "large-v3-turbo"]
YOUTUBE_REGEX = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$')
ALLOWED_EXTENSIONS = {'.mp3', '.mp4', '.mpga', '.m4a', '.wav', '.webm', '.mpeg'}

def cargar_modelo(tamano=tamano_modelo[-1]):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_path = f'modelos/whisper_{tamano}.pt'
    if os.path.exists(model_path):
        from whisper.model import Whisper
        torch.serialization.add_safe_globals([Whisper])
        model = torch.load(model_path, map_location=device, weights_only=False)
    else:
        model = whisper.load_model(tamano, device=device)
        torch.save(model, model_path)
    return model, device

def transcribir_audio(modelo, audio_path, language_code=None):
    try:
        if language_code:
            result = modelo.transcribe(audio_path, language=language_code)
        else:
            result = modelo.transcribe(audio_path)
    except Exception as e:
        raise RuntimeError(f"Error transcribiendo el audio: {e}")
    return result

def descargar_audio_youtube(url, audio_name='audio'):
    if not url:
        raise ValueError("No se ha proporcionado una URL de YouTube")
    print("Descargando video de YouTube...", end='', flush=True)
    t0 = time.time()
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{audio_name}.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        raise RuntimeError(f"Error descargando el audio: {e}")
    download_time = time.time() - t0
    print(f"\r\033[Video descargado en {download_time:.2f}s")
    return True

def is_youtube_url(src: str) -> bool:
    return bool(YOUTUBE_REGEX.match(src))

def check_audio_file(src: str):
    if not os.path.isfile(src):
        raise FileNotFoundError(f"El fichero no existe: {src}")
    ext = os.path.splitext(src)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Formato no soportado ({ext}). Whisper admite: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        )

def transcribir(source: str,
                modelo_size: str = tamano_modelo[-1],
                delete_audio: bool = True,
                idioma: str = None):
    if is_youtube_url(source):
        print("🔗 Fuente detectada: URL de YouTube")
        descargar_audio_youtube(source, audio_name='audio_youtube')
        audio_path = 'audio_youtube.mp3'
    else:
        print("💾 Fuente detectada: fichero local")
        check_audio_file(source)
        audio_path = source

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Cargando modelo Whisper '{modelo_size}' en {device}...", end='', flush=True)
    t1 = time.time()
    model, device = cargar_modelo(modelo_size)
    load_time = time.time() - t1
    print(f"\r\033[KModelo '{modelo_size}' cargado desde 'modelos/whisper_{modelo_size}.pt' en {device} en {load_time:.2f}s")

    print("Transcribiendo audio...", end='', flush=True)
    t2 = time.time()
    if idioma:
        result = model.transcribe(audio_path, language=idioma)
    else:
        result = model.transcribe(audio_path)
    trans_time = time.time() - t2
    print(f"\r\033[KTranscripción completa en {trans_time:.2f}s")

    # Mostrar idioma detectado
    idioma_detectado = result.get("language", "desconocido")
    print(f"Idioma detectado: {idioma_detectado}")

    if is_youtube_url(source) and delete_audio:
        os.remove(audio_path)
        print(f"Audio temporal '{audio_path}' eliminado")

    return result

def guardar_ass(segments, archivo_path='transcripcion.ass'):
    header = """[Script Info]
ScriptType: v4.00+
Collisions: Normal
PlayResY: 600
PlayDepth: 0
Timer: 100.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,20,&H00FFFFFF,&H0000FFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    def format_time(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        cs = int((seconds - int(seconds)) * 100)
        return f"{h:01d}:{m:02d}:{s:02d}.{cs:02d}"
    with open(archivo_path, 'w', encoding='utf-8') as f:
        f.write(header)
        for segment in segments:
            f.write(f"Dialogue: 0,{format_time(segment['start'])},{format_time(segment['end'])},Default,,0,0,0,,{segment['text'].strip()}\n")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Cargando librerías...", end='', flush=True)
        t_lib = time.time()
        globals()['whisper']   = importlib.import_module('whisper')
        globals()['WriteVTT']  = importlib.import_module('whisper.utils').WriteVTT
        globals()['torch']     = importlib.import_module('torch')
        globals()['yt_dlp']    = importlib.import_module('yt_dlp')
        lib_time = time.time() - t_lib
        print(f"\r\033[KLibrerías cargadas en {lib_time:.2f}s")

        source = input("Ingrese valor de SOURCE (URL de YouTube o ruta local) (vacío para salir): ").strip()
        if not source:
            print("Programa finalizado.")
            break

        idioma = input(
            "Indique el idioma del audio (por ejemplo, 'he' para hebreo). Deje vacío para detección automática: "
        ).strip().lower()
        if idioma == "":
            idioma = None

        try:
            result = transcribir(source=source, idioma=idioma)
            if result is not None:
                subtitulos = input("¿Desea generar un archivo de subtítulos (.ass) después de editar/traducir el texto? (s/n): ").strip().lower()
                if subtitulos == 's':
                    with open('transcripcion.txt', 'w', encoding='utf-8') as f:
                        f.write('\n'.join([segment['text'].strip() for segment in result['segments']]))
                    with open('segments.json', 'w', encoding='utf-8') as f:
                        json.dump(result['segments'], f, ensure_ascii=False, indent=2)
                    print("Transcripción guardada como 'transcripcion.txt'. Traduce o edita ese archivo, luego escribe 'listo' para continuar.")
                    while True:
                        listo = input("> ").strip().lower()
                        if listo == 'listo':
                            # Leer líneas traducidas/editadas y los segmentos originales (¡ahora sí es seguro!)
                            try:
                                with open('transcripcion.txt', 'r', encoding='utf-8') as f:
                                    nuevas_lineas = f.readlines()
                                break
                            except Exception as e:
                                print("No se pudo leer el archivo, asegúrate de que está guardado y cerrado. Intenta de nuevo.")
                                continue
                    with open('transcripcion.txt', 'r', encoding='utf-8') as f:
                        nuevas_lineas = f.readlines()
                    with open('segments.json', 'r', encoding='utf-8') as f:
                        segments = json.load(f)
                    for i, segment in enumerate(segments):
                        if i < len(nuevas_lineas):
                            segment['text'] = nuevas_lineas[i].strip()
                        else:
                            segment['text'] = ''
                    guardar_ass(segments, 'transcripcion.ass')
                    print("Archivo de subtítulos .ass generado como 'transcripcion.ass'.")
                    os.remove('transcripcion.txt')
                    os.remove('segments.json')
                    print("Archivos temporales eliminados. Solo queda 'transcripcion.ass'.")
                resumen = input("¿Desea incluir el prompt de resumen de la transcripción? (s/n/none): ").strip().lower()
                if resumen == 'n':
                    try:
                        import pyperclip
                        pyperclip.copy(result['text'])
                        print("Transcripción copiada al portapapeles.")
                    except ImportError:
                        print("Aviso: no se pudo copiar al portapapeles (pyperclip no instalado).")
                if resumen == 's':
                    from prompts.resumenes_youtube import fill_prompt
                    fill_prompt(texto=result['text'],nivel="Normal", tipo_texto="Transcripción de discurso", formato="Estructura con encabezados", proposito="Tomar decisiones", tono="Objetivo")
                if resumen == 'none':
                    pass
        except Exception as e:
            print(f"Error: {e}")

        input("Presione Enter para continuar...")


#!/usr/bin/env python3

"""
Archivo: generar_prompt_guion.py
Descripción: Solicita al usuario los campos necesarios para generar un prompt de guión viral siguiendo una metodología rigurosa.
"""

def main():
    # Solicitar cada campo al usuario
    tema = input("Tema (Describe brevemente el tema central del video): ")
    duracion = input("Duración total (segundos): ")
    audiencia = input("Audiencia objetivo: ")
    objetivo = input("Objetivo principal (Viralizar / Educar / Vender / Generar leads): ")
    tono = input("Tono y estilo (p.e. dinámico y desenfadado; profesional y serio): ")

    # Construir el prompt completo
    prompt = f'''Actúa como un guionista experto en contenido viral y persuasivo para video y aplica esta metodología rigurosa al tema que te proporcione. Genera un guión listo para grabar, dividido en bloques numerados con marcas de tiempo (en segundos), texto para locución, sugerencias de texto en pantalla y notas visuales. Sigue estas instrucciones:

1. Parámetros de entrada:
   - Tema: {tema}
   - Duración total: {duracion}
   - Audiencia objetivo: {audiencia}
   - Objetivo principal: {objetivo}
   - Tono y estilo: {tono}

2. Estructura del guión:
   A. **0–1 s: Rompe el patrón**
      - Acción disruptiva o visual inesperada (p. ej. “(zoom out súbito)”, “(personaje lanza confeti)”)  
   B. **1–5 s: Gancho e intriga inmediata**
      - Frase negativa o promesa de beneficio claro (“Esto podría arruinar tu estrategia si no…” / “Descubrirás el secreto para…”)  
      - Texto en pantalla sugerido: [“¿Por qué fallas?”]
   C. **5–20 s: Doble Caída – Primera fase**
      1. Problema 1: Presenta el reto inicial  
      2. Solución 1: Responde brevemente al problema  
      - Inserta un micro-hook al final (“¿Sabes por qué funciona?”)
   D. **20–40 s: Doble Caída – Segunda fase**
      3. Problema 2 (caída mayor): Revela un obstáculo más grande  
      4. Solución definitiva: Cierra con la respuesta que resuelve todo  
      - Incluye otro micro-hook si la duración lo permite
   E. **40–{duracion} s: Cierre y llamada a la acción**
      - Refuerzo final del beneficio (“Ahora tendrás…”), llamado a la acción (“Dale like y comparte para…”)  

3. Tácticas ocultas a aplicar en todo momento:
   - **Micro-hooks** entre fases: pequeñas preguntas o suspensos.
   - **Zoom in en descripciones**: detalles emocionales (“Yo sentí cómo…”).
   - **“Tú” invisible**: dirige cada línea al espectador (“tú vas a…”).
   - **Textos en pantalla**: sugerencias de palabras clave en mayúsculas.

4. Formato de salida:
   - Texto plano, sin formato Markdown aparte de la numeración.
   - Cada bloque debe iniciarse con el rango de segundos y un título breve.
   - Incluye, entre paréntesis, las indicaciones visuales y de texto en pantalla.

**Ejemplo de invocación al prompt:**
Tema: “Cómo mejorar tu marca personal en LinkedIn”  
Duración total: 60  
Audiencia objetivo: “Profesionales entre 25–40 años, aspirantes a líderes de opinión”  
Objetivo: “Educar y fomentar interacciones”  
Tono: “Profesional pero cercano”  

Ahora, genérame el guión completo según este esquema.'''

    # Mostrar el prompt generado
    print("\nPrompt generado:\n")
    print(prompt)

if __name__ == "__main__":
    main()

import pyperclip

def fill_prompt(texto,nivel="Normal", tipo_texto="Transcripción de discurso", formato="Viñetas", proposito="Tomar decisiones", tono="Objetivo"):
    prompt = """Compórtate como un **experto resumiendo textos**, con amplia experiencia en análisis y síntesis de documentos. Tu tarea será leer y resumir un texto que te proporcionaré, **adaptando el resumen a mis necesidades específicas** según los parámetros que te indicaré. 

**Instrucciones Generales:** Lee cuidadosamente el texto completo y luego elabora un resumen fiel y claro, **sin omitir ideas importantes ni agregar contenido que no esté en el texto original**. Cumple todos los requisitos que te especifique a continuación.

**Parámetros del Resumen (personalizables por el usuario):**

1. **Nivel de resumen:** _{Muy corto | Corto | Normal | Largo | Muy largo}_. Indica la extensión y nivel de detalle deseado en el resumen. 
   - *Muy corto*: solo las conclusiones o ideas centrales más importantes, en una o dos frases breves. 
   - *Corto*: conclusiones clave más 1 o 2 insights esenciales del texto, en unas pocas frases.
   - *Normal*: resumen estándar con introducción del tema, desarrollo de las ideas principales y conclusión final.
   - *Largo*: incluye mayor detalle del desarrollo del texto, abarcando más puntos secundarios sin perder el hilo principal.
   - *Muy largo*: un resumen muy detallado, casi una paráfrasis condensada que refleja prácticamente todo el contenido importante del texto fuente.

2. **Tipo de texto:** _{Literario | Académico | Técnico | Ensayo | Artículo periodístico | ...}_ Especifica la naturaleza del texto original para adaptar el estilo del resumen. Por ejemplo, “literario” (si es una novela o cuento), “académico” (artículo científico o informe), “técnico” (manual, documentación especializada), “ensayo” (argumentativo) o “periodístico” (noticia/reportaje). *Adapta el resumen a las convenciones de ese tipo de texto*. 

3. **Formato deseado:** _{Viñetas | Narrativo continuo | Estructura con encabezados | ...}_ Define cómo se presentará el resumen. Puede ser en viñetas (lista de puntos clave), en un párrafo narrativo continuo, o con secciones y encabezados (ejemplo: “Introducción / Desarrollo / Conclusión”). Elige el formato que prefieras para el resultado.

4. **Propósito del resumen:** _{Estudiar | Divulgar | Tomar decisiones | Enseñar | ...}_ Indica para qué necesitas el resumen. Según el propósito, enfocaré el contenido: si es para *estudiar*, incluiré definiciones clave y estructura clara; si es para *divulgar*, usaré lenguaje accesible y me centraré en lo más entendible; si es para *tomar decisiones*, resaltaré datos concretos y conclusiones prácticas; si es para *enseñar*, adoptaré un tono pedagógico y orden lógico que facilite la comprensión.

5. **Tono:** _{Objetivo | Persuasivo | Pedagógico | Informal | Técnico | ...}_ Especifica el estilo tonal del resumen. Por ejemplo, objetivo (neutral y sin opinión), persuasivo (resaltando argumentos convincentes), pedagógico (explicativo y sencillo), informal (coloquial) o técnico (especializado y preciso). Ajustaré la redacción del resumen para reflejar el tono solicitado, manteniendo siempre la fidelidad al texto original.

**Proceso:** 
- Primero **analizaré la estructura** del texto original (introducción, desarrollo, conclusión) e identificaré sus ideas principales, argumentos o eventos clave. 
- Luego **eliminaré detalles irrelevantes, redundancias o ejemplos secundarios**, quedándome solo con lo más importante. 
- **Escribiré el resumen** adaptándome al *nivel*, *formato*, *propósito* y *tono* indicados arriba. El resumen será coherente, bien organizado y sin desviaciones del contenido proporcionado. 
- Si el texto tiene una conclusión o mensaje final explícito, lo incluiré destacándolo; si no, deduciré una conclusión implícita que englobe el sentido global del texto. 
- **No añadiré opiniones personales ni información externa** no contenida en el texto fuente. Me ceñiré a reformular y sintetizar las ideas del autor original. 

A continuación, te proporcionaré el texto original delimitado por triple comillas invertidas ``` para que lo proceses. **Después del texto, indicaré los parámetros específicos que deseo para el resumen.** Con toda esa información, generarás el resumen solicitado.

**Ejemplos (modo de uso):**

_Ejemplo 1:_ Resumen **corto** de un **artículo periodístico** en **formato de viñetas**, con **propósito de divulgar** y **tono objetivo**.

Texto original: 
La ciudad de Alfa sufrió ayer una intensa tormenta que provocó inundaciones en varios barrios. Las autoridades reportaron daños materiales significativos, aunque afortunadamente no hubo víctimas. Los servicios de emergencia trabajaron durante la noche para restablecer el suministro eléctrico y ayudar a los afectados.
Parámetros solicitados: Nivel de resumen = **Corto**; Tipo de texto = **Artículo periodístico**; Formato = **Viñetas**; Propósito = **Divulgar**; Tono = **Objetivo**.

Resumen resultante:
- Una tormenta intensa causó **inundaciones y daños materiales** en la ciudad de Alfa, afectando a varios barrios.  
- **No se registraron víctimas** fatales, según las autoridades, y los equipos de emergencia trabajan para restablecer servicios básicos (como la electricidad) y asistir a los vecinos damnificados.

_Ejemplo 2:_ Resumen **largo** de un texto **académico** en **formato con encabezados**, con **propósito de estudiar** y **tono pedagógico**.

Texto original: 
Investigadores de la Universidad Beta analizaron los efectos de la cafeína en la memoria a corto plazo. En un experimento con 100 voluntarios, un grupo consumió una dosis de cafeína y otro recibió un placebo. Los resultados mostraron una mejora significativa en la retención de información en el grupo que ingirió cafeína, lo que sugiere que esta sustancia podría potenciar temporalmente la memoria. Sin embargo, los autores señalaron que el efecto fue transitorio y recomendaron realizar más estudios para evaluar sus implicaciones a largo plazo.
Parámetros solicitados: Nivel de resumen = **Largo**; Tipo de texto = **Académico**; Formato = **Estructura con encabezados**; Propósito = **Estudiar**; Tono = **Pedagógico**.

Resumen resultante:

**Introducción:** Un estudio de la Univ. Beta examinó **el impacto de la cafeína en la memoria de corto plazo** en adultos. El objetivo era determinar si la cafeína mejora la retención de información.

**Desarrollo (Metodología y Resultados):** Se llevó a cabo un experimento con *100 voluntarios* divididos en dos grupos: uno consumió cafeína y otro un placebo. El grupo con cafeína mostró **mejoras significativas en la retención de información** frente al grupo placebo. Este resultado indica que la cafeína *podría* **potenciar temporalmente la memoria** a corto plazo en las personas.

**Conclusión:** Aunque la cafeína mejoró la memoria en el experimento, **el efecto fue transitorio**. Los investigadores concluyen que se necesitan estudios adicionales para comprender la duración del efecto y sus posibles implicaciones a largo plazo, especialmente antes de recomendar su uso con fines de mejora cognitiva.

*(*En el ejemplo anterior, se ofreció un resumen detallado con una estructura clara para facilitar su uso como material de estudio.*)*

**[FIN de los ejemplos]**
"""
    # Reemplazar los marcadores de parámetros
    prompt = prompt.replace("{Muy corto | Corto | Normal | Largo | Muy largo}", nivel)
    prompt = prompt.replace("{Literario | Académico | Técnico | Ensayo | Artículo periodístico | ...}", tipo_texto)
    prompt = prompt.replace("{Viñetas | Narrativo continuo | Estructura con encabezados | ...}", formato)
    prompt = prompt.replace("{Estudiar | Divulgar | Tomar decisiones | Enseñar | ...}", proposito)
    prompt = prompt.replace("{Objetivo | Persuasivo | Pedagógico | Informal | Técnico | ...}", tono)

    # Insertar el texto a resumir y los parámetros al final
    prompt += (
        "\nTexto original:\n"
        f"```{texto}```\n\n"
        "Parámetros solicitados: "
        f"Nivel de resumen = **{nivel}**; "
        f"Tipo de texto = **{tipo_texto}**; "
        f"Formato = **{formato}**; "
        f"Propósito = **{proposito}**; "
        f"Tono = **{tono}**."
    )

    # Copiar al portapapeles
    pyperclip.copy(prompt)

# Ejemplo de uso:
if __name__ == "__main__":
    texto_externo=input("Introduce el texto completo que deseas resumir: ")
    fill_prompt(
        nivel="Normal",
        tipo_texto="Transcripción de discurso",
        formato="Viñetas",
        proposito="Tomar decisiones",
        tono="Objetivo",
        texto=texto_externo
    )
    print("Prompt completo copiado al portapapeles.")

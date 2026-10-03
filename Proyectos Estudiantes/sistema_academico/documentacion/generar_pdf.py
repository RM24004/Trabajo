#!/usr/bin/env python
# -*- coding: ascii -*-
"""
Generador del PDF de documentacion del Sistema Academico.

Lee todos los archivos del proyecto y los compila en un PDF que contiene:
portada, requisitos, guia paso a paso, estructura del proyecto, ejemplo de
los archivos JSON, tabla de permisos y el codigo completo de cada archivo.

Todo el texto del documento esta en ASCII puro (sin tildes ni letra n con
tilde) para evitar problemas de codificacion al generar el PDF.
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE, "documentacion", "Sistema_Academico_Documentacion.pdf")

# Orden en el que se crean los archivos (sigue las dependencias de importacion)
ARCHIVOS = [
    ("config.py", "Configuracion global",
     "Rutas absolutas de los cuatro archivos JSON y constantes de validacion. "
     "Es el unico lugar donde hay que cambiar rutas si el proyecto se mueve."),
    ("nucleo/__init__.py", "Paquete nucleo (vacio)",
     "Marca la carpeta como paquete de Python. No lleva codigo."),
    ("nucleo/seguridad.py", "Seguridad de contrasenas",
     "Genera la sal, calcula el hash PBKDF2-SHA256 y compara contrasenas en "
     "tiempo constante. Las contrasenas nunca se guardan en texto plano."),
    ("nucleo/almacen.py", "Almacenamiento en archivos JSON",
     "Lee y escribe listas de diccionarios en archivos JSON. La escritura es "
     "atomica: primero escribe en un archivo temporal y despues lo renombra, "
     "para que un corte de luz no deje el JSON a medias."),
    ("nucleo/servicios.py", "Reglas de negocio y permisos",
     "El corazon del programa. Valida los datos, controla que cada rol solo "
     "pueda hacer lo que le corresponde, genera los identificadores, calcula "
     "promedios y resuelve los borrados en cascada."),
    ("interfaz/__init__.py", "Paquete interfaz (vacio)",
     "Marca la carpeta como paquete de Python. No lleva codigo."),
    ("interfaz/estilos.py", "Tema visual",
     "Define los colores y los estilos de ttk (botones, tablas, etiquetas, "
     "pestanas). Todo el aspecto de la aplicacion sale de aqui."),
    ("interfaz/widgets.py", "Componentes reutilizables",
     "Clases que se usan en todos los formularios: CampoTexto, CampoSeleccion, "
     "Tabla y TarjetaEstadistica. Evita repetir codigo en cada pantalla."),
    ("interfaz/vista_login.py", "Pantalla de inicio de sesion",
     "Tarjeta centrada con el formulario de usuario y contrasena. Valida las "
     "credenciales y decide que panel abrir segun el rol."),
    ("interfaz/dialogos.py", "Formularios (ventanas emergent)",
     "Las cuatro ventanas de formulario: estudiante, materia, nota y cambio de "
     "contrasena. Contienen la logica de alto automatico y la barra de scroll."),
    ("interfaz/vista_docente.py", "Panel del docente",
     "Tres pestanas (Estudiantes, Materias, Notas) con buscador, botones de "
     "agregar, editar y eliminar, y tarjetas con el resumen general."),
    ("interfaz/vista_estudiante.py", "Panel del estudiante",
     "Solo lectura: sus notas, el promedio por materia y su ficha personal."),
    ("principal.py", "Punto de entrada",
     "Crea la ventana principal, aplica el tema, decide que vista mostrar y "
     "maneja los errores de arranque."),
]

ESTRUCTURA = [
    "sistema_academico/",
    "|-- principal.py ................ Ventana principal y control de vistas",
    "|-- config.py ................... Rutas de los JSON y constantes",
    "|-- README.md ................... Texto de ayuda del proyecto",
    "|-- nucleo/",
    "|   |-- __init__.py ............. Paquete vacio",
    "|   |-- seguridad.py ............ Hash de contrasenas (PBKDF2 + sal)",
    "|   |-- almacen.py .............. Lectura y escritura de JSON",
    "|   `-- servicios.py ............ Reglas de negocio, validaciones, permisos",
    "|-- interfaz/",
    "|   |-- __init__.py ............. Paquete vacio",
    "|   |-- estilos.py .............. Colores y estilos de ttk",
    "|   |-- widgets.py .............. Campos de formulario, tablas, tarjetas",
    "|   |-- vista_login.py .......... Pantalla de inicio de sesion",
    "|   |-- dialogos.py ............ Formularios de estudiante, materia, nota",
    "|   |-- vista_docente.py ........ Panel completo del docente",
    "|   `-- vista_estudiante.py ..... Panel de consulta del estudiante",
    "|-- datos/",
    "|   |-- usuarios.json ........... Cuentas de acceso (docentes y alumnos)",
    "|   |-- estudiantes.json ........ Fichas de los estudiantes",
    "|   |-- materias.json ........... Materias del plan de estudios",
    "|   `-- notas.json .............. Calificaciones",
    "`-- documentacion/",
    "    `-- generar_pdf.py .......... Este generador de documentacion",
]

EXPLICACION_ESTRUCTURA = [
    ["Archivo", "Funcion dentro del sistema"],
    ["principal.py", "Arranca el programa. Crea la ventana, aplica el tema y "
                     "muestra la vista de login o el panel segun el rol."],
    ["config.py", "Define donde viven los archivos JSON y los limites validos "
                  "de notas, creditos y semestres."],
    ["nucleo/seguridad.py", "Protege las contrasenas con sal y hash PBKDF2. "
                            "Ninguna contrasena se guarda en texto plano."],
    ["nucleo/almacen.py", "Guarda y lee los datos en JSON. Si un archivo se "
                          "dania, avisa en lugar de perder la informacion."],
    ["nucleo/servicios.py", "Valida los datos y aplica las reglas. Aqui se "
                            "bloquea que un estudiante modifique calificaciones."],
    ["interfaz/estilos.py", "El tema: colores, fuentes y estilos de los "
                            "controles de Windows."],
    ["interfaz/widgets.py", "Los piezas reutilizables de los formularios."],
    ["interfaz/vista_login.py", "La pantalla donde se escribe usuario y contrasena."],
    ["interfaz/dialogos.py", "Las ventanas de formulario de estudiante, materia, "
                             "nota y cambio de contrasena."],
    ["interfaz/vista_docente.py", "El tablero de trabajo del docente."],
    ["interfaz/vista_estudiante.py", "La pantalla de consulta del alumno."],
    ["datos/*.json", "La informacion del sistema. Se puede copiar como "
                     "respaldo o abrir con cualquier editor de texto."],
]

REQUISITOS = [
    "Python 3.10 o superior (probado en 3.13).",
    "Tkinter: viene incluido con Python en Windows y macOS.",
    "En Linux puede hacer falta instalarlo aparte: sudo apt install python3-tk",
    "Libreria reportlab: solo para generar este PDF (pip install reportlab).",
    "La aplicacion NO usa base de datos. Los datos se guardan en archivos JSON.",
    "La aplicacion NO necesita instalar nada mas. No hay pip install para ella.",
]

PASOS_CONSTRUCCION = [
    "Crea la carpeta <b>sistema_academico</b> y dentro las carpetas "
    "<b>nucleo</b>, <b>interfaz</b>, <b>datos</b> y <b>documentacion</b>.",

    "Crea los archivos vacios <b>nucleo/__init__.py</b> e "
    "<b>interfaz/__init__.py</b>. Sirven para que Python reconozca las carpetas "
    "como paquetes y los imports funcionen.",

    "Crea <b>config.py</b>. Aqui se decide en que carpeta se guardan los JSON.",

    "Crea <b>nucleo/seguridad.py</b>. Debe estar antes que los demas porque "
    "servicios.py lo usa para las contrasenas.",

    "Crea <b>nucleo/almacen.py</b>. La clase AlmacenJSON es la que sabe leer y "
    "escribir un archivo de datos.",

    "Crea <b>nucleo/servicios.py</b>. Es la capa con todas las reglas: aqui se "
    "validan los datos y se comprueba el rol de quien esta usando el programa.",

    "Crea <b>interfaz/estilos.py</b>. Define el tema para que todas las "
    "pantallas se vean iguales.",

    "Crea <b>interfaz/widgets.py</b>. Los componentes que se reutilizan en "
    "todos los formularios.",

    "Crea <b>interfaz/vista_login.py</b>. La primera pantalla que ve el usuario.",

    "Crea <b>interfaz/dialogos.py</b>. Los formularios de estudiante, materia, "
    "nota y contrasena.",

    "Crea <b>interfaz/vista_docente.py</b>. El panel con las tres pestanas.",

    "Crea <b>interfaz/vista_estudiante.py</b>. El panel de solo lectura.",

    "Crea <b>principal.py</b> al final, porque es el que importa todos los "
    "modulos anteriores.",

    "Abre una terminal dentro de la carpeta sistema_academico y ejecuta: "
    "<b>python principal.py</b>",

    "Inicia sesion con el usuario <b>admin</b> y la contrasena "
    "<b>admin123</b>. Esa cuenta de docente se crea sola la primera vez.",
]

PASOS_USO_DOCENTE = [
    "Entra con <b>admin / admin123</b> (o la cuenta de docente que te den).",
    "En la pestana <b>Materias</b> pulsa <b>+ Nueva materia</b> y registra las "
    "materias: codigo, nombre, creditos y semestre.",
    "En la pestana <b>Estudiantes</b> pulsa <b>+ Nuevo estudiante</b>. Llena "
    "cedula, nombres, apellidos, email, telefono y carrera.",
    "Deja vacios <b>Usuario de acceso</b> y <b>Contrasena inicial</b> y el "
    "programa los genera. Anota los datos: se muestran una sola vez.",
    "En la pestana <b>Notas</b> pulsa <b>+ Nueva nota</b>, elige estudiante y "
    "materia, y escribe la calificacion de 0 a 100.",
    "Usa el campo <b>Buscar</b> de cada pestana para filtrar por nombre, "
    "codigo, carrera o periodo.",
    "Selecciona una fila y pulsa <b>Editar</b> o <b>Eliminar</b>. Si borras un "
    "estudiante o una materia, sus notas se borran tambien.",
    "Si un alumno pierde su clave, seleccionalo y pulsa <b>Restablecer clave</b>.",
]

PASOS_USO_ESTUDIANTE = [
    "Entra con el usuario y la contrasena que te dio el docente.",
    "Pestana <b>Todas mis notas</b>: lista completa con el estado Aprobado o "
    "Reprobado en cada fila. Se considera aprobado desde 60 puntos.",
    "Pestana <b>Por materia</b>: el promedio de cada materia y sus creditos.",
    "Pestana <b>Mi perfil</b>: cedula, carrera, email y telefono.",
    "El alumno no puede agregar, editar ni borrar nada. Solo consultar.",
]

ESTRUCTURA_JSON = [
    ("usuarios.json", [
        "[",
        "  {",
        '    "id": "USR-0001",',
        '    "nombre_usuario": "admin",',
        '    "sal": "a3f9c1b2d4e5f60718293a4b5c6d7e8f",',
        '    "clave_hash": "8c1d... (hash de la contrasena, no la contrasena)",',
        '    "rol": "docente",',
        '    "nombre": "Docente Principal",',
        '    "estudiante_id": null',
        "  },",
        "  {",
        '    "id": "USR-0002",',
        '    "nombre_usuario": "anago",',
        '    "sal": "9b2e4d7f1a3c5e8b0d2f4a6c8e0b1d3f",',
        '    "clave_hash": "4e7a... (hash de la contrasena)",',
        '    "rol": "estudiante",',
        '    "nombre": "Ana Maria Gomez",',
        '    "estudiante_id": "EST-0001"',
        "  }",
        "]",
    ]),
    ("estudiantes.json", [
        "[",
        "  {",
        '    "id": "EST-0001",',
        '    "cedula": "1-2345678-9",',
        '    "nombres": "Ana Maria",',
        '    "apellidos": "Gomez Ruiz",',
        '    "email": "ana@correo.com",',
        '    "telefono": "0991234567",',
        '    "carrera": "Ingenieria de Sistemas",',
        '    "activo": true,',
        '    "fecha_registro": "2026-10-02"',
        "  }",
        "]",
    ]),
    ("materias.json", [
        "[",
        "  {",
        '    "id": "MAT-0001",',
        '    "codigo": "MAT101",',
        '    "nombre": "Algebra Lineal",',
        '    "creditos": 4,',
        '    "semestre": 1,',
        '    "docente": "Docente Principal"',
        "  }",
        "]",
    ]),
    ("notas.json", [
        "[",
        "  {",
        '    "id": "NOT-0001",',
        '    "estudiante_id": "EST-0001",',
        '    "materia_id": "MAT-0001",',
        '    "valor": 85.0,',
        '    "tipo": "Parcial 1",',
        '    "periodo": "2026-1",',
        '    "fecha": "2026-10-02"',
        "  }",
        "]",
    ]),
]

PERMISOS = [
    ["Accion", "Docente", "Estudiante"],
    ["Ver todos los estudiantes", "Si", "No"],
    ["Ver sus propias notas", "Si", "Si"],
    ["Agregar estudiantes", "Si", "No"],
    ["Editar estudiantes", "Si", "No"],
    ["Eliminar estudiantes", "Si", "No"],
    ["Agregar materias", "Si", "No"],
    ["Editar materias", "Si", "No"],
    ["Eliminar materias", "Si", "No"],
    ["Agregar notas", "Si", "No"],
    ["Editar notas", "Si", "No"],
    ["Eliminar notas", "Si", "No"],
    ["Cambiar su propia contrasena", "Si", "Si"],
    ["Restablecer clave de un alumno", "Si", "No"],
]

ERRORES_CORREGIDOS = [
    "La tarjeta del login se dibujaba de 1 pixel de alto porque se combinaba "
    "place(relwidth) con pack_propagate(False). Se uso un alto calculado segun "
    "el contenido.",

    "El formulario de estudiante perdia 199 pixels de la parte de abajo y los "
    "botones Guardar y Cancelar ni siquiera se mostraban. La causa era que la "
    "geometria se fijaba antes de agregar los campos, y el cuerpo del dialogo "
    "absorbia todo el espacio dejando el pie en cero.",

    "Al editar una nota se perdian las referencias del estudiante y de la "
    "materia, y la nota quedaba huerfana.",

    "Las 15 llamadas a messagebox tenian el titulo y el mensaje invertidos, "
    "porque Tkinter recibe el titulo como palabra clave y no como posicion.",

    "El filtro de notas no buscaba por el codigo de la materia, solo por el "
    "nombre.",

    "Si un registro del JSON venia sin el campo docente, el programa se caia "
    "con un error de clave. Ahora los registros incompletos se saltan.",
]

# ---------------------------------------------------------------- estilos ----

header_style = ParagraphStyle(
    "Header", fontName="Helvetica-Bold", fontSize=22, leading=27,
    textColor=colors.white, alignment=TA_CENTER,
    backColor=colors.HexColor("#1f4e79"), borderPadding=14, spaceAfter=8,
)
subheader_style = ParagraphStyle(
    "Subheader", fontName="Helvetica", fontSize=12, leading=16,
    textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=12,
)
section_style = ParagraphStyle(
    "Section", fontName="Helvetica-Bold", fontSize=15, leading=19,
    textColor=colors.HexColor("#ffffff"), spaceBefore=10, spaceAfter=6,
    backColor=colors.HexColor("#1f4e79"), borderPadding=8,
)
desc_style = ParagraphStyle(
    "Desc", fontName="Helvetica-Oblique", fontSize=10, leading=14,
    textColor=colors.HexColor("#444444"), spaceAfter=8, alignment=TA_LEFT,
)
inner_style = ParagraphStyle(
    "Inner", fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=colors.black, spaceAfter=7, alignment=TA_LEFT,
)
toc_style = ParagraphStyle(
    "Toc", fontName="Helvetica-Bold", fontSize=13, leading=17,
    textColor=colors.HexColor("#1f4e79"), spaceBefore=6, spaceAfter=8,
)
path_style = ParagraphStyle(
    "Path", fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=colors.HexColor("#2e6da4"), spaceAfter=3,
)
code_style = ParagraphStyle(
    "Code", fontName="Courier", fontSize=6.6, leading=8.4,
    textColor=colors.black, leftIndent=0, spaceAfter=0,
)
nota_style = ParagraphStyle(
    "Nota", fontName="Helvetica-Oblique", fontSize=9, leading=12,
    textColor=colors.HexColor("#777777"), alignment=TA_CENTER,
)
finish_style = ParagraphStyle(
    "Finish", fontName="Helvetica-Bold", fontSize=19, leading=25,
    textColor=colors.white, alignment=TA_CENTER,
    backColor=colors.HexColor("#1e7e34"), borderPadding=16, spaceBefore=90,
)
celda_style = ParagraphStyle(
    "Celda", fontName="Helvetica", fontSize=9, leading=12, textColor=colors.black,
)
celda_negrita = ParagraphStyle(
    "CeldaB", fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=colors.HexColor("#1f4e79"),
)


def esc(texto):
    return (str(texto).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace("\n", "<br/>"))


def a_ascii(texto):
    """Convierte cualquier caracter no ASCII a su equivalente o lo elimina."""
    if isinstance(texto, bytes):
        texto = texto.decode("utf-8", "replace")
    texto = texto.replace("\u2019", "'").replace("\u2018", "'")
    texto = texto.replace("\u201c", '"').replace("\u201d", '"')
    texto = texto.replace("\u2013", "-").replace("\u2014", "-")
    texto = texto.replace("\u00a1", "!").replace("\u00bf", "?")
    return "".join(c if ord(c) < 128 else "?" for c in texto)


def bloque_codigo(lineas, etiqueta=None):
    """Devuelve una tabla con lineas de codigo, dividida en bloques pequenos."""
    elementos = []
    TOTAL = 60
    for inicio in range(0, len(lineas), TOTAL):
        trozo = lineas[inicio:inicio + TOTAL]
        filas = []
        if len(lineas) > TOTAL and etiqueta:
            filas.append(Paragraph(
                f"{esc(etiqueta)} - lineas {inicio + 1} a {min(inicio + TOTAL, len(lineas))} "
                f"de {len(lineas)}",
                ParagraphStyle("Cont", fontName="Helvetica", fontSize=7, leading=9,
                               textColor=colors.HexColor("#999999"))))
        filas.append(Paragraph(esc("\n".join(trozo)), code_style))
        tabla = Table([filas], colWidths=[7.3 * inch])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f7f8fa")),
            ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#c8d0d8")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        elementos.append(tabla)
        elementos.append(Spacer(1, 7))
    return elementos


def tabla_datos(datos, anchos, estilo_cabecera=True):
    filas = []
    for indice, fila in enumerate(datos):
        celdas = []
        for celda in fila:
            if indice == 0 and estilo_cabecera:
                celdas.append(Paragraph(f"<b>{esc(celda)}</b>", celda_negrita))
            else:
                celdas.append(Paragraph(esc(celda), celda_style))
        filas.append(celdas)
    tabla = Table(filas, colWidths=anchos, repeatRows=1 if estilo_cabecera else 0)
    estilo = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#ccd4dc")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if estilo_cabecera:
        estilo.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f0f8")))
        estilo.append(("ROWBACKGROUNDS", (0, 1), (-1, -1),
                       [colors.white, colors.HexColor("#f7f8fa")]))
    tabla.setStyle(TableStyle(estilo))
    return tabla


def pie_de_pagina(canvas, documento):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(letter[0] / 2.0, 0.35 * inch,
                             "Sistema Academico  -  Documentacion completa  -  Pagina %d"
                             % documento.page)
    canvas.setStrokeColor(colors.HexColor("#cccccc"))
    canvas.line(0.6 * inch, 0.52 * inch, letter[0] - 0.6 * inch, 0.52 * inch)
    canvas.restoreState()


def construir():
    documento = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
        topMargin=0.6 * inch, bottomMargin=0.75 * inch,
        title="Sistema Academico - Documentacion Completa del Codigo",
        author="Sistema Academico",
    )
    historia = []

    # ------------------------------------------------------------ portada ----
    historia.append(Spacer(1, 1.1 * inch))
    historia.append(Paragraph("SISTEMA ACADEMICO", header_style))
    historia.append(Paragraph(
        "Gestion de estudiantes, materias y notas - Documentacion completa "
        "del codigo fuente", subheader_style))
    historia.append(Spacer(1, 0.2 * inch))

    historia.append(Paragraph("1. QUE HACE ESTE SISTEMA", toc_style))
    historia.append(Paragraph(esc(a_ascii(
        "Aplicacion de escritorio escrita en Python para llevar el control de "
        "alumnos, materias y calificaciones de una institucion educativa. "
        "Tiene dos tipos de usuario: el docente, que registra y modifica todo, "
        "y el estudiante, que unicamente consulta sus propias notas. "
        "No usa base de datos: toda la informacion se guarda en archivos JSON "
        "dentro de la carpeta datos.")), inner_style))

    historia.append(Spacer(1, 0.15 * inch))
    historia.append(Paragraph("2. REQUISITOS", toc_style))
    for requisito in REQUISITOS:
        historia.append(Paragraph(f"- {esc(a_ascii(requisito))}", inner_style))

    historia.append(Spacer(1, 0.15 * inch))
    historia.append(Paragraph("3. COMO EJECUTARLO", toc_style))
    historia.append(Paragraph(esc(a_ascii(
        "1) Abre la carpeta sistema_academico.<br/>"
        "2) Abre una terminal (CMD o PowerShell) en esa carpeta.<br/>"
        "3) Escribe: <b>python principal.py</b><br/>"
        "4) Inicia sesion con <b>admin</b> / <b>admin123</b>.")), inner_style))

    historia.append(Spacer(1, 0.2 * inch))
    historia.append(Paragraph(
        esc(a_ascii("En este documento el codigo aparece en el ORDEN EXACTO en "
                    "el que se debe crear cada archivo. Empieza por config.py y "
                    "termina en principal.py.")), nota_style))
    historia.append(PageBreak())

    # ------------------------------------------------------ paso a paso -----
    historia.append(Paragraph("4. GUIA PASO A PASO PARA CONSTRUIR EL PROYECTO",
                              section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Sigue estos pasos en orden. Cada archivo depende del anterior, por eso "
        "importarlos en desorden produce error de modulo no encontrado.")),
        desc_style))
    for indice, paso in enumerate(PASOS_CONSTRUCCION, start=1):
        historia.append(Paragraph(f"<b>{indice}.</b> {esc(a_ascii(paso))}", inner_style))
    historia.append(PageBreak())

    historia.append(Paragraph("5. ESTRUCTURA DEL PROYECTO", section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Este es el arbol de carpetas y archivos del proyecto terminado:")),
        desc_style))
    historia.extend(bloque_codigo(ESTRUCTURA, "ESTRUCTURA"))
    historia.append(Spacer(1, 0.1 * inch))

    historia.append(Paragraph("Que hace cada archivo", toc_style))
    historia.append(tabla_datos(EXPLICACION_ESTRUCTURA, [1.9 * inch, 5.4 * inch]))
    historia.append(PageBreak())

    # ------------------------------------------------------ flujo de uso ----
    historia.append(Paragraph("6. PASO A PASO DE USO", section_style))
    historia.append(Paragraph("6.1 El docente", toc_style))
    for paso in PASOS_USO_DOCENTE:
        historia.append(Paragraph(f"- {esc(a_ascii(paso))}", inner_style))

    historia.append(Spacer(1, 0.15 * inch))
    historia.append(Paragraph("6.2 El estudiante", toc_style))
    for paso in PASOS_USO_ESTUDIANTE:
        historia.append(Paragraph(f"- {esc(a_ascii(paso))}", inner_style))
    historia.append(PageBreak())

    # ------------------------------------------------------ permisos --------
    historia.append(Paragraph("7. ROLES Y PERMISOS", section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Esta regla no depende de que el boton este oculto: la comprobacion "
        "esta en nucleo/servicios.py, asi que ningun estudiante puede modificar "
        "calificaciones aunque se llame al metodo directamente.")), desc_style))
    historia.append(tabla_datos(PERMISOS, [4.3 * inch, 1.5 * inch, 1.5 * inch]))
    historia.append(PageBreak())

    # ------------------------------------------------------ json ------------
    historia.append(Paragraph("8. ESTRUCTURA DE LOS ARCHIVOS JSON", section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Cada archivo JSON es una lista de objetos. El campo id sirve para "
        "enlazar los datos: la nota guarda el id del estudiante y el id de la "
        "materia. Para respaldar el sistema solo hay que copiar la carpeta "
        "datos.")), desc_style))
    for nombre, lineas in ESTRUCTURA_JSON:
        historia.append(Paragraph(f"{esc(nombre)}", toc_style))
        historia.extend(bloque_codigo(lineas, nombre.upper()))
        historia.append(Spacer(1, 0.08 * inch))
    historia.append(PageBreak())

    # ------------------------------------------------------ errores ---------
    historia.append(Paragraph("9. ERRORES CORREGIDOS DURANTE EL DESARROLLO", section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Se documentan porque explican por que el codigo esta escrito de "
        "cierta manera y son los errores mas comunes al hacer un formulario "
        "con Tkinter.")), desc_style))
    for indice, error in enumerate(ERRORES_CORREGIDOS, start=1):
        historia.append(Paragraph(f"<b>{indice}.</b> {esc(a_ascii(error))}", inner_style))
    historia.append(PageBreak())

    # ------------------------------------------------------ codigo ----------
    historia.append(Paragraph("10. CODIGO COMPLETO DE CADA ARCHIVO", section_style))
    historia.append(Paragraph(esc(a_ascii(
        "Cada archivo se explica y luego se muestra su contenido integro. "
        "Copia el bloque dentro de un archivo con el mismo nombre y la misma "
        "carpeta.")), desc_style))

    for indice, (relpath, titulo, descripcion) in enumerate(ARCHIVOS, start=1):
        completa = os.path.join(BASE, relpath.replace("/", os.sep))
        historia.append(Spacer(1, 0.12 * inch))
        historia.append(Paragraph(f"10.{indice}  {esc(a_ascii(titulo))}", toc_style))
        historia.append(Paragraph(f"<b>Ruta:</b> sistema_academico/{esc(relpath)}",
                                  path_style))
        historia.append(Paragraph(esc(a_ascii(descripcion)), desc_style))

        if not os.path.exists(completa):
            historia.append(Paragraph("(archivo vacio de proposito)", nota_style))
            continue

        with open(completa, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        lineas = contenido.replace("\t", "    ").splitlines()
        if not lineas:
            historia.append(Paragraph("(archivo vacio de proposito)", nota_style))
            continue

        historia.append(Paragraph(
            f"<b>{len(lineas)} lineas</b>", path_style))
        historia.extend(bloque_codigo(lineas, os.path.basename(relpath).upper()))

    # ------------------------------------------------------------- fin ------
    historia.append(PageBreak())
    historia.append(Paragraph("FIN DEL PROYECTO", finish_style))
    historia.append(Spacer(1, 0.25 * inch))
    historia.append(Paragraph(esc(a_ascii(
        "Recorriste el Sistema Academico completo: la estructura, la guia paso "
        "a paso, los permisos por rol y el codigo de los "
        "13 archivos del proyecto. Para ponerlo en marcha sigue el punto 3 de "
        "la portada.")), subheader_style))
    historia.append(Spacer(1, 0.3 * inch))
    historia.append(Paragraph(esc(a_ascii(
        "Python + Tkinter + archivos JSON. Sin base de datos y sin instalar "
        "librerias para que la aplicacion funcione.")), nota_style))

    documento.build(historia, onFirstPage=pie_de_pagina, onLaterPages=pie_de_pagina)
    print("PDF generado:", OUTPUT)
    print("Archivos incluidos:", len(ARCHIVOS))


if __name__ == "__main__":
    construir()
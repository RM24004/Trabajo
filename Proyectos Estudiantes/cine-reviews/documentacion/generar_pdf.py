#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de PDF de documentacion del proyecto CineReviews.
Lee todos los archivos del proyecto y los compila en un PDF ordenado.
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 PageBreak, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase.pdfmetrics import stringWidth

PROJECT = r"C:\Users\Victor-Deskyop1\Documents\Default Project\cine-reviews"
OUTPUT = os.path.join(PROJECT, "documentacion", "CineReviews_Documentacion_Completa.pdf")

# Extensiones que vamos a incluir
INCLUDE_ORDER = [
    # (subpath, titulo, descripcion)
    ("sql/database.sql", "Punto 1 - BASE DE DATOS (MySQL)", 
     "Importa este archivo en phpMyAdmin o MySQL para crear la base de datos cine_reviews con las tablas: users, movies y reviews, mas datos de ejemplo."),
    ("config/config.php", "Configuracion - config.php",
     "Archivo de configuracion global. Ajusta aqui las credenciales de la base de datos."),
    ("config/database.php", "Conexion a BD - database.php",
     "Funcion que devuelve una conexion PDO reutilizable a MySQL."),
    ("models/User.php", "Modelo User.php",
     "Gestiona el registro y login de usuarios, y datos de sesion."),
    ("models/Movie.php", "Modelo Movie.php",
     "Operaciones CRUD y consultas sobre las peliculas."),
    ("models/Review.php", "Modelo Review.php",
     "Operaciones CRUD y consultas sobre las resenas."),
    ("includes/auth.php", "Helpers - auth.php",
     "Funciones de sesion, saneamiento y mensajes flash."),
    ("includes/header.php", "Layout - header.php",
     "Cabecera HTML con la barra de navegacion y alertas."),
    ("includes/footer.php", "Layout - footer.php",
     "Pie de pagina HTML."),
    ("index.php", "Pagina Principal - index.php",
     "Pagina de inicio que muestra mejores peliculas y resenas recientes."),
    ("pages/login.php", "Login.php",
     "Formulario de inicio de sesion."),
    ("pages/register.php", "Register.php",
     "Formulario de registro de nuevos usuarios."),
    ("pages/logout.php", "Logout.php",
     "Cierra la sesion del usuario."),
    ("pages/movies.php", "Movies.php",
     "Listado de peliculas con busqueda, filtros por genero y orden."),
    ("pages/movie.php", "Movie.php",
     "Detalle de una pelicula con sus resenas y calificaciones."),
    ("pages/add_movie.php", "Add Movie.php",
     "Formulario para agregar una nueva pelicula."),
    ("pages/edit_movie.php", "Edit Movie.php",
     "Formulario para editar una pelicula existente."),
    ("pages/delete_movie.php", "Delete Movie.php",
     "Elimina una pelicula y sus resenas."),
    ("pages/add_review.php", "Add Review.php",
     "Formulario para escribir una resena con calificacion."),
    ("pages/edit_review.php", "Edit Review.php",
     "Formulario para editar una resena."),
    ("pages/delete_review.php", "Delete Review.php",
     "Elimina una resena."),
    ("pages/my_reviews.php", "My Reviews.php",
     "Muestra todas las resenas del usuario logueado."),
    ("css/style.css", "Estilos - style.css",
     "Hoja de estilos CSS responsive de toda la plataforma."),
]


# Estilos
header_style = ParagraphStyle(
    "Header", fontName="Helvetica-Bold", fontSize=22, leading=27,
    textColor=colors.white, alignment=TA_CENTER,
    backColor=colors.HexColor("#e50914"), borderPadding=14, spaceAfter=8,
)
subheader_style = ParagraphStyle(
    "Subheader", fontName="Helvetica", fontSize=12, leading=16,
    textColor=colors.HexColor("#666666"), alignment=TA_CENTER, spaceAfter=12,
)

section_style = ParagraphStyle(
    "Section", fontName="Helvetica-Bold", fontSize=16, leading=20,
    textColor=colors.HexColor("#141414"), spaceBefore=10, spaceAfter=4,
    backColor=colors.HexColor("#f0f0f0"), borderPadding=8,
)
desc_style = ParagraphStyle(
    "Desc", fontName="Helvetica-Oblique", fontSize=10, leading=14,
    textColor=colors.HexColor("#555555"), spaceAfter=8, alignment=TA_LEFT,
)
inner_title = ParagraphStyle(
    "InnerTitle", fontName="Helvetica-Bold", fontSize=12, leading=16,
    textColor=colors.HexColor("#16213e"), spaceBefore=12, spaceAfter=4,
)
body_style = ParagraphStyle(
    "Body", fontName="Courier", fontSize=6.5, leading=8.2,
    textColor=colors.black, spaceAfter=6, leftIndent=2,
)

def esc(s):
    """Escapa HTML para reportlab Paragraph."""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("\n", "<br/>"))

def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.6*inch, bottomMargin=0.6*inch,
        title="CineReviews - Documentacion Completa del Codigo",
        author="CineReviews"
    )

    story = []

    # ===== PORTADA =====
    story.append(Spacer(1, 1.2*inch))
    story.append(Paragraph("&#127916; CINE REVIEWS", header_style))
    story.append(Paragraph("Plataforma de Resenas de Peliculas - Documentacion Completa del Codigo", subheader_style))
    story.append(Spacer(1, 0.3*inch))

    # Tabla de contenido / estructura
    toc_title = ParagraphStyle("TOC", fontName="Helvetica-Bold", fontSize=14,
                               textColor=colors.HexColor("#e50914"), spaceAfter=10)
    story.append(Paragraph("Estructura del Proyecto", toc_title))

    tree_lines = [
        "cine-reviews/",
        "|-- sql/ .................. database.sql  (Crear la BD primero)",
        "|-- config/ ............... config.php, database.php",
        "|-- models/ ............... User.php, Movie.php, Review.php",
        "|-- includes/ ............. auth.php, header.php, footer.php",
        "|-- pages/ ................ login, register, logout, movies, movie,",
        "|                       ................ add_movie, edit_movie, delete_movie,",
        "|                       ................ add_review, edit_review, delete_review, my_reviews",
        "|-- css/ .................. style.css",
        "|-- documentacion/ ........ Este PDF",
        "|-- assets/ ............... (carpeta vacia para imagenes locales)",
        "`-- index.php ............. Pagina principal"
    ]
    t = Table([[Paragraph(esc(l), body_style)] for l in tree_lines], colWidths=[7.3*inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ]))
    story.append(t)

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("GUIA RAPIDA DE INSTALACION", toc_title))
    steps = [
        "<b>1.</b> Abre phpMyAdmin (o MySQL) y ejecuta el archivo <b>sql/database.sql</b> para crear la base de datos 'cine_reviews' y sus tablas.",
        "<b>2.</b> Abre <b>config/config.php</b> y confirma las credenciales de tu servidor MySQL (host, usuario, contrasena).",
        "<b>3.</b> Copia la carpeta <b>cine-reviews</b> dentro de la raiz de tu servidor local (p. ej. C:/xampp/htdocs/).",
        "<b>4.</b> Accede en el navegador a: <b>http://localhost/cine-reviews/</b>",
        "<b>5.</b> Inicia sesion con el usuario de prueba: <b>admin@cinereviews.com</b> / <b>password</b> (o registra una nueva cuenta).",
    ]
    for s in steps:
        story.append(Paragraph(s, ParagraphStyle("st", fontName="Helvetica", fontSize=10,
                                                 leading=15, spaceAfter=8)))

    story.append(Spacer(1, 0.2*inch))
    cover_note = ParagraphStyle("cn", fontName="Helvetica-Oblique", fontSize=9,
                                textColor=colors.HexColor("#888888"), alignment=TA_CENTER)
    story.append(Paragraph(
        "INSTRUCCIONES: En este documento el codigo se presenta en el ORDEN EXACTO en que debe configurarse.<br/>"
        "Marca <b>&#128204; PUNTO 1</b> para empezar (base de datos) y avanza hasta <b>&#127937; FIN DEL PROYECTO</b>.",
        cover_note))
    story.append(PageBreak())

    # ===== CUERPO =====
    total = len(INCLUDE_ORDER)
    for idx, (relpath, display_title, desc) in enumerate(INCLUDE_ORDER, start=1):
        full = os.path.join(PROJECT, relpath)
        if not os.path.exists(full):
            continue
        with open(full, "r", encoding="utf-8") as f:
            content = f.read()

        # Numero de archivo
        marker = "&#128204;" if idx == 1 else "&#128196;"
        story.append(Paragraph(f"{marker} ARCHIVO {idx} de {total} --- {esc(display_title)}",
                               section_style))
        story.append(Paragraph(f"<b>Ruta:</b> cine-reviews/{esc(relpath)} - <b>{len(content.splitlines())} lineas</b>",
                               ParagraphStyle("path", fontName="Helvetica", fontSize=9,
                                              textColor=colors.HexColor("#e50914"), spaceAfter=2)))
        if desc:
            story.append(Paragraph(esc(desc), desc_style))

        # Codigo - dividido en bloques de a lo mas 55 lineas por tabla
        # para evitar que un bloque exceda el alto de la pagina.
        lines = content.splitlines()
        CHUNK = 55
        for start in range(0, len(lines), CHUNK):
            chunk = "\n".join(lines[start:start+CHUNK])
            code_block = Table([[Paragraph(esc(chunk), body_style)]], colWidths=[7.3*inch])
            code_block.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#fafafa")),
                ("BOX", (0,0), (-1,-1), 0.6, colors.HexColor("#dddddd")),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
                ("LEFTPADDING", (0,0), (-1,-1), 6),
                ("RIGHTPADDING", (0,0), (-1,-1), 6),
                ("TOPPADDING", (0,0), (-1,-1), 4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ]))
            story.append(code_block)
            story.append(Spacer(1, 8))

    # ===== FIN =====
    story.append(PageBreak())
    finish_style = ParagraphStyle(
        "Finish", fontName="Helvetica-Bold", fontSize=20, leading=26,
        textColor=colors.white, alignment=TA_CENTER,
        backColor=colors.HexColor("#2ecc71"), borderPadding=16, spaceBefore=150,
    )
    story.append(Paragraph("&#127937; FIN DEL PROYECTO&#127937;", finish_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "Has recorrido todo el codigo de CineReviews desde la base de datos (PUNTO 1) hasta la pagina principal.<br/>"
        "Sigue la guia rapida de instalacion de la portada para poner en marcha tu plataforma.",
        subheader_style))
    story.append(Spacer(1, 0.3*inch))
    cred = Table([[Paragraph(
        "CINE REVIEWS - Desarrollado con PHP, MySQL, HTML y CSS.<br/>"
        "Carpeta 'documentacion' dentro del proyecto.",
        ParagraphStyle("cr", fontName="Helvetica-Oblique", fontSize=10,
                       textColor=colors.HexColor("#888888"), alignment=TA_CENTER))]],
        colWidths=[7.3*inch])
    story.append(cred)

    doc.build(story)
    print("PDF generado:", OUTPUT)

if __name__ == "__main__":
    build()

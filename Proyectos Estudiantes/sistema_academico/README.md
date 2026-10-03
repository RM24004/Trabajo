# Sistema Academico

Aplicacion de escritorio en Python para gestionar **estudiantes, materias y notas**, con inicio de sesion y dos roles: **docente** y **estudiante**.

No usa base de datos. Los datos se guardan en archivos **JSON** dentro de la carpeta `datos/`.

## Requisitos

- Python 3.10 o superior
- Tkinter (viene incluido con Python en Windows y macOS)

En Linux puede hacer falta instalarlo aparte:

```
sudo apt install python3-tk
```

No hay dependencias externas: no se usa `pip install`.

## Como ejecutarlo

```
python principal.py
```

## Acceso

La primera vez se crea una cuenta de docente por defecto:

| Usuario | Contrasena | Rol     |
| ------- | ---------- | ------- |
| admin   | admin123   | docente |

El docente da de alta a los estudiantes desde el boton **+ Nuevo estudiante**. Si dejas vacios los campos *Usuario de acceso* y *Contrasena inicial*, el sistema los genera solos y te los muestra en una ventana al guardar. Anotalos: no volveran a mostrarse. Si un alumno pierde su clave, el docente puede usar **Restablecer clave**.

## Permisos

| Accion                       | Docente | Estudiante |
| ---------------------------- | :-----: | :--------: |
| Ver estudiantes              |   Si    |    No      |
| Ver y editar notas propias   |    -    |    Si      |
| Agregar / editar estudiantes |   Si    |    No      |
| Agregar / editar materias    |   Si    |    No      |
| Agregar / editar notas       |   Si    |    No      |
| Cambiar su propia contrasena |   Si    |    Si      |

El estudiante unicamente ve **sus propias notas**, promedios y datos personales. Esta limitacion se aplica en la capa de servicios (`nucleo/servicios.py`), no solo ocultando botones en la pantalla.

## Estructura

```
sistema_academico/
  principal.py                punto de entrada
  config.py                   rutas de los archivos JSON y constantes
  nucleo/
    almacen.py                lectura y escritura atomica de JSON
    seguridad.py               hash de contrasenas con PBKDF2 y sal
    servicios.py              reglas de negocio, validaciones y permisos
  interfaz/
    estilos.py                tema visual
    widgets.py                campos de formulario, tablas y tarjetas
    vista_login.py            pantalla de inicio de sesion
    vista_docente.py          panel completo del docente
    vista_estudiante.py       panel de consulta del estudiante
    dialogos.py               formularios de estudiante, materia, nota y contrasena
  datos/
    usuarios.json
    estudiantes.json
    materias.json
    notas.json
```

## Notas

- Las contrasenas nunca se guardan en texto plano: se almacena un hash PBKDF2-SHA256 con sal aleatoria.
- Los archivos se escriben de forma atomica (archivo temporal + `os.replace`), asi un corte de luz no deja el JSON a medias.
- Nota valida: de 0 a 100. Se considera aprobada a partir de **60**.
- Al borrar un estudiante o una materia se eliminan tambien sus notas en cascada.
- Si un JSON queda danado, el programa avisa en lugar de borrar informacion en silencio.
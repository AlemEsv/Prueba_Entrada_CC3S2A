# Cambios realizados

## Día 1:

1. Creación del archivo CHANGELOG.md
    - En el **CHANGELOG.md** se subirán los cambios realizados diariamente en toda la semana.
2. Creación del **dockerfile**
    - Se colocó la estructura inicial de un dockerfile con la imagen de **python**, y pedirá los requisitos puestos en el archivo **requeriments.txt**. 
3. Creación del **docker-compose.yml**
    - Se colocó la estructura inicial que propone **postgres** para trabajar con la imagen de **PostgreSQL** en **Docker**. 
    Información en https://hub.docker.com/_/postgres. 
4. Creación de la rama **develop**
    - Se colocó dicha rama para seguir el desarrollo del juego, de esta rama se extenderán las ramas de cada día antes de ser *fusionado* con la rama **main**.
5. Creación de la rama **feature/dia1**
    - Como primer cambio en la rama **feature/dia1**, actualicé el **CHANGELOG.md** para documentar qué se agregó en la estructura inicial del proyecto.
6. Creación del primer tag del proyecto

## Día 2:

1. Modificación del archivo **requeriments.txt** y **test_trivia.py** 
    - Se agregó el requisito de pytest en **requeriments.txt** para las pruebas unitarias hechas en **test_trivia.py**.
2. Creación del archivo **trivia.py**
    - Definición del constructor de la clase **Question** con parametros *descripción, opciones y respuesta correcta*
    - Definición del método **is_correct()** para revisar si una pregunta es correcta o no.
3. Creación del archivo **test_trivia.py**
    - Se importa la libreria **pytest**.
    - Se hacen pruebas para ver si el método **is_correct()** está bien definido.
4. Pruebas unitarias con pytest
    - Se ejecutó el comando pytest sobre la carpeta *app* para revisar si era capaz de pasar el testeo de prueba.

## Día 3:

1. Agregar clase Quiz
    - Se coloca la clase **Quiz** en **trivia.py** la cuál nos añadirá preguntas y podrá avanzar entre preguntas dentro de la cantidad de preguntas que tengamos para el juego.
2. Creación función **run_quiz()**
    - Se creó la función **run_quiz()** dentro de la clase **Quiz** que imprimirá todas las preguntas que tenga nuestro quiz.
3. Creación rama **feature/quiz-trivia**
    - se coloca todos los cambios realizados en conjunto con el cambio en el **CHANGELOG.md** dentro de la rama **feature/quiz-trivia**, para luego hacer un merge --no-ff con la rama develop para finalizar lo hecho el día 3.

## Día 4:
1. Modificación de la clase **Quiz**
    - Se agregó la lógica de tener preguntas correctas e incorrectas dentro de nuestro **Quiz** para cada pregunta añadida.
2. Actualización de pruebas unitarias
    - Se añadió la función **test_quiz_scoring()** para corroborar si las preguntas y respuestas añadidas están bien implementadas.
    - Se verificó con una prueba con **pytest**.
3. Creación de la rama **feature/quiz-puntuacion**
4. Actualización de la función **run_quiz()**
    - Lógica simple modificada para que **run_quiz()** pueda visualizar como máximo las 10 preguntas establecidas.

## Día 5:
1. Actualización a la función **run_quiz()**
    - Actualización final de la interfaz que tendrá nuestro juego de preguntas, se visualizará cada pregunta, las preguntas correctas e incorrectas y finalizará el juego.
2. Pruebas con 5, 10, 20 preguntas usando **run_quiz()**
3. Creación de la rama **feature/implementacion-run_quiz**

## Día 6:
1. Configuración de **GitHub Actions** para ejecutar pruebas unitarias y de integración.
    - Creé el repositorio en github para colocar los cambios que he estado haciendo hasta el día 6, para de ahí crear el primer **secreto** dentro de mis variables ocultas con la KEY proporcionada en SonarQube
2. Archivo `.github/workflows/ci.yml` agregado.
3. Configuración de los archivos **base_datos_preguntas.py** y **conection_fastAPI.py**.
    - Creación de clases que permiten la conexión de la base de datos con las preguntas organizadas por dificultad creadas con Adminer gracias a la imagne creada por docker de postgre.
4. Organización de archivos dentro de la carpeta *app*
    Para hacer que el archivo **trivia.py** no esté cargado de funciones y clases coloqué varias partes en diferentes archivos más especificos.
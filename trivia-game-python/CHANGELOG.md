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
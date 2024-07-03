---
title: USMAPS
intro: 'Mapa de navegación dentro de la  Universidad Técnica Federico Santa María'
type: Mapa de navegación
topics:
  - Python
versions:
  - 1.1
---

## Introduction
Proyecto USMAPS
Integrantes:

•	Antonia Cortes
202430003-2

•	Sebastián Moya
202430009-1

•	Alonso Armand
202430015-6

## ¿Que es USMAPS?

USMAPS es un mapa guía para todos los estudiantes de la Santa María, pero especialmente para los estudiantes de primer y segundo año, la función sería similar a Google maps la diferencia radica en que el proyecto se implementara en la universidad Federico Santa María. 
En USMAPS podrás buscar tu sala y por medio de obtención de la obtención de ubicación mediante un formulario, se le pregunta al usuario donde esta y donde quiere ir. Al obtener la información el software calcula la mejor ruta y al final se muestra mediante un mapa la ruta escogida.
La Visualización y pasos a seguir

## Principal objetivo
Como grupo buscamos la manera de solucionar este problema y poder facilitar el comienzo de esta nueva etapa que tienen todos los estudiantes universitarios sobre todo los de primer y segundo año.
## Descripción del problema
Normalmente cuando uno empieza una nueva etapa de la vida, en este caso la etapa de ser universitario, los primeros años siempre son complejos y la mayor problemática que se repite en estos casos es saber dónde es la siguiente clase, ya que al principio como estudiante no conoce la universidad, además de no conocer los nombres y ubicación de los edificios y salas.
## Propuesta de solución
Como grupo nos planteamos diversos problemas, al final llegamos a la conclusión de un problema común entre todos los estudiantes y sobre todo para los estudiantes más nuevos, perderse en la universidad, en nuestro esfuerzo para buscar una forma de cambiar esta problemática para los futuros estudiantes. En conjunto como grupo apoyamos la idea de desarrollar un sistema inspirado en Google maps que pueda guiar a los estudiantes a sus respectivas salas mediante un sistema de GPS que le pueda marcar la ruta más corta a la sala que desea llegar.

## Primeros pasos
Aquí se encuentra el proceso de aprendizaje y descubrimiento, ya que, como estudiantes nuevos de primer año, no tenemos un gran conocimiento de la materia, algunos somos novatos en el ámbito de la programación, en la escritura de códigos y sobre todo en la creación de un proyecto de este estilo.
Por esta misma razón como grupo nos centramos mucho en el tema de investigar a fondo todo lo necesario y poder profundizar en los temas que fueran necesarios además de compenetrarnos como grupo y poder sacar este proyecto a flote.
## Investigación y Planificación
Como grupo comenzamos a planear como realizaríamos este tipo de tipo de proyecto, algunos integrantes tenían cierto conocimiento mayor que el resto sobre ciertas cosas, como ejemplo las diversas maneras que se podía utilizar una Raspberry Pi o también con el tema de la creación de códigos. el resto del equipo empezó a investigar de diversas fuentes viendo videos o utilizando ChatGPT.
Medición del edificio C y sus salas
Como grupo nos dividimos la tarea de medir el edificio C por diferentes partes con instrumentos especiales de medición para así poder señalar con exactitud en el mapa la ubicación correcta de la sala que desea llegar.
## Ultimo paso
Lo último que nos faltaba era crear la página web de USMAPS y que pudiera funcionar correctamente la página, al final quedo funcional, quedando así finalizado nuestro proyecto. Cabe recalcar que esto no indica que el proyecto no tenga algún error y hay un pequeño detalle que es la entrada del Ciac que para poder ubicarlo en el mapa se tiene que escribir específicamente "Entrada desde el Ciac".
Esperamos que el proyecto haya sido de su agrado, mucha suerte y gracias por participar.


### Información sobre USMAPS
La carpeta mapa alberga todas las versiones antiguas del mapa del edificio C de la universidad en formato geojsom u osm. La carpeta código es un registro de todos los códigos probados para poder llegar al proyecto final, en esta carpeta se almacena los códigos descontinuados y el código final en primera fase.
Esto se hizo para tener un registro de todo lo que se hizo y para tener constancia de lo que se hizo.
La carpeta Proyecto USMAPS contiene el proyecto, en el hay distintas carpetas, archivos y códigos esenciales para su ejecución, como USMAPS se desarrolló como una página HTML, hecha con flask.. https://flask.palletsprojects.com/en/3.0.x/ Véase la documentación de flask para más información respecto a su uso.
Para hacer la página se ocupó la plantilla iCREAM – Ice Cream Shop Website Template, de HTML Codex el cual se adaptó al modo de uso de Flask
La carpeta static contiene subcarpetas que contienen archivos estáticos,
La carpeta templates contiene los archivos html que se usan para la página en general.
Después tenemos diversos archivos:

-EDIFICIO_C_MAPA.geojson: es el mapa final del segundo edificio C

-app.py: es el código donde se une todo gracias a Flask

-c.graphml es el archivo de grafos del edificio C

-funciones.py es el código que recibe la ubicación y entrada y genera la ruta en un mapa HTML

-limitesPasillos.txt archivo de texto que contiene el id del grafo y a que ubicación o ubicaciones corresponde cada grafo.

-salaPasillo.tx es el archivo de texto que contiene el nombre de la ubicación, las coordenadas, el pasillo o lugar donde se encuentra la ubicación y las coordenadas en el pasillo donde se encuentra la ubicación.

### Modo de uso:
Descargue la carpeta proyecto USMAPS, posteriormente descargue e instale las librerías siguientes librerías de Python Flask, Folium y networkx
Para qué sirve cada librería:

-Flask: hacer la página web y que integre las funciones de Python

-Folium: hacer el mapa

-Networkx: para calcular la ruta mediante grafos

Luego de instalar las librerías, abra con su editor de código la carpeta de proyecto USMAPS, luego ejecute el archivo app.py, este debiese entregar una dirección web o un vínculo, lo seleccionas o abres en tu navegador y al final de estes agregas /home
Esto abrirá la página donde podrás saber más acerca del proyecto, o bien usar USMAPS en la sección mapa.
En la sección mapa encontraras un mapa que, si haces clic en una de las marcas de ubicación, te saldrá el nombre de esta. Más abajo puedes encontrar un formulario donde tienes que rellenarlo con la ubicación donde te encuentras y a la que te quieres dirigir, pero ten cuidado cuando ingreses la ubicación ya que el formulario solo acepta los mismos nombres de las ubicaciones disponibles en el mapa de arriba.
Luego aprietas enviar y te llevara al mapa.


### Créditos y atribuciones
-Plantilla html iCREAM - Ice Cream Shop Website Template diseñado por HTML Codex

https://htmlcodex.com/ice-cream-shop-website-template

-Documentación de Flask

https://flask.palletsprojects.com/en/3.0.x/

-Chat GPT para tener una idea de cómo hacer ciertas partes de los códigos

https://openai.com/index/chatgpt/

-Openstreetmap y JOSM para hacer el mapa

https://www.openstreetmap.org/

https://josm.openstreetmap.de/

-Graph Online para hacer el archivo de grafos del edificio

https://graphonline.ru/es/

###
si no funciona, ocurre cualquier error o consulta, escribir al correo acorteb@usm.cl

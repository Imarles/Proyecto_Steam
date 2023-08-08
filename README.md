# Proyecto_Steam
Analisis Exploratorio De Datos &amp; Modelo de prediccion (Steam)
Análisis Explorarotio De Datos & Modelo De Prediccion
Introducción al proyecto:
Análisis Exploratorio y Transformación de los Datos, y Modelado con Técnicas de Machine Learning.
1
Crearemos consultas específicas para obtener información relevante, como los géneros más ofrecidos, los juegos lanzados en un año determinado y otras consultas interesantes relacionadas con el análisis
2
limpiaremos y exploraremos los datos para prepararlos adecuadamente para la predicción. El Análisis Exploratorio de los Datos será un paso crucial para entender las relaciones entre las variables y detectar posibles patrones y anomalías.
3
 Aquí entrenaremos nuestro algoritmo de machine learning para que pueda realizar predicciones precisas sobre los precios de los juegos en Steam. Tomaremos en cuenta características como género, año, especificaciones y otras variables relevantes para lograr una predicción precisa.


Evaluación del cumplimiento de los objetivos:
Transformaciones en las bases de datos: Link al Notebook
Desarrollo de la API :Link a la API
Deployment: Link al Render
Video: Link al Video
Propuesta de trabajo:
1. Transformación del dataset:
   - Leer el dataset con el formato correcto.
2. Desarrollo de la API con FastAPI:
   - Crear una API RESTful con el framework FastAPI.
   - Implementar 6 funciones para los endpoints, cada una con un decorador @app.get('/') para consumir los datos de la empresa según las siguientes consultas:
     - genero(Año: str): Devuelve una lista con los 5 géneros más ofrecidos en el orden correspondiente para un año específico.
     - juegos(Año: str): Devuelve una lista con los juegos lanzados en un año específico.
     - specs(Año: str): Devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente para un año específico.
     - earlyacces(Año: str): Devuelve la cantidad de juegos lanzados en un año con early access.
     - sentiment(Año: str): Devuelve una lista con la cantidad de registros categorizados con un análisis de sentimiento para un año específico.
       Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
     - metascore(Año: str): Devuelve los 5 juegos con mayor metascore para un año específico.
3. Deployment:
   - Utilizar un servicio como Render o Railway para desplegar la API y hacerla accesible desde la web.


4. Análisis exploratorio de los datos (EDA):
   - Realizar un análisis exploratorio de los datos para investigar las relaciones entre las variables del dataset.
   - Identificar posibles outliers o anomalías en los datos.
   - Buscar patrones interesantes que puedan ser útiles en un análisis posterior.
   - Generar nubes de palabras para conocer las palabras más frecuentes en los títulos de los juegos.
5. Modelo de predicción:
   - Entrenar un modelo de machine learning para realizar predicciones.
   - Utilizar características como Género, Año, Metascore, y/o otras relevantes para el modelo.
   - Implementar una función predicción(genero, earlyaccess, otras_variables) que, ingresando ciertos parámetros, devuelva el precio y RMSE (Error cuadrático medio) de las predicciones realizadas por el modelo.


Video explicativo del proyecto
https://youtu.be/aeCfvMVYi3g


Deployment:
Para realizar el deploy de esta aplicación, se utilizó la plataforma Render. Render es una plataforma en la nube que facilita el despliegue y el hosting de 

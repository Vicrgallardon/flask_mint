# W6-api-project

![foto_hp](https://user-images.githubusercontent.com/85116761/125535912-3d1f29a6-c48e-462f-a9d1-2174425bd5a5.jpeg)

El objetivo de este proyecto es crear una api desde nuestro propio terminal. La api debe ser capaz de recibir información y extraerla. 

## ESTRUCTURA. 

### Carpeta notebooks 
- Carpeta data
    Dentro de ellas hemos realizado una limpieza de aquello que posteriormente introduciremos en la base de sql. 
    Debido a la falta de tiempo he decidido decantarme por el script de la primera película de Harry Potter. 

-GET_ID
    En este jupyter notebook hemos generado funciones para que el usuario pueda obtener la id del grupo a partir del nombre del grupo y la id del usuario a partir del nombre de usuario. Posteriormente esto nos resultara útil a la hora de ejecutar los endpoints de get. 

-tablassqls
    En este jupyter hemos creado la conexión con sql y hemos creado las tablas. En estas tablas hemos introduciod tanto información a mano como información del script de Harry Potter. La información introducida será la que se optendrá a parir de los endponts. 

Carpeta de tools 
-get.py
   Este file contiene todas las funciones necesarias para obtener información de nuestra base de datos. 

-get.py
   Este file contiene todas las funciones necesarias para introducir información de nuestra base de datos. 

Apimia 
    En este file se encuentran todos los enpoitns tanto para introducir como extraer información de nuestra base de datos. 


PENDIENTE. 

1. Cambiar el script de harry potter, por el de el script de Rick & Morty, ya que este último no lo hemos visto en clase. 
2. Terminar de generar las conexiones y los mensajes(texto) del script de Harry Potter.
4. Generar un jupyter notebook para testear la api y no tener que acudir a la pestaña de google. Se que este paso es muy fácil, pero ayer se me estaba quedando todo el rato enganchado.
5. Aplicar el analisis de sentimientos.  

###### Esta es una aplicacion desarrollada para: **MercadoLibre Challenge**

# Google Drive API Simplificado
Esta aplicación permite simplicar ciertas funciones provistas por la API de Google Drive.
## Pasos para su uso
##### Antes de empezar con la aplicacion:
- Debe crear un proyecto en [Google Cloud Platform](https://console.developers.google.com/ "Google Cloud Platform")
- Acceda a la biblioteca de APIs, busque y habilite la biblioteca con el nombre "Google Drive API"
- Luego configure las Credenciales y la pantalla de Consentimiento.
- Descargue la credencial en formato JSON.

El proyecto creado es el que va a solicitar los permisos al Drive del usuario.

##### Una vez realizado lo anterior:
- Clone el repositorio: <br>
`git clone https://github.com/danhorna/MercadoLibre-Challenge.git`
- Almacene la credencial descargada anteriormente con el nombre "credentials.json" en el directorio ./app/static/

## Comenzando
##### Existen dos formas de arrancar la aplicación:
- **Python & pip:**
Antes de ejecutar la aplicación debe asegurarse que posee las dependecias necesarias.
Para agiliar este proceso, puede realizar la instalacion de todo lo necesario ejecutando el siguiente comando:<br>
`pip install -r requirements.txt`<br>
Una vez realizado esto, ejecute el siguiente comando para arrancar la app:<br>
`python run.py`

- **Docker:**
**IMPORTANTE: **Por el momento solo funciona en sistemas Linux.
Primeramente debe crear la imagen con el siguiente comando:<br>
`docker build -t nombredelaimagen .`<br>
Una vez creada la imagen ya puede ejecutarla con el siguiente comando:<br>
`docker run -it --net=host nombredelaimagen`

## Uso
La aplicacion funciona bajo el puerto 5000.
Al iniciar, se le va a pedir que ingrese a una URL provista por Google para que se loguee y le conceda los permisos de su Drive a la aplicación. Una vez realizado esto, la app ya esta lista para usarse.
### Tenemos las siguientes funciones:
- #### Buscar una palabra en un documento(titulo, descripcion o contenido):
Realizando una peticion GET a la url: <br>
`http://tusitio:5000/search-in-doc/PAR1?word=PAR2`<br>
*(donde PAR1 es la ID del documento y PAR2 es la palabra a buscar)*
**Existen tres tipos de respuestas:**
 - Status: 400 : No se envió el parametro "word".
 - Status: 404 : El documento no existe en el Drive del usuario logueado o la palabra no se encuentra en el documento.
 - Status: 200 : La palabra buscada se encuentra en el documento.
 
- #### Crear un archivo con titulo y descripcion:
Realizando una peticion POST a la url:<br>
`http://tusitio:5000/file`<br>
Con el siguiente formato:
```json
{
	"titulo": "Titulo del archivo",
	"descripcion": "Descripcion del archivo"
}
```
**Existen tres tipos de respuestas:**
 - Status: 500 : Si no se puede crear el archivo.
 - Status: 400 : En caso de enviar mal los parametros.
 - Status: 200 : El archivo fue creado correctamente.
 En este ultimo caso se recibe la informacion del archivo creado:
 ```json
{
		"id": "123123",
		"titulo": "Titulo del archivo",
		"descripcion": "Descripcion del archivo"
}
```

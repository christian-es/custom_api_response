# Customizar respuesta de petición a API

### Creación de entorno

```$ virtualenv env```

### Instalación de dependencias

```$ . env/bin/activate ```

```$ pip install -r requirements.txt ```

### Ejemplo

En esta ocasión para el ejemplo se han creado dos objetos: Autor y Libro, entendiéndose que un autor puede tener muchos libros y un libro solo es de un autor.

### Imagenes

<b>Listado de libros mostrando ID foráneo</b>
![ScreenShot](https://raw.github.com/christian-es/custom_api_response/master/screenshot/autores_id.png)

<b>Listado de libros mostrando detalles de autores</b>
![ScreenShot](https://raw.github.com/christian-es/custom_api_response/master/screenshot/autores_detalle.png)

<b>Libro solicitado por ID mostrando ID de autor</b>
![ScreenShot](https://raw.github.com/christian-es/custom_api_response/master/screenshot/libro_id.png)

<b>Libro solicitado por ID mostrando detalles de autores</b>
![ScreenShot](https://raw.github.com/christian-es/custom_api_response/master/screenshot/libro_id_detalle.png)


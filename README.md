# GalaxyStore

![GalaxyStore Logo](./ecommerce/ecommerce/static/images/logo.png)

GalaxyStore es una plataforma de comercio electrónico diseñada para la venta de productos relacionados con el espacio y la ciencia ficción. Este repositorio contiene el código fuente y los recursos necesarios para ejecutar la aplicación GalaxyStore.

## Características

- Registro de usuarios
- Inicio de sesión de usuarios
- Búsqueda y navegación de productos
- Agregar productos al carrito de compras
- Proceso de pago y checkout
- Administración de productos y pedidos (para administradores)
- Y más...

## Instalación

### Requisitos previos

- Python 3.x
- Django 3.x
- PostgreSQL (opcional)

### Pasos de instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/galaxystore.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd galaxystore
   ```

3. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos (si es necesario) en `settings.py`.

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   
   ```

6. Carga datos iniciales (opcional):

   ```bash
   python manage.py migrate
   ```

7. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

8. Accede a la aplicación desde tu navegador web:

   ```
   http://localhost:8000
   ```

## Uso

- Para acceder como administrador, debes crear un superusuario:

  ```bash
  python manage.py createsuperuser
  ```

- Explora los productos, agrega elementos al carrito y procede al proceso de pago.

## Contribuir

Si deseas contribuir a GalaxyStore, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama para tu función: `git checkout -b feature/nueva-caracteristica`.
3. Realiza tus cambios y haz commit de ellos: `git commit -m 'Agrega una nueva característica'`.
4. Sube tus cambios a tu fork: `git push origin feature/nueva-caracteristica`.
5. Abre una solicitud de extracción en GitHub.

## Licencia

GalaxyStore está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Contacto

Para cualquier pregunta o comentario, no dudes en ponerte en contacto con el equipo de desarrollo:

- Nombre:Elkin Dario Rojas
- Correo electrónico: elkin.rojas@utp.edu.co


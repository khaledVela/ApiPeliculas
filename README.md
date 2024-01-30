# Django Movie API

Esta API de cartelera de películas en Django te permite gestionar películas, usuarios personalizados y guardar imágenes asociadas a las películas.

## Configuración del Entorno

### 1. Crear un entorno virtual
Si no tienes un entorno virtual, crea uno utilizando el siguiente comando:
```bash
pip install -r requirements.txt
```
### 2. Aplicar migraciones
Si aún no tienes la base de datos SQLite configurada, ejecuta las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 3. Crear un Superusuario
Crea un superusuario para acceder al panel de administración y gestionar los datos:
```bash
python manage.py createsuperuser
```
### 4. Ejecutar la aplicación
Inicia el servidor para ejecutar la aplicación:
```bash
python manage.py runserver
```
La aplicación estará disponible en http://localhost:8000/.

## Endpoints de Géneros

### Obtener la lista de géneros
- **GET /api/generos:** Obtiene la lista de géneros.

### Obtener detalles de un género por ID
- **GET /api/generos/{id}:** Obtiene detalles de un género por ID.

### Crear un nuevo género
- **POST /api/generos:** Crea un nuevo género.

### Actualizar detalles de un género por ID
- **PUT /api/generos/{id}:** Actualiza detalles de un género por ID.

### Eliminar un género por ID
- **DELETE /api/generos/{id}:** Elimina un género por ID.

## Endpoints de Clasificaciones

### Obtener la lista de clasificaciones
- **GET /api/clasificaciones:** Obtiene la lista de clasificaciones.

### Obtener detalles de una clasificación por ID
- **GET /api/clasificaciones/{id}:** Obtiene detalles de una clasificación por ID.

### Crear una nueva clasificación
- **POST /api/clasificaciones:** Crea una nueva clasificación.

### Actualizar detalles de una clasificación por ID
- **PUT /api/clasificaciones/{id}:** Actualiza detalles de una clasificación por ID.

### Eliminar una clasificación por ID
- **DELETE /api/clasificaciones/{id}:** Elimina una clasificación por ID.

## Endpoints de Películas

### Obtener la lista de películas
- **GET /api/peliculas:** Obtiene la lista de películas.

### Obtener detalles de una película por ID
- **GET /api/peliculas/{id}:** Obtiene detalles de una película por ID.

### Crear una nueva película
- **POST /api/peliculas:** Crea una nueva película.

### Actualizar detalles de una película por ID
- **PUT /api/peliculas/{id}:** Actualiza detalles de una película por ID.

### Eliminar una película por ID
- **DELETE /api/peliculas/{id}:** Elimina una película por ID.

### Buscar películas por nombre
- **POST /api/peliculas/buscarPelicula:** Busca películas por nombre.

  Para buscar películas por nombre, envía una solicitud POST a este endpoint con el parámetro `q` en el cuerpo de la solicitud:

  Ejemplo en formato JSON:
  ```json
  {
    "q": "nombre_de_la_pelicula"
  }

### Buscar películas por género
- **POST /api/peliculas/buscarGenero:** Busca películas por género.

  Para buscar películas por género, envía una solicitud POST a este endpoint con el parámetro `q` en el cuerpo de la solicitud:

  Ejemplo en formato JSON:
  ```json
  {
    "q": "nombre_del_genero"
  }
  
## Endpoints de Usuarios

### Obtener la lista de usuarios
- **GET /api/usuarios:** Obtiene la lista de usuarios.

### Obtener detalles de un usuario por ID
- **PATCH /api/usuarios/{id}:** Obtiene detalles de un usuario por ID.

### Eliminar un usuario por ID
- **DELETE /api/usuarios/{id}:** Elimina un usuario por ID.

### Crear un nuevo usuario
- **POST /api/usuarios:** Crea un nuevo usuario.

### Iniciar sesión (Login)
- **POST /api/token:** Inicia sesión y obtiene un token.

  Para iniciar sesión, envía una solicitud POST a este endpoint con los siguientes parámetros en el cuerpo de la solicitud:
  
  - **username:** Nombre de usuario del usuario.
  - **password:** Contraseña del usuario.

  Ejemplo en formato JSON:
  ```json
  {
    "username": "nombre_de_usuario",
    "password": "contraseña_secreta"
  }

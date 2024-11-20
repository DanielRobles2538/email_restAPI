# User Management API 🚀  

**Autor:** [Daniel Robles Aller](www.linkedin.com/in/danielroblesaller)  

Bienvenido a **User Management API**, una aplicación sencilla RESTful construida con **Python** y **Flask** para gestionar usuarios en una base de datos **PostgreSQL**. Esta API te permite realizar operaciones CRUD y probar los endpoints con la interfaz de documentación automática generada por **Swagger**.

---

## 🌟 Características  

🔹 Operaciones CRUD completas: **Crear, Leer, Actualizar y Eliminar usuarios**.  
🔹 **PostgreSQL** como base de datos relacional para garantizar integridad y escalabilidad.  
🔹 Documentación interactiva generada automáticamente por **Swagger** para pruebas directas desde el navegador.  

---

## 🚀 Tecnologías utilizadas  

- [Flask](https://flask.palletsprojects.com/): Framework ligero para desarrollar aplicaciones web rápidas y escalables.  
- [Flask-RESTx](https://flask-restx.readthedocs.io/): Extensión para la construcción eficiente de APIs RESTful.  
- [SQLAlchemy](https://www.sqlalchemy.org/): Toolkit SQL en Python para manejar bases de datos relacionales.  
- [PostgreSQL](https://www.postgresql.org/): Sistema de gestión de bases de datos relacional de código abierto y alto rendimiento.  

---

## 🛠️ Instalación y configuración  

### **Requisitos previos**  

Antes de comenzar, asegúrate de tener instalados:  

- [Python](https://www.python.org/downloads/)  
- [PostgreSQL](https://www.postgresql.org/download/)  
- [Pip](https://pip.pypa.io/en/stable/)  

---

### **Pasos de instalación**  

1. **Clona este repositorio:**  
   ```bash
   git clone https://github.com/tu-usuario/User-Management-API.git  
   cd User-Management-API
   ```

2. **Instala las dependencias necesarias:**  
   ```bash
   pip install flask flask-restx sqlalchemy psycopg2
   ```

3. **Configura la base de datos PostgreSQL:**  
   Accede a tu consola de PostgreSQL y ejecuta el siguiente script SQL:  
   ```sql
   -- Crear la base de datos  
   CREATE DATABASE flask;  
   CREATE USER postgres PASSWORD '1234';  
   GRANT ALL PRIVILEGES ON DATABASE flask TO postgres;  

   -- Crear la tabla User  
   CREATE TABLE "User" (
       id SERIAL PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
       email VARCHAR(100) UNIQUE NOT NULL
   );

   -- Insertar datos de ejemplo  
   INSERT INTO "User" (username, email) VALUES
   ('usuario1', 'usuario1@example.com'),
   ('usuario2', 'usuario2@example.com'),
   ('usuario3', 'usuario3@example.com');
   ```

4. **Ejecuta la API:**  
   Inicia el servidor ejecutando el archivo `email_api.py`:  
   ```bash
   python email_api.py
   ```

---

## 🌐 Acceso a la API  

1. Abre tu navegador en **[http://localhost:5000](http://localhost:5000)**.  
2. Podrás:  
   - Visualizar la documentación generada automáticamente por **Swagger**.  
   - Probar los endpoints de manera interactiva.  

---

## 📌 Endpoints principales  

- **GET /users**: Obtiene todos los usuarios registrados.  
- **GET /users/<user_id>**: Obtiene un usuario específico por ID.  
- **POST /users**: Crea un nuevo usuario enviando un JSON con los campos `username` y `email`.  
- **PUT /users/<user_id>**: Actualiza los datos de un usuario existente.  
- **DELETE /users/<user_id>**: Elimina un usuario de la base de datos.  

---

## 📧 Contacto  

Si tienes dudas o sugerencias, no dudes en contactarme:  

- **Correo:** [danielroblesaller@gmail.com](danielroblesaller@gmail.com)  
- **LinkedIn:** [Daniel Robles Aller](www.linkedin.com/in/danielroblesaller)  

--- 

¡Gracias por visitar este proyecto! 😊
```

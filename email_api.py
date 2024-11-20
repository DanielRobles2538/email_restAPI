# Importar librerias
from flask import Flask, request
from flask_restx import Api, Resource, fields
from sqlalchemy import create_engine, MetaData, select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError

# Crear aplicación Flask:
# Crear el objeto APP
app = Flask(__name__)

# Initializar la API DE Flask-Restx
api = Api(app, version='1.0', title='API de Usuarios', description='Una API para gestionar usuarios')

# Crear el motor de la base de datos
db_uri = 'postgresql://postgres:1234@localhost:5432/flask'
engine = create_engine(db_uri)

# Reflejar los datos de la tabla 'User'
metadata = MetaData()
try:
    metadata.reflect(bind = engine)
    users_table = metadata.tables['User']
    
except SQLAlchemyError as e:
    print(f'Error reflecting table: {e}')
    
#Definir el modelo de entrada y salida de la API
user_model = api.model('User', {
    'id' : fields.Integer(readonly=True, description='El ID de usuario'),
    'username' : fields.String(required=True, description='El nombre del usuario'),
    'email' : fields.String(requiered=True, description='La dirección de correo electrónico del usuario')
    }
)

# Crear los recursos y sus rutas en la API
class UserResource(Resource):
   
    # Obtener usuario
    @api.doc(description='Obtener un usuario por su ID', responses={404: 'Usuario no encontrado'})
    @api.marshal_with(user_model)
    def get(self, user_id):
        # Crear conexión con la base de datos
        with engine.connect() as connection:
            # Construir la query para seleccionar los datos de la tabla
            query = select(
                users_table.c.id,
                users_table.c.username,
                users_table.c.email
            ).where(users_table.c.id == user_id)
            
            # Ejecutar la query y obtener los resultados del fech
            result = connection.execute(query).fetchone()

            # Si el usuario existe retornar los datos, sino retornar error
            if result:
                return result
            else:
                api.abort(404, 'Usuario no encontrado')

    # Actualizar usuario
    @api.doc(description='Actualizar un usuario existente', responses={200: 'Usuario actualizado', 404: 'Usuario no encontrado'})
    @api.expect(user_model)
    def put(self, user_id):
        # Extraer los datos del usuario
        updated_user_data = request.json
        
        # Crear conexión con la base de datos
        with engine.connect() as connection:
            # Construir query de actualización
            query = update(users_table).where(users_table.c.id == user_id).values(
                username=updated_user_data['username'],
                email=updated_user_data['email']
            )
            
            # Ejecutar query de actualización
            result = connection.execute(query)

            connection.commit()

        
        if result.rowcount == 0:
            return {'message': 'Usuario no encontrado'}, 404
        else:
            return {'message': 'Usuario actualizado'}, 200
            
    # Eliminar usuario
    @api.doc(description='Eliminar un usuario existente', responses={204: 'Usuario eliminado', 404: 'Usuario no encontrado'})
    def delete(self, user_id):
        # Create a database connection
        with engine.connect() as connection:
            # Construir query de eliminación
            query = delete(users_table).where(users_table.c.id == user_id)
            
            # Ejecutar query de eliminación
            result = connection.execute(query)
            
            connection.commit()
        
        if result.rowcount == 0:
            return {'message': 'Usuario no encontrado'}, 404
        else:
            return {'message': 'Usuario eliminado'}, 204
        
class UsersResource(Resource):

    # Obtener todos los usuarios
    @api.doc(description='Obtener todos los usuarios', responses={404: 'Usuarios no encontrados'})
    @api.marshal_with(user_model, as_list=True)
    def get(self):
        # Crear conexión con la base de datos
        with engine.connect() as connection:
            # Construir la query para seleccionar todos los datos
            query = select(
                users_table.c.id,
                users_table.c.username,
                users_table.c.email
            )
            
            # Ejecutar la query para obtenere todos los datos del fech
            results = connection.execute(query).fetchall()

            # Si el usuario existe retornar datos, sino retornar mensaje de  error
            if results:
                return results
            else:
                api.abort(404, 'Usuarios no encontrados')

    # Crear un nuevo usuario
    @api.doc(description='Crear un nuevo usuario', responses={201: 'Usuario creado'})
    @api.expect(user_model)
    def post(self):
        # Extraer los datos del usuario
        new_user_data = request.json
        
        # Crear conexión con la base de datos
        with engine.connect() as connection:
            try:
                # Construir la query para introducir datos
                query = insert(users_table).values(
                    username=new_user_data['username'],
                    email=new_user_data['email']
                )
                
                # Ejecutar la query para introducir datos nuevos
                connection.execute(query)
                connection.commit()

                # Retonar mensaje cuando el usuario ha sido creado
                return {'message': 'Usuario creado'}, 201
            except Exception as e:
                # Retornar mensaje de error si no se ha podido crear el usuario
                return {'error': str(e)}, 500


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UsersResource, '/users')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
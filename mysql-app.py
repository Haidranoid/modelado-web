from flask import Flask, jsonify, render_template
import mysql.connector as sql

app = Flask(__name__)

# Configuración de la conexión
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',  # O la IP del servidor MySQL
    'database': 'prueba',
    'port': 3306  # Puerto por defecto de MySQL
}

def get_connection():
    try:
        # Conectar a la base de datos
        connection = sql.connect(**config)

        if connection.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            return connection

    except sql.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")

def close_connection(connection):
    # Cerrar conexión
    connection.close()
    print("🔒 Conexión cerrada.")

def insert_row(connection, numerito):
    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    sql = "INSERT INTO pruebita (numerito) VALUES (%s)"
    values = (numerito,)

    # Ejecutar una consulta de prueba
    cursor.execute(sql, values)
    connection.commit()
    print("Datos insertados con exito!")

    # Cerrar cursor y conexión
    cursor.close()

def get_data(connection):
    """Función para obtener los valores de la tabla pruebita."""
    data = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pruebita")
        data = cursor.fetchall()  # Lista de tuplas [(id1, valor1), (id2, valor2), ...]

        cursor.close()
        connection.close()
    except sql.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")

    return data


@app.route('/')
def index():
    return render_template('index-mysql.html')

@app.route('/data')
def data():
    """Endpoint que devuelve los datos en formato JSON."""
    connection = get_connection()
    data = get_data(connection)
    close_connection(connection)

    return jsonify({'labels': [d[0] for d in data], 'values': [d[1] for d in data]})

if __name__ == '__main__':
    app.run(debug=True)

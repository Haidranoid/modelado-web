from mysql.connector import connect, Error

def crear_conexion():
    try:
        conexion = connect(
            host='localhost',
            port=3306,
            user='root',
            password='password',
            database='modelado_web'
        )

        if conexion.is_connected():
            print("Conexion exitosa a la base de datos")
            return conexion

    except Error as e:
        print("Error al conectar a la base de datos")
        return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexion cerrada")

def obtener_pesos(connection):
    data = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pesos")
        data = cursor.fetchall()

        pesos = [float(valor) for valor in data[0]]

        cursor.close()
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")

    return pesos

def obtener_tethas(connection):
    data2 = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tethas")
        data2 = cursor.fetchall()

        tethas = [float(valor) for valor in data2[0]]


        cursor.close()
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")

    return tethas

if __name__ == '__main__':
    conexion = crear_conexion()

    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT VERSION()")
        resultado = cursor.fetchone()
        print("Version de MySQL:", resultado[0])

        cursor.close()
        cerrar_conexion(conexion)
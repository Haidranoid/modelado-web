from flask import Flask, jsonify, render_template, request
from conexion_db import *
from model_weight_XOR import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index-xor.html')

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    x = float(data.get('x'))
    y = float(data.get('y'))

    print(f"Valores recibidos: x={x}, y={y}")

    conexion = crear_conexion()
    if conexion:
        pesos = obtener_pesos(conexion)
        tethas = obtener_tethas(conexion)
        print(pesos)
        print(tethas)
        cerrar_conexion(conexion)

        weights_1_2_3_4 = [
            [pesos[0],pesos[1]],
            [pesos[2],pesos[3]]
        ]

        print(type(weights_1_2_3_4[0][0]))  # Debe ser float
        print(type(tethas[0]))  # Debe ser float

        tethas_1_2 = [tethas[0], tethas[1]]

        weights_5_6 = [pesos[4], pesos[5]]

        tetha_3 = tethas[2]

        result = f_xy(x, y, weights_1_2_3_4, tethas_1_2, weights_5_6, tetha_3)


        return jsonify({
            'x': x,
            'y': y,
            'pesos': pesos,
            'tethas': tethas,
            'result': result
        })
    else:
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente entrenado
modelo = tf.keras.models.load_model("celsius_to_fahrenheit_model.keras")

@app.route('/')
def index():
    return render_template('index-IA.html')

@app.route('/convert', methods=['POST'])
def convertir():
    try:
        datos = request.get_json()
        celsius = float(datos['celsius'])  # Convertir entrada a float

        # Realizar la predicción con el modelo
        resultado = modelo.predict(np.array([[celsius]]))

        # Convertir float32 a float nativo de Python
        fahrenheit = float(resultado[0][0])

        return jsonify({'fahrenheit': fahrenheit})  # Serializar correctamente
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Manejar errores

if __name__ == '__main__':
    app.run(debug=True)

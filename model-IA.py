import tensorflow as tf
import numpy as np

# Datos de entrenamiento
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38, 50, 75, 100, -20, 30], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100, 122, 167, 212, -4, 86], dtype=float)

# Definir el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

# Entrenar el modelo
print("Entrenando el modelo...")
model.fit(celsius, fahrenheit, epochs=750, verbose=0)
print("Modelo entrenado.")

# Guardar en formato .keras
model.save('celsius_to_fahrenheit_model.keras')
print("Modelo guardado en formato .keras.")

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

Patrones = [
    [1,1]
]

Clases = np.array([
    [0]
])

Datos_entrenamiento = np.array(Patrones,"float32")

modelo = Sequential()
modelo.add(Dense(1,input_dim=2, activation = 'sigmoid'))
modelo.add(Dense(1,activation='sigmoid'))

modelo.compile(loss='mean_squared_error',optimizer='adam', metrics = ['binary_accuracy'])

modelo.fit(Datos_entrenamiento,Clases,epochs=1000, verbose=1)

print(modelo.get_weights())
print(modelo.predict(np.array([[1,1]])))
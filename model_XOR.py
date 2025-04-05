import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

Patrones = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]
Clases = np.array([
    [0],
    [1],
    [1],
    [0]
])

Datos_entrenamiento = np.array(Patrones,"float32")

modelo = Sequential()
modelo.add(Dense(2,input_dim=2, activation = 'sigmoid'))
modelo.add(Dense(1,activation='sigmoid'))

modelo.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.5), metrics=['binary_accuracy'])

modelo.fit(Datos_entrenamiento,Clases,epochs=2000, verbose=1)

print(modelo.get_weights())
for p in Patrones:
    pred = modelo.predict(np.array([p]), verbose=0)
    print(f"{p} → {pred}")
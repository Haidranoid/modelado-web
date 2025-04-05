import math

# Pesos capa oculta
#weights_1_2_3_4 = [
#    [-6.4825053, 5.475634],
#    [6.364246, -5.8070006]
#]

#theta_1_2 = [-3.5674365, -3.006179]

# Pesos capa salida
#weights_5_6 = [9.252907, 9.361484]
#theta_3 = -4.5522704

def f_xy(x,y, weights_1_2_3_4, theta_1_2, weights_5_6, theta_3):
    h1 = g_fxy(weights_1_2_3_4[0][0] * x + weights_1_2_3_4[1][0] * y + theta_1_2[0])
    h2 = g_fxy(weights_1_2_3_4[0][1] * x + weights_1_2_3_4[1][1] * y + theta_1_2[1])

    output = g_fxy(h1 * weights_5_6[0] + h2 * weights_5_6[1] + theta_3)
    return output

def g_fxy(fxy):
    return 1 / (1 + math.exp(-fxy))

vars = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]
#if __name__ == '__main__':
#    for v in vars:
#        result = f_xy(v[0], v[1])
#        print(f"{v} → {result}")
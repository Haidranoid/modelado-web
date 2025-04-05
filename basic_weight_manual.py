import math

weight_1 = 1
weight_2 = 2
teta = 3

def f_xy(x,y):
    return (weight_1 * x) + (weight_2 * y) + teta

def g_fxy(fxy):
    return 1 / (1 + math.exp(-fxy))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fxy_result = f_xy(1,1)
    g_fxy_result = g_fxy(fxy_result)
    print(g_fxy_result)
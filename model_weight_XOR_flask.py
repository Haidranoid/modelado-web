import math

# w(5)
alpha = 9.121551
# w(6)
beta = 9.227267
# teta(3)
teta = -4.4863048

def f_xy(x,y):
    return (alpha * x) + (beta * y) + teta

def g_fxy(fxy):
    return 1 / (1 + math.exp(-fxy))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fxy_result = f_xy(0,0)
    g_fxy_result = g_fxy(fxy_result)
    print(g_fxy_result)
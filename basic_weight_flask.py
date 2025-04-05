from flask import Flask, request, render_template
import math

app = Flask(__name__)

weight_1 = 1
weight_2 = 2
teta = 3

def f_xy(x, y):
    return (weight_1 * x) + (weight_2 * y) + teta

def g_fxy(fxy):
    return 1 / (1 + math.exp(-fxy))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            x = float(request.form['x'])
            y = float(request.form['y'])
            fxy_result = f_xy(x, y)
            result = g_fxy(fxy_result)
        except ValueError:
            result = "Error: Ingresa valores numéricos válidos"
    return render_template('index-fxy.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from flask import jsonify
# import requests

app = Flask(__name__)

dataRadio = []


# chamar todas as rotas aqui pelos links
@app.route("/")
def getHome():
  return render_template('home.html')

# - O servidor web deve ter uma rota para receber os dados via requests no formato json.
@app.route("/get/radio-data/analogico")
def getRadioDataAnalogico():
    r = requests.get('https://http://127.0.0.1:8000/')
    dataRadio.append(r.content)
    return jsonify(dataRadio)

@app.route("/get/radio-data/digital")
def getRadioDataDigital():
    r = requests.get('https://http://127.0.0.1:8000/')
    dataRadio.append(r.content)
    return jsonify(dataRadio)


# - O servidor web deve ter uma rota para exibir os últimos 10 dados recebidos;
@app.route("/show/radio-data")
def showRadioData():
    # analogico e digital
    tenLastData = []
    lista = list(range(100))
    for x in lista[-10:-1]:
        tenLastData.append(x)
    return jsonify(tenLastData)

# - O servidor web deve ter uma rota para exibir dois gráficos, um do sinal analógico e outro do sinal
# digital;
@app.route("/show/graficos")
def showGraficos():
  pass

# - O servidor web deve ter uma rota para acionar a saída digital no cliente (button) e um form para
# receber um valor numérico correspondente ao valor digital;
@app.route("/turn-on/radio", methods=['GET', 'POST'])
def turnOnRadio():
    if request.method == 'POST':
        if request.form.get('input-text') == '0':
            print("Desligar Rádio")
            # r = requests.get('https://http://127.0.0.1:8000/', params=[0])
        elif  request.form.get('input-text') == '1':
            print("Ligar Rádio")
            # r = requests.get('https://http://127.0.0.1:8000/', params=[1])
        elif request.form.get('button'):
            print('Botão')
            # r = requests.get('https://http://127.0.0.1:8000/', params=[1])
    return render_template('turn_on_radio.html')

 
if __name__ == '__main__':
 app.run(debug=True)
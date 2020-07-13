from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

run_with_ngrok(app)

# rota p/ ligar ou desligar o radio (0 / 1)
# exibir os valores neste servidos além de enviar!
@app.route("/")
def getRadioStatus():
  pass
  
# rota p/ aumentar o volume (0.....5.....10)
# exibir os valores neste servidos além de enviar!
@app.route("/radio")
def getRadioVolume():
 return render_template('radio.html')
 
if __name__ == '__main__':
 app.run(debug=True)

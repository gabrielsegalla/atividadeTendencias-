import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from flask import Flask, render_template
from dash.dependencies import Input, Output
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

# rota para receber os dados via requests no formato json
@app.route('/')
def getData():
  pass

# rota para exibir os últimos 10 dados recebidos
@app.route('/')
def getLastTen():
  pass

# rota para exibir os últimos 10 dados recebidos
@app.route('/')
def getLastTen():
  pass


if __name__ == '__main__':
 app.run()

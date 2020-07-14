from flask import Flask, render_template, request
from radio import Radio

app = Flask(__name__)


radio = Radio()

@app.route("/")
def getHome():
  return render_template('home.html')
  
@app.route("/radio", methods = ['GET','POST'])
def getRadio():
  if request.method == 'post':
    radio.set_status()
  else:
    return render_template('radio.html', status=radio.get_status(), set_status=radio.set_status())

@app.route("/radio/status")
def getStatus():
  pass

@app.route("/radio/frequency")
def getFrequency():
  pass

@app.route("/radio/status/set")
def setStatus():
  radio.set_status()

@app.route("/radio/frequency/set")
def setFrequency():
  pass

@app.route("/radio/frequency/next")
def setNextFrequency():
  pass

@app.route("/radio/frequency/previous")
def setPreviousFrequency():
  pass
 
if __name__ == '__main__':
 app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actone')
def actone():
    return render_template('actone.html')

@app.route('/actfive')
def actfive():
    return render_template('actfive.html')

@app.route('/actsix')
def actsix():
    return render_template('actsix.html')

app.run(host="localhost", debug=True)
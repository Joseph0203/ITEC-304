from lib2to3.pgen2.token import GREATER
from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
                    <h1>MAY I ASK YOU A QUESTION?</h1>
                    <form action='/greet'>
                        What is your Name? <input type='text' name='name'><br>
                        May I know one of your Characteristics? <input type='text' name='character'><br>
                        <input type='submit' value='Submit'>
              </body></html>
           """

@app.route('/greet')
def greet():
    name = request.args.get('name')
    character = request.args['character']
    if character == '':
        msg = 'So want it to be a secret, huh?'
    else:
        msg = character

    return """
        <html><body>
                    <h2>{0} is {1}<h2>
              </body></html>
           """.format(name, msg)


# Launch the Flask dev server
app.run(host="localhost", debug=True) 

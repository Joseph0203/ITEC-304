from lib2to3.pgen2.token import GREATER
from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html>
            <style>
                div{
                    padding: 40px 0 40px 0;
                    background-color: #FFCC99;
                    margin-top: 100px;
                    text-align: center;
                    margin: 100px 300px 0 300px;
                }
                h1{
                    text-shadow: 2px 2px 2px #CE5937;
                }
            </style>
    
            <body>
            <div class="container">
                    <h1>MAY I ASK YOU A QUESTION?</h1>
                    <form action='/greet'>
                        What is your Name? <br> <input type='text' name='name'><br><br>
                        May I know one of your Characteristics? <br> <input type='text' name='character'><br><br>
                        Do you play any sports? <br>
                        <input type="radio" id="yes" name="answer" value="Yes">
                            <label for="yes">Yes</label><br>
                        <input type="radio" id="no" name="answer" value="No">
                            <label for="no">No</label><br>
                        <input type="reset" value="Reset">
                        <input type='submit' value='Submit'>
                        
            </div>
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

    answer = request.args['answer']
    if answer == '':
        ms = 'you need to select from yes or no'
    elif answer == 'Yes':
        ms = 'So you play, huh?'
    else:
        ms = 'nerd'

    return """
        <html>     
        <body>
                <div>
                    <h2>{0} is {1}<h2>
                 {2} <br><br>

                <form action="/sport">
                    <label for="que">What sport do you play?</label><br><br>
                    <input type="text" id="que" name="que" value="put answer here..."><br><br>
                    <input type="submit" value="Submit">
                </form>
                </div>
              </body></html>
           """.format(name, msg, ms)

@app.route('/sport')
def sport():
    que = request.args.get('que')
    if que == '':
        mssg = 'So want it to be a secret, huh?'
    else:
        mssg = que

        return """
        <html><body>
                    <h2>So you play {0}<h2>

                    <form action="/question">
                    <label for="quest">When did you start playing {0}?</label><br><br>
                    <input type="date" id="start" name="trip-start" value="2018-07-22" min="2018-01-01" max="2018-12-31"><br><br>
                    <input type="submit" value="Submit">
                </form>


              </body></html>
           """.format(que, mssg)

@app.route('/question')
def question():
    quest = request.args.get('trip-start')
    if quest == '':
        msssg = 'So want it to be a secret, huh?'
    else:
        msssg = quest

        return """
        <html><body>
                    <h2>{0}, nice.<h2>
\
              </body></html>
           """.format(quest, msssg)



# Launch the Flask dev server
app.run(host="localhost", debug=True)
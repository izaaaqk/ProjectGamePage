from flask import Flask
from flask import request
from flask import render_template
import random

randomint = random.randint(0,5)

words = ["computer", "unicorn", "pizza", "cat", "bat", "tribe"]

correctWord = words[randomint]
def dashes(word):
    dashWord = ''
    for i in word:
        dashWord += "_"
    
    return dashWord
dashWord = dashes(correctWord)
guesses = 15

count = 0
message = 'Please Guess a Letter!'

app = Flask(__name__)

@app.route('/new')
def my_form():
    return render_template("index.html")
@app.route('/new', methods = ['Post'])
def my_form_post():
    global correctWord
    global count
    global dashWord
    
    message = 'Please Guess a Letter!'

    print(count)

    if count < guesses:
        count+=1
        inputGuess = request.form['inputGuess']

        if inputGuess not in correctWord:
            message = "Incorrect Guess"
            return render_template("index.html", message=message, word ="Word: " +str(dashWord), count = "Guesses Remaining: " + str(guesses-count))
        else:
            print("correct")
            message = "Correct Guess " + inputGuess
            dashWord = addCorrectLetter(dashWord, correctWord, inputGuess)
            if dashWord == correctWord:
                winCount= count
                count = 0
                randomint = random.randint(0,5)
                correctWord = words[randomint]
                dashWord = dashes(correctWord)
                return render_template("highscore.html", score = "Score: " +str(round(len(correctWord)/winCount*100,2)), message = "You Won")
            return render_template("index.html", message=message, guess="You Guessed " +inputGuess, word ="Word: " +str(dashWord), count = "Guesses Remaining: " + str(guesses-count))
    else:
        loseCount = count
        count = 0
        randomint = random.randint(0,5)
        correctWord = words[randomint]
        dashWord = dashes(correctWord)
        return render_template("highscore.html", score = "Score: " +str(round(len(correctWord)/loseCount*100,2)), message = "You Lost")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route("/highscore.html")
def highscore():
    return render_template('highscore.html')

@app.route("/login.html")
def login():
    return render_template('login.html')



def addCorrectLetter(dashWord, correctWord, inputGuess):
    positions = []
    
    print("correct guess " + inputGuess + ' ' + correctWord)
    pos = correctWord.find(inputGuess)
    if pos <0:
        return dashWord
    else:
        positions.append(pos)
        
        while pos<len(correctWord)-1:
            pos = correctWord.find(inputGuess, pos+1)
            if pos == -1:
                break
            positions.append(pos)
            



    list1 = list(dashWord)
    size = len(positions)
    for i in range(size):        
        list1[positions[i]] = inputGuess
        print (list1[positions[i]] + ' ' + str(i) + ' ' + inputGuess)

    dashWord = ''.join(list1)
    
    return dashWord




    




if __name__ == '__main__':
    app.run(debug=True)
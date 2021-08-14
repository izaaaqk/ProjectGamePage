from flask import Flask
from flask import request
from flask import render_template
import random

#Picking a random number between 0-5
randomint = random.randint(0,5)

#Array for random words
words = ["computer", "unicorn", "pizza", "cat", "bat", "tribe"]

#Picking a random word from the array to be used in the game
correctWord = words[randomint]

#This function takes the randomly chosen word and return the correct amount of dashes to be displayed on the page
def dashes(word):
    dashWord = ''
    for i in word:
        dashWord += "_"
    
    return dashWord
dashWord = dashes(correctWord)

#total number of guesses
guesses = 6

#initalize count to zero
count = 0

#inital message
message = 'Please Guess a Letter!'

app = Flask(__name__)

@app.route('/new')
def my_form():
    return render_template("index.html")

#Function fires when button is clicked
@app.route('/new', methods = ['Post'])
def my_form_post():
    global correctWord
    global count
    global dashWord
    
    message = 'Please Guess a Letter!'

#if count is less than guesses then get data from html
    if count < guesses:
        inputGuess = request.form['inputGuess']

#if letter is not in the word increment the count and update the page
        if inputGuess not in correctWord:
            count+=1
            message = "Incorrect Guess"
            hangmanImg = imagePicker(count)
            return render_template("index.html", message=message, word ="Word: " +str(dashWord), count = "Guesses Remaining: " + str(guesses-count), hangmanImg = hangmanImg)

#if letter is correct adds letter to dashes
        else:
            message = "Correct Guess " + inputGuess
            dashWord = addCorrectLetter(dashWord, correctWord, inputGuess)

#if the dashes is equal to the correct word you win and go to high score page otherwise update index page
            if dashWord == correctWord:
                winCount= count
                count = 0
                randomint = random.randint(0,5)
                correctWord = words[randomint]
                dashWord = dashes(correctWord)                
                return render_template("highscore.html", score = "Score: " +str(round(len(correctWord)/winCount*100,2)), message = "You Won")
            hangmanImg = imagePicker(count)    
            return render_template("index.html", message=message, guess="You Guessed " +inputGuess, word ="Word: " +str(dashWord), count = "Guesses Remaining: " + str(guesses-count), hangmanImg = hangmanImg)

#if count is not less then guesses you loose and navigate highscore.html
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


#takes dashWord, correctWord, inputGuess as variables and adds the correct letter to dashes then returs dashes with new letters
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


def imagePicker(count):
    switcher = {
        0: r"img/hangman0.jpg",
        1: r"img/hangman1.jpg",
        2: r"img/hangman2.jpg",
        3: r"img/hangman3.jpg",
        4: r"img/hangman4.jpg",
        5: r"img/hangman5.jpg",
        6: r"img/hangman6.jpg"
    }
    image = switcher.get(count, r"img/hangman0.jpg")
    return image
    

    




if __name__ == '__main__':
    app.run(debug=True)
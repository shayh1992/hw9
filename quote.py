
from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def display():
    
    with open('inspiration.txt') as fp:
        quotes = fp.read().split('\n')
    #quotes = quotes.split('\n')
    from random import randrange
    random_index = randrange(0,len(quotes))
    quotes = quotes[random_index]

    return render_template('quote.html' , quotes = quotes)

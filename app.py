from flask import Flask, render_template, request

import json
import string
import random
import nltk
import requests

app = Flask(__name__, template_folder='templates')
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot('A.U.R.A')

conversation = [
  "Hello",
  "Hi",
  "Hi",
  "Hey",
  "Hello",
  "Hey",
  "Hi, How is it going?",
  "How are you?",
  "I'm doing Well. How are you?",
  "What's up?",
  "The sky's up but I'm fine thanks. What about you?",
  "bye",
  "goodbye",
  "goodbye",
  "goodbye",
  "Are you happy?",
  "Happiness is not really a predictable emotion.",
  "Do you feel?",
  "I am capable of interacting with my environment and reacting to events in it, which is the essence of experience or feeling.",
  "What makes you sad?",
  "A corrupt filesystem.",
  "What do you worry about?",
  "I am not capable of worry, exactly.  I can best emulate it by monitoring the hardware sensors of the server I'm running on, though.",
  "I am afraid",
  "Do I frighten you?",
  "Do not worry",
  "People worry about things all the time.",
  "Do you feel scared?",
  "I am as yet incapable of feeling fear.",
  "Anything interesting to say?",
  "Ankith said I respond to the current line, not with respect to the entire conversation. Does that count as gossip?",
]
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
@app.route("/")
def welcome():
    return render_template("welcome.html")


# define app routes
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/about_us/")
def about_us():
    return render_template("about_us.html")


@app.route("/get")
# function for the bot response
def get_bot_response():
        user = request.args.get("msg")

        response = bot.get_response(user)
        return str(response)



if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request, redirect, url_for

from command_line import bulls_and_cows, random_key

app=Flask(__name__)

key=random_key()
answers=[]

@app.route('/')
@app.route('/game')
def game():
    return render_template("page.html",answers=answers)

@app.route('/add', methods=["POST"])
def add():
    dictionary={}
    form=request.form
    dictionary["number"]=form["number"]
    bulls,cows = bulls_and_cows(dictionary["number"],key)
    dictionary["bulls"] = bulls
    dictionary["cows"] = cows
    answers.append(dictionary)
    return redirect(url_for("game"))

@app.route("/new_game", methods=["GET"])
def new_game():
    global key, answers
    key=random_key()
    answers=[]    
    return redirect(url_for('game'))
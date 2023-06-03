from flask import Flask, render_template, request, redirect, url_for, session

from command_line import bulls_and_cows, random_key

app=Flask(__name__)
app.secret_key = 'DA-9A-C9-9D-AB-65'

def reset():
    global key, answers, num_list, n, win_status
    n=0
    win_status=False
    num_list=[]
    key=random_key()
    answers=[]

@app.before_request
def before_request():
    if 'visited' not in session:
        reset()

@app.route('/')
@app.route('/game')
def game():
    if 'visited' not in session:
        session['visited'] = True
    return render_template("page.html",answers=answers, n=n, win_status=win_status)

@app.route('/add', methods=["POST"])
def add():
    global win_status, n
    n+=1
    dictionary={}
    form=request.form
    number=form["number"]
    if number==key:
        win_status=True
    if number and (number not in num_list):
        num_list.append(number)
        dictionary["number"] = number
        bulls,cows = bulls_and_cows(number,key)
        dictionary["bulls"] = bulls
        dictionary["cows"] = cows
        answers.append(dictionary)
    return redirect(url_for("game"))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/new_game", methods=["GET"])
def new_game():
    reset()
    return redirect(url_for('game'))
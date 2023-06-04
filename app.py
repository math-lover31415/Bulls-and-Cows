from flask import Flask, render_template, request, redirect, url_for, session

from command_line import bulls_and_cows, random_key

app=Flask(__name__)
app.secret_key = 'DA-9A-C9-9D-AB-65'

def reset():
    session['n'] = 0
    session['win_status'] = False
    session['num_list'] = []
    session['key'] = random_key()
    session['answers'] = []

@app.before_request
def before_request():
    if 'visited' not in session:
        reset()

@app.route('/')
@app.route('/game')
def game():
    if 'visited' not in session:
        session['visited'] = True
    return render_template("page.html",answers=session.get('answers', []), n=session.get('n', 0), win_status=session.get('win_status', False), key=session.get('key', random_key()))

@app.route('/add', methods=["POST"])
def add():
    session['n'] = session.get('n', 0)+1
    dictionary = {}
    form = request.form
    number = form["number"]
    key = session.get('key', random_key())
    session['key'] = key
    if number == key:
        session['win_status'] = True
    if number and (number not in session.get('num_list', [])):
        session['num_list'] = session.get('num_list', []) + [number]
        dictionary["number"] = number
        bulls,cows = bulls_and_cows(number,key)
        dictionary["bulls"] = bulls
        dictionary["cows"] = cows
        session['answers'] = session.get('answers', []) + [dictionary]
    return redirect(url_for("game"))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/new_game", methods=["GET"])
def new_game():
    reset()
    return redirect(url_for('game'))
from flask import Flask, render_template, request , redirect
import random

app = Flask(__name__)

list = [0,1,2,3,4,5,6,7,8,9]

@app.get("/")
def index():
    integer = random.randint(0, 100)
    color = request.args.get("color", "white")
    return render_template("index.html", integer=integer, list=list, color=color)

@app.get('/<color>')
def redirect_to_index(color):
    return redirect('/', code=302)

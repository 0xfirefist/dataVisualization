import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from flask import render_template, Flask, request
import base64
from io import BytesIO

app = Flask("dev")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def visualize():
    x=list(map(float,request.form["xaxis"].split(",")))
    y=list(map(float,request.form["yaxis"].split(",")))
    if len(x)!=len(y):
        return "enter correct values"
    img=BytesIO()
    plt.plot(x,y)
    plt.savefig(img)
    return render_template("submit.html",img=base64.b64encode(img.getvalue()).decode())    

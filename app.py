import matplotlib.pyplot as plt
matplotlib.use('agg')
from flask import render_template, Flask, request
import base64
import io.BytesIO

app = Flask()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",method=["POST"])
def visualize():
    x=list(map(float,request.form["xaxis"].split(",")))
    y=list(map(float,request.form["yaxis"].split(",")))
    if len(x)!=len(y):
        return "enter correct values"
    img=BytesIO()
    plt.plot(x,y)
    plt.savefig(img)
    return render_template("submit.html",img=base64.b64encode(img))    

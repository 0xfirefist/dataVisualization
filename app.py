import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from flask import render_template, Flask, request, url_for
import base64
from io import BytesIO

app = Flask("dev")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/submit",methods=["POST"])
def visualize():
	try:
		x=list(map(float,request.form["xaxis"].split(",")))
		y=list(map(float,request.form["yaxis"].split(",")))
	except:
		return render_template("error.html")
	if len(x)!=len(y):
		return render_template("error.html")
	if len(x)==0 or len(y)==0:
		return render_template("error.html")
	img=BytesIO()
	if request.form["graph"] == "plot" :
		plt.figure()
		plt.plot(x,y)
		plt.title('LINE PLOT')
		
	if request.form["graph"] == "bargraph" :
		plt.figure()
		plt.bar(x,y)
		plt.title('BARGRAPH')
	
	if request.form["graph"] == "scatter" :
		plt.figure()
		plt.scatter(x,y)
		plt.title('SCATTER PLOT')


	plt.xlabel('X AXIS')
	plt.ylabel('Y AXIS')
	plt.xticks(range(0,int(max(x)+2)))
	plt.yticks(range(0,int(max(y)+2)))
	plt.grid(True)	
		


	plt.savefig(img)
	return render_template("submit.html",img=base64.b64encode(img.getvalue()).decode())  

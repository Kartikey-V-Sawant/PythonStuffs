from flask import Flask,request
app=Flask(__name__)
@app.route("/method",methods=["GET","POST"])
def method():
	if request.method=="POST":
		return "IT IS POST REQUEST"
	else: 
		return "You are using GET Request"
		
app.run()


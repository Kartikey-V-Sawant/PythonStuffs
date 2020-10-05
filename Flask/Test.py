from flask import Flask #import Flask Package
app=Flask(__name__) #instancing the flask object and passing the application name.

@app.route('/') #Creating Route -Currently it is pointing to the root of directory.
def welcome():
	return "This is Home Page"

@app.route('/contactus') #Creating Route -Currently it is pointing to the contact us.
def contactus():
	return "This is Contact us Page"
	
@app.route('/aboutus') #Creating Route -Currently it is pointing to the about us.
def aboutus():
	return "This is about us Page"
	
app.run() #this will start the server

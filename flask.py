from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__) #Creates instance of Flask and assigns to variable app. __name__ establishes the current directory that the flask app lives in, to find /static and /templates

users = [] #empty user llst for our instance testing, before we move on to databases for permanent save.



@app.route('/signup', methods=['GET', 'POST']) #/signup lets Flask know that it should handle requests to /signup. methods list the http methods that Flask should handle from /signup
def signup():    #signup function defines what to do when /signup is accessed
  if request.method == 'POST':   #if the user has clicked the submit button which POST
    user = request.form.get('username')
    pass = request.form.get('password')
    users.append.('user':user, 'pass':pass)  #adds user and pass to the users list as a dictionary value. So the list would look like ['user':'bob','pass':'bob123']
    return '<h2>Thanks for signing up, ' + user + '!</h2>' #a confirmation message for the user


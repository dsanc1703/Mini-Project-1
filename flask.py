from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__) #Creates instance of Flask and assigns to variable app. __name__ establishes the current directory that the flask app lives in, to find /static and /templates

users = [] #empty user llst for our instance testing, before we move on to databases for permanent save.



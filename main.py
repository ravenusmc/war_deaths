#This is the main file of the program that will actually run everything.

#import libraries which will be used in the project.
import pandas as pd
import numpy as np
from flask import Flask, session, redirect, url_for, escape, render_template, request
from pymongo import MongoClient
import bcrypt

#Setting up flask
app = Flask(__name__)

#This function will be the login page for the app
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login Page')


@app.route('/war_data')
def war_data():
    return render_template('war_data.html', title='Login Page')


#This line will actually run the app.
app.run(debug=True)
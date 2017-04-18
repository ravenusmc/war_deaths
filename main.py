#This is the main file of the program that will actually run everything.

#import libraries which will be used in the project.
import pandas as pd
import numpy as np
from flask import Flask, session, redirect, url_for, escape, render_template, request
from pymongo import MongoClient
import bcrypt

#importing files that I made for this project
from mongo import *

#Setting up flask
app = Flask(__name__)

#This function will be the login page for the app
@app.route('/', methods=['GET', 'POST'])
def login():
    #I am creating a member object which will be used to login to the site.
    member = User_Database()
    if request.method == 'POST':
        #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        #Now checking to see if the user is in the database.
        flag = member.check(username, password)
        print(flag)
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            return redirect(url_for('index'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            return redirect(url_for('sign_up'))
    return render_template('login.html', title='Login Page')

#This function is for the sign up page where users will go to sign up to use the
#program.
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    #This is the object that will deal with Mongo DB.
    member = User_Database()
    if request.method == 'POST':
        #Getting the correct data from the form that was submitted.
        username = request.form['username']
        password = request.form['password']
        #Here the identity object uses the add method to add the user to the mongo
        #databse. Once that is done, the user will be redirected to the index page.
        member.add(username, password)
        return redirect(url_for('index'))
    return render_template('sign_up.html', title='Sign Up Page')

#This function will bring the user to the index page.
@app.route('/index')
def index():
    return render_template('index.html', title='Login Page')

#This function will allow the user to select what type of war data they want to
#look at.
@app.route('/data')
def war_data():
    name = "Mike"
    return render_template('war_data.html', title='War Data Page')

@app.route('/sex_results', methods=['POST'])
def sex_results():
    sex = str(request.form['sex'])
    return render_template('sex_results.html', title="sex_results",  sex = sex)


#This line will actually run the app.
app.run(debug=True)

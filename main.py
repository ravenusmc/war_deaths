#This is the main file of the program that will actually run everything.

#import libraries which will be used in the project.
import pandas as pd
import numpy as np
from flask import Flask, session, redirect, url_for, escape, render_template, request
from pymongo import MongoClient
import bcrypt

#importing files that I made for this project
from mongo import *
from data import *

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
            session['username'] = request.form['username']
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
@app.route('/index', methods=['GET', 'POST'])
def index():
    #This line will ensure that the user is logged in.
    if 'username' not in session:
        return redirect(url_for('login'))
    name = session['username']
    if request.method == 'POST':
        data = Data()
        number_entered = int(request.form['number'])
        values = data.wounded(number_entered)
        print(values)
        return values
    return render_template('index.html', title='Login Page', name = name)

#This function will display the wars where a specific amount of people died.
@app.route('/death_numbers', methods=['POST'])
def death_numbers():
    data = Data()
    number_entered = int(request.form['number'])
    wars = data.dead(number_entered)
    return render_template('death_numbers.html', title='Death By the Numbers', numbers = wars, deaths = number_entered)

#This function will display the data where a specific amount of people were wounded
@app.route('/wounded', methods=['POST'])
def wounded():
    data = Data()
    number_entered = int(request.form['number'])
    wars = data.wounded(number_entered)
    print(wars)
    return render_template('wounded.html', title='Wounded in War', wounded = number_entered)

#This function is what will log out the user.
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

# set the secret key.  keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
app.run(debug=True)

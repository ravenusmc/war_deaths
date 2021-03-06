#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient
import bcrypt
from bson.son import SON

#This class will handle all of the members that join the site. It will also prevent
#unauthorized users from entering.
class User_Database():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.member #Creating the member DB
        self.db.members = self.db.members #Creating a members collection within the titanic DB

    def encrypt_pass(self, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed

    #This method will add a new member to the database.
    def add(self, username, password):
        self.db.members.insert_one({
            "username": username,
            "password": password
        })

    #This method will see if the user is actual member of the site.
    def check(self, username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        #I then search for a user that matches the username
        user = self.db.members.find_one({
            "username": username
        });
        #If user is not found then flag is set to False
        if str(user) == 'None':
            flag = False
        #If the user is found, then another check is done to see if the hidden
        #password matches the original one.
        else:
            #Setting the hashed variable to be used in the conditional statement.
            hashed = user['password']
            if bcrypt.hashpw(password, hashed) == hashed:
                #I don't believe I need this user real. I only need to return
                #the flag.
                user_real = self.db.members.find_one({
                    "username": username,
                    "password": password
                });
                flag = True
        return flag

    #These methods would be used for showing comments however, it was getting hot
    #and I had spent hours getting the comments section to work. I then realized
    #that the reason why I could not get it to work is because an error would be
    #thrown for users that did not have comments. Thus, in order ot fix this, I
    #would have to do a search to find only those users which had comments. Thus,
    #I decided simply to create a new data base, thoughts.py to solve my problem
    #quickly. 
    # def add_comment(self, username, comment):
    #     self.db.members.insert_one({
    #         "username": username,
    #         "comments":[
    #             SON([("comment", comment)])
    #         ]
    #     })
    #
    # def show(self):
    #     thoughts = self.db.members.find()
    #     return thoughts

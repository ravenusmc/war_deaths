#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient
import bcrypt

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
        password = password.encode('utf-8')
        user = self.db.members.find_one({
            "username": username
        });
        if str(user) == 'None':
            flag = False
        else:
            hashed = user['password']
            if bcrypt.hashpw(password, hashed) == hashed:
                user_real = self.db.members.find_one({
                    "username": username,
                    "password": password
                });
                flag = True
        return flag

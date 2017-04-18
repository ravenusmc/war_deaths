#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient

#This class will handle all of the members that join the site. It will also prevent
#unauthorized users from entering.
class User_Database():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.member #Creating the member DB
        self.db.members = self.db.members #Creating a members collection within the titanic DB

    #This method will add a new member to the database.
    def add(self, username, password):
        self.db.members.insert_one({
            "username": username,
            "password": password
        })

    #This method will see if the user is actual member of the site.
    def check(self, username, password):
        user_real = self.db.passengers.find_one({
            "username": username,
            "password": password
        });
        if str(user_real) == 'None':
            flag = False
        else:
            flag = True
        return flag

Skip to content
This repository
Search
Pull requests
Issues
Gist
 @ravenusmc
 Sign out
 Unwatch 1
  Star 1
 Fork 0 ravenusmc/war_deaths
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Pulse  Graphs  Settings
Branch: data Find file Copy pathwar_deaths/thoughts.py
2b89912  an hour ago
@ravenusmc ravenusmc added a feature to check for comments
1 contributor
RawBlameHistory
38 lines (31 sloc)  1.15 KB
#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient
import bcrypt
from bson.son import SON

#This class will handle all of the members who add comments to the site.
class Thoughts():

    #Setting up the initial database
    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.thought #Creating the member DB
        self.db.thoughts = self.db.thoughts #Creating a members collection within the titanic DB

    #Adding the comment to the database
    def add_comment(self, username, comment):
        self.db.thoughts.insert_one({
            "username": username,
            "comments":[
                SON([("comment", comment)])
            ]
        })

    #This method will return the comments to be displayed on the web page.
    def show(self):
        thoughts = self.db.thoughts.find()
        return thoughts

    def check_comment_present(self):
        thought = self.db.thoughts.find()
        if str(thought) == 'None':
            flag = False
        else:
            flag = True
        return flag
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help

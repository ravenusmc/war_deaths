#This file will hold the class that will manipulate the data from data.csv file.

#Importing files that will be used for the project
import pandas as pd
import numpy as np

#This class will deal with all the methods that will handle the data.
class Data():

    #This method will return the wars that get the amount of dead that the user entered
    def dead(self, number):
        self.__data = pd.read_csv('data.csv')
        self.__data = self.__data[(self.__data.Dead >= number)]
        count = 0
        wars = []
        while count < len(self.__data):
            war = self.__data.iloc[count][0]
            wars.append(war)
            count += 1
        return wars

    #This method will return the wars that get the amount of wouned that the user entered
    def wounded(self, number):
        self.__data = pd.read_csv('data.csv')
        self.__data = self.__data[(self.__data.Wounded >= number)]
        count = 0
        wars = []
        while count < len(self.__data):
            war = self.__data.iloc[count][0]
            wars.append(war)
            count += 1
        return wars

    #This method will return the wars that get the amount of wouned and dead
    #that the user wants to see
    def wounded_dead(self, number):
        self.__data = pd.read_csv('data.csv')
        self.__data = self.__data[(self.__data.Dead_Wounded >= number)]
        count = 0
        wars = []
        while count < len(self.__data):
            war = self.__data.iloc[count][0]
            wars.append(war)
            count += 1
        return wars

    #This method will allow the csv file to be used by D3.js. 
    def convert_csv_for_d3(self):
        self.__data = pd.read_csv('data.csv')
        df = pd.DataFrame(self.__data)
        return df


# data = Data()
# data.test()

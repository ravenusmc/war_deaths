#This file will hold the class that will manipulate the data from data.csv file.


#Importing files that will be used for the project
import pandas as pd
import numpy as np

#This class will deal with all the methods that will handle the data.
class Data():

    # def dead(self, number):
    #     self.__data = pd.read_csv('data.csv')
    #     wars = self.__data[(self.__data.Dead >= number)]
    #     print(wars)

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

    def wounded(self, number):
        self.__data = pd.read_csv('data.csv')
        self.__data = self.__data[(self.__data.Wounded >= number)]
        count = 0
        wars = []
        while count < len(self.__data):
            war = self.__data.iloc[count][0]
            wars.append(war)
            count += 1
        print(wars)
        return wars


data = Data()
data.wounded(30000)

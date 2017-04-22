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

    def dead(self):
        self.__data = pd.read_csv('data.csv')
        wars = self.__data[(self.__data.Dead >= 600000)]
        wars = wars.iat([0],[0])
        print(wars)
        # war_names = wars[[0]]
        # print(war_names[[0]][1])

data = Data()
data.dead()

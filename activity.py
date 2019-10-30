#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:08:23 2019

@author: tombalcombe
"""

import sys
import time

#Day activity usefulness checker!

class activity():
    def __init__(self):
        self.activity = []
        self.usefulness = []
        self.hour = []
    def add(self):
        activity_item = input("Type in your activity: ")
        no_of_hours = input("Type in number of hours you do this a day: ")
        try:
            no_of_hours_int = int(no_of_hours)
            if no_of_hours_int > 24 or no_of_hours_int <= 0:
                print("error Type in a number less than 24 / greater than 0.")
                self.add()
            self.activity.append(activity_item)
            self.hour.append(no_of_hours_int)
        except:
            print("error For number of hours, type in a number only.")
            self.add()
        self.add2()
    def add2(self):
        usefactor = input("Type in how beneficial this is, 1 being detrimental to you up to 10 being the most beneficial thing ever: ")
        try:
            usefulfactor1 = int(usefactor)
            usefulfactor2 = usefulfactor1 * 0.1
            if usefulfactor1 > 10 or usefulfactor1 < 1:
                print("error Type something between 1 and 10.")
                self.activity.pop()
                self.hour.pop()
                self.add()
            self.usefulness.append(usefulfactor2)
        except:
            print("error For how useful, type in a number only.")
            self.add2()
        self.check()
        self.add()
    def check(self):
        x = 0
        for i in self.hour:
            x = i + x
        if x > 24:
            print("error You've exceeded number of hours in day!")
            print(f"You have {24-x} hours remaining.")
            x = 0
            self.activity.pop()
            self.hour.pop()
            self.usefulness.pop()
            return()
        if x == 24:
            print("You have plotted in a full day of activities")
            self.calculate()
            sys.exit()
        print(f"Activities: {self.activity}")
        print(f"Hours: {self.hour}")
        print(f"Usefulness: {self.usefulness}")
        print(f"Please type in more activities for the day. You have used {x} hours and have {24-x} hours remaining in the day.")
        return()
    def calculate(self):
        yourscore = 0
        scorelist = []
        print("The perfect score is 0.0 which means all hours were spent usefully.")
        print("The higher the score, the worse")
        for activeindex, i in enumerate(self.activity):
            try:
                activescore = (self.hour[activeindex] / self.usefulness[activeindex])
            except:
                print("error It looks like you typed 24 hours for one activity that has a usefulness of 0. Try again.")
                day.add()
            yourscore = yourscore + activescore
            scorelist.append(activescore)
        print(f"Your score is {24-yourscore}.")
        time.sleep(2)
        print("Here are your activities and their corresponding scores:")
        for index, i in enumerate(scorelist):
            print(self.activity[index], (i-self.hour[index]))
        time.sleep(2)
        print("The higher the number, the worse.")
        print("")
        print("Consider lowering the number of hours of some of your activities with a worse score to improve them")
        print("The key is not to try and reach 0, but to get as close to 0 as possible given your lifestyle.")
        print("You could try changing the activities so they are more useful/beneficial to you.")
        print("Or reducing the number of hours of some activities, and increasing the hours of others.")
        print("")
        print("Hope this was helpful!")
        input("Press anything to quit...")
        sys.exit()
           
day = activity()
print("Day activity usefulness calculator")
input("press anything to begin")
day.add()

        
    
        

        

        

   

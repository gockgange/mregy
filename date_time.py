# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 06:53:20 2018

@author: Mregy
"""

#
# Example file for working with timedelta objects
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
 	##DATETIME OBJECTS
    #Get today's date from datetime class
    today=datetime.now()
	#print today
	# Get the current time
	#t = datetime.time(datetime.now())
	#print "The current time is", t
	#weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)
	#Days start at 0 for monday
days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# print ("Today is day number %d" % wd)
print ("today is: " + str(datetime.now()))
print ("which is a " + days[wd])
        
        # construct a basic timedelta and print it
# print (timedelta(days=365, hours=8, minutes=15))
# print today's date

# print today's date one year from now
print ("which date do you wanna know?")
x = int(input("Enter a number: "))
days_ask = x
print ("%d days from now it will be:" % days_ask +   str(datetime.now() + timedelta(days_ask)),)
#print ("in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))


wd_2 = (date.weekday(today) + days_ask)%7
print ("which is a " + days[wd_2])


#
## create a timedelta that uses more than one argument
## print (in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))
## How many days until New Year's Day?
#today = date.today()  # get todays date
#nyd = date(today.year, 1, 1)  # get New Year Day for the same year
## use date comparison to see if New Year Day has already gone for this year
## if it has, use the replace() function to get the date for next year
#if nyd < today:
#    print ("New Year day is already went by %d days ago" % ((today - nyd).days))

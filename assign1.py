#!/usr/bin/env python3

# OPS435 Assignment 1 - Fall 2021
# Program: assign1.py
# Author: Jeffrey Zheng
# Student Number: 020232513
# The python code in this file (assign1.py) is original work written by
# Jeffrey Zheng. No code in this file is copied from any other source 
# except those provided by the course instructor, including any person, 
# textbook, or on-line resource. I have not shared this python script 
# with anyone or anything except for submission for grading.  
# I understand that the Academic Honesty Policy will be enforced and 
# violators will be reported and appropriate action will be taken.

# Description: This script will take an inputted date in the DD-MM-YYYY format along with a positive or negative integer, and calculate the new date

# Date: 2023-07-11

import sys

def usage(): #takes no arguement and prints string to describe usage 
    print("Usage: assign1.py DD-MM-YYYY N")
    
def days_in_mon(month, year): #takes month and year int and calculates the max days in the month
    if month == 2: #if month is 2, then sets the day to 29 or 28 depending on if the leap_year function returns true or false
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 9, 10, 12]: #if month falls within these, then sets the max day to 31, if not then 30 
        return 31
    else:
        return 30

def valid_date(date): 
    if len(date) != 10: #checks if length of date is 10, if not prints error and returns valeu False
        print("Error: wrong date entered")
        return False

    str_day, str_month, str_year = date.split('-')
    day = int(str_day)
    month = int(str_month)
    year = int(str_year)

    if month < 1 or month > 12: #checks if month value is from 1-12 and if not prints error and returns false
        print("Error: wrong month entered")
        return False

    if day < 1 or day > days_in_mon(month, year): #checks if day value is less than 1 or more than the max day from the called days_in_mon function, and if so prints error and returns false
        print("Error: wrong day entered")
        return False

    return True #if all if checks pass then return true

def leap_year(year):
    leap = year % 4  #if the year is divisible by 4 then return True
    if leap == 0:
        return True

    leap = year % 100 # if the year is divisible by 10 then return False
    if leap == 0:
        return False

    leap = year % 400 # if the year is divisible by 400 then return True
    if leap == 0:
        return True

def after(today):
    str_day, str_month, str_year = today.split('-') #splts variable into day, month, year and converts to integers
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    maxdays = days_in_mon(month, year) #converts variable from called days_in_mon function to new maxdays variable

    tmp_day = day + 1 # next day

    if tmp_day > maxdays:
        to_day = tmp_day % maxdays  # if tmp_day is mopre than the max date then it resets to 1 and puts int to_day variable and adds 1 to month
        tmp_month = month + 1  
    else:
        to_day = tmp_day #sets tmp_da value to to_day and sets month value to tmp_month
        tmp_month = month + 0 

    if tmp_month > 12: #if tmp_month is more than 12 and sets month value to 1 and adds 1 to year value
        to_month = 1 
        year = year + 1 
    else:
        to_month = tmp_month + 0 #sets tmp_value to to_month

    next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year) #takes the new variables and converts back to a DD-MM-YYYY date format and puts in next_date variable
    return next_date

def before(today):
    str_day, str_month, str_year = today.split('-') #splts variable into day, month, year and converts to integers
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day - 1 # previous day

    if tmp_day < 1: # if previous day is less than 1, subtract 1 from month and get the correct new month in new variable
        tmp_month = month - 1 
        if tmp_month < 1: 
            tmp_month = 12 
            year -= 1
        to_day = days_in_mon(tmp_month, year)
        to_month = tmp_month
    else: #else no changes but new variables
        to_day = tmp_day
        to_month = month

    prev_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year) #takes the new variables and converts back to a DD-MM-YYYY date format and puts in next_date variable
    return prev_date
    
def dbda(firstdate, changedays):
    if changedays > 0: #if changedays variable is more than 0(its a positive number), then it calls after function
        for _ in range(changedays):
            firstdate = after(firstdate)
    elif changedays < 0: #if changedays variable is less than 0(its a negative number), then it calls before function
        for _ in range(-changedays):
            firstdate = before(firstdate)
    return firstdate

if __name__ == "__main__":
    if len(sys.argv) != 3: #checks if there are two arguements, and if not, executes usage function and exits script
        usage()
        sys.exit(1)

    firstdate = sys.argv[1] #sets arguement 1 to firstdate variable
    changedays = int(sys.argv[2]) #sets arguement 2 to changedays variable

    if valid_date(firstdate) != True: #executes valid_date function and exits script if return value is not true
        sys.exit(1)

    newdate = dbda(firstdate, changedays) #executes dbda with firstdate/changedays variables and stores in variable newdate
    print(newdate) #prints variable newdate
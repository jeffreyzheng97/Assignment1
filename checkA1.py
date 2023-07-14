#!/usr/bin/env python3

'''
This check script will run the sample tests on assignment 1 script
before submitting to blackboard by the students.
Please note that this script does not check the docstring of the script
or its functions.

Released by Raymond Chan on Oct 30, 2018
Updated for the 2021 Fall Semester version on September 28 2021

'''

import types
import sys
import os
import subprocess
import glob
from datetime import date, datetime


def preliminary_grading(stud_name):
    message = '\n== Preliminary A1 Test Run Report for '+stud_name+'==\nThe following is your preliminary test run report for assignment 1. Please review the report and fix all the errors identified before submitting your algorithm, python script, and test report to blackboard using the assignment 1 submission link which will be available on Monday, October 25, 2021.\n'
    return message

def get_a1_filename():
    filelist = glob.glob('*.py')
    try:
        filelist.remove('a1_template.py')
    except:
        pass
    try:
        filelist.remove('checkA1.py')
    except:
        pass
    if 'assign1.py' in filelist:
        return 'assign1.py'
    elif len(filelist) == 1:
        return filelist[0]
    else:
        raise FileNotFoundError


def get_days_between(stop, start=None):
    if start is None:
        startdate = datetime.combine(date.today(), datetime.min.time())
    else:
        startdate = datetime.strptime(start, '%d-%m-%Y')
    stopdate = datetime.strptime(stop, '%d-%m-%Y')
    num_days = (stopdate - startdate).days
    return num_days


def get_username_from_git():
    p = subprocess.Popen(
        ['git config user.name'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
        )
    userid = p.communicate()[0].decode('utf-8').strip("\n")
    if userid == None:
        print("You haven't configured your git properly. Run these two commands:")
        print("git config --global user.name '<your name>'")
        print("git config --global user.email '<your email>'")
        userid = 'student'
    else:
        return userid


if __name__ == '__main__':
    try:
        assignment1script = get_a1_filename()
    except FileNotFoundError:
        print("Your assignment could not be found.")
        print("Remember to rename a1_template.py to assign1.py.")
        print("There should be only one file in your directory beginning in assignment1 and ending in .py.")
        sys.exit()

    student = get_username_from_git()
    print(preliminary_grading(student))
    print('=' * 40)
    doc_marks = {}  # data dictionary for documentation mark
    total_doc_marks = 0
    # test running student's script
    tests = {1: ['01-01-2019 1', '02-01-2019'],
             2: ['01-01-2019 -1', '31-12-2018'],
             3: ['01-06-2020 365', '01-06-2021'],
             4: ['01-01-2019 365', '01-01-2020'],
             5: ['01-01-2018 500', '16-05-2019'],
             6: ['01-99-2018 1', 'Error: wrong month entered'],
             7: ['32-01-2018 1', 'Error: wrong day entered'],
             8: ['2018 2', 'Error: wrong date entered'],
             9: ['28-02-2020 1', '29-02-2020'],
            10: ['01-03-2020 -1', '29-02-2020'],
            11: ['29-06-2021 2', '01-07-2021'],
            12: ['01-01-2021 -366', '01-01-2020']
            }
    test_marks = {}
    for test_no in range(1, len(tests)+1):
        cmd = 'python3 ' + str(assignment1script) +' '+ tests[test_no][0]
        print('Test run command', test_no, ':', cmd)
        p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        result = p1.communicate()[0].decode('utf-8').strip('\n')
        expected = tests[test_no][1].strip('\n')
        if result == expected:
            print('--test passed--')
            test_marks[test_no] = 1
        else:
            print('--test failed--')
            print('---- expect:', expected)
            print('----  given:', result)
            test_marks[test_no] = 0
    print('Test Results:', test_marks)
    total_test_marks = 0
    for item in test_marks:
        total_test_marks += test_marks[item] 
    total_test_marks = total_test_marks / len(tests) * 30 
    print('Total test run marks: ', total_test_marks)
    grand_total = total_test_marks + total_doc_marks
    print('Total marks for script (max. 30):', grand_total)
#!/usr/bin/env python
"""Program: Welcome Script
Programmer: Michael Fryar
Created: August 19, 2017
Purpose: Illustrate basic python script
"""

def welcome_message(name):
#Prints out a personalised welcome message
    return "Keep it up and you will become a ninja, " + name + "!"

#Call the welcome message function with the input "Udacity Student"
#and print the output
print(welcome_message("Michael"))

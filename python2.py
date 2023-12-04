#!/usr/bin/python3

# How to use string formatters in python 
# Python str.format() method of string class allows you to do variable subtitutions and value formatting. This lets you concatenate
# elements together within a string through positional formatting. 

# Formatters work by putting one or more replacement fields or placeholders - defined by a pair of curly braces{} - into a string
# and calling the str.format method. 
print("Leone is {} percent qualified Software Engineer.".format(100))

# We can aslo asign a variable to be equal to the value of a string that has formatter placeholders 

open_string = "Leone is a {}."
print(open_string.format("Software Engineer"))

# Formatter in python allow you to use curly braces as placeholders for the values that you will pass through with the str.format()
# method.

# Using formatters with muiltiple placeholders
# You can use pair of curly braces when using formatters.

open_string1 = "His basic salary per month {} {}."
print(open_string1.format("is", "forty million kenyan shillings"))
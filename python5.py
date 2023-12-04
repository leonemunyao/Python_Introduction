#!/usr/bin/python3

# Python Modules
# If you quit the python interpreter and enter it again, the definitions you have made(functions and variables) are lost. Therefore
# if you want to write a somewhat longer program, you are better of using a text editor to prepare the input for the interpreter. 
# and running it with that files as input instead. This is known as creating a script. Python has a way to put definitions in a file and 
# use them in a script or interactive instance of the interpreter. Such a file is called a module. A module is a file containing 
# python definitions and statements. The filename is the module name. 

# Fibonacci number module
def fib(n): # write fibonacci series upto n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Fibonacci number module
def fib2(n):  # return fibonacci series upto n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# More on Modules
# A module can contain executable statements as well as function definitions These statements are intended to initialize the module
# Each module has its own private namespace which is used as the global namespace by all functions defined on the module.
# 
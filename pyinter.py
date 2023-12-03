# USING THE PYTHON INTERPRETER

# Invoking the Interpreter
# The pyhton interpreter is usually installed as /usr/local/bin/python3.12
# The interpreter functiions like somewhat the unix shell. When called with standard input connected to a tty device, it reads and executes commands interactively, when called with a file name argument
# or with a file as a standard input, it reads and executes a script from that file. The secodn way of starting the interpreter is python -c command [arg]... which executes the statements in command, analogous to the shell -c 
# option. Since python statements often contain spaces or other characters that are so special to the shell, it is usually advised to quote a command in its entirety. Some python modules are aslo useful as scripts. These can 
# be invoked using python -m module [arg]... which executes the source file for module as if you had spelled out its full name on the command line. When a script filed is used, it is sometimes useful to be able to run the script 
# and enter interactive mode afterwards. This can be done by passing -i before the script.

# Argument Passing
# When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assinged to the argv variable in the sys module. You can access the list by executing import sys. The length
# of the list is aleast one. When no script and no arguments are given, sys.argv[0] is an empty string. When the script name is given as '-'(meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is
# set to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c command or -m module are not consumed by the python interpreter's option processing but left in sys.argv for
# the command or module to handle. 

# Interactive Mode
# When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater than signs (>>>). For continuation lines it prompts
# with the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt 

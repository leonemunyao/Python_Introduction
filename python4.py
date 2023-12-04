#!/usr/bin/python3

# Break and continue statements and else clause loops
# The break statement breaks out of the innermost enclosing for or while loop 
# A for or a while can include an else clause. In a for loop, the else clause is executed after the loop reaches its final iterration
# In a while loop, its executed after the loop's condition becomes false. In either of the loops, else clause is not executed if
# the loop was terminated by a break. 

# Check this loop that searches for prime numbers.

for n in range(2, 26):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


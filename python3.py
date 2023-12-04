#!/usr/bin/python3

# Understanding the range function. 

for i in range(10):
    print(i)
# Given the endpoint is not part of the generated sequence. range(10) generates 10 values. 

list(range(0, 10, 3))

a = ['Leone', 'has', 'a', 'Land', 'Rover', 'Discovery', '110', 'the', 'latest', 'model']
for i in range(len(a)):
    print(i, a[i])
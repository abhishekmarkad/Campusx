"""
Find the factorial of a given number.
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5
"""
n=int(input('Enter Number '))
k=n
fab=1
while n>1:
    fab*=n
    n-=1
print(k,'! =',fab)    

"""
Problem 12:Write a program to print whether a given number is a prime number or not
"""
n=int(input('Enter Number'))

for i in range(2,n//2):
    if(n%i==0):
        print('Not Prime Number')
        break
else:
    print('prime Number')

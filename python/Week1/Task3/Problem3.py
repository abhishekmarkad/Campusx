"""
Problem 3:Write a program to pring the following pattern
    *
  * * *
* * * * *
"""
n=int(input('enter a number'))

for i in range(1,n+1,1):
    for j in range(0,n-i):
        print('  ',end='')
    for j in range(n-i,n):
        print('* ',end='')
    for j in range(n-i,n-1):
        print('* ',end='')    
    print()    

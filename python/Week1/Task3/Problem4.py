"""
Problem 4:Write a program to print the following pattern
1

2 1

3 2 1

4 3 2 1

5 4 3 2 1
"""

n=int(input('enter a number'))

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end='')
    print()    
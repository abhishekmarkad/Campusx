"""
Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
"""
import math
x=int(input('enter x'))
n=int(input('enter n'))
sum=0
for i in range(1,n+1):
   sum+=(math.pow(x,n)/i)
print(sum)   


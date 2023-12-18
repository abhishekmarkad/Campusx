"""
Problem 6: The natural logarithm can be approximated by the following series.
temp.jpg

If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.

"""
import math
x=int(input('enter x'))

sum=0

for i in range(1,8):
    sum+=(math.pow((x-1)/x,i))/2
print(sum)    
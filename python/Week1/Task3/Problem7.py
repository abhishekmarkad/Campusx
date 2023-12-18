"""
Problem 7 - Find the sum of the series upto n terms.
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.
"""
n=int(input('enter n'))

sum=0
number=2

for i in range(n):
    sum+=number
    number=number*10 + 2
print(sum)    
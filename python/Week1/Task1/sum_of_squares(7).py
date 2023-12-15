"""
Write a program to find the sum of squares of first n natural numbers where n will be provided by the user
"""
n=int(input('Enter the Number'))

#Formula for Sum of squares of n natural numbers: (n(n+1)(2n+1)) / 6

sum=(n*(n+1)*(2*n+1)) / 6
print('Sum of the squares of first ',n ," number  is ", sum)
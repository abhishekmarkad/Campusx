"""
Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user
"""
a=int(input('Enter the First term of AP'))
b=int(input('Enter the second term of AP'))
n=int(input('Enter the N, i will tell you Nth term of AP'))
d=b-a

#nth = a+(n-1)d.

nth_term=a+(n-1)*d

print(n,'th term of AP is ',nth_term)
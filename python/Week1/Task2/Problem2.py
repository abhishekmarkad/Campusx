"""
Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
"""
ang1=float(input('Enter Angle 1 in celcius'))
ang2=float(input('Enter Angle 2 in celcius'))
ang3=float(input('Enter Angle 3 in celcius'))

if(ang1+ang2+ang3 == 180):
    print('It form a Trianlge')
else:
    print("It doen't form a triangle")    
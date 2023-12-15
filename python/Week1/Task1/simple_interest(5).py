"""
Calculate Simple interest when Principal amount,rate of interest and time is provided by user 
I=p*r*t/100
"""
principat_amount=float(input('Enter principal Amount'))
rate=float(input('Enter Rate of Interest'))
Time=float(input('Enter Period of Time'))

interest=(principat_amount*rate*Time)/100
print('Interest ',interest,'[units ruppes/dollar]')
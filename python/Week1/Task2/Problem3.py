"""
Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
"""

cp=float(input('Enter CP'))
sp=float(input('Enter SP'))

if(cp>sp):
    print("ohh! you are having a loss.")
elif(cp<sp):
    print('congrats, you are at profit.')
else:
    print('You are neither having profit not loss.')        
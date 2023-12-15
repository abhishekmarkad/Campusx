"""
Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:
Dimensions of the milk tank
H = 20cm, L = 20cm, B = 20cm

Dimensions of the glass
h = 3cm, r = 1cm
"""
h=int(input('Enter height of tank'))
w=int(input('enter width of tank'))
b=int(input('enter breadth of tank'))

# (h*w*b)/(3.14*3*1*1)

no_of_milk=(h*w*b)//(3.14*3*1*1)

print('number of milk glasses ',no_of_milk)
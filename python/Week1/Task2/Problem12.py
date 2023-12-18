"""
Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
The numbers after the direction are steps.

! means robot stop there.

Please write a program to compute the distance from current position after a sequence of movement and original point.

If the distance is a float, then just print the nearest integer.
"""
import math
i=input('Move robot')
horizontal=0
vertical=0

while i.split(' ')[0]!='!':
    if(i.split(' ')[0]=='UP'):
        horizontal+=int(i.split(' ')[1])
    elif(i.split(' ')[0]=='DOWN'):
        horizontal-=int((i.split(' ')[1]))
    elif(i.split(' ')[0]=='LEFT'):
        vertical+=int((i.split(' ')[1]))
    else:
        vertical-=int((i.split(' ')[1]))  
    i=input('Move Robot')
else:
    print('distance travel',int(math.sqrt(horizontal*horizontal + vertical*vertical)))

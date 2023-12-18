"""
Problem 15:Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
Note: It may be assumed that the rectangles are parallel to the coordinate axis.

"""
x11,y11=[int(i) for i in input("enter First rectangel's left lower corner (x,y)" )]
x12,y12=[int(i) for i in input("enter First rectangel's right upper corner (x,y)" )]
x21,y21=[int(i) for i in input("enter second rectangel's left lower corner (x,y)" )]
x22,y22=[int(i) for i in input("enter second rectangel's right upper corner (x,y)" )]

if(x12<x21 or y12<y21 or x11>x22 or y11>y22):
    print('Not overlappiing')
else:
    print('Two rectangles are overllaping')
        
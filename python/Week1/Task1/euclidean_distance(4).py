"""
Calculate euclidean distance bewtween two point 
"""
import math
x1,y1=[int(i) for i in input('Enter First coordinate (x,y)').split(',')]
x2,y2=[int(i) for i in input('Enter Second coordinate (x,y)').split(',')]

euclidean_distance=math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

print('euclidean Distance between Two provided Coordinates is ',euclidean_distance,'units')
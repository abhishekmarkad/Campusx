"""Write a list comprehension that can flatten a nested list
Input
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
def flatten(l:list) -> list:
    output=[]
    
    for i in l:
        if(isinstance(i,list)):
            output.extend(flatten(i))
        else:    
         output.append(i)
    return output        
l=[
[1,2,3],
[4,5,6],
[7,8,[10,11]]
]

print(flatten(l))
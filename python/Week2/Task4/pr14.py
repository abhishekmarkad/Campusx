"""
Write a list comprehension that can transpose a given matrix
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
"""
def transpose(l:list) ->list :
    "considering it as matrix"
    r=len(l)
    c=len(l)
    output=[[0]*r for _ in range(c)]
    c_ind=0
    r_ind=0
    for i in l:
        c_ind=0
        for j in i:
           output[c_ind][r_ind]=j
           c_ind+=1
        r_ind+=1   
    
    return output     
            
    
l=[
[1,2,3],
[4,5,6],
[7,8,9]
]

print(transpose(l))
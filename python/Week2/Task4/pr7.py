"""
Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:

['1ac21', '23fg', '456', '098d','1','kls']
Output:

['456', '23fg', '1ac21', '1', 'kls', '098d']
"""
def product(x:str) -> int:
    pro=1
    for i in x:
        if(i>='0' and i<='9'):
            pro=pro*int(i)
    return pro        
            
list1=[i for i in input().split(" ")]

temp_list=[]

list1.sort(key=lambda x:product(x),reverse=True)

print(list1)


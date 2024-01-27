"""
### `Problem 12:` Write a program that can find the max number of each row of a matrix

**Example:**

Input:

```bash
[[1,2,3],[4,5,6],[7,8,9]]
```

Output:
```bash
[3,6,9]
```
"""
m=[[1,2,3],[4,5,6],[7,8,9]]

r=len(m)
c=len(m[0])
output=[]
for i in m:
    mx=None
    for j in i:
        if(mx is None):
            mx=j
        mx=max(mx,j)
    output.append(mx)    
print(output)
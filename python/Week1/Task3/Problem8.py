"""
###`Problem 8`: Write a program to print all the unique combinations of 1,2,3 and 4 

"""
c=0
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        if(j==i):
            continue
        for k in [1,2,3,4]:
            if(k==i or k==j):
                continue
            for m in [1,2,3,4]:
                if(m==i or m==k or m==j):
                    continue
                print(i,j,k,m)
                c+=1
print(c)                

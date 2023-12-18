"""
Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
"""

"""
euclidean therom 
ldm(a,b)=lcm(b-a,b) considering b is greater number 
  let's prove it first 
    let say lcm(a,b) is k 
     so a=k*x and b=k*y , x,y are some intergers

     let say b-a = c
             k*y-k*x=c
             k(y-x)=c 
     so we can say k(lcm of a,b) divides c        
     
     k divides a,b,c 
     
     lcm(a,b) >= lcm(b-a,b)

     lcm(c,a)=m
     c=m*x1
     a=m*y1 
     (x1,y1 are some integers)
     
     b=a+c = m*y1+m*x1 = m(x1+y1)

     so m divides a,b,c 
      k divides a,b,c




"""

a=int(input('enter first number'))
b=int(input('enter second number'))
a,b=min(a,b),max(a,b)
x=a
y=b
hcf=None
while a!=0:
    k=a    
    a=b%a
    b=k
    print(a,b)
    if(a==0):
        hcf=b
        break
print("LCM= ",x*y/hcf)
print("HCF= ",hcf)    

    
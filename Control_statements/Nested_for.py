"""
NESTED FOR LOOPS

#Pattern Printing

#Ascending order
n = eval(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

#Descending order
n = eval(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()


#Finding Prime Numbers
n = eval(input("Enter a number:"))
for i in range(1,n):
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f=f+1
    if f==2:
         print("Prime numbers are: ",i)
         
n = eval(input("Enter a number: "))
for i in range(2,n+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("---------------")

n = eval(input("Enter a number: "))
for i in range(2,n+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("---------------")


n=eval(input("Enter a number"))  #n=5
k=1
for i in range(1,n+1): 
    for j in range(1,i+1):   
        print(k,end="")   
        k=k+1
    print(end="\n")
"""
n=eval(input("Enter a number"))  #n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")  
    print(end="\n")     

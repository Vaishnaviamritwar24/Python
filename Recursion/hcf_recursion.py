#Highest comman factor

def hcf(a,b):  
    if(b==0):
        return a
    else:
        return hcf(b,a%b)  
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("HCF of {} and {} is {}: ".format(a,b,hcf(a,b)))

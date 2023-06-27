"""
while()
=======

intital value counter_variable
while counter_variable condition:
      ===============
	  ===============
	  ==============
	  update the counter_variable

for is normally used when the number of iterations is known.
while is normally used when the number of iterations is unknown.

#Program to print prime numbers

n=eval(input("Enter a number:")) 
flag=0
for i in range(2, n//2 +1):
    if n%i==0:
        flag=1
if flag==1:
    print("composit")
else:
    print("prime")

# Checks if the number is Pollindrum or not
n=eval(input("Enter the number:"))
#for i in range(1,n+1)
s=0
temp=n #(i)
#store a value in temp variable so that original number can be used for comparison
while n>0:
    r=n%10
    s=s*10+r
    n=n//10

if s==temp:
    print("Is a palindrome")
else:
    print("Not polindrum number")
    
#Program to print the Pollindrum numbers between 1 to  given limit
n=eval(input("Enter a number")) #131
for i in range(1,n+1):
    s=0
    temp=i
    while temp>0:
        r=temp%10
        s=s*10+r
        temp=temp//10

    if s==i:
        print("polindrum number",i)

#Checks if the number is armstrong or not
n=eval(input("Enter a number:"))
temp=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if sum==temp:
    print("Is an Armstrong number")
else:
    print("Not an Armstrong number")
    

#Program to print the ArmStrong numbers between 1 to  given limit

n=eval(input("Enter a number:")) #10
for i in range(1,n+1):
    temp=i
    sum=0
    while temp>0:
        sum=sum+(temp%10)*(temp%10)*(temp%10)
        temp=temp//10
        
    if sum==i:
        print("Is an Armstrong number",i)
    else:
        print("Not an Armstrong number",i)
    
"""
#Factorial of a given number
n=eval(input("Enter a number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print("Factoral of {} is {} ".format(n,fact))

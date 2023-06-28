#Assignment

#1
for i in "Myblog":
    print(i,'?')
print("----------")
    

for i in range (5):
    print(i)
print("----------")

for i in range (10,15):
    print(i)
print("----------")

#2 Write a program to print first 10 natural numbers
for i in range (1,11):
    print(i)
print("----------")

#3 Write a program to print first 10 even numbers
for i in range (1,21):
    if i%2==0:
        print("The even numbers are:",i)
print("----------")

#4 Write a program to print first 10 odd numbers
for i in range (1,21):
    if i%2!=0:
        print("The odd numbers are:",i)
print("----------")

#5 Write a program to print first 10 even numbers in reverse
for i in range (21,1,-1):
    if i%2==0:
        print("The even numbers in rev are:",i)
print("----------")

#6 Numbers accepted from user to print a table
num=eval(input("Enter a number"))
for i in range(1,11): 
    print(num*i)

#7 factorial of a number
n = eval(input("Enter a number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print("Factoral of {} is {} ".format(n,fact))

#9 Sum of digits of a number
n = eval(input("Enter a number"))
sum=0
while (n):
    sum=sum+n%10
    n=n//10
print("The sum of digits is:",sum)

#10 Prime number or not
n=eval(input("Enter a number:")) 
flag=0
for i in range(2, n//2 +1):
    if n%i==0:
        flag=1
if flag==1:
    print("composit")
else:
    print("prime")



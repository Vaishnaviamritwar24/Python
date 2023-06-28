#Test-4

#Print the pattern
n=eval(input("Enter a number:"))  #n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")  
    print(end="\n")
 
#Print the pattern(star pattern)
n = eval(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()

#Accept 10 numbers from the user and calculate their avg
sum=0
for i in range(10):
    n=eval(input("Enter the numbers:"))
    sum=sum+n
print("Average is:",sum/i)

# Program to display sum of odd and even numbers that fall between 12 and 37
Se=0
So=0
for i in range(12,38):
    if i%2==0:
        Se=Se+i
    else:
        So=So+i
print("Sum of even numbers is:",Se)
print("Sum of odd numbers is:",So)

#Display numbers which are divisible by 11 but not by 2 between 100 and 500
for i in range(100,500):
    if i%11==0 and i%2!=0:
        print(i)
        
#Print table of a number input from the user
n=eval(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#Write a program to print numbers from 1-20 except multiples of 2&3

for i in range(1,21):
    if i%3!=0 and i%2!=0:
        print(i)


        

#Assignment

#Perfect number or not (sum of its factors = number: fact of 6=1,2,3 i.e 1+2+3=6)
def Is_perfect(n):
    sum=0
    for i in range (1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("Perfect number:",n)

#Check for the given range of 1-1000
for i in range(1,1000):
    Is_perfect(i)
print("-----------------------------------")
    
#Write a program to determine the given number is Armstrong number or not using Functions
def Is_armstrong(num):
    s=0
    temp=num
    while num>0:
        s=s+(num%10)*(num%10)*(num%10)
        num=num//10
    if s==temp:
        print("Armstrong number:",s)
        
#Check for the given range of 1-1000
for i in range (1,1000):
    Is_armstrong(i)
print("-----------------------------------")
    
# Write a program to determine the given number is polindrum number or not using Functions
def Is_palindrome(num):
    sum=0
    temp=num
    while num>0:
        sum=sum*10+(num%10)
        num=num//10
    if sum==temp:
        print("Pallindrome nummber:",sum)

#Check for the range of 1-1000         
for i in range(1,1000):
    Is_palindrome(i)
print("-----------------------------------")

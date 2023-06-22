"""
IF ELSE
-----------
If the condition evaluates to True,

the code inside if is executed
the code inside else is skipped
If the condition evaluates to False,

the code inside else is executed
the code inside if is skipped

if condition:
    # code block to execute if condition is true
else:
    # code block to execute if condition is false
"""
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
    
#Positive or negetive
num = int(input("Enter a num:"))
if num>=0:
    print("The number {} is positive".format(num))
else:
    print("The number {} is negetive".format(num))

#Leap year or not

year=int(input("Enter a Year"))
if year%4 == 0:
    print("{} is Leap Year".format(year))
else:
    print("{} is Non Leap Year".format(year))

#Odd or even number
    
num1=int(input("Enter a number"))
if num1%2==0:
    print("{} is even".format(num1))
else:
    print("{} is odd".format(num1))

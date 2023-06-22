"""
Elif statements
----------------
Syntax:

if boolean_expression_1:
	statement(s)
elif boolean_expression_2:
	statement(s)
elif boolean_expression_3:
	statement(s)
else
	statement(s)
"""

# Program to print Day of the week
num=int(input("Enter day number: "))
if num==1:
    print("Sunday")
elif num==2:
     print("Monday")
elif num==3:
     print("Tueday")
elif num==4:
     print("Wednesday")
elif num==5:
     print("Thursday")
elif num==6:
     print("Friday")
elif num==7:
     print("Saturday")
else:
    print("Invalid Day")
    

#Determine number greater , lesser or equal to

x = 15
y = 20

if x>y:
    print("{} is greater than {}".format(x,y))
elif x==y:
    print("{} is eyal to {}".format(x,y))
else:
    print("{} is lesser than {}".format(x,y))


# Determine if the number is +ve or -ve and also range between 0-5

a = int(input("Enter a number: "))
if a<0:
    print("{} is a negetive number".format(a))
elif a==0:
    print("{} is zero".format(a))
elif a>0 and a<5:
    print("{} is in the range 0-5".format(a))
else:
    print("{} equal or greater than 5 ".format(a))
    

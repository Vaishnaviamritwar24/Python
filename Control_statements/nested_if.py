"""
Nested if
-----------
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)

"""

#Determine the maximum value amongst the three variables

x=eval(input("Enter a number:"))
y=eval(input("Enter a number:"))
z=eval(input("Enter a number:"))
if x>y:
    if x>z:
        max=x
    else:
        max=z
else:
    if y>z:
        max=y
    else:
        max=z
    
print("maximum value among {}, {} and {} is {}".format(x,y,z,max))

#check if the number is 200,150,100,50 else no such expression

var = eval(input("Enter a number:"))
if var < 200:
   print ("Expression value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   elif var < 50:
      print ("Expression value is less than 50")
else:
   print ("Could not find true expression")

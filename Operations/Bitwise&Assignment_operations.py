"""
Bitwise Operators:
==================
operations performed on bitlevel


bitwise And (&)
bitwise or  (|)
bitwise XOR (^)
leftshift   <<
rightshift  >>

decimal_num = 52
binary_num = bin(decimal_num)
print(binary_num)
"""
x=34  #100010
y=52  #110100 

#BitAnd
c= x&y
print(" BitAnd value is:",c)

#BitOr
c= x|y
print(" BitOr value is:",c)

#BitXor
c= x^y
print("BitXor value is:",c)

#LeftShift Operator (<<) 
a=10
b=a<<2
print(" LeftShift Operator value is",b)

#Right Shift Operator (>>)
a=10
b=a>>2
print(" RightShift Operator value is",b)

#ASSIGNMENT OPERATORS
print("ASSIGNMENT OPERATORS")

x+=20
print("Adding ",x)
x-=2
print("Subtracting ",x)
x*=3
print("Multiplying ",x)
y/=2
print("Dividing ",y)
y%=2
print("Modulo ",y)


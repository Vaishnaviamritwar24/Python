#Lambda functions

f=lambda x,y : x if x>y else y
print(f(10,20))

f=lambda x: x*x
print(f(4))

s=lambda n:"is even" if n%2==0 else "is odd"
print(s(5))
print(s(8))

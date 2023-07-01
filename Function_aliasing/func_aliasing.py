#function aliasing

def calculations(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a%b)
    print(a/b)
    print(a//b)
    
calculations(50,4)
cal=calculations #short name for the functions is called function aliasing
print("After aliasing")
cal(64,12)

#2
def calculations(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a%b)
    print(a/b)
    print(a//b)
    
calculations(50,4)
cal=calculations 
del calculations #we can still call by the alias name even if the og func is deleted
cal(64,12)

#To prove
def calculations(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a%b)
    print(a/b)
    print(a//b)
    
cal=calculations
cl=cal
print(id(calculations))
print(id(cal)) #both id is the same hence meaning both are pointing to same location
print(id(cl))


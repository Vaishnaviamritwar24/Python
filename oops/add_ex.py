"""
def add(x,y):
    return(x+y)

def add(x,y,z):
    return(x+y+z)

def add():
    x=0
    y=0
    return(x+y)
"""
def add(*arg):
    s=0
    for i in arg:
        s+=i
        return s
    
print(add())
print(add(10,20))
print(add(10,20,30,45,50))
print(add(10,20,45,65))

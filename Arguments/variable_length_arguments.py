#4. Variable length Arguements

def add(*a):
    print(a)
    print(type(a))
    s=0
    for i in a:
       s=s+i
    return s

print(add(1,2,3,4))
print(add(10,20,30,40,50,60))
print(add(1,2,3,4,5,6,7,8,9,10))


def printdetails(**items):
    print(items)
    print(type(items))
    for i in items.keys():
        print("Key is",i," And Value is ",items[i])

printdetails(a=10,b=20,c=30)
printdetails(empid=210475,ename="Sai",location="Hyd",pincode="500029")


# Nested function: When we define one function inside another function

#1
def disp():
    def show():
        print("Show Function")
    print("Display Function")
    show()
disp()

#2
def sample(x,y,z):  #x=10 y=20 z=30
    print("x={} y={} and z={}".format(x,y,z))

    def innerfunction(a,b): #a=20 b=30
         print("a={} b={} ".format(a,b))
         def innermost(k): #k=30
             print("k={} ".format(k))
         innermost(b)    

    innerfunction(y,z)
    

a=10
b=20
c=30
sample(a,b,c)

#3
def disp(st):
    def show():
        return "Show Function"
    result=show() + st+ " Display Function"
    return result

print(disp(" Display all"))

"""
#Global variable:
It is the one which is ont a part of any function. Hence can be used in any function

#local variable:
One which can be used only inside the function but cannot be used in any
"""
y=200 #global variable
def f1():
    x=10 #local variable
    global y
    print("x=",x)
    print("y=",y)
   
    y=3000
    print("Updated y=",y)
    
def f2():
    y=20
    print("y=",y)
    print("Global y=",globals()['y'])
    
    
def f3():
     print("y in F3 function is =",y)


f1()
f2()
f3()


    

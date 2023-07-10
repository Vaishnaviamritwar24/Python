#class ex1
class sample:
    x=10                #class variables or attributes

    def f1(self):       #class methods
        a=100            #local to method f1       
        print("a=",a)
        print("x=",sample.x)
    def f2(self):       #method
        b=200           #local to method f2   
        print("b=",b)
        print("x=",sample.x)
    def f3(self):
        print("current values:")
        self.f1()
        self.f2()
# x f1 and f2 are called members of a class sample
# will use . operator to access the members of a class . it(.) is member accessing operator
obj=sample()
obj.f1()
obj.f2()
obj.f3()
print("x value is",obj.x)

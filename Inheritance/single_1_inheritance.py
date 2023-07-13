#single inheritance

class MyBase:
    def __init__(self,x,y,z):
        print("This is MyBase class constructor")
        self.a=x
        self.b=y
        self.c=z
    def BaseDisplay(self):
        print("a={} b={} c={}".format(self.a,self.b,self.c))
        

class MyDerived(MyBase):
     def __init__(self,a,b,c,d,e):
        print("This is MyDerived class constructor") 
        super().__init__(a,b,c)
        self.i=d
        self.j=e
     def DerivedDisplay(self):
        print("i={} j={}".format(self.i,self.j))
        print("a={} b={} c={}".format(self.a,self.b,self.c))

ob=MyDerived(10,20,30,40,50)
ob.DerivedDisplay()
#ob.BaseDisplay()

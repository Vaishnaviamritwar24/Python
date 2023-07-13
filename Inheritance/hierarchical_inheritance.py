#Hierarchical inheritance

class Base:
    def display(self):
        print("\n I am display method from base class")

class child1(Base):
     def display(self):
        super().display()
        print("\n I am display method from child class 1")
    
class child2(Base):
      def display(self):
        super().display()
        print("\n I am display method from child class 2 ")
        

d=child1()
d.display()

print(child1.__mro__)  
print(child1.mro())  

d=child2()
d.display()

print(child2.__mro__)  
print(child2.mro())  

#hybrid inheritance

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

class Grandchild(child1,child2):
    def display(self):
        print("I am Display method from GrandChild class")
        

d=Grandchild()
d.display()

print(Grandchild.__mro__)  
print(Grandchild.mro())  

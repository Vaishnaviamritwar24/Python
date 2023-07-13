#Multi Level Inherintance

class Base1:
    def display(self):
        print("\n I am display method from base1 class")

class Base2(Base1):
     def display(self):
        print("\n I am display method from base2 class")
    
class derived(Base2):
      def display(self):
        print("\n I am display method from Derived class")

d=derived()
d.display()

print(derived.__mro__)  
print(derived.mro())  

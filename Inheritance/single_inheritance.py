#single inheritance

class Base:
    def display(self):
        print("\n I am display method from base class")

class derived(Base):
    
      def display(self):
        print("\n I am display method from Derived class")


d=derived()
d.display()

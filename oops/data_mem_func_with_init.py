#Class_ex2
class test:
    def __init__(self):
        a=0
        b=0
    def read(self):
        test.a=eval(input("enter a value:"))
        test.b=eval(input("enter b value:"))

    def print(self):
        print("A value is",test.a)
        print("B value is",test.b)

test_obj=test()
test_obj.read()
test_obj.print()

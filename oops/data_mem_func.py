class test:
    a=0
    b=0
    def read_data(self):
        test.a=eval(input("enter a value:"))
        test.b=eval(input("enter b value:"))

    def print_data(self):
        print("A value is",test.a)
        print("B value is",test.b)

test_obj=test()
test_obj.read_data()
test_obj.print_data()

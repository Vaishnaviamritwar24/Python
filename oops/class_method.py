class student:
    def __init__(self):
        print("This is constructor") #constructor will automatically called

    def display(self):
        print("This is instant method")
    @classmethod
    def class_method(cls):
        print("This is class method")
    @staticmethod
    def static_method():
        print("This is static method")

s1=student()
s1.display()
#display with class method
#student.display(self)-error

student.class_method()
student.static_method()

#accessing class_method with object
s1.class_method()
s1.static-method()

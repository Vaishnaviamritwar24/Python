class student:
    def __init__(self):
        self.rollno=0
        self.name=" "
        self.marks=[0,0,0,0,0,0]

    def read_data(self):
        print("\n Enter student details:")
        self.rollno=input("Enter roll.no:")
        self.name = input("Enter name:")
        self.marks[0]=eval(input("Enter marks of 1st subject:"))
        self.marks[1]=eval(input("Enter marks of 2nd subject:"))
        self.marks[2]=eval(input("Enter marks of 3rd subject:"))
        self.marks[3]=eval(input("Enter marks of 4th subject:"))
        self.marks[4]=eval(input("Enter marks of 5th subject:"))
        self.marks[5]=eval(input("Enter marks of 6th subject:"))

    def calculate(self):
        self.total=self.marks[0]+self.marks[1]+self.marks[2]+self.marks[3]+self.marks[4]+self.marks[5]
        self.avg= self.total/6
        if (self.marks[0]<35 or self.marks[1]<35 or self.marks[2]<35 or self.marks[3]<35 or self.marks[4]<35 or self.marks[5]<35 ):
            self.result = "Fail"
        elif self.avg>=60:
            self.result="First class"
        elif self.avg>=50:
            self.result="Second class"
        else:
            self.result="Pass"

    def display(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)
        print("Student marks in all subjects:",self.marks)
        print("Student average marks:",self.avg)
        print("Student Result:",self.result)

s1=student()
s1.read_data()
s1.calculate()
s1.display()

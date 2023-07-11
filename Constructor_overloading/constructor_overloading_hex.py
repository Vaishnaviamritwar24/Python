class student:
    count=0 #class variable or static variable
    def __init__(self,sno,sname,location): #it is a constructor ( invoke when object is created)
        student.count+=1
        self.rno=sno
        self.sname=sname
        self.location=location
    def display(self):  #instant method
        print("Roll Number is:",self.rno)
        print("Name is:",self.sname)
        print("Location is:",self.location)

s1=student("1","sai","hyd")
print("Address of s1",hex(id(s1)))
print("No of objects for student class",s1.count)
print("No of objects for student class",student.count)
s2=student("2","Ram","chennai")
print("Address of s2",hex(id(s2)))
print("No of objects for student class",s2.count)
print("No of objects for student class",student.count)
s1.display()
s2.display()

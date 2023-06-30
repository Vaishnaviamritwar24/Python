"""
Default arguments:
• Sometimes we can provide default values for our positional arguments
• If we are not passing any course then only default value will be considered
• After default arguments we should not take non default arguments
"""
#1
def f1(course="python"):
    print("course is:",course)

f1("c")
f1()

#2
def student_details(student_name,college="MAllaReddy",streetno="2nd Street",area="Ameerpet",pincode="519007",location="Hyd",collegephonenunber="9898989898"):
    print("Student name is",student_name)
    print("College is",college)
    print("Streetno is",streetno)
    print("Area is",area)
    print("Pincode is",pincode)
    print("Location is",location)
    print("Concat number is",collegephonenunber)

student_details("Rama")
student_details("Sai","SRM","3rd","Sathyabama","500009","Chennai","8989898989")
    

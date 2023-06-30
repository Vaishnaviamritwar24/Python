"""
Keyword only arguments:
• If we declare a function for accepting only keyword arguments then that
function will work only with keyword arguments.
"""

#1

def greet(name,dept):
 print(f"Hello {name}")
 print(f"Are you from {dept} department?")

greet(dept="EXTC",name="Vaishnavi")


#2

def sub(a,b):
    print("sub is:",a-b)
    
sub(a=20,b=10)
sub(b=7,a=35)

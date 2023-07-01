"""
Type of Arguements
=================
1. positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments

Positional arguments:
• The arguments which are passed to a function in correct positional order is
called positional arguments.
• The number of arguments and position of arguments must be matched. If
we change the order then result may be changed.
"""
#1
def greet(name,dept):
 print(f"Hello {name}")
 print(f"Are you from {dept} department?")

greet("Vaishnavi","EXTC")

#2
def sub(a,b):
    print("sub is:",a-b)
    
sub(20,10)
sub(10,20)
    

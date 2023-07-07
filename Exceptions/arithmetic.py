
try:
    a=eval(input("Enter 1st number:"))
    b=eval(input("Enter 2nd number:"))
    print(a/b)
    print(a*b)
    print(a-b)
    print(a+b)
    print(a%b)
except ZeroDivisionError as e:
    print("Divisor should not be zero",e)
except ValueError as e:
    print("Value Error is",e)
except IndexError as e:
    print("Index out of bound",e)
except Exception as e:
    print("Generic Exception",e)

finally:
    print("Thank you")

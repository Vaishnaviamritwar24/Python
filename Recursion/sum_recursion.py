# Sum of a number using recursion
#
def sum(n):
    if n>0:
        return (n + sum(n-1))
    else:
        return 0

n=eval(input("Enter a number:"))
print("Sum  of {} is {} ".format(n,sum(n)))

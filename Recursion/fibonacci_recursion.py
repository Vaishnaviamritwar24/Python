#Fibonacci using recursion

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

for i in range(10):
   print(fib(i),end=" ")

		
#Approach 2
def fib1(n):
     a=0
     b=1
     if n<=0:
         print("Not valid")
     elif n==1:
         print(a)
     else:
         print(a)
         print(b)
         for i in range(2,n):
             c=a+b
             a=b
             b=c
             print(c)
        
n=eval(input("Enter a number:"))
print(fib1(n))

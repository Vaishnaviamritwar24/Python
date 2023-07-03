# prime numbers


def is_prime(n):
    fact=0
    for i in range(1,n+1):
        if n%i==0:
            fact=fact+1
    if fact==2:
        return True
    else:
        return False
        
test_list = list(range(1,101))

test_prime=list(filter(is_prime,test_list))
print(test_prime)


#Reduce method

from functools import reduce

L = [10,20,30,40,50,60,70,80,90]
sum= reduce(lambda x,y:x+y,L)
print(sum)

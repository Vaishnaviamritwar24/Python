#max element using reduce method

from functools import reduce
L = [10,20,30,40,50,60,70,80,90]
max_element = reduce(lambda x,y: x if x>y else y,L)
print(max_element)

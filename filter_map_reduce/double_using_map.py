# Map method using labmda function

#1 Doubling values

L = [12,23,34,45,56,67,78,89,90]
double = list(map(lambda x: x*2,L))
print(double)


#2 Multiple lists

L1 = [2,3,4,5,6,7]
L2 = [9,18,27,13,14,15]

L3 = list(map(lambda x,y:x+y,L1,L2))
print(L3)

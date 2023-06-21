"""
#range data type
===============
range(start,end,step):
"""

print("The range is:")
for i in range(15):
    print(i)


print("The range is:")      
for i in range(1,15,2):
    print(i)

#Frozenset operations

#set01 = frozenset(["abc",4,2,3,5,"xyz"])
#print(set01)

#Lists as frozenset

set1 = frozenset([1, 2, 3, 5, 7, 10])
set2 = frozenset([2, 3, 4, 5, 6])

# Union
union = set1 | set2
print("The union is:",union)  

# Intersection
intersection = set1 & set2
print("The intersection is:",intersection)  

# Difference
difference = set1 - set2
print("The difference is:",difference)

#Passing dictionary to set as frozenset

Employee = {"emp_id":102, "emp_name":"Gayathri", "working_mode":"offline"}
set3 = set(Employee)
print("The set is:",set3)
fset = frozenset(Employee.values())
print("The frozenset is",fset)

# copying a frozenset
C = set1.copy()
print("The copied set C=",C)






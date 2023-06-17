"""
TUPLES and their operations
"""

t1 = (50,60 ,70,'Hello','My','name','is','Vaishnavi', 3.14)
tuple1 = (10,20,25,30,45,55,65,70)
tuple2 = ('a', 'b', 'c')

#Accessing Elements
print("Accessing Elements")
print("Element at index (0) is:",t1[0]) 
print("Element at index (1) is:",t1[1])

#Slicing
print("Slicing")
print("Sliced tuple is:",t1[1:4])

#Concatenation
concatenated_tuple = tuple1 + tuple2
print("The concatenated tuple is:",concatenated_tuple)

#Repetetion 
repeated_tuple =tuple2 * 3
print("The repeated tuple is:",repeated_tuple)

#Length
length = len(t1)
print("The length of the tuple is:",length)

#Maximuv & MInimum value
print("The max value from t1 is:",max(tuple1))
print("The min value from t1 is:",min(tuple1))

#Sum
print("The sum of tuple t1 is:",sum(tuple1))
print("Add 4 to the total sum:",sum(tuple1,4))

#Membership
print("'Hello' in t1",'Hello' in t1)  
print("50 in t1",50 in t1)
print ("10 in t1",10 in t1)
print("100 not in t1",100 not in t1)

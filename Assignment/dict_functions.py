# Passing and Returning different data structures in dictionary

def read_data_dictionary():
    student={}  
    print("\n Enter how many elements in the dictionary")
    n=eval(input("Enter no of subjects"))
    for i in range(n):
        sub=input("Enter {} subject ".format(i+1))
        marks=int(input("Enter Marks"))
        student[sub]=marks
    return (student)
def max_marks(s):
    max_mark=0
    for i in s.keys():
        if s[i]>max_mark:
            max_mark=s[i]
    return max_mark

def min_marks(s):
    min_mark=100
    for i in s.keys():
        if s[i]<min_mark:
            min_mark=s[i]
    return min_mark

def sum_marks(s):
    total_mark=0
    for i in s.keys():
            total_mark=total_mark+s[i]
    return total_mark

s=read_data_dictionary()
print(s)
print("Max Mark marks is:",max_marks(s))
print("Min Mark marks is:",min_marks(s))
print("Total marks is:",sum_marks(s))


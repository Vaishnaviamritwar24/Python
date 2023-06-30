#Sum Max and Min values for sets!!

def set_values():
    print("\n Enter no. of elements neend in a set:")
    n=int(input("Enter value"))
    set1=set()
    for i in range(n):
        set1.add(int(input("Enter {} value".format(i))))
    return(set1)

def sum_sets(set1):
    s=0
    for i in set1:
        s=s+i
    return s

def max_sets(set1):
    max(set1)
    return max

def min_sets(set1):
    min(set1)
    return min
    
set_items = set_values()
sum_of_sets = sum_sets(set_items)
print("Sum of set items is",sum_of_sets)


max_of_sets = max(set_items)
print("Max of set items is",max_of_sets)

min_of_sets = min(set_items)
print("Min of list items is",min_of_sets)



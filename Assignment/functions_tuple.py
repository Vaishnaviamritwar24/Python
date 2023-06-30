def Read_tuple_values():
    print("\n Enter number of elements needed in your tuple:")
    n=int(input("Enter value:"))
    tup=()
    y=list(tup)
    for i in range(n):
        y.append(int(input("Enter {} value".format(i))))

    return (y)

def sum_tuple(y):
    s=0
    for i in y:
        s=s+i
    return s

def max_tuple(y):
    max=y[0]
    for i in y:
        if max<i:
            max=i
    return max

def min_tuple(y):
    min=y[0]
    for i in y:
        if min>i:
            min=i
    return min
    
tuple_items=Read_tuple_values()
sum_of_tuple_items=sum_tuple(tuple_items)
print("Sum of list items is",sum_of_tuple_items)


max_of_tuple_items=max_tuple(tuple_items)
print("Max of list items is",max_of_tuple_items)

min_of_tuple_items=min_tuple(tuple_items)
print("Min of list items is",min_of_tuple_items)


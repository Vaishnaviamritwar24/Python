#sum max min  for list

def Read_list_values():
    print("\n Enter how many elements in the list you want")
    n=int(input("Enter value"))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value".format(i))))

    return (l)

def sum_list(l):
    s=0
    for i in l:
        s=s+i
    return s

def max_list(l):
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max

def min_list(l):
    min=l[0]
    for i in l:
        if min>i:
            min=i
    return min
    
list_items=Read_list_values()
sum_of_list_items=sum_list(list_items)


print("Sum of list items is",sum_of_list_items)


max_of_list_items=max_list(list_items)
print("Max of list items is",max_of_list_items)

min_of_list_items=min_list(list_items)
print("Min of list items is",min_of_list_items)



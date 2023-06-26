"""
FOR loop

#FOR LOOP ON A STRING
"""
#for loop to find the length and number of words in string without using len function
str1 = "Vaishnavi Amritwar"
cnt = 0
word_cnt = 0
for i in str1:
    print(i)
    cnt = cnt+1
    if i == " ":
        print(i)
        word_cnt = word_cnt+1
if cnt>=0:
    word_cnt=word_cnt+1 
print("The count of the string is: ",cnt)
print("The word count of the string is: ",word_cnt)

#for loop to find length using len
str1 = "Vaishnavi Amritwar"
print("The count of the string is: ",len(str1))

#Converting the string into upper case without using upper() function
str2 = "My name is Rachel"
upper_str="" #new string
for j in str2:
    if (ord(j)>=97 and ord(j)<=122):#ord provides an ascii value, here we check the ascii values of given string
        upper_str=upper_str+chr(ord(j)-32)#chr basically gives the alphabet value (inverse of ord) here we append the new string with the calc one
    else:
        upper_str=upper_str+j
print(upper_str)

#Converting the string into lower case without using lower() function
str2 = "MY NAME IS PHEOBE"
lower_str=""
for j in str2:
    if (ord(j)>=65 and ord(j)<=90):
        lower_str=lower_str+chr(ord(j)+32)
    else:
        lower_str=lower_str+j
print(lower_str)


#for loop on lists

list1 = [23,45,67,86,73,69]
sum = 0
min = list1[0]
max = list1[0]
cnt = 0
for i in list1:
    print(i)
    cnt = cnt+1
    sum+=i
    if i<=min:
        min = i
    if i>= max:
        max = i
print("The max value from the list is:",max)
print("The min value from the list is:",min)
print("The sum of the list is:",sum)
print("The average value of the list is:",sum/cnt)


#Removing the duplicates
list1 = [23,45,67,86,73,69,45,67,86,101,34,56,78,120]
final_list = []
for i in list1:
    print(i)
    if i not in final_list:
        final_list.append(i)
print("Result list is",final_list)

#another approach (using set coz set does not allow duplicate values)
list1 = [23,45,67,86,73,69,45,67,86,101,34,56,78,120]
(set(list1))
print("Final list is:",list1)

#for loop on tuple
tup1 = (23,45,67,86,73,69)
sum = 0
min = tup1[0]
max = tup1[0]
cnt = 0
for i in tup1:
    print(i)
    cnt = cnt+1
    sum+=i
    if i<=min:
        min = i
    if i>= max:
        max = i
print("The max value from the list is:",max)
print("The min value from the list is:",min)
print("The sum of the list is:",sum)
print("The average value of the list is:",sum/cnt)
print("Number of items in tuple ",cnt)


# For loop on Sets
set1={45,65,23,12,78}
cnt=0
max=0
min=0
sum=0
for each_set_item in set1:
    print(each_set_item)
    cnt=cnt+1
    sum=sum+each_set_item
    if max<=each_set_item:
        max=each_set_item
    if min>=each_set_item:
        min=each_set_item
print("Number of items in set ",cnt)
print("Max set element is",max)
print("Min set element is",min)
print("Sum of set elements is",sum)

# For loop on Dictionaries
colors = {"red": 3, "blue": 2, "green": 4}
count = 0
for i in colors.values():
    count += i
    print("Total count:",count)
print(colors.keys())
print(colors.values())





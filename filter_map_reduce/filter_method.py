# Filter method using lambda

#1 To find even numbers in the given list

nums = [2,31,17,28,39,40,53,71,85,97]

even_num = list(filter(lambda n : n%2==0,nums))
print("The even numbers are:",even_num)

#2 For a range of numbers

nums_list = list(range(1,101))
even_nums = list(filter(lambda n: n%2==0,nums_list))
print("The even numbers for the given range are:",even_nums)

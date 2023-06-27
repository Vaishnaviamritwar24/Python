
#Break statements:terminates the loop forcibly
i=1
while(i<=100):
    if i%3==0 and i%7==0:
        break
    print(i)
    i+=1
#here as 21 is a factor of 3 and 7 it stops at 20
    
#Pass statements are null operations
count = 0

while count < 5:
    if count == 3:
        pass  # Placeholder for future code
    else:
        print(count)
    count += 1



#continue: it will skip the current iteration and trnasfer the control to the begining of the loop (next iteration)
for i in 'python':
   if i=='h':
      continue
   print("letter:",i) #pyton
   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
 







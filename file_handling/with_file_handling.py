with open("abcd2.txt","w") as f:
 f.write("Hello\n")
 f.write("Hyderabad\n")
 print("is file closed?",f.closed)
 
print("is file closed?",f.closed)


with open("abcd2.txt","r") as f:
    print(f.read())
    print("is file closed?",f.closed)

print("is file closed?",f.closed)

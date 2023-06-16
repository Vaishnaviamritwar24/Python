"""
STRINGS AND THEIR OPERATIONS
"""

s1=" Hi I am Vaishnavi"
s2="Amritwar"

print("Indexing")
print(s2[2:7])

length = len(s1)
print("The length of s1",length)

lowercase = s1.lower()
print("String s1 in lowercase is:",lowercase)

uppercase = s1.upper()
print("String s1 in uppercase is:",uppercase)

strip = s1.strip()
print("String s2 strriped is:",strip)

words = s1.split(", ")
print("The split string is:",words)

string = ", ".join(s1)
print(string)

replaced = s1.replace("Hi", "Hello")
print("The replaced string is:",replaced)







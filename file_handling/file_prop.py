#Properties of file object

f=open("sample.txt","w")
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed)
f.close()
print("is file closed?",f.closed)



f=open("sample.txt","a+")
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed)
f.close()
print("is file closed?",f.closed)

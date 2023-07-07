#append()

try:
    f=open("test2.txt","a")
    data="This file is currently in append mode.\nIt won't override existing data.\nIf the specified file is not already available then this mode will create a new file."
    f.write(data)
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("File operations completed")

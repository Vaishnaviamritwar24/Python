
try:
    f=open("test1.txt","w")
    data="write():We can write the date to a file.\nThis file write mode.\nOpen an existing file for write operation.\nIf the file already contains some data then it will be overridden.\nIf the specified file is not already available then this mode will create that file."
    f.write(data)
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("File operations completed")


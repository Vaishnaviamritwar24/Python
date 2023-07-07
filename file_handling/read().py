#File handling
#read()


try:
    f=open("test1.txt","r")
    list_data=f.read(50)
    print(list_data)
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("File operations completed")

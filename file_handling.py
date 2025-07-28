try:
    f=open("filehandling.py","r") 
#print (f.write("# This is a file handling example in Python\n"))
    print(f.read())
    print("f mode is",f.mode)
    print("fname is",f.name)
finally:
    f.close()
    print("if the is closed",f.closed) 
with open("image.jpg", "rb") as f:
    content = f.read()
    print("File content read successfully.")
    f.close()
#append refers to adding content to the end of a file
#readlinre reads a single line from the file
#os.remove() is used to delete a file
#os.rename() is used to rename a file
#os.rmdir() is used to delete a directory
#with statement automatically handles file opening and closing
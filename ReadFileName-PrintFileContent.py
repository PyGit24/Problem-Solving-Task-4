# Program to get the file name and read the contents
print("Program to Get the Input File and Read the File content")
inpfile=str(input("Enter the name of the file with .txt extension to read:"))
rfile=open(inpfile,'r')
line=rfile.readline()
while(line!=""):
    print(line)
    line=rfile.readline()
rfile.close()
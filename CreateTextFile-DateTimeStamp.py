# importing module
from datetime import datetime

# current date and time
print("Program to Create a Text File and input the Timestamp in it")
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)

# converting datetime obj to string
str_current_datetime = str(current_datetime)

# creating a file object along with extension and writing the current time stamp

file_name = str_current_datetime+".txt"
file = open(file_name, 'w')
file.write(str_current_datetime)

print("File created : ", file.name)
file.close()
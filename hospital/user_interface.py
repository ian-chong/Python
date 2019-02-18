import employee_records 

print ("Welcome to NEXT Hospital")
print ("---------------------------")

user_name_list = ["Tom", "Nic", "Darren"]

username = input("Please enter your username: \n")
if username in user_name_list:
    password = input("Please enter your password: \n")

else:
    print ("Invalid username")


import re

def password_encry():
    password = input("Please enter your password\n")
    new_password = password
    new_password = re.sub("e", "3", new_password)
    new_password = re.sub("a", "4", new_password)
    new_password = re.sub("B", "8", new_password)
    new_password = re.sub("G", "5", new_password)
    new_password = re.sub("A", "4", new_password)
    print(new_password)

password_encry()

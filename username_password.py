username = input("Enter username:")
password = input("Enter password:")

if (username == "admin" and password == "pass"):
    print("success")
else:
    if (username != "admin"):
        print("wrong username")
    else:
        print("wrong password")
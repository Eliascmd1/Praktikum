import sys

with open("Versuch.txt", "r") as f:
    loginData = f.read().split(";")

wrong_password = 0
tries = 3
validUsername = False
user = 0
while not validUsername:
    userinput = input("Please enter your username: ")
    for i in loginData:
        userdata = i.split(",")
        if userinput == userdata[0]:
            print(f"Hello {userdata[0]}")
            validUsername = True
            user = userdata[0]
            break

while tries > 0:
    userinput2 = input("Please enter your password: ")
    password = ""
    for i in loginData:
        userdata = i.split(",")
        if user == userdata[0]:
            password = userdata[1]

    if userinput2 == password:
        print(f"Hello {user}")
        tries = 0
    else:
        wrong_password = wrong_password + 1
        tries = tries - 1
        if tries == 0:
            print("You tried too many times")
            sys.exit()
        else:
            print(f"You have {tries} tries left")
            print("Wrong password")
while True:
    changepassword = input("Do you want to change your password?(yes/no): ")
    if changepassword == "yes":
        newpassword = input("Please enter your new password: ")
        with open("Versuch.txt", "w") as f:
            for i in loginData:
                userdata = i.split(",")
                if userdata[0] == user:
                    loginData.pop(loginData.index(i))
            f.write(f"{user},{newpassword}")
            f.write(";")
            loginData.pop(-1)
            for i in loginData:
                f.write(f"{i};")
        break
    elif changepassword == "no":
        print("Goodbye")
        break
    else:
        print("You need to enter yes or no")
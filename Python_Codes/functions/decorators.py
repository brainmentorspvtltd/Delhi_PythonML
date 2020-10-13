def add():
    x = 5
    y = 5
    z = x + y
    print("Sum is",z)

login = True
def check_login(func):
    if login:
        print("Login Success")
    else:
        print("Login Failed")

    return add

@check_login
def comment():
    p = input("Enter your comment : ")
    print("Your comment : ",p)

comment()
# check_login(comment)
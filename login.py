import json

from signup import*

def login(user_name,Email,password):
    with open ("user_info.json","r") as k:
        a=json.load(k)
        if (user_name in a and a[user_name][0] == Email) :
            if a[user_name][1] == password :
                print("login succesfull hii",user_name)
            else:
                print("incorrect password please try again")
        else:
            print("incoorect password user name you need to signup first")
            signup()




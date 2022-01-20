import json
def signup():
    user_name = input ("enter your name ")
    Email = input ("enter your Email ")
    password = input ("enter your password ")
    with open ("user_info.json","r") as k:
        a = json.load(k)
        a[user_name] = [Email,password]
        a = json.dumps(a,indent=4)
        with open ("user_info.json","w") as k:
            k.write(a)
            print("signup complete")


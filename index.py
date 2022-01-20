from login import*

from signup import*

a = input ("do you want to login or signup for login please enter 1 or for signup enter 2 ")
if a =="1":
    x = input ("enter  your name ")
    y = input ("enter your Email ")
    z = input ("enter your password ")
    login(x,y,z)
elif a == "2" :
    signup()
else:
    print("you must enter 1 or 2 ")
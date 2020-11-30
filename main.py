import sqlite3
from sqlite3 import Error
import random
import setup

def registerUser():
    print("registerUser")
    id = len(setup.select_all_ids()) + 1
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    setup.addUser(id,username,password)

def signin():
    print("signIn")
    username = input("please enter your username: ")
    userinfo = setup.getUser(username)
    print(userinfo)

choose = input("would you like to: \n1:setupDB\n2:registerUser\n3:signIn\n4:listAllUsers\nanswer: ")
if choose == "1":
    setup.setupMain()
elif choose == "2":
    registerUser()
elif choose == "3":
    signin()
elif choose == "4":
    setup.select_all_user()
else:
    print("not valid input")

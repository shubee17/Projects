from Tkinter import *
from tkMessageBox import * 
from class_gui import *
import threading

class User :
    data = {}

    def __init__(self, name, random_list) :
        global tk
        if User.data[name] == None :
            tk = main( self.data, name, random_list )
            User.data[name] = tk

        else :
            return None



data = {}
with open("input.txt","r") as f_obj :
    for line in f_obj.readlines() :
        line = line.split()
        data[line[0]] = line[1]

random_list = []
string = "abcdefsti"
random_list = Generate_random(random_list,string)

print data
User.data = {key : None for key in data}
print User.data

while(True) :
    username = str(raw_input("Enter UserName :"))
    password = str(raw_input("Enter Password :"))

    if username in data and password == data[username] :
        obj = User(username, random_list)

    else :
        showerror("Invalid", "Username/Password")

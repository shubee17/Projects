from Tkinter import *
from dictionary import *
import random
import threading

def Generate_random(random_list,string):
    while(1):
        rand = random.choice(string)
        if rand not in random_list:
            random_list.append(rand)
            if len(random_list) == 9:
                return random_list


def display(check_list, data, name) :
    score = 0
    root = Tk()
    t = Text(root,width = 60, height=25, font=("Helvetica", 14))
    root.title("CrossWord Result")
    t.insert(END, "INPUT")
    t.insert(END, "\t")
    t.insert(END, "OUTPUT")
    t.insert(END, "\n\n")

    for i in range(len(check_list)) :
        t.insert(END, check_list[i][0])
        t.insert(END, "\t")
        t.insert(END, check_list[i][1])

        if check_list[i][1] == "Valid Word\n" :
            score += 1

    string = "\n\nSCORE .:\t" + str(score)
    t.insert(END, string)
    if score > 3 :
        string = "\n\nCONGRATULATIONS " + name + " ..!!! You Won"
    else :
        string = "\n\nBETTER LUCK NEXT TIME..!!!"

    t.insert(END, string)

    t.pack()
    data[name] = None




def check(random_list,counter,tk,final,index,a,check_list,data, name):
    #global counter, final, index
    if final :
        str1 = "".join(final)
        s = str1[0]
        lst =  dicton[str(s)]
        flag = 1
        for i in range(len(index)):
            x = index[i][0]
            x1 = index[i][1]
            if i == len(index) - 1:
                pass
            else:
                y = index[i+1][0]
                y1 = index[i+1][1]
                z = abs(x - y)
                z1 = abs(x1 - y1)
                if (z == 1 or z == 0) and (z1 == 1 or z1 == 0):
                    pass
                else:
                    flag = 0
                    break
        if flag == 1:
            if str1 in lst:
                check_list.append((str1,"Valid Word\n"))

            else :
                check_list.append((str1,"Invalid Word\n"))

        else :
            check_list.append((str1,"Invalid Path Selection\n"))

        counter += 1




   # print check_list[counter]

    final, index, a = [],[],[]
    Grid(random_list,counter,tk,final,index,a,check_list, data, name)

    if counter == 5 :
        display(check_list, data, name)



def fun1(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(int(row))
        a.append(int(column))
        index.append(a)
        button1.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun2(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button2.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun3(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button3.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun4(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button4.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun5(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button5.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun6(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button6.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun7(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button7.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r)

def fun8(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button8.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 

def fun9(r,i,row,column,a,final,index):
    if r in final:
        pass
    else:
        a.append(row)
        a.append(column)
        index.append(a)
        button9.config(bg = 'Green' ,activebackground='Green', relief=SUNKEN)
        final.append(r) 
        
def Grid(random_list,counter,tk,final,index,a,check_list, data, name):
    global button1,button2,button3,button3,button4,button5,button6,button7,button8,button9
    button1 = Button(tk,bg = "Yellow",text=random_list[0],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun1(random_list[0],button1,1,0,[],final,index))
    button1.grid(row=1,column =0,sticky = S+N+E+W)

    button2 = Button(tk,bg = "Yellow",text=random_list[1],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun2(random_list[1],button2,1,1,[],final,index))
    button2.grid(row=1,column = 1,sticky = S+N+E+W)

    button3 = Button(tk,bg = "Yellow",text=random_list[2],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun3(random_list[2],button3,1,2,[],final,index))
    button3.grid(row=1,column = 2,sticky = S+N+E+W)

    button4 = Button(tk,bg = "Yellow",text=random_list[3],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun4(random_list[3],button4,2,0,[],final,index))
    button4.grid(row=2,column = 0,sticky = S+N+E+W)

    button5 = Button(tk,bg = "Yellow",text=random_list[4],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun5(random_list[4],button5,2,1,[],final,index))
    button5.grid(row=2,column = 1,sticky = S+N+E+W)

    button6 = Button(tk,bg = "Yellow",text=random_list[5],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun6(random_list[5],button6,2,2,[],final,index))
    button6.grid(row=2,column = 2,sticky = S+N+E+W)

    button7 = Button(tk,bg = "Yellow",text=random_list[6],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun7(random_list[6],button7,3,0,[],final,index))
    button7.grid(row=3,column = 0,sticky = S+N+E+W)

    button8 = Button(tk,bg = "Yellow",text=random_list[7],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun8(random_list[7],button8,3,1,[],final,index))
    button8.grid(row=3,column = 1,sticky = S+N+E+W)

    button9 = Button(tk,bg = "Yellow",text=random_list[8],font=('Times 26 bold'),height = 4,width =8,command = lambda:fun9(random_list[8],button9,3,2,[],final,index))
    button9.grid(row=3,column = 2,sticky = S+N+E+W)

    check_Button = Button(tk,bg = "Red",activebackground = "Red",text="Check",font=('Times 26 bold'),height = 2,width =4,command = lambda:check(random_list,counter,tk,final,index,a,check_list, data, name))
    check_Button.grid(row=6,column = 0,sticky = S+N+E+W)

   # refresh_button = Button(tk,bg = "Purple",activebackground = "Purple",text="Refresh",font=('Times 26 bold'),height=2,width =4,command = lambda:Generate_random(random_list,string))
   # refresh_button.grid(row=6,column = 1,sticky = S+N+E+W)


def main( data, name, random_list ) :
    #global counter, tk
    final,index,a = [],[],[]
    check_list = []


    #global tk, random_list, counter, check_list
    counter = 0
    check_list = []

    string = "abcdefsti"
    #random_list = Generate_random(random_list,string)

    tk = Tk()
    tk.title("Puzzle Game")

    threading.Thread(target=Grid(random_list,counter,tk,final,index,a,check_list, data, name)).start()
    return tk

    tk.mainloop()


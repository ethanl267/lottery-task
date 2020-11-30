#Ethan lesch class2

from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("My lottery App")
root.config(bg="purple")
root.geometry("300x300")

#make the button to function so that you can input youre name and age to work
def enter():

    if int(entry.get())<18:
        messagebox.showinfo("You are underage")
    if int(entry.get())>=18:
        messagebox.showinfo("you can play")
        entry1_info=entry1.get()
        entry_info=entry.get()
        file=open('data.txt', "w")
        file.write("person name:"+ entry1_info)
        file.write("person age:"+ entry_info)
        file.close()
        root.withdraw()
        import lottery
        lottery.lottery()


#making label and entry for name and age
label = Label(root, text="Enter your Age")
label.place(x=80, y=20)
entry = Entry(root, text="enter age")
entry.place(x=50, y=70)

label1=Label(root, text="Enter your name")
label1.place(x=70 , y=150)
entry1=Entry(root,text="enter name" )
entry1.place(x=50, y=180)


#button to command
btn_enter=Button(root, text="enter" , width=20 , bg='blue' , fg='black', command=enter)
btn_enter.place(x=50, y=100)

root.mainloop()
from tkinter import *
from random import shuffle
from tkinter import messagebox

root = Tk()
root.title("My lottery App")
root.config(bg="purple")
root.geometry("500x500")

#textbox for information to generate into the textbox
my_text = Text(root, width=35, height=2)
my_text.place(x=100, y=210)


'''def Lotto_No():
    a = shuffle.randint(0, 50);
    b = shuffle.randint(0, 50);
    c = shuffle.randint(0, 50);
    d = shuffle.randint(0, 50);
    e = shuffle.randint(0, 50);
    f = shuffle.randint(0, 50);
    num1.set(a)
    num2.set(b)
    num3.set(c)
    num4.set(d)
    num5.set(e)
    num6.set(f)
    return


num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()'''

#labels and entries
label1 = Label(root, text='Enter Your Lottery Numbers', font=50)
label1.place(x=135, y=5)

textbox = Text(root, width=35, height=3)
textbox.place(x=100, y=100)


#define the generate to allow the functions of each entry to work
def generate():
    def winning():
        import random
        nums = random.sample(range(1, 49), 6)
        print(nums)
        return nums

    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    d = int(entry4.get())
    e = int(entry5.get())
    f = int(entry6.get())
    lot_list = [a, b, c, d, e, f]
    textbox.insert(1.0, lot_list)
    user = lot_list
    lotto = winning()
    my_text.insert(END, lotto)
    print(user)
    print(lotto)
    count = 0
    for i in user:
        if i in lotto:
            count += 1

    print("you got " + str(count) + " number(s) correct")

    if count == 0:
        messagebox.showinfo(" ", "You Won nothing")
        with open('data.txt', 'a') as file:
            for numbers in user:
                file.write("%s" % numbers)
    elif count ==1:
        messagebox.showinfo(" ", "you got 1 out of 6 you have won 100 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)
    elif count ==2:
        messagebox.showinfo(" ", "you got 2 out of 6 you have won 500 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)
    elif count ==3:
        messagebox.showinfo(" ", "you got 3 out of 6 you have won 1000 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)
    elif count ==4:
        messagebox.showinfo(" ", "you got 4 out of 6 you have won 4,000 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)
    elif count ==5:
        messagebox.showinfo(" ", "you got 5 out of 6 you have won 8,000 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)
    elif count ==6:
        messagebox.showinfo(" ", "you got 6 out of 6 you have won 10 ,000,000,00 rand")
        with open('data.txt', 'a') as file:
            for numbers in lotto:
                file.write("%s" % numbers)

    return lot_list

    # lotto = winning()
    # print(lotto)






#entries for the user numbers
entry1 = Entry(root, width=2)
entry1.place(x=100, y=50)
entry2 = Entry(root, width=2)
entry2.place(x=150, y=50)
entry3 = Entry(root, width=2)
entry3.place(x=200, y=50)
entry4 = Entry(root, width=2)
entry4.place(x=250, y=50)
entry5 = Entry(root, width=2)
entry5.place(x=300, y=50)
entry6 = Entry(root, width=2)
entry6.place(x=350, y=50)

#button to generate youre lottery numbers
btn1 = Button(root, text='generate', font=10, bg='blue', fg='black', command=generate)
btn1.place(x=200, y=170)

root.mainloop()

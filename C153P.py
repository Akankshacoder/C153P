from tkinter import*
import random as ran
root= Tk()
root.title("Testing Random Function")
root.geometry("500x500")
pass_word=[[[1,2,3,4,5,6,7,8,9,10],["A","B","C","D","E","F","G","H","I","J","K","L"],["Head","Tail"],["!","@","£","$","%","&"]]]

input = Entry(root)
input.place(relx=0.3, rely = 0.5, anchor = CENTER)

l1 = Label(root)
l1.place(relx= 0.5, rely=0.5, anchor= CENTER)

def grp():
    r1 = ran.randint(0, 9)
    r2 = ran.randint(0,11)
    r3 = ran.randint(0,1)
    r4 = ran.randint(0, 5)
    
    a1= pass_word[0][0][r1]
    a2= pass_word[0][1][r2]
    a3= pass_word[0][2][r3]
    a4= pass_word[0][3][r4]
    
    b= str(a1 )+ a2  +a3 + a4
    
    l1["text"]= "Guessed Password: "+ input.get()

b1 = Button(root, text="Generate Random Password", command= grp)
b1.place(relx= 0.5, rely=0.3, anchor= CENTER)


root.mainloop()
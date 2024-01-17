from tkinter import *
from tkinter import messagebox
import random
import time
L = ["Apple","Lemon","Cherry","Banana","Kiwi","Melon","Mango","Grape"]
L_length = len(L)
dict_cards = {}
clicked_cards = 0
fst= ""
scnd= ""
start = time.time()

game = Tk()
game.resizable(0,0)
game.title("Memory Game")

f1 = Frame(game)
f1.pack()

fonts = ['Helvetica', '15', 'bold']

bt1 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt1))
bt1.grid(row=0,column=0,padx=20, pady=40)
dict_cards[bt1] = ""

bt2 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt2))
bt2.grid(row=0,column=1,padx=20, pady=40)
dict_cards[bt2] = ""

bt3 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt3))
bt3.grid(row=0,column=2,padx=20, pady=40)
dict_cards[bt3] = ""

bt4 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt4))
bt4.grid(row=0,column=3,padx=20, pady=40)
dict_cards[bt4] = ""

f2 = Frame(game)
f2.pack()

bt5 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt5))
bt5.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt5] = ""

bt6 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt6))
bt6.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt6] = ""

bt7 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt7))
bt7.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt7] = ""

bt8 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt8))
bt8.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt8] = ""

f3 = Frame(game)
f3.pack()

bt9 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt9))
bt9.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt9] = ""

bt10 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt10))
bt10.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt10] = ""

bt11 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt11))
bt11.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt11] = ""

bt12 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt12))
bt12.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt12] = ""

f4 = Frame(game)
f4.pack()

bt13 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt13))
bt13.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt13] = ""

bt14 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt14))
bt14.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt14] = ""

bt15 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt15))
bt15.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt15] = ""

bt16 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt16))
bt16.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt16] = ""

def random_text():

    occurances = {"Apple":0,"Lemon":0,"Cherry":0,"Banana":0,"Kiwi":0,"Melon":0,"Mango":0,"Grape":0}
    
    for bttn in dict_cards:
        
        if len(L) > 0:
            random.shuffle(L)
            x = L[0]
            dict_cards[bttn] = x
            occurances[x] = occurances[x] + 1
        
            if occurances[x] == 2:
                L.remove(x)
        
def bttn_clicked(btn):
    global clicked_cards
    global fst
    global scnd
    clicked_cards = clicked_cards + 1
    
    if clicked_cards == 1:
        fst= btn
        btn.configure(text=dict_cards[btn],state=DISABLED) 
    
    if  clicked_cards == 2:
        scnd = btn
        btn.configure(text=dict_cards[btn],state=DISABLED)
        
        game.after(500,check_same)
        
def check_same():
    global clicked_cards
    global fst
    global scnd
    global L_length
    
    if scnd['text'] != fst['text']:
        fst.configure(text="",state="normal")
        scnd.configure(text="",state="normal")
    
             
random_text() 

game.mainloop()
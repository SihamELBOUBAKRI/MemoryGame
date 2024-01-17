from tkinter import *
from tkinter import messagebox
import random
import time
L= ["Apple","Lemon","Banana","Melon","Ananas","Kiwi","Orange","Cherry","Citron","Papaya"]
L_length = len(L)
game_end = 0
dict_cards = {}
clicked_cards = 0
fst_ = ""
scnd_ = ""
start = time.time()

game = Tk()
game.resizable(0,0)
game.title("Memory Game")

f1 = Frame(game,bg='#AC87C5')
f1.pack()

fonts = ['Helvetica', '10', 'bold']

bt1 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt1),bg="lightpink")
bt1.grid(row=0,column=0,padx=20, pady=40)
dict_cards[bt1] = ""

bt2 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt2),bg="lightpink")
bt2.grid(row=0,column=1,padx=20, pady=40)
dict_cards[bt2] = ""

bt3 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt3),bg="lightpink")
bt3.grid(row=0,column=2,padx=20, pady=40)
dict_cards[bt3] = ""

bt4 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt4),bg="lightpink")
bt4.grid(row=0,column=3,padx=20, pady=40)
dict_cards[bt4] = ""

f2 = Frame(game,bg='#756AB6')
f2.pack()

bt5 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt5),bg="lightpink")
bt5.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt5] = ""

bt6 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt6),bg="lightpink")
bt6.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt6] = ""

bt7 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt7),bg="lightpink")
bt7.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt7] = ""

bt8 = Button(f2,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt8),bg="lightpink")
bt8.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt8] = ""

f3 = Frame(game,bg='#AC87C5')
f3.pack()

bt9 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt9),bg="lightpink")
bt9.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt9] = ""

bt10 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt10),bg="lightpink")
bt10.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt10] = ""

bt11 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt11),bg="lightpink")
bt11.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt11] = ""

bt12 = Button(f3,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt12),bg="lightpink")
bt12.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt12] = ""

f4 = Frame(game,bg='#756AB6')
f4.pack()

bt13 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt13),bg="lightpink")
bt13.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt13] = ""

bt14 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt14),bg="lightpink")
bt14.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt14] = ""

bt15 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt15),bg="lightpink")
bt15.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt15] = ""

bt16 = Button(f4,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt16),bg="lightpink")
bt16.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt16] = ""

f5 = Frame(game,bg='#AC87C5')
f5.pack()

bt17 = Button(f5,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt17),bg="lightpink")
bt17.grid(row=1,column=0,padx=20, pady=40)
dict_cards[bt17] = ""

bt18 = Button(f5,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt18),bg="lightpink")
bt18.grid(row=1,column=1,padx=20, pady=40)
dict_cards[bt18] = ""

bt19 = Button(f5,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt19),bg="lightpink")
bt19.grid(row=1,column=2,padx=20, pady=40)
dict_cards[bt19] = ""

bt20 = Button(f5,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt20),bg="lightpink")
bt20.grid(row=1,column=3,padx=20, pady=40)
dict_cards[bt20] = ""

def center_window(window):
    window.update_idletasks()
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
    window.geometry("+%d+%d" % (x, y))
def show_popup():
    game.withdraw()  
    popup = Toplevel(game)
    popup.title("Welcome to Memory Game")
    label = Label(popup, text="Welcome to the Memory Game!\nClick 'Start Game' to begin.")
    label.pack(padx=10, pady=10)
    start_button = Button(popup, text="Start Game", command=lambda: [popup.destroy(), start_game()])
    start_button.pack(pady=10)
    center_window(popup)
    popup.protocol("WM_DELETE_WINDOW", lambda: [popup.destroy(), game.deiconify()])  
    popup.focus_force()


def start_game():
    random_text()
    game.after(100, game.deiconify)  



show_popup()


def random_text():
    
    occurances = {"Apple":0,"Lemon":0,"Banana":0,"Melon":0,"Ananas":0,"Kiwi":0,"Orange":0,"Cherry":0,"Citron":0,"Papaya":0}
    
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
    global fst_
    global scnd_
    
    
    clicked_cards = clicked_cards + 1
    
    if clicked_cards == 1:
        fst_ = btn
        btn.configure(text=dict_cards[btn],state=DISABLED) 
    
    if  clicked_cards == 2:
        scnd_ = btn
        btn.configure(text=dict_cards[btn],state=DISABLED)
        
        game.after(500,check_same)
        
def check_same():
    global clicked_cards
    global fst_
    global scnd_
    global game_end
    global L_length
    
    if scnd_['text'] != fst_['text']:
        fst_.configure(text="",state="normal")
        scnd_.configure(text="",state="normal")
    else:
        game_end = game_end + 1
        

    if game_end == L_length:
        messagebox.showinfo("MEMORY GAME", "You have spent "+str(int(time.time() - start))+" sec!")
        
        game.destroy()
            
    clicked_cards = 0
    
game.update_idletasks()
x = (game.winfo_screenwidth() - game.winfo_reqwidth()) / 2
y = (game.winfo_screenheight() - game.winfo_reqheight()) / 2
game.geometry("+%d+%d" % (x, y))
            
random_text() 

game.mainloop()
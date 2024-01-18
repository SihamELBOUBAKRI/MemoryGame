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

bt1 = Button(f1,font=(fonts),width="5",height="3",command=lambda:bttn_clicked(bt1),bg="lightpink")#command=lambda:bttn_clicked(bt1) --> kat3iyet lina 3la l fonction li ghadi dar ila derna click l card
bt1.grid(row=0,column=0,padx=20, pady=40)#lgrid bach nt7ekmo f blasa dyal button
dict_cards[bt1] = ""#kat3emer l button b wa7d string khawi (empty string) 7it men be3d kan3emroha b ra9em l 3chwa2i men list li ghadi nkhelto f function l te7t


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
#hena ghangolo lih bli 9elebna f internet 3la l 7el o l9ina l jawab 3end chi wa7ed kan la7 code dyalo o kan 3endo nefess mochkil
#fchere7 gal bli hadi tari9a bach l3ebar dyal l'ecran it9essem b tasawi o btari9a motasawiya 9edachma kant l hajem dyal l'ecran dyalk
def center_window(window):
    window.update_idletasks()
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
    window.geometry("+%d+%d" % (x, y))
#hetal hena o kayna 7eta fel te7t tani 
    

#lpopup to start the game 
def show_popup():
    game.withdraw()  
    popup = Toplevel(game)
    label = Label(popup, text="Welcome to the Memory Game!\nClick 'Start Game' to begin.")
    label.pack(side=TOP)
    start_button = Button(popup, text="Start Game", command=lambda: [popup.destroy(), start_game()])
    start_button.pack(side=TOP)
#bach tban f center    
    center_window(popup)
    popup.focus_force() 
#hada mochkil kan 3endna mabghach tle3 l game men be3dma zedna l popup 
#bhadi 9edrat tban
def start_game():
    game.after(100, game.deiconify)  



show_popup() 


def random_text():
    
    words = {"Apple":0,"Lemon":0,"Banana":0,"Melon":0,"Ananas":0,"Kiwi":0,"Orange":0,"Cherry":0,"Citron":0,"Papaya":0}
    
    for bttn in dict_cards:
        
        if len(L) > 0:
            random.shuffle(L) #tkhlet dakchi 3achwa2iyan
            x = L[0] #awel 9ima men la list lmekhelta
            dict_cards[bttn] = x #men be3d x kat3eta l bttn bach t9ad lina la liste dyal game 
            words[x] = words[x] + 1 # ila khedemena b chi kelma men list kat3etaha wa7d bach ila jab lahh 3awd tekhetarat ite3etaha 2
        
            if words[x] == 2:# te3etaha 2 ya3ni tkhtarat men 9ebel o ghat7iyed men list 
                L.remove(x)
      
def bttn_clicked(btn):
    global clicked_cards
    global firstcard
    global secondcard
    
    
    clicked_cards = clicked_cards + 1
    
    if clicked_cards == 1: #awel card tkhetarat
        firstcard = btn 
        btn.configure(text=dict_cards[btn],state=DISABLED) #button li tkhtar maymknch t3awd tghet 3lih bach tb9a l card dayra
    
    if  clicked_cards == 2:#tanya
        secondcard = btn
        btn.configure(text=dict_cards[btn],state=DISABLED)
        
        game.after(500,check_same)# men be3d te2khir dyal 500 milliseconds call check_same bach it3ta we9t l player ichof bita9a tanya
        
def check_same():
    global clicked_cards
    global firstcard
    global secondcard
    global game_end
    global L_length
    
    if secondcard['text'] != firstcard['text']: #comparaison bin first card o tanya
        firstcard.configure(text="",state="normal")#kanbedlo l configuration dyal card . ila machi b7al b7al kayrje3 string khawi o state normale ya3ni ki3awd itgeleb 
        secondcard.configure(text="",state="normal")
    else:
        game_end = game_end + 1 #ila b7al b7al ya3ni player l9a wa7d zawj o kitzad l game_end wa7d 7it ila wssel l 10 rah l9a azwaj kamlin o ghatsala l game o tban l popup dyal time
        

    if game_end == L_length:#ila wslat 10 azwaj iban l popup dyal rah tssala o time li dowz
        messagebox.showinfo("MEMORY GAME", "You have spent "+str(int(time.time() - start))+" sec!")
        
        game.destroy()#kaysed l window dyal l game
            
    clicked_cards = 0 # bach player i9edr i3awd ikhetar joj cards khrin o t3awd la boucle . bla biha makat3awdch
    
#hadi b7al li l fo9
game.update_idletasks()
x = (game.winfo_screenwidth() - game.winfo_reqwidth()) / 2
y = (game.winfo_screenheight() - game.winfo_reqheight()) / 2
game.geometry("+%d+%d" % (x, y))
            
random_text() 

game.mainloop()
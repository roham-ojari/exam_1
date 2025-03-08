from tkinter import *
import random
win = Tk()
win.geometry('500x300+430+220')
win.title('بازی رنگ ها')
win.config(bg='light blue')
#===========================================================
color =['red','yellow','blue','purple','orange','pink','green','black','white','brown']
time = 30
score = 0
def start():
    if time == 30:
        count()
    next_color()
def next_color():
    global score
    global time
    if time > 0 :
        ent_color.focus_set()
        random.shuffle(color)
        if ent_color == color[1]:
            score +=1
        ent_color.delete(0,END )
        lbl_1.config(fg = str(color[1]),text=str (color[0]))
        lbl_score.config(str(score))

def count():
    global time
    if time > 0:
        time-=1 
        lbl_time2.config(str({time}))
        lbl_time2.after(1000,count)
#===========================================================
lbl_discribe = Label(win,text='رنگ هر کلمه را به زبان انگلیسی وارد کنید',font='bold 16',bg='light blue')
lbl_discribe.pack(side=TOP)

lbl_emtyaz = Label(win,text=' : امتیاز',font='bold 15',bg='light blue')
lbl_emtyaz.pack(side=TOP)

lbl_time = Label(win,text=' : زمان',font='bold 15',bg='light blue')
lbl_time.pack(side=TOP)

lbl_time2 = Label(win,text='',font='bold 15',bg='light blue')
lbl_time2.place(x=200,y=30)

lbl_1 = Label(win,text='',font='bold 15',bg='light blue')
lbl_1.pack(side=TOP)

lbl_score = Label(win,text='',font='bold 15',bg='light blue')
lbl_score.place(x=200,y=24)
#===========================================================
ent_color = Entry(win,font='bold 15')
ent_color.place(x=150,y=180)
#===========================================================
btn_start = Button(win,text='START',font='bold 15',command=start,bg='light blue')
btn_start.place(x=100,y=240)

btn_start_again = Button(win,text='AGAIN',font='bold 15',bg='light blue')
btn_start_again.place(x=340,y=240)

#===========================================================

#===========================================================
















win.mainloop()
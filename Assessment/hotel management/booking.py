from tkinter import * 
screen=Tk()
screen.geometry("1000x400")
screen.title("Hotel Management system")
from bookinglogic import *

l1 = Label(screen,text='YOU CLICKED ON       :      CHECK IN',height=2,width=80,borderwidth=1,relief='solid',font=('black',15,'bold'))
l1.place(x=20,y=20)

r1 = Label(screen,text='ENTER YOUR NAME  :',font=('black',10,'bold'))
r1.place(x=80,y=100)
r2=Entry(screen,width=30,textvariable=name)
r2.place(x=250,y=100)

r1 = Label(screen,text='ENTER YOUR ADDRESS  :',font=('black',10,'bold'))
r1.place(x=80,y=150)
r2=Entry(screen,width=30,textvariable=address)
r2.place(x=250,y=150)

r1 = Label(screen,text='ENTER YOUR NUMBER  :',font=('black',10,'bold'))
r1.place(x=80,y=200)
r2=Entry(screen,width=30,textvariable=number)
r2.place(x=250,y=200)

r1 = Label(screen,text='NUMBER OF DAYS  :',font=('black',10,'bold'))
r1.place(x=80,y=250)
r2=Entry(screen,width=30,textvariable=days)
r2.place(x=250,y=250)

l1 = Label(screen,text='CHOOSE YOUR ROOM',height=1,width=20,borderwidth=1,relief='solid')
l1.place(x=400,y=300)


r1 = Label(screen,text='CHOOSE PAYMENT METHOD',font=('black',15,'bold'))
r1.place(x=350,y=450)



Button1 = Radiobutton(screen, text = "DELUXE",variable = room,value="deluxe",height = 2,width = 10,font=('black',10,'bold'))
Button2 = Radiobutton(screen, text = "GENERAL",variable = room,value="general",height = 2,width = 10,font=('black',10,'bold'))
Button3 = Radiobutton(screen, text = "FULL DELUXE",variable = room,value="full deluxe",height = 2,width = 10,font=('black',10,'bold'))
Button4 = Radiobutton(screen, text = "JOINT",variable = room,value="joint",height = 2,width = 10,font=('black',10,'bold'))
    
Button1.place(x=200,y=330)
Button2.place(x=200,y=380)
Button3.place(x=600,y=330)
Button4.place(x=600,y=380)



payment1 = Radiobutton(screen, text = "By Cash",variable = payment,value="bycash",height = 2,font=('black',10,'bold'))
payment2 = Radiobutton(screen, text = "By Credit Card / Debit Card",variable = payment,value="by credit card,debit car",height = 2,font=('black',10,'bold'))

payment1.place(x=200,y=480)
payment2.place(x=600,y=480)

rb=Button(screen,width=20,text='SUBMIT',font=('black', 10,'bold'),height=2,command=booking)
rb.place(x=400,y=560)

screen.mainloop()
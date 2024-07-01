import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='hotelManagement')
mycursor=mydb.cursor()

from tkinter import *
screen =Tk()
screen.geometry("600x600")
screen.title("Hotel Management")

l1 = Label(screen,text='WELCOME',height=1,width=20,borderwidth=1,relief='solid')
l1.place(x=220,y=20)
l2 = Label(screen,text='HOTEL MANAGEMENT',height=2,width=30,font=('black',15,'bold'))
l2.place(x=270,y=65)
l3 = Label(screen,text='PYTHON TKINTER',height=2,width=30,font=('black',15,'bold'))
l3.place(x=270,y=140)
l4 = Label(screen,text='GUI',height=2,width=30,font=('black',15,'bold'))
l4.place(x=270,y=220)



c_value=StringVar()
def check_inn():
    value1="Check Inn button clicked"
    c_value.set(value1)

b1= Button(screen,width=30,height=2,text='1. CHECK INN',command=check_inn)
b1.place(x=80,y=65)
l4 = Label(screen,textvariable=c_value,height=2,width=30,font=('black',15,'bold'))
l4.place(x=80,y=350)

showguestlist=StringVar()
def show_guest_list():
    query = "select * from booking"
    mycursor.execute(query)
    alldata=mycursor.fetchall()
    showguestlist.set('\n'.join([str(item) for item in alldata]))
    print(alldata)
b2= Button(screen,width=30,height=2,text='2. SHOW GUEST LIST',command=show_guest_list)
b2.place(x=80,y=110)
l4 = Label(screen,textvariable=showguestlist,height=2,width=30,font=('black',15,'bold'))
l4.place(x=80,y=470)


check_out =StringVar()
def checkout():
    value2="Check Out button clicked"
    check_out.set(value2)
b3= Button(screen,width=30,height=2,text='3. CHECK OUT',command=checkout)
b3.place(x=80,y=155)
l4 = Label(screen,textvariable=check_out,height=2,width=30,font=('black',15,'bold'))
l4.place(x=80,y=400)


getinfo =StringVar()
def get_info():
    value3="Get Info of Any Guest button clicked"
    getinfo.set(value3)
b4= Button(screen,width=30,height=2,text='4. GET INFO OF ANY GUEST',command=get_info)
b4.place(x=80,y=200)
l4 = Label(screen,textvariable=getinfo,height=2,width=30,font=('black',15,'bold'))
l4.place(x=80,y=400)


def exit_app():
    quit.destroy()
b5= Button(screen,width=30,height=2,text='5. EXIT',command=exit)
b5.place(x=80,y=245)


screen.mainloop()


                               






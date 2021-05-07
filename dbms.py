import tkinter as tk
from tkinter import *
import mysql.connector 
from tkinter import messagebox
from tkinter import ttk

global db

db = mysql.connector.connect(host ="localhost", user = "root", password = "pass", db ="traindbms")


def notfilld(msg):
    messagebox.showwarning("Train Ticket Reservation",msg)

def tcktbookdmsg():
    messagebox.showinfo("Train Ticket Reservation","Ticket Booked")


def adminlogin():
    adlogwin = tk.Tk()
    adlogwin.geometry("360x220")
    adlogwin.title("Train Ticket Reservation - Train")

    Admin_name = Label(adlogwin,text="Admin Name :")
    Admin_name.grid(row=0, column=0,padx=10,pady=20)
    admin_nme = Entry(adlogwin,width=37)
    admin_nme.grid(row=0, column=1,padx=10,pady=20,ipady=2.2)
    
    Admin_id = Label(adlogwin,text="Admin ID :")
    Admin_id.grid(row=1, column=0,padx=10,pady=20)
    admin_id = Entry(adlogwin,width=37)
    admin_id.grid(row=1, column=1,padx=10,pady=20,ipady=2.21)

    logbtn = Button(adlogwin,text = "Login", command= "#")
    logbtn.grid(row=2,column=0,columnspan=2,padx=10,pady=10,ipadx=100)


    print("admin login")


def View(tree):

    
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM train""")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)


def trnaval(): # Train Available
    
    cursor = db.cursor()


    trnavalwin = tk.Tk()
    trnavalwin.resizable(False,False)
    trnavalwin.title("Train Ticket Reservation")
    
    tree = ttk.Treeview(trnavalwin, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
    tree.column("c1", width=110,anchor='c')
    tree.heading("c1", text="From")

    tree.column("c2", width=110,anchor='se')
    tree.heading("c2", text="To")

    tree.column("c3", width=110,anchor='se')
    tree.heading("c3", text="Date")

    tree.column("c4",width=110, anchor='se')
    tree.heading("c4", text="Time")

    tree.column("c5",width=110, anchor='se')
    tree.heading("c5", text="Train_No")

    tree.column("c6",width=110, anchor='se')
    tree.heading("c6", text="Train_Name")

    tree.column("c7",width=110, anchor='se')
    tree.heading("c7", text="Pantry")

    tree.pack()
    View(tree)

    print("Train Available")


def bktktf(arrval): # Book Ticket Function For Database
    
    cursor = db.cursor()
    arr = [str(x.get()) for x in arrval]
    mi = min(arr)
    
    #insert into train(frm,to_,dte,tme,trn_no,trn_nme,pantry) values("chennai egmore","Hnizamuddin","5/05/21","9:05","06011","NZM EXP","yes");

    if ((mi!="") and (mi!=" ")):

        cursor.execute("""INSERT INTO passengers(name,age,gender,phn_no,trn_nme,cls,frm,to_,dte,tme,trn_no,pid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",arr);

        print(arrval)
        for x in arrval:
            x.delete(0,END)
        tcktbookdmsg()
        print("ticket booked")
        db.commit()
    else:
        notfilld("Please Fill All The Fields !!!")
        print("ticket not booked")


def tcktres(): # Ticket Reservation
    scndwin = tk.Tk()
    scndwin.resizable(False,False)
    scndwin.title("Train Ticket Reservation")

    Pidl = Label(scndwin,text="ID :").grid(row = 0,column=0,padx=5,pady=5)
    pid = Entry(scndwin,width=37)
    pid.grid(row = 0,column=1,padx=20,pady=5)
    

    Namel = Label(scndwin,text="Name :").grid(row = 1,column=0,padx=5,pady=5)
    name = Entry(scndwin,width=37)
    name.grid(row = 1,column=1,padx=20,pady=5)

    Agel = Label(scndwin,text="Age :").grid(row = 2,column=0,padx=5,pady=5)
    age = Entry(scndwin,width=37)
    age.grid(row = 2,column=1,padx=20,pady=5)

    Genderl = Label(scndwin,text="Gender :").grid(row = 3,column=0,padx=5,pady=5)
    gender = Entry(scndwin,width=37)
    gender.grid(row = 3,column=1,padx=5,pady=5)

    Phone_no = Label(scndwin,text="Phone no :").grid(row = 4,column=0,padx=5,pady=5)
    phn_no = Entry(scndwin,width=37)
    phn_no.grid(row = 4,column=1,padx=5,pady=5)

    Train_name = Label(scndwin,text="Train Name :").grid(row = 5,column=0,padx=5,pady=5)
    trn_nme = Entry(scndwin,width=37)
    trn_nme.grid(row = 5,column=1,padx=5,pady=5)

    Train_nol = Label(scndwin,text="Train no :").grid(row = 6,column=0,padx=5,pady=5)
    trn_no = Entry(scndwin,width=37)
    trn_no.grid(row = 6,column=1,padx=20,pady=5)
    
    Class_ = Label(scndwin,text="Class :").grid(row = 7,column=0,padx=5,pady=5)
    cls_ = Entry(scndwin,width=37)
    cls_.grid(row = 7,column=1,padx=5,pady=5)
    
    from_ = Label(scndwin,text="From :").grid(row = 8,column=0,padx=5,pady=5)
    frm = Entry(scndwin,width=37)
    frm.grid(row = 8,column=1,padx=5,pady=5)
    
    To_ = Label(scndwin,text="To :").grid(row = 9,column=0,padx=5,pady=5)
    to_ = Entry(scndwin,width=37)
    to_.grid(row = 9,column=1,padx=5,pady=5)
    
    Date = Label(scndwin,text="Date :").grid(row = 10,column=0,padx=5,pady=5)
    date = Entry(scndwin,width=37)
    date.grid(row = 10,column=1,padx=5,pady=5)
    
    Time_ = Label(scndwin,text="Time :").grid(row = 11,column=0,padx=5,pady=5)
    time_ = Entry(scndwin,width=37)
    time_.grid(row = 11,column=1,padx=5,pady=5)

    arr = [name,age,gender,phn_no,trn_nme,cls_,frm,to_,date,time_,trn_no,pid]


    submitbtn = tk.Button(scndwin,text="Book Ticket", command=lambda:[bktktf(arr)])#,tcktbookdmsg()
    submitbtn.grid(row=12,column=0,columnspan=2,padx=10,pady=10,ipadx=100)


    print("ticket reserved")
    
def tckt(): # Train Ticket Button Window
    tcktwin = tk.Tk()
    tcktwin.resizable(False,False)
    tcktwin.title("Train Ticket Reservation")
    tcktwin.geometry("300x245")

    trnavalbtn = tk.Button(tcktwin,text="Train Available",command=trnaval,height=3,width=16)
    tcktresbtn =  tk.Button(tcktwin,text="Ticket Reservation",command=tcktres,height=3,width=16)

    trnavalbtn.grid(row=0,column=1)
    tcktresbtn.grid(row=1,column=2)

    trnavalbtn.place(relx=0.5, rely=0.25, anchor=CENTER)
    tcktresbtn.place(relx=0.5, rely=0.7, anchor=S)




root = tk.Tk()
root.resizable(False, False)

root.title("Train Ticket Reservation")
root.geometry("300x245")

adminbtn = tk.Button(root,text="Admin Login",command=adminlogin,height=3,width=16)
tktresbtn =  tk.Button(root,text="Passengers",command=tckt,height=3,width=16)

db.commit()

adminbtn.grid(row=0,column=1)
tktresbtn.grid(row=1,column=2)

adminbtn.place(relx=0.5, rely=0.25, anchor=CENTER)
tktresbtn.place(relx=0.5, rely=0.7, anchor=S)


mainloop()

db.close()

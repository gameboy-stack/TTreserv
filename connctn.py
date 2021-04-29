import tkinter as tk
import mysql.connector
from tkinter import *

def submitf():
	usern = Username.get()
	passf = password.get()
	if ((usern == "admin") and (passf == "pass")):
		print("welcome")

	else:
		print("sorry")
		
db = mysql.connector.connect(host ="localhost", user = "root", password = "pass", db ="world")
if db:
	print("Connected")
	cursor = db.cursor()
else:
	print("Nc")



root = tk.Tk()
root.geometry("300x300")
root.title("Train Ticket Reservation")


# Definging the first row
lblfrstrow = tk.Label(root, text ="Username :", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password :")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",bg ='blue', command = submitf)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import random
import string

window = Tk()
window.title("Welcome")
window.state('zoomed') 

photo = PhotoImage(file="img.png")

name = StringVar()
email = StringVar()
dob = StringVar()
telephone = StringVar()
branch = StringVar()
image= StringVar()

lbl0 = Label(window, text="ID CARD GENERATOR", width=20, font=("Times New Roman", 30))
lbl0.place(x=550, y=50)
lbl1 = Label(window, text="Name:", width=20, font=("Times New Roman", 20))
lbl1.place(x=200, y=200)
lbl2 = Label(window, text="Email:", width=20, font=("Times New Roman", 20))
lbl2.place(x=200, y=250)
lbl3 = Label(window, text="D.O.B:", width=20, font=("Times New Roman", 20))
lbl3.place(x=200, y=300)
lbl4 = Label(window, text="Telephone:", width=20, font=("Times New Roman", 20))
lbl4.place(x=200, y=350)
lbl4 = Label(window, text="Branch:", width=20, font=("Times New Roman", 20))
lbl4.place(x=200, y=400)
lb5 = Label(window, image=photo)
lb5.place(x=900, y=150)

entry_name = Entry(window, width=20, font=("Times New Roman", 20), textvar=name)
entry_name.place(x=450, y=200)
entry_email = Entry(window, width=20, font=("Times New Roman", 20), textvar=email)
entry_email.place(x=450, y=250)
entry_dob = Entry(window, width=20, font=("Times New Roman", 20), textvar=dob)
entry_dob.place(x=450, y=300)
entry_telephone = Entry(window, width=20, font=("Times New Roman", 20), textvar=telephone)
entry_telephone.place(x=450, y=350)

list1 = ['', 'COMPUTER', 'IT', 'MECHANICAL', 'EXTC', 'ETRX', 'AUTOMOBILE', ];
drop_list = OptionMenu(window, branch, *list1)
drop_list.config(width=24, font=("Times New Roman", 15))
branch.set('')
drop_list.place(x=450, y=400)

def emptyfield():
	if(entry_name.get()=="" or entry_email.get()=="" or entry_dob.get()=="" or entry_telephone.get()=="" or branch.get()==""):
		return 1

def duplicatetelephone():
	try:
		conn = sqlite3.connect('mydb.db')
		cursor = conn.cursor()
		telephone1 = int(telephone.get())
		result=cursor.execute("SELECT telephone FROM details")
		for i in result:
			if(i[0]==telephone1):
				return 1
	except ValueError:
		return 2

def duplicateemail():
	conn = sqlite3.connect('mydb.db')
	cursor = conn.cursor()
	email1 = email.get()
	result=cursor.execute("SELECT email FROM details")
	for i in result:
		if(i[0]==email1):
			return 1

def telephonecount():
	count=0
	for i in telephone.get():
		count=count+1
	if(count<10 or count>10):
		return 1

def dobcheck():
	for i in dob.get():
		if(i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='/'):
			return 1

def clicked():
	if(emptyfield()==1):
		messagebox.showinfo('Message', 'Some fields are empty')
	elif(duplicatetelephone()==1):
		messagebox.showinfo('Message', 'duplicate entry in telephone')
	elif(duplicatetelephone()==2):
		messagebox.showinfo('Message', 'Enter correct telephone no.')
	elif(duplicateemail()==1):
		messagebox.showinfo('Message', 'duplicate entry in email')
	elif(telephonecount()==1):
		messagebox.showinfo('Message', 'Enter only 10 digits in telephone no.')
	elif(dobcheck()==1):
		messagebox.showinfo('Message', 'Enter dob in format DD/MM/YYYY')
	else:
		database()

def selectimage(image):
	if(image==""):
		return 1

def idcard(image,name1,email1,dob1,telephone1,branch1,uniqueid):
	window1 = Toplevel(window,bg='yellow')
	window1.geometry('500x350')
	window1.title("ID CARD")
	window1.resizable(width=False, height=False)
	
	lbl7 = Label(window1, text="PCE STUDENT", width=12, font=("Times New Roman", 30),bg='yellow')
	lbl7.place(x=115, y=5)

	photo1 = PhotoImage(file=image)
	lbl8 = Label(window1,image=photo1)
	lbl8.place(x=275, y=60)

	lbl9 = Label(window1, text="Name:", width=5, font=("Times New Roman", 15),bg='yellow')
	lbl9.place(x=5, y=75)
	lbl10 = Label(window1, text=name1, width=13, font=("Times New Roman", 15),bg='yellow')
	lbl10.place(x=63, y=75)

	lbl11 = Label(window1, text="D.O.B:", width=6, font=("Times New Roman", 15),bg='yellow')
	lbl11.place(x=5, y=125)
	lbl12 = Label(window1, text=dob1, width=9, font=("Times New Roman", 15),bg='yellow')
	lbl12.place(x=67, y=125)

	lbl13 = Label(window1, text="Branch:", width=6, font=("Times New Roman", 15),bg='yellow')
	lbl13.place(x=5, y=175)
	lbl14 = Label(window1, text=branch1, width=11, font=("Times New Roman", 15),bg='yellow')
	lbl14.place(x=75, y=175)
	
	lbl15 = Label(window1, text="Email:", width=5, font=("Times New Roman", 15),bg='yellow')
	lbl15.place(x=5, y=225)
	lbl16 = Label(window1, text=email1, width=19, font=("Times New Roman", 15),bg='yellow')
	lbl16.place(x=60, y=225)
			
	lbl17 = Label(window1, text="Tel/Mob:", width=7, font=("Times New Roman", 15),bg='yellow')
	lbl17.place(x=5, y=275)
	lbl18 = Label(window1, text=telephone1, width=9, font=("Times New Roman", 15),bg='yellow')
	lbl18.place(x=85, y=275)
			
	lbl19 = Label(window1, text="ID:", width=3, font=("Times New Roman", 15),bg='yellow')
	lbl19.place(x=5, y=317)
	lbl20 = Label(window1, text=uniqueid, width=10, font=("Times New Roman", 15),bg='yellow')
	lbl20.place(x=35, y=317)
	
	reset()
	window1.mainloop()

def database():
	messagebox.showinfo('Message', 'Select Image')
	window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))#Opens file explorer
	image=window.filename
	if(selectimage(image)==1):
		messagebox.showinfo('Message', 'Please Select image')
	else:
		conn = sqlite3.connect('mydb.db')
		cursor = conn.cursor()
		
		name1 = name.get()
		email1 = email.get()
		dob1 = dob.get()
		telephone1 = telephone.get()
		branch1 = branch.get()
		
		#Generate random id
		random1=''.join([random.choice(string.ascii_letters) for n in range (2)])
		random1=random1.upper()
		random2=''.join([random.choice(string.digits) for n in range (4)])
		uniqueid='2019'+random1+random2

		cursor.execute('CREATE TABLE IF NOT EXISTS details(name TEXT,email TEXT,dob TEXT,telephone NUMERIC,branch TEXT,image TEXT,uniqueid TEXT)')#Creates a table if it doesnt exist
		cursor.execute('INSERT INTO details (name,email,dob,telephone,branch,image,uniqueid) VALUES(?,?,?,?,?,?,?)', (name1, email1, dob1, telephone1, branch1,image,uniqueid))#Inserts into the table
		conn.commit()
		messagebox.showinfo('Message', 'ID Card Generated')
		cursor.close()
		conn.close()
		idcard(image,name1,email1,dob1,telephone1,branch1,uniqueid)

def reset():
	entry_name.delete(0,20)
	entry_email.delete(0,30)
	entry_dob.delete(0,20)
	entry_telephone.delete(0,20)
	branch.set('')

btn1 = Button(window, text="Generate", width=10, font=("Times New Roman", 20), command=clicked)
btn1.place(x=550, y=600)
btn2 = Button(window, text="Reset", width=10, font=("Times New Roman", 20), command=reset)
btn2.place(x=400, y=600)

window.mainloop()
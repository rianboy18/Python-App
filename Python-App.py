from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import cx_Oracle
import ds2				#<------Name of weather module imported for weather information.


flash=Tk()
flash.title("Boom you're here")
flash.geometry('500x500+200+200')

def flash_to_root():
		root.deiconify()
		flash.withdraw()
		return

lblWelcome=Label(flash,text="Welcome!",font=('Verdana',25,'bold'))
lblWeather=Label(flash,text=ds2.weather(),font=('Times New Roman ',15,'italic'))
lblAuthor=Label(flash,text='Developed by Pranav Nair',font=('Ariel',12,'italic'))												#
lblWelcome.pack(pady=60)
lblWeather.pack(pady=35)
lblAuthor.pack(pady=15)

def loc_info():
		lblWeather.configure(text=ds2.weather())
		flash.after(5000,flash_to_root())
		return
flash.after(1000,loc_info)


root=Toplevel(flash)
root.title("Student Management System")
root.geometry("400x400+200+200")
root.configure(background='Beige')
Welcome=Label(root,text='Welcome!',font=('ariel',20,'bold'))
Welcome.pack(pady=5)		

adst=Toplevel(root)					
adst.title("Add Student")
adst.geometry("400x400+200+200")
adst.withdraw()

lblRnoAd=Label(adst,text="Enter Rno")
entRnoAd=Entry(adst,bd=5)
lblNameAd=Label(adst,text="Enter Name")
entNameAd=Entry(adst,bd=7)



def f1():
	adst.deiconify()
	root.withdraw()
btnAdd=Button(root,text="Add",width=10,command=f1)

def f2():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print('connected')
		try:
			rno=int(entRnoAd.get())
		except ValueError:
			messagebox.showerror("Issue","invalid rno")
			entRnoAd.delete(0,END)
			entRnoAd.focus()
			return
		name=entNameAd.get()
		if (len(name)==0 or not name.isalpha()):
			messagebox.showerror("Issue","Invalid Name")
			entNameAd.delete(0,END)
			entNameAd.focus()
			return
		cursor=con.cursor()
		sql="insert into student values(%d,'%s')"
		args=(rno,name)
		cursor.execute(sql%args)
		con.commit()
		print(cursor.rowcount,'rows inserted')
		messagebox.showinfo("Success",'Record inserted')
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror("issue",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		print("disconnected")
	entRnoAd.delete(0,END)
	entNameAd.delete(0,END)
	entRnoAd.focus()

btnAddSave=Button(adst,text="Save",command=f2)


def f3():
	root.deiconify()
	adst.withdraw()
btnAddBack=Button(adst,text="Back",command=f3)

lblRnoAd.pack(pady=10)
entRnoAd.pack(pady=10)
lblNameAd.pack(pady=10)
entNameAd.pack(pady=10)
btnAdd.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

vist=Toplevel(root)
vist.title("View Student")
vist.geometry("400x400+200+200")
vist.withdraw()

stViewData=scrolledtext.ScrolledText(vist,width=30,height=10)

def f4():
	root.deiconify()
	vist.withdraw()
	stViewData.delete('1.0',END)
btnViewBack=Button(vist,text="Back",command=f4)
stViewData.pack()
btnViewBack.pack()

def f5():
	vist.deiconify()
	root.withdraw()
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		sql="select * from student order by rno"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			print("rno",d[0],"name",d[1])
			info=info + "rno" +str(d[0])+ "  name  " +d[1] + "\n"
			
		stViewData.insert(INSERT,info)

	except cx_Oracle.DatabaseError as e:			
			print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		print("disconnected") 
	
btnView=Button(root,text="View",width=10,command=f5)
btnView.pack(pady=20)

updst=Toplevel(root)
updst.title("Update Record")
updst.geometry('400x400+200+200')
updst.withdraw()

lblRnoUp=Label(updst,text="enter rno")			
entRnoUp=Entry(updst,bd=5)
lblNameUp=Label(updst,text="enter name")
entNameUp=Entry(updst,bd=7)

def f6():
	updst.deiconify()
	root.withdraw()
btnUpdate=Button(root,text="Update",width=10,command=f6)

def f7():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		try:
			rno=int(entRnoUp.get())
		except ValueError:
			messagebox.showerror("Issue","invalid rno")
			entRno.delete(0,END)
			entRno.focus()
			return
		name=entNameUp.get()
		if(len(name)==0 or not name.isalpha()):
			messagebox.showerror("Issue","invalid name")
			entNameUp.delete(0,END)
			entNameUp.focus()
			return
		cursor=con.cursor()
		sql="update student set name='%s' where rno=%d"	
		args=(name,rno)
		cursor.execute(sql % args)
		con.commit()
		print(cursor.rowcount,'rows updated')
		messagebox.showinfo("Success","record updated")
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
		messagebox.showerror("Issue",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		print("disconnected")
	entRnoUp.delete(0,END)
	entNameUp.delete(0,END)
	entRnoUp.focus()
btnUpdateUpdate=Button(updst,text="Update",command=f7)


def f8():
	root.deiconify()
	updst.withdraw()
btnUpdateBack=Button(updst,text="Back",command=f8)

btnUpdate.pack(pady=20)
lblRnoUp.pack(pady=10)
entRnoUp.pack(pady=10)
lblNameUp.pack(pady=10)
entNameUp.pack(pady=10)
btnUpdateUpdate.pack(pady=10)
btnUpdateBack.pack(pady=10)

delst=Toplevel(root)
delst.title('Delete Student')
delst.geometry('400x400+200+200')
delst.withdraw()

lblRnoDel=Label(delst,text="enter rno")			
entRnoDel=Entry(delst,bd=5)

def f9():
	delst.deiconify()
	root.withdraw()
btnDelete=Button(root,text="Delete",width=10,command=f9)

def f10():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected") 
		try:
			rno=int(entRnoDel.get())
		except ValueError:
			messagebox.showerror("Issue","Invalid Rno")
			entRnoDel.delete(0,END)
			entRnoDel.focus()
			return
	
		cursor=con.cursor()
		sql="delete from student where rno=%d"
		args=(rno)
		cursor.execute(sql%args)
		con.commit()
		print(cursor.rowcount,'rows deleted')
		messagebox.showinfo("Success","Roll no has been deleted")	
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("issue",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		print("disconnected") 
	entRnoDel.delete(0,END)
	entRnoDel.focus()

btnDeleteDelete=Button(delst,text="Delete",command=f10)

def f11():
	root.deiconify()
	delst.withdraw()
btnDeleteBack=Button(delst,text="Back",width=10,command=f11)

lblRnoDel.pack(pady=10)
entRnoDel.pack(pady=10)
btnDelete.pack(pady=10)
btnDeleteDelete.pack(pady=10)
btnDeleteBack.pack(pady=10)

def f12():											#<-------}
	ans=messagebox.askyesno("Exit","Are u done ?")		
	if ans:											#<-------}Do you want to exit code
		import sys				
		sys.exit()									#<-------}
							
root.protocol("WM_DELETE_WINDOW",f12)		
adst.protocol("WM_DELETE_WINDOW",f12)
vist.protocol("WM_DELETE_WINDOW",f12)
updst.protocol("WM_DELETE_WINDOW",f12)
delst.protocol("WM_DELETE_WINDOW",f12)



root.mainloop()





















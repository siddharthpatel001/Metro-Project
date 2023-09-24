# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:49:05 2021

@author: sidpa
"""
import dashboard
import signup
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Metro Portal')
window.geometry('720x320')
def log_in():
    import mysql.connector
    dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "1516",
                     database = "passenger") 
    cursorObject = dataBase.cursor()
    if username.get()=='':
            messagebox.showerror('Username Error','Kindly Provide Username')
            return
    if password.get()=='':
            messagebox.showerror('Password Error','Kindly Provide Password')
            return
    try:
        query1 = "select * from login where username = %s and password = %s"
        x=username.get()
        y=password.get()
        cursorObject.execute(query1,[(x),(y)])
        result=cursorObject.fetchall()
        if len(result)==0:
            messagebox.showerror('Error','Username/Password Wrong.')
            # label5=Label(window,text="---------------Wrong Email / Password--------------",font=('arial',10),fg='white',bg='red')
            # label5.grid(row=7,column=2,pady=10)
            return
        else:
            # label5=Label(window,text="---------------Logged In--------------",font=('arial',10),fg='white',bg='green')
            # label5.grid(row=7,column=2,pady=10)
            window.destroy()
            dashboard.dashboard()
            
    except:
        print('NO')
    
    dataBase.commit()
    dataBase.close()



label1=Label(window,text='Welcome to Metro Portal',font=('elephant',35))
label1.grid(row=0,column=0,columnspan=6,padx=80,pady=20)


label2=Label(window,text='Username',font=('arial',16))
label2.grid(row=3,column=1)
username=Entry(window,width=40,borderwidth=4) # taking username from here
username.grid(row=3,column=2,columnspan=3,padx=5,pady=6)

label3=Label(window,text='Password',font=('arial',16))
label3.grid(row=4,column=1)
password=Entry(window,width=40,borderwidth=4) # taking password from here
password.grid(row=4,column=2,columnspan=3,padx=5,pady=6)
global button1
button1=Button(window,text='LOGIN',font=('Comic Sans MS',12),command=log_in,bg='blue',fg='white',borderwidth=4,padx=3,pady=3).grid(row=5,column=2,columnspan=3,padx=2,pady=4)


label4=Label(window,text="Don't have an account ?",font=('arial',10))
label4.grid(row=6,column=1,pady=10)
button2=Button(window,text="Click To Sign Up",font=('Comic Sans MS',9),command=signup.sign_up,bg='purple',fg='white',borderwidth=4,padx=3,pady=3).grid(row=6,column=2)



window.mainloop()

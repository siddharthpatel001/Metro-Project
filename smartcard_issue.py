# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:27:57 2021

@author: sidpa
"""
from tkinter import *
import mysql.connector
from tkinter import messagebox

def newuser():
    global username,amount_entry,root
    dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "1516",
                     database = "passenger" ) 

    cursorObject=dataBase.cursor()
    sql="select * from card where username=%s"
    r=[username.get()]
    cursorObject.execute(sql,r)
    table = cursorObject.fetchall()
    if table:
        dataBase.close()
        messagebox.showwarning('Account Error','Already Registered User !\nKindly Go and Add Money via Smartcard Balance')
        # label2=Label(root,text='Already Registered User !\nKindly Go and Add Money via Smartcard Balance',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=4,column=1)
        
    else:
        try:
            sql = "INSERT INTO card (username, amount) VALUES (%s, %s)"
            val = (username.get(),amount_entry.get())
            cursorObject.execute(sql,val)
            dataBase.commit()
            dataBase.close()
            # label3=Label(root,text=amount_entry.get()+' Successfully added').grid(row=3,column=1)
            messagebox.showinfo('Successful','SmartCard Issued\n'+amount_entry.get()+'Rs Successfully added')
            # label2=Label(root,text='----SmartCard Issued----\n----'+amount_entry.get()+' Successfully added----',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=4,column=1)
        except:
            dataBase.close()
            messagebox.showerror('Account Name Error','Create Account First !')
            # label2=Label(root,text='Account Not Created',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=4,column=1)
            # print("Account Not Created")
       
def booking():

    global root
    root = Tk()
    root.title('Smart Card Issue')
    root.geometry( "470x210" )
    
    label1=Label(root,text='Issue New Smart Card',font=('lucida console',20))
    label1.grid(row=0,column=0,columnspan=6,padx=80,pady=20)
    
    global username,amount_entry
    label1=Label(root,text='Username',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=1,column=0)
    username=Entry(root,width=40)
    username.grid(row=1,column=1)
    label2=Label(root,text='Amount',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=2,column=0)
    amount_entry=Entry(root,width=40)
    amount_entry.grid(row=2,column=1)
    print(amount_entry.get())
    submit_button=Button(root,text='Add Money',command=newuser,fg='white',bg='black',borderwidth=4,padx=3,pady=3).grid(row=3,column=0,columnspan=2)
    
    
    
    
    root.mainloop()
# booking()
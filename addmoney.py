# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:58:40 2021

@author: sidpa
"""

from tkinter import *
import mysql.connector
from tkinter import messagebox
def addmoney():
    try:
        global username,amount_entry,root
        
        if username.get()=='':
            messagebox.showerror('Username Error','Kindly Provide Username')
            return
        if amount_entry.get()=='':
            messagebox.showerror('Amount Error','Kindly Provide Amount')
            return
        if int(amount_entry.get())<0:
            messagebox.showerror('Amount Error','Kindly Provide valid Amount')
            return
        
        
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
            # print(table[0][1])
            x=int(amount_entry.get())+int(table[0][1])
            try:
                sql = "UPDATE card SET amount=%s where username=%s"
                val = (x,username.get())
                cursorObject.execute(sql,val)
                dataBase.commit()
                dataBase.close()
                # label3=Label(root,text='--'+amount_entry.get()+' Successfully added--').grid(row=3,column=1)
                messagebox.showinfo('Success!',amount_entry.get()+' Rs Successfully added!')
                root.destroy()
            except:
                dataBase.close()
                print("ERROR")
            
        else:
            dataBase.close()
            messagebox.showerror('Account Error','No Record of Username\nKindly Register Smartcard!')
            # label3=Label(root,text='First Register Smart card.').grid(row=3,column=1)
    except:
        messagebox.showerror('Amount Error','Integer Input Valid only.')
        # print('Provide Digit Input')
        
def show_balance():
    global username,amount_entry,root
    if username.get()=='':
        messagebox.showerror('Username Error','Kindly Provide Username')
        return
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
        # print(table[0][1])
        # x=int(amount_entry.get())+int(table[0][1])
        try:
            # sql = "UPDATE card SET amount=%s where username=%s"
            # val = (x,username.get())
            # cursorObject.execute(sql,val)
            dataBase.commit()
            dataBase.close()
            messagebox.showinfo('Success!','Account Balance :'+str(table[0][1])+' Rs')
            root.destroy()
            # label3=Label(root,text='-->Account Balance :'+str(table[0][1])).grid(row=4,column=1)
        except:
            dataBase.close()
            print("ERROR")
        
    else:
        dataBase.close()
        messagebox.showerror('Account Error','No Record of Username\nKindly Register Smartcard!')
        # label3=Label(root,text='First Register Smart card.').grid(row=4,column=1)
        
def booking():

    global root
    root = Tk()
    root.title('Smart Card Balance')
    root.geometry( "335x150" )
    
    global username,amount_entry
    label1=Label(root,text='Username',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=0,column=0)
    username=Entry(root,width=40)
    username.grid(row=0,column=1)
    label2=Label(root,text='Amount',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=1,column=0)
    amount_entry=Entry(root,width=40)
    amount_entry.grid(row=1,column=1)
    print(amount_entry.get())
    submit_button=Button(root,text='Add Money',command=addmoney,fg='white',bg='black',borderwidth=4,padx=3,pady=3).grid(row=2,column=0,columnspan=2)
    show_bal=Button(root,text='Show Balance',command=show_balance,fg='white',bg='red',borderwidth=4,padx=3,pady=3).grid(row=4,column=0,columnspan=2)
    
    
    
    
    root.mainloop()

# booking()
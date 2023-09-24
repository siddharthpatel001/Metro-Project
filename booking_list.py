# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:32:42 2021

@author: sidpa
"""

from tkinter import *
import mysql.connector
from tkinter import messagebox
def list():
    dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "1516",
                     database = "passenger") 
    cursorObject = dataBase.cursor()
    
    try:
        query1 = "select username from ticket where username = %s"
        cursorObject.execute(query1,[(username.get())])
        result=cursorObject.fetchall()
        if len(result)==0:
            messagebox.showwarning('Error','No Data Found!\nCheck Username.')
            dataBase.close()
            return
        else:
            query1 = "select * from ticket where username = %s"
            cursorObject.execute(query1,[(username.get())])
            result=cursorObject.fetchall()
            print(len(result))
            data=''
            for i in range(len(result)):
                data+=str(result[i][2])+'  |  '+str(result[i][3])+'  |  '+str(result[i][4])+'\n'
            messagebox.showinfo('Transactions','   PNR                SOURCE                DESTINATION\n\n'+data)
            dataBase.close()
            root.destroy()

    except:
        messagebox.showwarning('Error','Database Connection Error')
        dataBase.close()

    
    
    
    
def booking_list():

    global root
    root = Tk()
    root.title('Booking List')
    root.geometry( "335x150" )
    
    global username
    label1=Label(root,text='Username',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=0,column=0)
    username=Entry(root,width=40)
    username.grid(row=0,column=1)

    submit_button=Button(root,text='Show Transaction',command=list,fg='white',bg='black',borderwidth=4,padx=3,pady=3).grid(row=2,column=0,columnspan=2)
    
    
    
    
    
    root.mainloop()
# booking_list()
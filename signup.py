# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:55:29 2021

@author: sidpa
"""
from tkinter import *

def sign_up():
    global window2
    window2=Tk()
    window2.title('Sign Up')
    window2.geometry('420x700')
    
    
    label1=Label(window2,text='Sign Up Here',font=('Ink Free',20))
    label1.grid(row=0,column=0,columnspan=6,padx=80,pady=20)

    
    global f_name,l_name
    f_name=Entry(window2,width=30)
    f_name.grid(row=1,column=1,padx=20)
    
    l_name=Entry(window2,width=30)
    l_name.grid(row=2,column=1,padx=20)
    global username
    username=Entry(window2,width=30)
    username.grid(row=3,column=1,padx=20)
    
    global password
    password=Entry(window2,width=30)
    password.grid(row=4,column=1,padx=20)
    
    global confirm_password
    confirm_password=Entry(window2,width=30)
    confirm_password.grid(row=5,column=1,padx=20)
    
    global age
    age=Entry(window2,width=30)
    age.grid(row=6,column=1,padx=20)
    
    global contact
    contact=Entry(window2,width=30)
    contact.grid(row=7,column=1,padx=20)
    
    f_name_label=Label(window2,text='First Name',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=1,column=0)
    l_name_label=Label(window2,text='Last Name',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=2,column=0)
    username_label=Label(window2,text='Username',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=3,column=0)
    password_label=Label(window2,text='Password',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=4,column=0)
    confirm_password_label=Label(window2,text='Confirm Password',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=5,column=0)
    age_label=Label(window2,text='Age',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=6,column=0)
    contact_label=Label(window2,text='Contact',font=('Comic Sans MS',15),fg='black',borderwidth=4,padx=3,pady=3).grid(row=7,column=0)
    
    check=Button(window2,text="Check Details",command=check_activity,font=('Century',9),bg='green',fg='white',borderwidth=4,padx=3,pady=3).grid(row=8,column=1)
    global otp_btn
    
    window2.mainloop()

def check_activity():
    import mysql.connector
    dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "1516",
                     database = "passenger") 
    cursorObject = dataBase.cursor()
    global username
    global window2
    global submit
    global f_name,l_name
    if f_name.get()=='':
        messagebox.showwarning('Error','Enter First name')
        # label6=Label(window2,text='---Enter First name---').grid(row=9,column=1)
        return
    if l_name.get()=='':
        messagebox.showwarning('Error','Enter last name')
        # label6=Label(window2,text='---Enter Last name---').grid(row=9,column=1)
        return
    
    submit=0
    f=0
    while f==0:
        if username.get()=='':
            submit=0
            messagebox.showwarning('Error','Enter Email')
            return
        if '@' not in username.get():
            messagebox.showwarning('Error','Invalid Email')
            # label6=Label(window2,text='---Invalid Email---').grid(row=9,column=1)
            submit=0
            return
        try:
            query1 = "select username from login where username = %s"
            cursorObject.execute(query1,[(username.get())])
            result=cursorObject.fetchall()
            if len(result)==0:
                f=1
                submit=1
                # label6=Label(window2,text='-----------------------').grid(row=9,column=1)
                dataBase.close()
        except:
            messagebox.showwarning('Error','Database Connection Error')
            # label6=Label(window2,text='Database Connection Error').grid(row=9,column=1)
            dataBase.close()
            submit=0
            
        if f==0:
            messagebox.showwarning('Error','Email Already Exist')
            # label6=Label(window2,text='---Email Already Exist---').grid(row=9,column=1)
            submit=0
            dataBase.close()
            return
    global password
    global confirm_password
    while password.get()!=confirm_password.get() or password.get()=='':
        messagebox.showwarning('Error','Password Error!')
        # label6=Label(window2,text='---Password is not matching---').grid(row=9,column=1)
        submit=0
        return
    else:
        # label6=Label(window2,text='-----------------------').grid(row=9,column=1)
        submit=1
    
    global age
    
    
    while age.get()=='':
        messagebox.showwarning('Error','Age required')
        # label6=Label(window2,text='Age required').grid(row=9,column=1)
        submit=0
        return
    else:
        # label6=Label(window2,text='--------------------------').grid(row=9,column=1)
        submit=1
    
    while int(age.get())<18:
        messagebox.showwarning('Error','Age < 18')
        # label6=Label(window2,text='Age < 18').grid(row=9,column=1)
        submit=0
        return
    else:
        # label6=Label(window2,text='--------------------------').grid(row=9,column=1)
        submit=1
        
    global contact
    while contact.get()=='':
        messagebox.showwarning('Error','Phone Number required')
        # label6=Label(window2,text='Contact required').grid(row=9,column=1)
        submit=0
        return
    else:
        # label6=Label(window2,text='--------------------------').grid(row=9,column=1)
        submit=1    
    
    if submit==1: #to enable disabled otp button
        otp_btn=Button(window2,text='SEND OTP',command=send_otp,font=('arial',9),bg='red',fg='white',borderwidth=4,padx=3,pady=3).grid(row=11,column=1)
        # ,state=DISABLED
    
 

def on_submit():
    global otp
    global send_otp
    
    global f_name
    global l_name
    global username
    global password
    global confirm_password
    global contact
    global age
    
    
    import mysql.connector
    dataBase = mysql.connector.connect(
                 host = "localhost",
                 user = "root",
                 passwd = "1516",
                 database = "passenger") 
    cursorObject = dataBase.cursor()
    if int(otp)==int(send_otp.get()):
        # sql = "INSERT INTO login VALUES (%s, %s, %s, %s, %s, %s, %s)"
        sql="insert into login values(%s, %s, %s, %s, %s, %s, %s)"
        val = (f_name.get(), l_name.get(), username.get(), password.get(), confirm_password.get(), contact.get(), age.get())
        print(val)
        cursorObject.execute(sql,val)
        dataBase.commit()
        # label8=Label(window2,text='OTP VERIFIED !\nAccount Successfully Created').grid(row=14,column=1)
        
        messagebox.showinfo('Successfully created !',"You're Verfied User !\nWelcome to Portal")
        
        dataBase.close()
        global window2
        window2.destroy()
        return
    else:
        messagebox.showwarning('Error','Wrong OTP !')
        # label8=Label(window2,text='Wrong OTP !').grid(row=14,column=1)
        return
    
def send_otp():
    global send_otp
    send_otp=Entry(window2,width=30)
    send_otp.grid(row=12,column=1,padx=20)
    
    otp_label=Label(window2,text='Enter OTP').grid(row=12,column=0)
     
    import random
    global otp
    otp=random.randint(1000,9999)
    from twilio.rest import Client
    
    account_sid = 'ACf1ed5d545445872aebf88d15836b868c'
    auth_token = '58d6e6b8f3e582189d2063713d25acb6'
    client = Client(account_sid, auth_token)
    global contact
    p=contact.get()
    p='+91'+p
    message = client.messages.create(
                         body="Welcome to Metro Verification\nYour OTP is "+str(otp),
                         from_='+13213390045',
                         to=p
                     )
    print(message.sid)
    submit_otp=Button(window2,text="SUBMIT",command=on_submit,font=('arial',9),bg='black',fg='white',borderwidth=4,padx=3,pady=3).grid(row=13,column=1)

# sign_up()    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:25:47 2021

@author: sidpa
"""
import mysql.connector
from tkinter import *
from tkinter import messagebox
import random
def rate(source,destination):
    train_station=[['gyaspur deposite','apmc','jivaraj','rajiv nagar','shreyas','paldi','gandhigram','old high court'],
               ['motera stadium','sabarmati','aec','sabarmati railway','ranip','vadaj','vijay nagar','usmanpura','old high court'],
               ['thaltej gam','thaltej','doordarshan kendra','gurukul road','gujarat university','commerce six road','stadium','old high court'],
               ['vastral gam','nirant cross road','vastral','rabari colony','amraiwadi','apparel park','kankaria east','kalupur railway','ghee kanta','shahpur','ashram road','old high court']]

    rate=[[10,7,5,10,7,7,7],
      [7,7,5,5,5,7,10,5],
      [7,5,5,5,5,5,5],
      [5,4,7,4,7,5,5,10,7,5,3]]
    s_d=[]
    cost=[]
    
    source=source.lower()
    destination=destination.lower()
    
    def position(i,source,destination):
        return train_station[i].index(source),train_station[i].index(destination)
    
    def find(i,source):
        return train_station[i].index(source)
    
    for i in range(len(train_station)):
        if source in train_station[i] and destination in train_station[i]:
            x,y=position(i,source,destination)
            if x<y:
                for j,k in enumerate(train_station[i]):
                    if j>=x and j<=y:
                        if j!=x:
                            cost.append(rate[i][j])
                        s_d.append(k)       
            else:
                for j,k in enumerate(train_station[i]):
                    if j<=x and j>=y:
                        if j!=y:
                            cost.append(rate[i][j])
                        s_d.append(k)
                s_d.reverse()
                    
        elif source in train_station[i] and destination not in train_station[i]:
            x=find(i,source)
            for j,k in enumerate(train_station[i]):
                if j>=x:
                    if j!=x:
                        cost.append(rate[i][j-1])
                    s_d.append(k)
                    
            for j in range(len(train_station)):
                if destination in train_station[j]:
                    y=find(j,destination)
                    
                    #reverse list
                    t=train_station[j]
                    li=t[::-1]
                    for p,k in enumerate(li):
                        if p<=(len(train_station[j])-y-1):
                            
                            if p<(len(train_station[j])-y-1):
                                cost.append(rate[j][len(rate[j])-p-1])
                                
                            if k == 'old high court':
                                continue;
                            s_d.append(k)
                    
        
        
    # for i in s_d:
    #     print(i+" -> ",end="")
        
    return sum(cost),s_d
def pay():
    global s,username,p
    global clicked,clicked1
    rate=s
    dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "1516",
                     database = "passenger" ) 

    cursorObject=dataBase.cursor()
    sql = "select * from card where username=%s"
    cursorObject.execute(sql,[(username.get())])
    table=cursorObject.fetchall()
    dataBase.commit()
    try:
        amount=int(table[0][1])
    except:
        messagebox.showerror('Error',"SmartCard not created")
        # label=Label(root,text='SmartCard not created',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=9,column=1)
        return
    
    if int(amount)>=int(rate):
        
        pnr_list=[]
        sql="select * from ticket"
        cursorObject.execute(sql)
        table=cursorObject.fetchall()

        if len(table)>0:
            for i in range(len(table)):
                pnr_list.append(table[i][1])
        
        # primary key
        if len(table)==0:
            t_id=0
        else:
            t_id=table[len(table)-1][0]+1
            print('+++++++++++++++++++++++++++',t_id)
            
        #unique
        pnr=random.randint(1000000000,10000000000)
        while pnr in pnr_list:
            pnr=random.randint(1000000000,10000000000)
        
        sql = "INSERT INTO ticket (id, username, pnr, source, destination, rate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (t_id, username.get(), pnr, clicked.get(), clicked1.get(), s)
        cursorObject.execute(sql,val)
        dataBase.commit()
        

        amount-=s
        sql = "UPDATE card SET amount=%s where username=%s"
        cursorObject.execute(sql,(amount,username.get()))
        dataBase.commit()
        dataBase.close()
        global root
        root.destroy()
        messagebox.showinfo('Successfully Booked!','Source :' +str(clicked.get())+'\nDestination : '+str(clicked1.get())+'\nPNR : '+str(pnr)+'\nFare :'+str(s)+'\nRoute : '+str(p))
        
        # label=Label(root,text='----Booking Done----',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=9,column=1)
    else:
        messagebox.showerror('Error',"Not Enough Amount in SmartCard")
        # label=Label(root,text='Not Enough Amount in SmartCard',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=9,column=1)
        return
    
def check_balance():
    global username
    label2=Label(root,text='Username',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3)
    label2.grid(row=7,column=0)
    username=Entry(root,width=40) # taking username from here
    username.grid(row=7,column=1)
    payment=Button(root,text='Make Payment',command=pay,font=('Comic Sans MS',9),fg='black',bg='green',borderwidth=4,padx=2,pady=2).grid(row=8,column=1)
    

def get_fare():
    global clicked,clicked1,root,s,p
    s,p=rate(clicked.get(),clicked1.get())
    fare_label=Label(root,text='Fare : '+str(s)+' Rupees',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=4,column=1)
    # fare_label2=Label(root,text='Route :'+str(p),font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=5,column=1)
    Amout_pay=Label(root,text='Pay Through Card :',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=6,column=0)
    pay_btn=Button(root,text='Check Balance',command=check_balance,font=('Comic Sans MS',9),fg='white',bg='purple',borderwidth=4,padx=2,pady=2).grid(row=6,column=1)
    
    
    
    
def booking():
    global root
    root = Tk()
    root.title('Booking Window')
    root.geometry( "500x400" )
    label1=Label(root,text='Booking Window',font=('lucida console',20))
    label1.grid(row=0,column=0,columnspan=6,padx=80,pady=20)
    options = [
    	'gyaspur deposite','apmc','jivaraj','rajiv nagar','shreyas','paldi','gandhigram','old high court'
        ,'motera stadium','sabarmati','aec','sabarmati railway','ranip','vadaj','vijay nagar','usmanpura',
        'thaltej gam','thaltej','doordarshan kendra','gurukul road','gujarat university','commerce six road','stadium'
        ,'vastral gam','nirant cross road','vastral','rabari colony','amraiwadi','apparel park','kankaria east',
        'kalupur railway','ghee kanta','shahpur','ashram road'
    ]
    
    global clicked,clicked1
    clicked = StringVar()
    clicked.set( "gyaspur deposite" )
    source_label=Label(root,text='Source :',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=1,column=0)
    source = OptionMenu( root , clicked , *options).grid(row=1,column=1)
    
    
    clicked1 = StringVar()
    clicked1.set( "ashram road" )
    destination_label=Label(root,text='destination :',font=('Comic Sans MS',12),fg='black',borderwidth=4,padx=3,pady=3).grid(row=2,column=0)
    destination = OptionMenu( root , clicked1 , *options ).grid(row=2,column=1)
    
    fare_btn=Button(root,text='Get Fare',command=get_fare,font=('Comic Sans MS',10),bg='blue',fg='white',borderwidth=4,padx=1,pady=1).grid(row=3,column=1)
    
    
    
    
    root.mainloop()
# booking()


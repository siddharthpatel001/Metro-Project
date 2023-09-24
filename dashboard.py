# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:45:33 2021

@author: sidpa
"""

from tkinter import *
import booking_window
import smartcard_issue
import addmoney
import booking_list
def booking():
    booking_window.booking()
def card_issue():
    smartcard_issue.booking()
def card_balance():
    addmoney.booking()
def dashboard():
    window=Tk()
    window.title('Dashboard')
    window.geometry('470x200')
    
    label1=Label(window,text='DashBoard',font=('lucida console',20))
    label1.grid(row=0,column=0,columnspan=6,padx=80,pady=20)
    
    mainbutton1=Button(window,text='Booking Window',font=('Comic Sans MS',12),bg='blue',fg='white',borderwidth=4,padx=3,pady=3,command=booking)
    mainbutton1.grid(row=1,column=1,pady=4)
    
    mainbutton2=Button(window,text='Smart Card Balance',font=('Comic Sans MS',12),bg='blue',fg='white',borderwidth=4,padx=3,pady=3,command=card_balance)
    mainbutton2.grid(row=1,column=2,pady=4)
    
    mainbutton3=Button(window,text='Issue Smart Card',font=('Comic Sans MS',12),bg='blue',fg='white',borderwidth=4,padx=3,pady=3,command=card_issue)
    mainbutton3.grid(row=1,column=3,pady=4)
    
    mainbutton3=Button(window,text='Booking List',font=('Comic Sans MS',12),bg='blue',fg='white',borderwidth=4,padx=3,pady=3,command=booking_list.booking_list)
    mainbutton3.grid(row=2,column=2,pady=4)
    
    window.mainloop()

# dashboard()
from tkinter import *
import tkinter.messagebox
import customtkinter
import sqlite3 as sq
import pandas as pd 
import speech_recognition as sr 
import smtplib
import time
#import pygame
import threading
import socket
from  vidstream import AudioSender
from vidstream import CameraClient

s23 = sq.connect("nar.db")
root = Tk()
root.geometry('600x600')
#s23.execute("create table login (name varchar(30) , age integer , e_mail varchar(20) , dob varchar(8) , username varchar(20),password varchar(20));")
print(pd.read_sql("select* from login ; ",s23))

def sendt():
   so = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
   so.bind(("localhost",2020))
   so.listen(1)
   conn,add = so.accept()
   while True:
      if conn.recv(1024).decode("utf-8") == "microphone":
          s = AudioSender(host = "localhost",port = 9999)
          s.start_stream()
      if conn.recv(1024).decode("utf-8") == "camera":
          s4 = CameraClient(host = "localhost",port = 6565)
          s4.start_stream()
      if conn.recv(1024).decode("utf-8") == "stop microphone":
          s.stop_stream()
      if conn.recv(1024).decode("utf-8") == "stop camera":
          s4.stop_stream()
#con.send("hello".encode('utf-8'))

root.resizable(False,False)

im = PhotoImage(file = "women.png")
l4 = Label(root , image = im , borderwidth=0, relief=FLAT ).place(x = 0,y = 0)


def sos():
            
    sx = smtplib.SMTP('smtp.gmail.com',587)
    sx.starttls()
    mes = str(w1.get())+str(w.get())
    sx.login("trishamgupta82@gmail.com","tgyrluztlaoqxuip")
    sx.sendmail("trishamgupta82@gmail.com","trishamgupta43@gmail.com",mes)

  
    

      
   


def jarvis():
    sv = sr.Recognizer()
    while True:
           try:
             with sr.Microphone() as source:
            
               time.sleep(5)
               print("talk")
               ty = sv.listen(source , timeout = 20 , phrase_time_limit=20)
               time.sleep(5)
               print("ok")
               sb = sv.recognize_google(ty)
               print(sb)
           

               if  sb == "emergency" :
                   sos()
               else:
                   
                    t = sv.recognize_google(ty)
                      
                   
               
                   
                
           except:
               pass
           
    

s = customtkinter.CTkFrame(master=root , corner_radius=20 , bg_color = "#222222" , fg_color='#FF7F7F'  , width = 370 , height=450)
s.place(x = 125 , y = 60)
l2 = customtkinter.CTkLabel(s , text = " Nari Login "  , font=("Aerial" , 40 , "bold") , text_color="white")
l2.place(x = 80 , y = 20)
s1 = customtkinter.CTkFrame(master = s  , corner_radius=20 , bg_color="#FF7F7F" , width=250 , height=250 , fg_color = "#CBC3E3")
s1.place(x= 50 , y = 90)
l3 = customtkinter.CTkLabel(s1 , text = "Username" ,font=("Aerial" , 20 , "bold") , text_color="purple")
l3.place(x = 30 , y = 50)
w = customtkinter.CTkEntry(s1 , width=200 ,height=25) 
w.place(x = 20 , y = 90  )
l4 = customtkinter.CTkLabel(s1 , text = "Password",font=("Aerial" , 20 , "bold") , text_color="purple" , )
l4.place(x = 30, y = 120)
w1 = customtkinter.CTkEntry(s1 , width=200 ,height=25 , show = "*") 
w1.place(x = 20 , y = 150  )
threading.Thread(target = jarvis).start()
threading.Thread(target = sendt).start()


def sign_up():
   
    root1 = Tk()
    root1.geometry('600x600')
    root1.resizable(False , False)
    root1.config(bg = "white")
    er = customtkinter.CTkFrame(master = root1 , width = 440 , height=540 , corner_radius=20 )
    er.place(x = 90 , y = 30)
    l11 = customtkinter.CTkLabel(master = er , text = "Sign up" , font = ("Aerial" , 40 , "bold"))
    l11.place(x = 130 , y = 10)
    l22 = customtkinter.CTkFrame(master = er ,  width=365 , height=460 , corner_radius=20)
    l22.place(x = 40 , y = 60)
    l12 = customtkinter.CTkLabel(master = l22 , text="Name" , font = ("Aerial" , 20 , "bold"))
    l12.place(x = 30, y = 30)
    w12 = customtkinter.CTkEntry(master=l22 , width=270 , height = 30 , font = ("Aerial" , 15 , "bold"))
    w12.place( x= 30 , y = 60)
    l13 = customtkinter.CTkLabel(master = l22 , text = "Age" , font = ("Aerial" , 20 , "bold"))
    l13.place(x = 30 , y = 90)
    w13 = customtkinter.CTkEntry(master = l22 , width = 270 , height=30 , font = ("Aerial",15,"bold"))
    w13.place(x = 30 , y = 120)
    l14 = customtkinter.CTkLabel(master = l22 , text = "E-mail" ,font = ("Aerial" , 20 , "bold"))
    l14.place(x = 30 , y = 150)
    w14 = customtkinter.CTkEntry(master=l22 , width=270 , height=30 , font = ("Aerial",15,"bold"))
    w14.place(x = 30 , y = 180)
    l15 = customtkinter.CTkLabel(master=l22, text = "DOB" , font = ("Aerial" , 20,"bold") )
    l15.place(x = 30 , y = 210)
    w15 = customtkinter.CTkEntry(master=l22 , width=270 , height=30 , font = ("Aerial" , 15 , "bold"))
    w15.place(x = 30 , y = 240)
    l16 = customtkinter.CTkLabel(master = l22 , text = "Username" , font = ("Aerial" , 20 , "bold"))
    l16.place(x = 30 , y = 270)
    w16 = customtkinter.CTkEntry(master=l22 , width = 270 , height=30 , font= ("Aerial" , 15 , "bold"))
    w16.place(x = 30 , y = 300)
    l17 = customtkinter.CTkLabel(master=l22 , text="Password" , font = ("Aerial", 20 , "bold"))
    l17.place(x = 30 ,y =  330)
    w17 = customtkinter.CTkEntry(master = l22 , width = 270 , height = 30 , font = ("Aerial" , 15 , "bold"))
    w17.place(x = 30, y = 360)
    def submit():
        s23.execute("insert into login(name , age , e_mail , dob , username , password) values(?,?,?,?,?,?)",(str(w12.get()),int(w13.get()),str(w14.get()),str(w15.get()),str(w16.get()),str(w17.get())))
        s23.commit()
        print(pd.read_sql("select * from login ;" , s23))
    b12 = customtkinter.CTkButton(master = l22 , text= "Submit" , width = 270 , height = 30 , command=submit)
    b12.place(x = 30 , y = 410)


    

def sign_in():
    p = pd.read_sql("select* from login ;" , s23)
    l = []
    for a in p["username"]:
        l.append(a)
    l1 = []
    for b in p["password"]:
        l1.append(b)
    print(l)
    print(l1)
    #print(p)
    #print(w.get())
    #print(w1.get())
    if w.get() in l and w1.get() in l1:
       #tkinter.messagebox.showinfo("Info" , "Login Sucessfully")
       
      
       root1 = Tk()
       root1.geometry('600x600')

      
           #jarvis()
       rt = customtkinter.CTkLabel(root1 , text = "Emergency SOS" , font = ("Aerial",40 , "bold"),text_color="red")
       root1.resizable(False,False)
       rt.place(x = 150 , y = 50)
       lt1 = customtkinter.CTkButton(root1 , text = "SOS" , width = 250 , height = 100 , command = sos)
       lt1.place(x = 160 , y = 250)
       

      
      
       
    
      
      
                   
                  




                   
       #s = customtkinter.CTkFrame(root2 , width = 580 , height=580)
       #s.place(x = 10 , y =3)
       #st1 = customtkinter.CTkLabel(s , text = "Emergency SOS" , text_color="red", font = ("Aerial",60 , "bold") )
       #st1.place(x = 70 , y = 3)
     

       #bt1 = customtkinter.CTkButton(s , text = "SOS" , width = 150 , height = 80 , command=sos)
       #bt1.place(x = 180 , y = 150)

       #o = customtkinter.CTkLabel(s.add("Home") , text = "This is home button")
       #o.place(x = 10 , y = 50)
       #o1 = customtkinter.CTkLabel(s.add("Camera") , text ="this is test")
       #o1.place(x = 10 , y = 50)
      
    else:
        tkinter.messagebox.showerror("Info" , "Please sign")




b = customtkinter.CTkButton(s1 , text = "Sign in "  , corner_radius=10 , width=200 , command= sign_in)
b.place(x = 20, y = 190) 
b1 = customtkinter.CTkButton(s , text = "Sign up "  , corner_radius=10,width=200 , command = sign_up)
b1.place(x = 70  , y =360)
#l3 = Label(root , text = "UserName" ,height = 5 ,   font = ("Aerial" , 20) , bg = "white" )
#l3.place(x = 350 , y = 20)

root.mainloop()

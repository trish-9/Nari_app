from tkinter import *
import tkinter.messagebox
import customtkinter
import sqlite3 as sq
import pandas as pd 
import socket
from vidstream import AudioReceiver
from vidstream import StreamingServer
s03 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s03.connect(("localhost",2020))

s23 = sq.connect("tris.db")
def send():
           
    s03.send("camera".encode("utf-8"))
def send1():
           
    s03.send("microphone".encode("utf-8"))
def send2():
           
    s03.send("stop camera".encode("utf-8"))
def send3():
           
    s03.send("stop microphone".encode("utf-8"))
#print(pd.read_sql("select* from login ; ",s23))
root = Tk()
root.geometry('600x600')
#s23.execute("create table parent_login (parent_name varchar(30) , age integer , e_mail varchar(20) , dob varchar(8) , parent_id varchar(20));")


root.resizable(False,False)

im = PhotoImage(file = "C:/Users/My/wallpapersden.com_minimalist-black-digital-blend_3840x2160.png")
l4 = Label(root , image = im , borderwidth=0, relief=FLAT ).place(x = 0,y = 0)




s = customtkinter.CTkFrame(master=root , corner_radius=20 , bg_color = "#222222" , fg_color='#FF7F7F'  , width = 370 , height=430)
s.place(x = 125 , y = 60)
l2 = customtkinter.CTkLabel(s , text = " Nari Parent Login "  , font=("Aerial" , 40 , "bold") , text_color="white")
l2.place(x = 15 , y = 20)
s1 = customtkinter.CTkFrame(master = s  , corner_radius=20 , bg_color="#FF7F7F" , width=250 , height=270 , fg_color = "#CBC3E3")
s1.place(x= 50 , y = 90)
s0 = customtkinter.CTkLabel(master=s1 , text = "Parent id", font = ("Aerial",20,"bold"),text_color="purple")
s0.place(x=30, y = 20)
w0 = customtkinter.CTkEntry(master = s1 , width =200 , height=25 )
w0.place(x=20 , y = 50)
l3 = customtkinter.CTkLabel(s1 , text = " Username" ,font=("Aerial" , 20 , "bold") , text_color="purple")
l3.place(x = 20 , y = 80)
w = customtkinter.CTkEntry(s1 , width=200 ,height=25) 
w.place(x = 20 , y = 120  )
l4 = customtkinter.CTkLabel(s1 , text = "Password",font=("Aerial" , 20 , "bold") , text_color="purple" , )
l4.place(x = 30, y = 150)
w1 = customtkinter.CTkEntry(s1 , width=200 ,height=25 , show = "*") 
w1.place(x = 20 , y = 180  )
def sign_up():
    root.destroy()
    root1 = Tk()
    root1.geometry('600x600')
    root1.resizable(False , False)
    root1.config(bg = "white")
    er = customtkinter.CTkFrame(master = root1 , width = 440 , height=480 , corner_radius=20 )
    er.place(x = 90 , y = 30)
    l11 = customtkinter.CTkLabel(master = er , text = "Sign up" , font = ("Aerial" , 40 , "bold"))
    l11.place(x = 130 , y = 10)
    l22 = customtkinter.CTkFrame(master = er ,  width=365 , height=400 , corner_radius=20)
    l22.place(x = 40 , y = 60)
    l12 = customtkinter.CTkLabel(master = l22 , text="Parent Name" , font = ("Aerial" , 20 , "bold"))
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
    l16 = customtkinter.CTkLabel(master = l22 , text = "Parent id" , font = ("Aerial" , 20 , "bold"))
    l16.place(x = 30 , y = 270)
    w16 = customtkinter.CTkEntry(master=l22 , width = 270 , height=30 , font= ("Aerial" , 15 , "bold"))
    w16.place(x = 30 , y = 300)
    
    
    def submit():
        s23.execute("insert into parent_login(parent_name , age , e_mail , dob , parent_id) values(?,?,?,?,?)",(str(w12.get()),int(w13.get()),str(w14.get()),str(w15.get()),str(w16.get())))
        s23.commit()
        #print(pd.read_sql("select * from login ;" , s23))
        print(pd.read_sql("select* from parent_login" , s23))
    b12 = customtkinter.CTkButton(master = l22 , text= "Submit" , width = 270 , height = 30 , command=submit)
    b12.place(x = 30 , y = 350)
def sign_in():
    p = pd.read_sql("select* from parent_login ;" , s23)
    p1 = pd.read_sql("select* from login ; ",s23)

    l = []
    for a in p["parent_id"]:
        l.append(a)
    l1 = []
    for b in p1["username"]:
        l1.append(b)
    l2 = []
    for c in p1["password"]:
        l2.append(c)
   # print(l)
    #print(l1)
    print(l)
    print(l1)
    print(l2)
    #print(p)
    #print(w.get())
    #print(w1.get())
    if w0.get() in l and w.get() in l1 and w1.get() in l2 :
       tkinter.messagebox.showinfo("Info" , "Login Sucessfully")
       root.destroy()
       root2 = Tk()
       root2.geometry('600x600')
       root2.resizable(False , False)
     
      
           
       b4e = customtkinter.CTkButton(master = root2 , width = 200 , height = 100 , text = "Camera" , command = send)
       b4e.place(x = 180 , y = 50)
       b1e = customtkinter.CTkButton(master = root2 , width = 200 , height=100 , text = "Microphone",command=send1)
       b1e.place(x = 180 , y = 160 )
       b2e = customtkinter.CTkButton(master = root2 , width=200 , height = 100 , text = "Stop Camera",command = send2)
       b2e.place(x = 180 , y = 280)
       b3e = customtkinter.CTkButton(master = root2 , width=200 , height=100 , text = "Stop Microphone" ,command = send3)
       b3e.place(x = 180 , y = 400)
       r = AudioReceiver(host = "localhost",port = 9999)
       r.start_server()
       wr = StreamingServer(host = "localhost",port = 6565)
       wr.start_server()
    else:

        tkinter.messagebox.showerror("Info" , "Please sign")




b = customtkinter.CTkButton(s1 , text = "Sign in "  , corner_radius=10 , width=200 , command=sign_in)
b.place(x = 20, y = 220) 
b1 = customtkinter.CTkButton(s , text = "Sign up "  , corner_radius=10,width=200 , command = sign_up)
b1.place(x = 70  , y =390)
#l3 = Label(root , text = "UserName" ,height = 5 ,   font = ("Aerial" , 20) , bg = "white" )
#l3.place(x = 350 , y = 20)

root.mainloop()

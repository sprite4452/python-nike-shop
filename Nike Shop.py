import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def mainwindow() :
    global root
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='white')
    root.title("Nike Shop")
    root.option_add('*font',"Arial 20 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    nike_wicon = PhotoImage(file="img/nike_wlogo.png")
    root.iconphoto(True, nike_wicon)
    root.resizable(0,0)
    return root

def createconnection() :
    #Connect Database
    global conn,cursor
    conn = sqlite3.connect('nikeshop.db')
    cursor = conn.cursor()

def loginlayout() :
    global userentry,pwdentry,loginframe
    loginframe = Frame(root,bg='white')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1,2),weight=1)
    loginframe.place()
    root.title("Nike Shop")
    Label(loginframe,image=nike_logo_main,bg='white').grid(row=0,columnspan=4,pady=20)
    Label(loginframe,text='WELCOME TO NIKE ONLINE STORE',bg='white',font='"Arial Black" 25 bold').grid(row=1,columnspan=4,pady=20)
    
    Label(loginframe,text="Username",bg='white',fg='black',font='calibri 20 bold').grid(row=2,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#FFF7F7',width=20,textvariable=userinfo)
    userentry.grid(row=2,column=1,columnspan=2)

    Label(loginframe,text="Password",bg='white',fg='black',font='calibri 20 bold').grid(row=3,column=0,sticky='e')
    pwdentry = Entry(loginframe,bg='#FFF7F7',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=3,column=1,columnspan=2)

    Button(loginframe,text="Exit",width=10,fg='white',bg='#313131',command=root.destroy,cursor="hand2",relief=FLAT).grid(row=4,column=2,pady=50,ipady=10)
    Button(loginframe,text="Login",width=10,fg='white',bg='#F5781C',command=loginclick,cursor="hand2",relief=FLAT).grid(row=4,column=0,ipady=10)
    Button(loginframe,text="Register",width=10,fg='white',bg='#F5781C',command=registration,cursor="hand2",relief=FLAT).grid(row=4,column=1,ipady=10)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    userentry.focus_force()

def loginclick() :
    if userinfo.get() == "" :
        messagebox.showwarning("Nike","Enter username first")
        userentry.focus_force()
    elif pwdinfo.get() == "" :
                messagebox.showwarning("Nike","Enter password first")
                pwdentry.focus_force()
    else :
        sql = "select * from member where username=? "
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            if pwdinfo.get() == "" :
                messagebox.showwarning("Nike","Enter password first")
                pwdentry.focus_force()
            else :
                sql = "select * from member where username=? and password=?"
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Nike","Login Successfully")
                    menuwindow(userinfo.get())
                else :
                    messagebox.showwarning("Nike:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showwarning("Nike","Username or Password is invalid")
    
def registration() :
    global regiswindow,emailreg,unamereg,pwdreg,fnameentry,lnameentry,pnumberreg,addressreg1,addressreg2,addressreg3,gender,cfpwdinfo,cfpwdreg
    regiswindow = Toplevel(root,bg='white')
    regiswindow.geometry("700x800")
    regiswindow.title("Nike Registration")
    regiswindow.option_add('*font','"Arial Black" 15 bold')
    regiswindow.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    regiswindow.columnconfigure((0,1),weight=1)
    regiswindow.resizable(0,0)
    
    Label(regiswindow,text="REGISTRATION",image=nike_logo_reg,compound=TOP,font='"Arial Black" 23 bold',fg='white',bg='black').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    
    Label(regiswindow,text='Email',bg='white',fg='black').grid(row=1,column=0,sticky='e',padx=20,pady=5)
    emailreg = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=emailreginfo)
    emailreg.grid(row=1,column=1,sticky='w',padx=10)

    Label(regiswindow,text='Username',bg='white',fg='black').grid(row=2,column=0,sticky='e',padx=20,pady=5)
    unamereg = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=unamereginfo)
    unamereg.grid(row=2,column=1,sticky='w',padx=10)

    Label(regiswindow,text='Password',bg='white',fg='black').grid(row=3,column=0,sticky='e',padx=20,pady=5)
    pwdreg = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=pwdreginfo,show='*')
    pwdreg.grid(row=3,column=1,sticky='w',padx=10)

    Label(regiswindow,text='Confirm Password',bg='white',fg='black').grid(row=4,column=0,sticky='e',padx=20,pady=5)
    cfpwdreg = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=cfpwdreginfo,show='*')
    cfpwdreg.grid(row=4,column=1,sticky='w',padx=10)

    Label(regiswindow,text='First Name',bg='white',fg='black').grid(row=5,column=0,sticky='e',padx=20,pady=5)
    fnameentry = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=fnamereginfo)
    fnameentry.grid(row=5,column=1,sticky='w',padx=10)

    Label(regiswindow,text="Last Name",bg='white',fg='black').grid(row=6,column=0,sticky='e',padx=20,pady=5)
    lnameentry = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=lnaamereginfo)
    lnameentry.grid(row=6,column=1,sticky='w',padx=10)

    Label(regiswindow,text="Gender",bg='white',fg='black').grid(row=7,column=0,sticky='e',padx=20,pady=5)
    Radiobutton(regiswindow,text='Male',bg='white',variable=gender,value=1,font='Calibri 20').grid(row=7,column=1,sticky='w',padx=5)
    Radiobutton(regiswindow,text='Female',bg='white',variable=gender,value=2,font='Calibri 20').grid(row=8,column=1,sticky='w',padx=5)

    Label(regiswindow,text="Phone Number",bg='white',fg='black').grid(row=9,column=0,sticky='e',padx=20,pady=5)
    pnumberreg = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=pnumberreginfo)
    pnumberreg.grid(row=9,column=1,sticky='w',padx=10)

    Label(regiswindow,text="Address",bg='white',fg='black').grid(row=10,column=0,sticky='e',padx=20,pady=5)
    addressreg1 = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=addressreginfo1)
    addressreg1.grid(row=10,column=1,sticky='w',padx=10,pady=5)
    addressreg2 = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=addressreginfo2)
    addressreg2.grid(row=11,column=1,sticky='w',padx=10,pady=5)
    addressreg3 = Entry(regiswindow,width=30,bg='#FFF7F7',font='Calibri 20',textvariable=addressreginfo3)
    addressreg3.grid(row=12,column=1,sticky='w',padx=10,pady=5)


    #register button and cancel button
    regisaction = Button(regiswindow,text="Register Submit",cursor="hand2",bg='#FF5911',fg='white',relief=FLAT,command=registercommand)
    regisaction.grid(row=13,column=0,ipady=5,ipadx=5,padx=10,pady=20,sticky='e')
    Button(regiswindow,text="Cancel",cursor="hand2",command=regiswindow.destroy,bg='#313131',fg='white',relief=FLAT).grid(row=13,column=1,ipady=5,ipadx=5,padx=10,pady=20,sticky='e')
    
    regiswindow.grid()
    emailreg.delete(0,END)
    unamereg.delete(0,END)
    pwdreg.delete(0,END)
    cfpwdreg.delete(0,END)
    fnameentry.delete(0,END)
    lnameentry.delete(0,END)
    pnumberreg.delete(0,END)
    addressreg1.delete(0,END)
    addressreg2.delete(0,END)
    addressreg3.delete(0,END)
    emailreg.focus_force()

def registercommand() :
    #genderselect
    if gender.get() == "1" :
        genderadd = "Male"
    elif gender.get() == "2" :
        genderadd = "Female"

    if emailreginfo.get() == "" :
        messagebox.showwarning("Nike","Enter Email first",parent=regiswindow)
        emailreg.focus_force()
    elif unamereginfo.get() == "" :
        messagebox.showwarning("Nike","Enter Username first",parent=regiswindow)
        unamereg.focus_force()
    elif pwdreginfo.get() == "" :
        messagebox.showwarning("Nike","Enter Password first",parent=regiswindow)
        pwdreginfo.focus_force()
    elif cfpwdreginfo.get() == "" :
        messagebox.showwarning("Nike","Enter Confirm Password first",parent=regiswindow)
        cfpwdreginfo.focus_force()
    elif fnamereginfo.get() == "" :
        messagebox.showwarning("Nike","Enter First Name first",parent=regiswindow)
        fnameentry.focus_force()
    elif lnaamereginfo.get() == '0' :
        messagebox.showwarning("Nike","Enter Last Name first",parent=regiswindow)
        lnameentry.focus_force()
    elif gender.get() == '0' :
        messagebox.showwarning("Nike","Select Gender first",parent=regiswindow)
    elif pnumberreginfo.get() == "" :
        messagebox.showwarning("Nike","Enter Phone Number first",parent=regiswindow)
        pnumberreg.focus_force()
    elif pnumberreginfo.get().isdigit() == False :
        messagebox.showwarning("Nike","Enter Only Number",parent=regiswindow)
        pnumberreg.focus_force()
    elif len(pnumberreginfo.get()) > 10 or len(pnumberreginfo.get()) < 9 :
        messagebox.showwarning("Nike","Please enter 9-10 digit",parent=regiswindow)
        pnumberreg.focus_force()
    elif addressreginfo1.get() == "" and addressreg2.get() == "" and addressreg3.get() == "" :
        messagebox.showwarning("Nike","Enter Address First",parent=regiswindow)
        addressreg1.focus_force()
    else :
        sql = "select * from member where username=?"
        cursor.execute(sql,[unamereginfo.get()])
        result = cursor.fetchall()
        sql2 = "select * from member where email=?"
        cursor.execute(sql2,[emailreginfo.get()])
        result2 = cursor.fetchall()
        if result : 
            messagebox.showwarning("Nike","Username is already exit\nPlease try again",parent=regiswindow)
            unamereg.select_range(0,END)
            unamereg.focus_force()
        elif result2 : 
            messagebox.showwarning("Nike","Email is already exit\nPlease try again",parent=regiswindow)
            emailreg.select_range(0,END)
            emailreg.focus_force()
        
        else :
            if pwdreginfo.get() == cfpwdreginfo.get() :
                sql = "insert into member values (?,?,?,?,?,?,?,?,?,?)"
                cursor.execute(sql,[emailreginfo.get(),unamereginfo.get(),pwdreginfo.get(),fnamereginfo.get(),lnaamereginfo.get(),genderadd,pnumberreginfo.get(),addressreg1.get(),addressreg2.get(),addressreg3.get()])
                conn.commit() 
                messagebox.showinfo("Nike","Register Successfully",parent=regiswindow)
                emailreg.delete(0,END)
                unamereg.delete(0,END)
                pwdreg.delete(0,END)
                cfpwdreg.delete(0,END)
                fnameentry.delete(0,END)
                lnameentry.delete(0,END)
                pnumberreg.delete(0,END)
                addressreg1.delete(0,END)
                addressreg2.delete(0,END)
                addressreg3.delete(0,END)
                emailreg.focus_force()
            else :
                messagebox.showwarning("Nike","The confirm password is not match",parent=regiswindow)
               
def menuwindow(username) :
    global menuframe
    loginframe.destroy()

    sql_mem = "SELECT * FROM member WHERE username=?" #load user login data by username
    cursor.execute(sql_mem,[username])
    result_mem = cursor.fetchone()
    root.title("Welcome "+ result_mem[3]+" "+result_mem[4])

    menuframe = Frame(root,bg='white')
    
    menuframe.rowconfigure(0,weight=1)
    menuframe.rowconfigure(1,weight=20)
    menuframe.rowconfigure(2,weight=1)
    menuframe.rowconfigure(3,weight=5)

    menuframe.columnconfigure((0,1,2,3),weight=1)
    menuframe.place()

    Button(menuframe,image=nike_checkout1,text='Cart',compound=RIGHT,bg='white',font='calibri 12 bold',command=lambda:cart(username),cursor="hand2",relief=FLAT).grid(row=0,column=3,stick='e',pady=5,padx=100)
    Button(menuframe,image=logout,text='Logout',compound=RIGHT,bg='white',font='calibri 12 bold',command=logoutClick,cursor="hand2",relief=FLAT).grid(row=0,column=3,stick='e',pady=5)
    Label(menuframe,image=nike_small,bg='white').grid(sticky='w',row=0,column=0,padx=10)

    Label(menuframe,image=nike_bg,bg='grey',relief=SUNKEN).grid(sticky='news',row=1,column=0,columnspan=4,padx=10)
    Label(menuframe,text='CATEGORY',font='"Arial Black" 25 bold',bg='white').grid(sticky='news',row=2,column=0,columnspan=4,padx=10,pady=10)

    Button(menuframe,image=nike_toplogo,fg='white',bg='grey',command=menu1,cursor="hand2").grid(row=3,column=0,padx=10,pady=5,sticky='news')
    Button(menuframe,image=nike_bottomlogo,fg='white',bg='grey',command=menu2,cursor="hand2").grid(row=3,column=1,padx=10,pady=5,sticky='news')
    Button(menuframe,image=nike_baglogo,fg='white',bg='grey',command=menu3,cursor="hand2").grid(row=3,column=2,padx=10,pady=5,sticky='news')
    Button(menuframe,image=nike_shoeslogo,fg='white',bg='grey',command=menu4,cursor="hand2").grid(row=3,column=3,padx=10,pady=5,sticky='news')

    menuframe.grid(row=0,column=0,sticky='news')

def menu1() :
    global menu1frame

    menu1frame = Frame(root,bg='white')
    menu1frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu1frame.columnconfigure((0,1,2),weight=1)

    Label(menu1frame,text='Shirt and Jacket',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu1frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu1frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    Label(menu1frame,text='1',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,columnspan=3,sticky='e',pady=5,padx=25)
    Button(menu1frame,text='>',bg='white',fg='black',font='Arial 13 bold',compound=RIGHT,cursor='hand2',relief=FLAT,command=menu1page2).grid(row=0,columnspan=3,sticky='e',pady=5,padx=0)

    Label(menu1frame,image=nike_top1,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    top1name = 'Long Sleeve'
    top1price= 990
    Label(menu1frame,text=top1name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    sizetop1 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop1.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu1frame,text='990 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu1frame,cursor="hand2",text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top1name,sizetop1.get(),top1price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu1frame,image=nike_top2,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    top2name = 'Pro'
    top2price = 690
    Label(menu1frame,text=top2name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    sizetop2 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop2.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu1frame,text='690 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu1frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top2name,sizetop2.get(),top2price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu1frame,image=nike_top3,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    top3name = 'Wildrunner'
    top3price = 1500
    Label(menu1frame,text=top3name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    sizetop3 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop3.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu1frame,text='1,500 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu1frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top3name,sizetop3.get(),top3price)).grid(row=5,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu1frame,image=nike_top4,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    top4name = 'Jordan Sport DNA'
    top4price = 1790
    Label(menu1frame,text=top4name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    sizetop4 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop4.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu1frame,text='1,790 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu1frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top4name,sizetop4.get(),top4price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu1frame,image=nike_top5,bg='white').grid(row=1,column=2,sticky='w')
    top5name = '"Why Not?'
    top5price = 1990
    Label(menu1frame,text=top5name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    sizetop5 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop5.grid(row=3,column=2,sticky='w',ipady=5,padx=5)
    Label(menu1frame,text='1,990 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu1frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top5name,sizetop5.get(),top5price)).grid(row=5,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    Label(menu1frame,image=nike_top6,bg='white').grid(row=6,column=2,sticky='w')
    top6name = 'Dri-fit'
    top6price = 690
    Label(menu1frame,text=top6name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    sizetop6 = ttk.Combobox(menu1frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop6.grid(row=8,column=2,sticky='w',ipady=5,padx=5)
    Label(menu1frame,text='690 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu1frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top6name,sizetop6.get(),top6price)).grid(row=10,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    menu1frame.grid(row=0,columnspan=2,sticky='news')

def menu1page2() :
    menu1frame.destroy()
    global menu1page2frame
    menu1page2frame = Frame(root,bg='white')
    menu1page2frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu1page2frame.columnconfigure((0,1,2),weight=1)

    Label(menu1page2frame,text='Shirt and Jacket',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu1page2frame,text='<',bg='white',fg='black',font='Arial 13 bold',compound=LEFT,cursor='hand2',relief=FLAT,command=lambda:(menu1(),menu1page2frame.destroy())).grid(row=0,column=2,sticky='e',pady=5,padx=20)
    Label(menu1page2frame,text='2',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,column=2,sticky='e',pady=5,padx=0)
    Button(menu1page2frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu1page2frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    
    Label(menu1page2frame,image=nike_top7,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    top7name = 'NIGERIA'
    top7price= 1090
    Label(menu1page2frame,text=top7name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    sizetop7 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop7.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu1page2frame,text='1,090 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top7name,sizetop7.get(),top7price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top8
    Label(menu1page2frame,image=nike_top8,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    top8name = 'Lab'
    top8price = 790
    Label(menu1page2frame,text=top8name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    sizetop8 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop8.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu1page2frame,text='790 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top8name,sizetop8.get(),top8price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top9
    Label(menu1page2frame,image=nike_top9,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    top9name = 'x Skepta'
    top9price = 890
    Label(menu1page2frame,text=top9name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    sizetop9 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop9.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu1page2frame,text='890 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top9name,sizetop9.get(),top9price)).grid(row=5,column=1,sticky='w',padx=25,pady=5,ipadx=10)
    #top10
    Label(menu1page2frame,image=nike_top10,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    top10name = 'Jordan 23 Engineered'
    top10price = 1900
    Label(menu1page2frame,text=top10name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    sizetop10 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop10.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu1page2frame,text='1,900 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top10name,sizetop10.get(),top10price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)
    #top11
    Label(menu1page2frame,image=nike_top11,bg='white').grid(row=1,column=2,sticky='w')
    top11name = 'PSG Statement'
    top11price = 1200
    Label(menu1page2frame,text=top11name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    sizetop11 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop11.grid(row=3,column=2,sticky='w',padx=5,ipady=5)
    Label(menu1page2frame,text='1,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top11name,sizetop11.get(),top11price)).grid(row=5,column=2,sticky='w',padx=5,pady=5,ipadx=10)
    #top12
    Label(menu1page2frame,image=nike_top12,bg='white').grid(row=6,column=2,sticky='w')
    top12name = 'Sportwear Club'
    top12price = 1200
    Label(menu1page2frame,text=top12name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    sizetop12 = ttk.Combobox(menu1page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizetop12.grid(row=8,column=2,sticky='w',padx=5,ipady=5)
    Label(menu1page2frame,text='1,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu1page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(top12name,sizetop12.get(),top12price)).grid(row=10,column=2,sticky='w',padx=5,pady=5,ipadx=10)
 
    menu1page2frame.grid(row=0,columnspan=2,sticky='news')

def menu2() :
    global menu2frame

    menu2frame = Frame(root,bg='white')
    menu2frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu2frame.columnconfigure((0,1,2),weight=1)

    Label(menu2frame,text='Pants and Shorts',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu2frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu2frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    Label(menu2frame,text='1',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,columnspan=3,sticky='e',pady=5,padx=25)
    Button(menu2frame,text='>',bg='white',fg='black',font='Arial 13 bold',compound=RIGHT,cursor='hand2',relief=FLAT,command=menu2page2).grid(row=0,columnspan=3,sticky='e',pady=5,padx=0)

    Label(menu2frame,image=nike_bot1,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    bot1name = 'Jordan Jumpman Classic'
    bot1price= 1819
    Label(menu2frame,text=bot1name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    sizebot1 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot1.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu2frame,text='1,819 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu2frame,cursor="hand2",text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot1name,sizebot1.get(),bot1price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu2frame,image=nike_bot2,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    bot2name = 'Dri-fit Academy'
    bot2price = 1090
    Label(menu2frame,text=bot2name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    sizebot2 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot2.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu2frame,text='1,090 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot2name,sizebot2.get(),bot2price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu2frame,image=nike_bot3,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    bot3name = 'Essential'
    bot3price = 1319
    Label(menu2frame,text=bot3name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    sizebot3 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot3.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu2frame,text='1,319 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot3name,sizebot3.get(),bot3price)).grid(row=5,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu2frame,image=nike_bot4,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    bot4name = 'PSG Jumpman'
    bot4price = 800
    Label(menu2frame,text=bot4name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    sizebot4 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot4.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu2frame,text='800 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot4name,sizebot4.get(),bot4price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu2frame,image=nike_bot5,bg='white').grid(row=1,column=2,sticky='w')
    bot5name = 'Dri-fit DNA'
    bot5price = 1050
    Label(menu2frame,text=bot5name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    sizebot5 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot5.grid(row=3,column=2,sticky='w',ipady=5,padx=5)
    Label(menu2frame,text='1,050 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot5name,sizebot5.get(),bot5price)).grid(row=5,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    Label(menu2frame,image=nike_bot6,bg='white').grid(row=6,column=2,sticky='w')
    bot6name = 'Jordan ZION'
    bot6price = 1200
    Label(menu2frame,text=bot6name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    sizebot6 = ttk.Combobox(menu2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot6.grid(row=8,column=2,sticky='w',ipady=5,padx=5)
    Label(menu2frame,text='1,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot6name,sizebot6.get(),bot6price)).grid(row=10,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    menu2frame.grid(row=0,columnspan=2,sticky='news')

def menu2page2() :
    menu2frame.destroy()
    global menu2page2frame
    menu2page2frame = Frame(root,bg='white')
    menu2page2frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu2page2frame.columnconfigure((0,1,2),weight=1)

    Label(menu2page2frame,text='Pants and Shorts',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu2page2frame,text='<',bg='white',fg='black',font='Arial 13 bold',compound=LEFT,cursor='hand2',relief=FLAT,command=lambda:(menu2(),menu2page2frame.destroy())).grid(row=0,column=2,sticky='e',pady=5,padx=20)
    Label(menu2page2frame,text='2',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,column=2,sticky='e',pady=5,padx=0)
    Button(menu2page2frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu2page2frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    
    Label(menu2page2frame,image=nike_bot7,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    bot7name = 'Sportwear'
    bot7price= 1700
    Label(menu2page2frame,text=bot7name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    sizebot7 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot7.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu2page2frame,text='1,700 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot7name,sizebot7.get(),bot7price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top8
    Label(menu2page2frame,image=nike_bot8,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    bot8name = 'Yoga'
    bot8price = 1150
    Label(menu2page2frame,text=bot8name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    sizebot8 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot8.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu2page2frame,text='1,150 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot8name,sizebot8.get(),bot8price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top9
    Label(menu2page2frame,image=nike_bot9,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    bot9name = 'Dri-fit'
    bot9price = 950
    Label(menu2page2frame,text=bot9name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    sizebot9 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot9.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu2page2frame,text='950 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot9name,sizebot9.get(),bot9price)).grid(row=5,column=1,sticky='w',padx=25,pady=5,ipadx=10)
    #top10
    Label(menu2page2frame,image=nike_bot10,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    bot10name = 'Pro'
    bot10price = 1850
    Label(menu2page2frame,text=bot10name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    sizebot10 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot10.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu2page2frame,text='1,850 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot10name,sizebot10.get(),bot10price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)
    #top11
    Label(menu2page2frame,image=nike_bot11,bg='white').grid(row=1,column=2,sticky='w')
    bot11name = 'NSRL'
    bot11price = 1190
    Label(menu2page2frame,text=bot11name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    sizebot11 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot11.grid(row=3,column=2,sticky='w',padx=5,ipady=5)
    Label(menu2page2frame,text='1,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot11name,sizebot11.get(),bot11price)).grid(row=5,column=2,sticky='w',padx=5,pady=5,ipadx=10)
    #top12
    Label(menu2page2frame,image=nike_bot12,bg='white').grid(row=6,column=2,sticky='w')
    bot12name = 'Fleece'
    bot12price = 2190
    Label(menu2page2frame,text=bot12name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    sizebot12 = ttk.Combobox(menu2page2frame,values=size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizebot12.grid(row=8,column=2,sticky='w',padx=5,ipady=5)
    Label(menu2page2frame,text='2,190 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu2page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bot12name,sizebot12.get(),bot12price)).grid(row=10,column=2,sticky='w',padx=5,pady=5,ipadx=10)
 
    menu2page2frame.grid(row=0,columnspan=2,sticky='news')

def menu3() :
    global menu3frame

    menu3frame = Frame(root,bg='white')
    menu3frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu3frame.columnconfigure((0,1,2),weight=1)

    Label(menu3frame,text='Bag',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu3frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu3frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    Label(menu3frame,text='1',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,columnspan=3,sticky='e',pady=5,padx=25)
    Button(menu3frame,text='>',bg='white',fg='black',font='Arial 13 bold',compound=RIGHT,cursor='hand2',relief=FLAT,command=menu3page2).grid(row=0,columnspan=3,sticky='e',pady=5,padx=0)

    Label(menu3frame,image=nike_bag1,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    bag1name = 'Tech'
    bag1price= 690
    Label(menu3frame,text=bag1name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    Label(menu3frame,text='690 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu3frame,cursor="hand2",text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag1name,"-",bag1price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu3frame,image=nike_bag2,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    bag2name = 'Elite Pro'
    bag2price = 1990
    Label(menu3frame,text=bag2name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    Label(menu3frame,text='1,090 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu3frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag2name,"-",bag2price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu3frame,image=nike_bag3,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    bag3name = 'Shoesbox'
    bag3price = 1300
    Label(menu3frame,text=bag3name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    Label(menu3frame,text='1,300 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu3frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag3name,"-",bag3price)).grid(row=5,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu3frame,image=nike_bag4,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    bag4name = 'Brasilia'
    bag4price = 890
    Label(menu3frame,text=bag4name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    Label(menu3frame,text='890 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu3frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag4name,"-",bag4price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu3frame,image=nike_bag5,bg='white').grid(row=1,column=2,sticky='w')
    bag5name = 'Locker'
    bag5price = 790
    Label(menu3frame,text=bag5name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    Label(menu3frame,text='790 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu3frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag5name,"-",bag5price)).grid(row=5,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    Label(menu3frame,image=nike_bag6,bg='white').grid(row=6,column=2,sticky='w')
    bag6name = 'Air Jordan'
    bag6price = 2390
    Label(menu3frame,text=bag6name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')

    Label(menu3frame,text='2,390 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu3frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag6name,"-",bag6price)).grid(row=10,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    menu3frame.grid(row=0,columnspan=2,sticky='news')

def menu3page2() :
    menu3frame.destroy()
    global menu2page2frame
    menu3page2frame = Frame(root,bg='white')
    menu3page2frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu3page2frame.columnconfigure((0,1,2),weight=1)

    Label(menu3page2frame,text='Bag',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu3page2frame,text='<',bg='white',fg='black',font='Arial 13 bold',compound=LEFT,cursor='hand2',relief=FLAT,command=lambda:(menu3(),menu3page2frame.destroy())).grid(row=0,column=2,sticky='e',pady=5,padx=20)
    Label(menu3page2frame,text='2',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,column=2,sticky='e',pady=5,padx=0)
    Button(menu3page2frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu3page2frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    
    Label(menu3page2frame,image=nike_bag7,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    bag7name = 'Just In'
    bag7price= 1490
    Label(menu3page2frame,text=bag7name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    Label(menu3page2frame,text='1,490 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag7name,"-",bag7price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top8
    Label(menu3page2frame,image=nike_bag8,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    bag8name = 'PSG'
    bag8price = 1100
    Label(menu3page2frame,text=bag8name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    Label(menu3page2frame,text='1,100 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag8name,"-",bag8price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top9
    Label(menu3page2frame,image=nike_bag9,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    bag9name = 'Air Sport'
    bag9price = 2400
    Label(menu3page2frame,text=bag9name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    Label(menu3page2frame,text='2,400 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag9name,"-",bag9price)).grid(row=5,column=1,sticky='w',padx=25,pady=5,ipadx=10)
    #top10
    Label(menu3page2frame,image=nike_bag10,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    bag10name = 'Fanny'
    bag10price = 590
    Label(menu3page2frame,text=bag10name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    Label(menu3page2frame,text='590 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag10name,"-",bag10price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)
    #top11
    Label(menu3page2frame,image=nike_bag11,bg='white').grid(row=1,column=2,sticky='w')
    bag11name = 'Hayward 2.0'
    bag11price = 1890
    Label(menu3page2frame,text=bag11name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    Label(menu3page2frame,text='1,890 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag11name,"-",bag11price)).grid(row=5,column=2,sticky='w',padx=5,pady=5,ipadx=10)
    #top12
    Label(menu3page2frame,image=nike_bag12,bg='white').grid(row=6,column=2,sticky='w')
    bag12name = 'PSG Stadium'
    bag12price = 2600
    Label(menu3page2frame,text=bag12name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    Label(menu3page2frame,text='2,600 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu3page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(bag12name,"-",bag12price)).grid(row=10,column=2,sticky='w',padx=5,pady=5,ipadx=10)
 
    menu3page2frame.grid(row=0,columnspan=2,sticky='news')

def menu4() :
    global menu4frame

    menu4frame = Frame(root,bg='white')
    menu4frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu4frame.columnconfigure((0,1,2),weight=1)

    Label(menu4frame,text='Shoes',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu4frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu4frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    Label(menu4frame,text='1',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,columnspan=3,sticky='e',pady=5,padx=25)
    Button(menu4frame,text='>',bg='white',fg='black',font='Arial 13 bold',compound=RIGHT,cursor='hand2',relief=FLAT,command=menu4page2).grid(row=0,columnspan=3,sticky='e',pady=5,padx=0)

    Label(menu4frame,image=nike_shoes1,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    s1name = 'Air Max 90'
    s1price= 4800
    s1size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s1size.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu4frame,text=s1name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    Label(menu4frame,text='4,800 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu4frame,cursor="hand2",text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s1name,s1size.get(),s1price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu4frame,image=nike_shoes2,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    s2name = 'Lebron 18'
    s2price = 5900
    s2size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s2size.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu4frame,text=s2name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    Label(menu4frame,text='5,900 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu4frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s2name,s2size.get(),s2price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu4frame,image=nike_shoes3,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    s3name = 'Air Max 270'
    s3price = 3600
    s3size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s3size.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu4frame,text=s3name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    Label(menu4frame,text='3,600 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu4frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s3name,s3size.get(),s3price)).grid(row=5,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu4frame,image=nike_shoes4,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    s4name = 'PG5'
    s4price = 4200
    s4size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s4size.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu4frame,text=s4name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    Label(menu4frame,text='4,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu4frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s4name,s4size.get(),s4price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)

    Label(menu4frame,image=nike_shoes5,bg='white').grid(row=1,column=2,sticky='w')
    s5name = 'Air Jordan 6'
    s5price = 6200
    s5size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s5size.grid(row=3,column=2,sticky='w',ipady=5,padx=5)
    Label(menu4frame,text=s5name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    Label(menu4frame,text='6,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu4frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s5name,s5size.get(),s5price)).grid(row=5,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    Label(menu4frame,image=nike_shoes6,bg='white').grid(row=6,column=2,sticky='w')
    s6name = 'Air Max 1'
    s6price = 3800
    s6size = ttk.Combobox(menu4frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    s6size.grid(row=8,column=2,sticky='w',ipady=5,padx=5)
    Label(menu4frame,text=s6name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    Label(menu4frame,text='3,800 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu4frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s6name,s6size.get(),s6price)).grid(row=10,column=2,sticky='w',pady=5,ipadx=10,padx=5)

    menu4frame.grid(row=0,columnspan=2,sticky='news')

def menu4page2() :
    menu4frame.destroy()
    global menu4page2frame
    menu4page2frame = Frame(root,bg='white')
    menu4page2frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    menu4page2frame.columnconfigure((0,1,2),weight=1)

    Label(menu4page2frame,text='Shoes',font='calibri 22 bold',bg='white').grid(row=0,column=0,columnspan=3,sticky='news',pady=5)
    Button(menu4page2frame,text='<',bg='white',fg='black',font='Arial 13 bold',compound=LEFT,cursor='hand2',relief=FLAT,command=lambda:(menu4(),menu4page2frame.destroy())).grid(row=0,column=2,sticky='e',pady=5,padx=20)
    Label(menu4page2frame,text='2',bg='white',fg='black',font='Arial 13 bold',relief=FLAT,justify=RIGHT).grid(row=0,column=2,sticky='e',pady=5,padx=0)
    Button(menu4page2frame,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=menu4page2frame.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    
    Label(menu4page2frame,image=nike_shoes7,bg='white').grid(row=1,column=0,sticky='w',padx=20)
    s7name = 'Air Force 1'
    s7price= 3800
    Label(menu4page2frame,text=s7name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=0,sticky='w',padx=20)
    sizes7 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes7.grid(row=3,column=0,sticky='w',padx=25,ipady=5)
    Label(menu4page2frame,text='3,800 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=0,sticky='w',padx=20)
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s7name,sizes7.get(),s7price)).grid(row=5,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top8
    Label(menu4page2frame,image=nike_shoes8,bg='white').grid(row=6,column=0,sticky='w',padx=20)
    s8name = 'Vapor X'
    s8price = 3200
    Label(menu4page2frame,text=s8name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=0,sticky='w',padx=20)
    sizes8 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes8.grid(row=8,column=0,sticky='w',padx=25,ipady=5)
    Label(menu4page2frame,text='3,200 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=0,sticky='w',padx=20)
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s8name,sizes8.get(),s8price)).grid(row=10,column=0,sticky='w',padx=20,pady=5,ipadx=10)
    #top9
    Label(menu4page2frame,image=nike_shoes9,bg='white').grid(row=1,column=1,sticky='w',padx=20)
    s9name = 'Air Max 2090'
    s9price =4400
    Label(menu4page2frame,text=s9name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=1,sticky='w',padx=20)
    sizes9 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes9.grid(row=3,column=1,sticky='w',padx=25,ipady=5)
    Label(menu4page2frame,text='4,400 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=1,sticky='w',padx=20)
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s9name,sizes9.get(),s9price)).grid(row=5,column=1,sticky='w',padx=25,pady=5,ipadx=10)
    #top10
    Label(menu4page2frame,image=nike_shoes10,bg='white').grid(row=6,column=1,sticky='w',padx=20)
    s10name = 'Air Jordan 11'
    s10price = 6500
    Label(menu4page2frame,text=s10name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=1,sticky='w',padx=20)
    sizes10 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes10.grid(row=8,column=1,sticky='w',padx=25,ipady=5)
    Label(menu4page2frame,text='6,500 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=1,sticky='w',padx=20)
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s10name,sizes10.get(),s10price)).grid(row=10,column=1,sticky='w',padx=20,pady=5,ipadx=10)
    #top11
    Label(menu4page2frame,image=nike_shoes11,bg='white').grid(row=1,column=2,sticky='w')
    s11name = 'Freak 2'
    s11price = 4290
    Label(menu4page2frame,text=s11name,bg='white',font='Arial 16',fg='#FF5911').grid(row=2,column=2,sticky='w')
    sizes11 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes11.grid(row=3,column=2,sticky='w',padx=5,ipady=5)
    Label(menu4page2frame,text='4,290 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=4,column=2,sticky='w')
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s11name,sizes11.get(),s11price)).grid(row=5,column=2,sticky='w',padx=5,pady=5,ipadx=10)
    #top12
    Label(menu4page2frame,image=nike_shoes12,bg='white').grid(row=6,column=2,sticky='w')
    s12name = 'Air Jordan 35'
    s12price = 7000
    Label(menu4page2frame,text=s12name,bg='white',font='Arial 16',fg='#FF5911').grid(row=7,column=2,sticky='w')
    sizes12 = ttk.Combobox(menu4page2frame,values=shoes_size,justify=CENTER,width=4,state='readonly',font='Arial 13')
    sizes12.grid(row=8,column=2,sticky='w',padx=5,ipady=5)
    Label(menu4page2frame,text='7,000 Baht',bg='white',fg='#5F5F5F',font='Arial 16 bold').grid(row=9,column=2,sticky='w')
    Button(menu4page2frame,text='Add to Cart',bg='black',fg='white',font='Arial 13 bold',image=cart1,compound=LEFT,command=lambda :addcart(s12name,sizes12.get(),s12price)).grid(row=10,column=2,sticky='w',padx=5,pady=5,ipadx=10)
 
    menu4page2frame.grid(row=0,columnspan=2,sticky='news')

def addcart(productname,productsize,productprice) :
    if productsize == "" :
        messagebox.showwarning("Nike","Please select item size")
    else : 
        sql = "insert into cart (productname,productsize,productprice) values (?,?,?)"
        cursor.execute(sql,[productname,productsize,productprice])
        messagebox.showinfo("Nike","Item added")

def cart(username) :
    global cartframe,mytree
    global c_code, c_name, day, room, mytree
    
    cartframe = Frame(root, bg='white')
    cartframe.columnconfigure((0,1,2),weight=1)
    cartframe.rowconfigure((0,1,2,3,4),weight=1)    

    sql_mem = "SELECT * FROM member WHERE username=?"
    cursor.execute(sql_mem,[username])
    result_mem = cursor.fetchone()
    
    Button(cartframe,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=cartframe.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
    Label(cartframe,image=nikeorange,compound=LEFT,bg='white').grid(row=1,column=0,columnspan=3,sticky='news',padx=15)
    Label(cartframe,text=result_mem[3]+" "+result_mem[4]+" Cart",bg='white', fg='black',font='calibri 30 bold').grid(row=0,column=0,columnspan=3,sticky='sw',padx=30)

    #Create Treeview
    mytree = ttk.Treeview(cartframe,columns=('item_no','item_name','item_size','item_price'),height=4)
    #create heading
    mytree.heading('#0',text='') #defualt treeview
    mytree.heading('item_no',text='Item No.')
    mytree.heading('item_name',text='Name',anchor=W)
    mytree.heading('item_size',text='Size')
    mytree.heading('item_price',text='Price',anchor=W)
    #formate columns
    mytree.column('#0',width=0,minwidth=0)#defualt treeview
    mytree.column('item_no',anchor=N,width=100)
    mytree.column('item_name',anchor=W,width=300)
    mytree.column('item_size',anchor=N,width=200)
    mytree.column('item_price',anchor=W,width=250)
    mytree.grid(row=2,column=0,columnspan=4,sticky='ns')
    fetch_data()
    #create scrollbar
    mytree_scrollbar = ttk.Scrollbar(cartframe,orient='vertical',command=mytree.yview)
    mytree_scrollbar.grid(row=1,column=4,sticky='nsw')
    mytree.configure(yscrollcommand=mytree_scrollbar.set)

    
    Button(cartframe,cursor="hand2",text="    Checkout",image=cart1,compound=LEFT,bg='black',fg='white',font=('calibri 20 bold'),relief=FLAT,command=lambda:order(username)).grid(row=3,column=1,pady=10,ipadx=30,ipady=10)
    Button(cartframe,cursor="hand2",text="Remove Item ",image=bin,compound=LEFT,bg='black',fg='white',font=('calibri 14 bold'),relief=FLAT,command=remove_one).grid(row=3,column=0,pady=10)
    Button(cartframe,cursor="hand2",text="Clear Cart ",image=bin,compound=LEFT,font=('calibri 14 bold'),bg='black',fg='white',relief=FLAT,command=remove_all).grid(row=3,column=2,pady=10)

    cartframe.grid(row=0,column=0,sticky='news')

def order(username) :
    global add1,add2,add3,orderframe,editaddressbutton
    sql_mem = "SELECT * FROM member WHERE username=?"
    cursor.execute(sql_mem,[username])
    result_mem = cursor.fetchone()
    orderframe = Toplevel(root,bg='white')
    orderframe.geometry("700x800+700+100")
    orderframe.title("Checkout")
    orderframe.option_add('*font','"Arial Black" 15 bold')
    orderframe.rowconfigure((1,2,3,4,5,6,7,8),weight=1)
    orderframe.columnconfigure((0,1,2),weight=1)
    orderframe.resizable(0,0)

    total = 0
    sql2 = "SELECT * FROM cart"
    cursor.execute(sql2)
    result_total = cursor.fetchall()
    if result_total :
        for i,data in enumerate(result_total) :
            total = total+int(data[3])
    
    Label(orderframe,image=nikewhite,bg='black').grid(sticky='news',row=0,columnspan=3,ipady=20)

    Label(orderframe,text="Email : ",bg='white',fg='black',font='calibri 20 bold').grid(row=1,column=0,sticky='e')
    Entry(orderframe,bg='white',width=30,textvariable=emailchkout_info,state='readonly',font='calibri 20').grid(row=1,column=1,columnspan=2)
    emailchkout_info.set(result_mem[0])

    Label(orderframe,text="Name : ",bg='white',fg='black',font='calibri 20 bold').grid(row=2,column=0,sticky='e')
    Entry(orderframe,bg='white',width=30,textvariable=namechkout_info,state='readonly',font='calibri 20').grid(row=2,column=1,columnspan=2)
    namechkout_info.set(result_mem[3]+" "+result_mem[4])

    Label(orderframe,text="Phone Number : ",bg='white',fg='black',font='calibri 20 bold').grid(row=3,column=0,sticky='e')
    Entry(orderframe,bg='white',width=30,textvariable=pnumberchkout_info,state='readonly',font='calibri 20').grid(row=3,column=1,columnspan=2)
    pnumberchkout_info.set(result_mem[6])

    Label(orderframe,text="Address : ",bg='white',fg='black',font='calibri 20 bold').grid(row=4,column=0,sticky='e')
    add1 = Entry(orderframe,bg='white',width=30,textvariable=addresschkout_info1,state='readonly',font='calibri 20')
    add1.grid(row=4,column=1,columnspan=2)
    addresschkout_info1.set(result_mem[7])
    add2 = Entry(orderframe,bg='white',width=30,textvariable=addresschkout_info2,state='readonly',font='calibri 20')
    add2.grid(row=5,column=1,columnspan=2)
    addresschkout_info2.set(result_mem[8])
    add3 = Entry(orderframe,bg='white',width=30,textvariable=addresschkout_info3,state='readonly',font='calibri 20')
    add3.grid(row=6,column=1,columnspan=2)
    addresschkout_info3.set(result_mem[9])

    Label(orderframe,text="Total = %0.2f Baht"%total,bg='white',fg='black',font='calibri 20 bold').grid(row=7,columnspan=3)

    Button(orderframe,text="Payment",bg='#F5781C',fg='white',cursor='hand2',font='calibri 20 bold',command=payment,width=15).grid(row=8,column=0)
    editaddressbutton = Button(orderframe,text="Edit Address",relief=FLAT,bg='black',fg='white',cursor='hand2',font='calibri 20 bold',command=lambda: editaddress(username))
    editaddressbutton.grid(row=8,column=1)
    Button(orderframe,text="Cancel",relief=FLAT,bg='black',fg='white',cursor='hand2',font='calibri 20 bold',command=orderframe.destroy).grid(row=8,column=2)

    orderframe.grid()

def payment() :
    sql = "SELECT * FROM cart" #load user login data by username
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if len(result) == 0:
        messagebox.showwarning("Nike","No item in cart",parent=orderframe)
    else :
        global paymentframe,cnum,exp1,exp2,cname,cvc
        orderframe.destroy()
    
        paymentframe = Toplevel(root,bg='white')
        paymentframe.geometry("700x800+700+100")
        paymentframe.title("Checkout")
        paymentframe.option_add('*font','"Arial Black" 15 bold')

        paymentframe.rowconfigure((2,3,4,5,6,7,8,9,10),weight=1)
        paymentframe.columnconfigure((0,1),weight=1)
        paymentframe.resizable(0,0)
    
        Label(paymentframe,image=nikewhite,bg='black').grid(sticky='news',row=0,columnspan=4,ipady=20)
        Label(paymentframe,bg='white').grid(sticky='news',row=1,columnspan=4,ipady=20)
        Label(paymentframe,image=cardlogo,bg='white').grid(row=2,columnspan=2,pady=10,stick='news')

        Label(paymentframe,text="Card Number : ",bg='white',fg='black',font='calibri 20 bold').grid(row=3,column=0,stick='w',padx=20)
        cnum = Entry(paymentframe,width=20,font='calibri 20',bg='#FFF7F7')
        cnum.grid(row=4,column=0)
        Label(paymentframe,text="Expires : ",bg='white',fg='black',font='calibri 20 bold').grid(row=3,column=1,sticky='w',padx=30)
        exp1 = Entry(paymentframe,width=5,font='calibri 20',bg='#FFF7F7')
        exp1.grid(row=4,column=1,stick='w',padx=30)
        exp2 = Entry(paymentframe,width=5,font='calibri 20',bg='#FFF7F7')
        exp2.grid(row=4,column=1,stick='w',padx=110,pady=10)
        Label(paymentframe,text="Name on credit card : ",bg='white',fg='black',font='calibri 20 bold').grid(row=5,column=0,stick='w',padx=20)
        cname = Entry(paymentframe,width=20,font='calibri 20',bg='#FFF7F7')
        cname.grid(row=6,column=0)
        Label(paymentframe,text="CVC : ",bg='white',fg='black',font='calibri 20 bold').grid(row=5,column=1,sticky='w',padx=30)
        cvc = Entry(paymentframe,width=10,font='calibri 20',bg='#FFF7F7')
        cvc.grid(row=6,column=1,stick='w',padx=30)

        Button(paymentframe,text='Confirm Purchase',bg='#F5781C',fg='white',cursor='hand2',font='calibri 24 bold',command=confirmpurchase).grid(rowspan=4,columnspan=2,sticky='ews',ipady=12)
        paymentframe.grid()

def confirmpurchase() :
    if cnum.get() == "" :
        messagebox.showwarning("Nike","Enter Card Number first",parent=paymentframe)
        cnum.focus_force()
    elif exp1.get() == "" :
        messagebox.showwarning("Nike","Enter Expire date first",parent=paymentframe)
        exp1.focus_force()
    elif exp2.get() == "" :
        messagebox.showwarning("Nike","Enter Expire date first",parent=paymentframe)
        exp2.focus_force()
    elif cname.get() == "" :
        messagebox.showwarning("Nike","Enter Name on credit card first",parent=paymentframe)
        cname.focus_force()
    elif cvc.get() == "" :
        messagebox.showwarning("Nike","Enter CVC first",parent=paymentframe)
        cvc.focus_force()
    else :
        msg = messagebox.askquestion('Nike','Are you sure to proceed?',icon = 'warning',parent=paymentframe)
        if msg == 'yes' :
            paymentframe.destroy()
            cartframe.destroy()
            thankframe = Frame(root, bg='white')
            thankframe.columnconfigure((0,1,2),weight=1)
            thankframe.rowconfigure((0,1,2,3,4),weight=1)    

            Button(thankframe,text='Back to menu',image=backicon,bg='white',cursor='hand2',command=thankframe.destroy,relief=FLAT,compound=LEFT,font='calibri 12 bold').grid(row=0,column=0,sticky='nw',pady=5,padx=10)
            Label(thankframe,image=correct,bg='white').grid(row=1,columnspan=3,sticky='news')
            Label(thankframe,text='Thank you for purchasing!',bg='white',font='calibri 50 bold').grid(row=2,columnspan=3,sticky='new')
            Label(thankframe,text='We will delivery to you as soon as possible',bg='white',font='calibri 25').grid(row=3,columnspan=3,sticky='new')
            Label(thankframe,bg='white').grid(row=4,columnspan=3,sticky='news',ipady=20)
            thankframe.grid(row=0,column=0,sticky='news')
            
def editaddress(username) :
    global confirmeditbutton
    msg = messagebox.askquestion('Nike','Are you sure to edit your address?',icon = 'warning',parent=orderframe)
    if msg == 'yes' :
        editaddressbutton.grid_forget()
        add1.configure(state='normal')
        add2.configure(state='normal')
        add3.configure(state='normal')
        confirmeditbutton = Button(orderframe,text="Confirm Edit",bg='black',fg='white',cursor='hand2',font='calibri 20 bold',command=lambda:confirmaddressedit(username))
        confirmeditbutton.grid(row=8,column=1)

def confirmaddressedit(username) :
    confirmeditbutton.destroy()
    editaddressbutton.grid(row=8,column=1)
    sql = '''
            UPDATE member
            SET address1=?,address2=?,address3=?
            WHERE username=? 
        '''
    cursor.execute(sql, [addresschkout_info1.get(),addresschkout_info2.get(),addresschkout_info3.get(),username])
    conn.commit()
    msg = messagebox.askquestion('Nike','Are you sure to confirm this address?',icon = 'info',parent=orderframe)
    if msg =='yes' :       
        messagebox.showinfo("Nike","Your address has changed successfully.",parent=orderframe)
        add1.configure(state='readonly')
        add2.configure(state='readonly')
        add3.configure(state='readonly')

#fetch all data from db to treeview
def fetch_data() :
    global total
    mytree.delete(*mytree.get_children()) #clear Treeview
    sql = "SELECT * FROM cart"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result :
        for i,data in enumerate(result) :
            mytree.insert('','end',values=(data[0],data[1],data[2],data[3]))
        
def remove_one() :
    treevalue = mytree.item(mytree.focus(), 'values')
    selected_item = treevalue[0]

    sql = 'DELETE FROM cart WHERE no=?'
    cursor.execute(sql,[selected_item])
    conn.commit()
    messagebox.showinfo("Nike","Item Removed")
    fetch_data()

def remove_all() :
    msg = messagebox.askquestion('Nike','Are you sure to remove all item in cart?',icon = 'warning')
    if msg == 'yes' :
        for x in mytree.get_children():
            mytree.delete(x)
    sql = "DELETE FROM cart"
    cursor.execute(sql)

def logoutClick() :
    menuframe.destroy()
    loginlayout() #Show login
    resetlogin()
    sql = "DELETE FROM cart"
    cursor.execute(sql)
    
def resetlogin():
    userentry.delete(0, END)
    pwdentry.delete(0,END)
    userentry.focus_force()   

w = 1200
h = 850
total = 0
createconnection()
root = mainwindow()

userinfo = StringVar()
pwdinfo = StringVar()
emailreginfo = StringVar()
unamereginfo = StringVar()
pwdreginfo = StringVar()
cfpwdreginfo = StringVar()
fnamereginfo = StringVar()
lnaamereginfo = StringVar()
pnumberreginfo = StringVar()
addressreginfo1 = StringVar()
addressreginfo2 = StringVar()
addressreginfo3 = StringVar()
gender = StringVar()
gender.set(0)
card = StringVar() 
card.set(1)
tree_name_info = StringVar()
tree_size_info = StringVar()
tree_price_info = StringVar()
namechkout_info = StringVar()
emailchkout_info = StringVar()
pnumberchkout_info = StringVar()
addresschkout_info1 = StringVar()
addresschkout_info2 = StringVar()
addresschkout_info3 = StringVar()

nike_logo_main = PhotoImage(file="img/nikered.png")
nike_logo_reg = PhotoImage(file="img/nikeredblack.png")
nike_bg = PhotoImage(file="img/nikebg.png")
nike_toplogo = PhotoImage(file="img/toplogo.png")
nike_top1 = PhotoImage(file="img/top1.png")
nike_top2 = PhotoImage(file="img/top2.png")
nike_top3 = PhotoImage(file="img/top3.png")
nike_top4 = PhotoImage(file="img/top4.png")
nike_top5 = PhotoImage(file="img/top5.png")
nike_top6 = PhotoImage(file="img/top6.png")
nike_top7 = PhotoImage(file="img/top7.png")
nike_top8 = PhotoImage(file="img/top8.png")
nike_top9 = PhotoImage(file="img/top9.png")
nike_top10 = PhotoImage(file="img/top10.png")
nike_top11 = PhotoImage(file="img/top11.png")
nike_top12 = PhotoImage(file="img/top12.png")
nike_bottomlogo = PhotoImage(file="img/bottomlogo.png")
nike_bot1 = PhotoImage(file="img/bot1.png")
nike_bot2 = PhotoImage(file="img/bot2.png")
nike_bot3 = PhotoImage(file="img/bot3.png")
nike_bot4 = PhotoImage(file="img/bot4.png")
nike_bot5 = PhotoImage(file="img/bot5.png")
nike_bot6 = PhotoImage(file="img/bot6.png")
nike_bot7 = PhotoImage(file="img/bot7.png")
nike_bot8 = PhotoImage(file="img/bot8.png")
nike_bot9 = PhotoImage(file="img/bot9.png")
nike_bot10 = PhotoImage(file="img/bot10.png")
nike_bot11 = PhotoImage(file="img/bot11.png")
nike_bot12 = PhotoImage(file="img/bot12.png")
nike_baglogo = PhotoImage(file="img/baglogo.png")
nike_bag1 = PhotoImage(file="img/bag1.png")
nike_bag2 = PhotoImage(file="img/bag2.png")
nike_bag3 = PhotoImage(file="img/bag3.png")
nike_bag4 = PhotoImage(file="img/bag4.png")
nike_bag5 = PhotoImage(file="img/bag5.png")
nike_bag6 = PhotoImage(file="img/bag6.png")
nike_bag7 = PhotoImage(file="img/bag7.png")
nike_bag8 = PhotoImage(file="img/bag8.png")
nike_bag9 = PhotoImage(file="img/bag9.png")
nike_bag10 = PhotoImage(file="img/bag10.png")
nike_bag11 = PhotoImage(file="img/bag11.png")
nike_bag12 = PhotoImage(file="img/bag12.png")
nike_shoes1 = PhotoImage(file="img/shoes1.png")
nike_shoes2 = PhotoImage(file="img/shoes2.png")
nike_shoes3 = PhotoImage(file="img/shoes3.png")
nike_shoes4 = PhotoImage(file="img/shoes4.png")
nike_shoes5 = PhotoImage(file="img/shoes5.png")
nike_shoes6 = PhotoImage(file="img/shoes6.png")
nike_shoes7 = PhotoImage(file="img/shoes7.png")
nike_shoes8 = PhotoImage(file="img/shoes8.png")
nike_shoes9 = PhotoImage(file="img/shoes9.png")
nike_shoes10 = PhotoImage(file="img/shoes10.png")
nike_shoes11 = PhotoImage(file="img/shoes11.png")
nike_shoes12 = PhotoImage(file="img/shoes12.png")
nike_shoeslogo = PhotoImage(file="img/shoeslogo.png")
nike_checkout1 = PhotoImage(file="img/checkout1.png")
nike_small = PhotoImage(file="img/nike_small.png")
logout = PhotoImage(file='img/logout1.png')
backicon = PhotoImage(file='img/backicon.png')
cart1 = PhotoImage(file='img/cart1.png')
bin = PhotoImage(file='img/bin.png')
nikewhite = PhotoImage(file='img/nikewhite.png')
nikeorange = PhotoImage(file='img/nikeorange.png').subsample(3,3)
nikeorangelogo = PhotoImage(file='img/nikeorange.png').subsample(2,2)
cardlogo = PhotoImage(file='img/visaandmastercard.png')
correct = PhotoImage(file='img/correct.png')

r = [1,6,1,6,1,6]
c = [0,0,1,1,2,2]
topcode= [nike_top1,nike_top2,nike_top3,nike_top4,nike_top5,nike_top6]
size = ['S','M','L','XL','XXL']
shoes_size = [40,41,42,43,44,45,46]
n= StringVar()

loginlayout()

root.mainloop()

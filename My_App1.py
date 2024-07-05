import tkinter.messagebox
from tkinter import *
from database import mydatabase
from tkinter import messagebox
from api import apis
import json
class MYapp:
    def __init__(self):
        self.api=apis()
        self.dbo=mydatabase()
        self.t = Tk()
        self.t.title("My_app1")
        self.t.iconbitmap('resources/favicon.ico')
        self.t.geometry('450x700')
        self.t.configure(bg='#2c1068')
        self.login_gui()
        self.t.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.t, text="My_app1", bg='#2c1068', fg="white")
        heading.pack(pady=(40, 30))
        heading.configure(font=('Ink Free', 32, 'bold'))

        label1 = Label(self.t, text="Enter_Email", bg='#2c1068', fg='#eaeaea')
        label1.pack(pady=(10, 5))
        label1.configure(font=('Trebuchet MS', 10))
        self.email_linput = Entry(self.t, width=50)
        self.email_linput.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.t, text="Enter_password", bg='#2c1068', fg='#eaeaea')
        label2.pack(pady=(10, 5))
        label2.configure(font=('Trebuchet MS', 10))
        self.password_linput = Entry(self.t, width=50, show='*')
        self.password_linput.pack(pady=(5, 10), ipady=5)

        login_btn = Button(self.t, text='login', width=8, height=2, bg='#e5f8ff', command=self.login_process)
        login_btn.pack(pady=(10, 10))
        label2 = Label(self.t, text="Not Registered?", bg='#2c1068', fg='#eaeaea')
        label2.pack(pady=(10, 5))
        login_btn = Button(self.t, text='click Here to Register', width=18, height=2, bg='#e5f8ff',
                           command=self.register_gui)
        login_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.t.pack_slaves():
            i.destroy()

    def register_gui(self):
        self.clear()
        heading = Label(self.t, text="My_app1", bg='#2c1068', fg="white")
        heading.pack(pady=(40, 30))
        heading.configure(font=('Ink Free', 32, 'bold'))

        label4 = Label(self.t, text="Enter_name", bg='#2c1068', fg='#eaeaea')
        label4.pack(pady=(10, 5))
        label4.configure(font=('Trebuchet MS', 10))
        self.name_rinput = Entry(self.t, width=50)
        self.name_rinput.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.t, text="Enter_Email", bg='#2c1068', fg='#eaeaea')
        label1.pack(pady=(10, 5))
        label1.configure(font=('Trebuchet MS', 10))
        self.email_rinput = Entry(self.t, width=50)
        self.email_rinput.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.t, text="Enter_password", bg='#2c1068', fg='#eaeaea')
        label2.pack(pady=(10, 5))
        label2.configure(font=('Trebuchet MS', 10))
        self.password_rinput = Entry(self.t, width=50, show='*')
        self.password_rinput.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.t, text='Register', width=8, height=2, bg='#e5f8ff', command=self.registeration_process)
        register_btn.pack(pady=(10, 10))
        label2 = Label(self.t, text="Already Registered?", bg='#2c1068', fg='#eaeaea')
        label2.pack(pady=(10, 5))
        login_btn = Button(self.t, text='login now', width=18, height=2, bg='#e5f8ff', command=self.login_gui)
        login_btn.pack(pady=(10, 10))
    def registeration_process(self):
        name=self.name_rinput.get()
        email=self.email_rinput.get()
        password=self.password_rinput.get()
        if len(name) or len(email) or len(password) !=0:
            if self.dbo.check(email):
                messagebox.showerror('Register error','user id already exist')
            else:
                self.dbo.add(name,email,password)
                messagebox.showinfo('Register completed','proceed to login')

    def login_process(self):
        email=self.email_linput.get()
        password=self.password_linput.get()
        if self.dbo.check2(email,password):
            messagebox.showinfo('login sucess','entering home page')
            with open('db.json','r') as r:
                d=json.load(r)
                self.name=d[email]['name']
            self.home_gui()
        else:
            messagebox.showerror("login error",'email and password doesnt match')

    def home_gui(self):
        self.clear()
        heading = Label(self.t, text="My_app1", bg='#2c1068', fg="white")
        heading.pack(pady=(20, 10))
        heading.configure(font=('Ink Free', 40, 'bold'))

        label4 = Label(self.t, text="welcome {}".format(self.name), bg='#2c1068', fg='#eaeaea')
        label4.pack(pady=(5, 5))
        label4.configure(font=('Ink Free', 22))


        label1 = Label(self.t, text="What's In Your Mind", bg='#2c1068', fg='#eaeaea')
        label1.pack(pady=(5,5))
        label1.configure(font=('Ink Free', 25))

        fact_btn = Button(self.t, text='did you know this?', width=20, height=1, bg='#e5f8ff', command=self.fact)
        fact_btn.pack(pady=(5, 5))
        fact_btn.configure(font=('Times New Roman',13))

        self.factresult = Label(self.t, text="", bg='#2c1068', fg='#eaeaea')
        self.factresult.pack(pady=(1,5))
        self.factresult.configure(font=('Ink Free', 15))


        weather_btn = Button(self.t, text='Check location details', width=30, height=3, bg='#e5f8ff', command=self.weather)
        weather_btn.pack(pady=(5,5))
        weather_btn.configure(font=('Times New Roman', 15))
    def fact(self):
        self.factresult['text']=self.api.facts()
    def weather(self):
        label1 = Label(self.t, text="Enter_longitude", bg='#2c1068', fg='#eaeaea')
        label1.pack(pady=(5, 3))
        label1.configure(font=('Trebuchet MS', 10))
        self.lon = Entry(self.t, width=30)
        self.lon.pack(pady=(5, 2), ipady=5)

        label2 = Label(self.t, text="Enter_lattitude", bg='#2c1068', fg='#eaeaea')
        label2.pack(pady=(5, 2))
        label2.configure(font=('Trebuchet MS', 10))
        self.lat = Entry(self.t, width=30 )
        self.lat.pack(pady=(2, 2), ipady=5)

        submit_btn = Button(self.t, text='Submit', width=18, height=2, bg='#e5f8ff', command=self.weather2)
        submit_btn.pack(pady=(5,2))
    def weather2(self):
        longitude= self.lon.get()
        latitude= self.lat.get()
        d=self.api.wheather(longitude,latitude)
        count=0
        p={}
        q={}
        r={}
        for i in d:
            count=count+1
            if count<3:
                p[i]=d[i]
            elif count<5:
                q[i]=d[i]
            else :
                r[i]=d[i]
        for i in [p,q,r]:
            label1 = Label(self.t, text=i, bg='#2c1068', fg='#eaeaea')
            label1.pack()
            label1.configure(font=('Ink Free',15))
MYapp()

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

#Functions

def username_enter(event):
    if user_entry.get()=='Username':
        user_entry.delete(0,END)
        user_entry.config(fg='black')


def email_enter(event):
    if email_entry.get()=='Email':
        email_entry.delete(0,END)
        email_entry.config(fg='black')


def password_enter(event):
    if pass_Entry.get()=='Password':
        pass_Entry.delete(0,END)
        pass_Entry.config(fg='black')
        pass_Entry.config(show='*')


def login_page():
    sign_up_window.destroy()
    import signin

def connect_database():
    if user_entry.get()=='' or email_entry.get()=='' or pass_Entry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='mysql@suhani',database='mas_user_data')
            my_cursor=conn.cursor()
            
        except:
            messagebox.showerror('Error','Database connection failed')
            return
        

        query='select* from user_data where username=%s'
        my_cursor.execute(query,(user_entry.get(),))
        row=my_cursor.fetchone()

        if row!=None:
            messagebox.showerror('Error','Username already exists. Try different name')
        else:
            query='insert into user_data(username,email,password) values(%s,%s,%s)'
            my_cursor.execute(query,(user_entry.get(),email_entry.get(),pass_Entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Registration Successfull! Please Click in Login to Proceed..')
    



#GUI
sign_up_window=Tk()
sign_up_window.geometry('1060x750+10+10')
sign_up_window.resizable(0,0)
sign_up_window.title('Register')
bgImg=ImageTk.PhotoImage(file='register_page.png')
bgLabel=Label(sign_up_window,image=bgImg)
bgLabel.place(x=0,y=0)

user_entry=Entry(sign_up_window,width=30,font=('Calibri',20),bg='gray91',fg='gray63')
user_entry.place(x=310,y=260)
user_entry.insert(0,'Username')
user_entry.bind('<FocusIn>',username_enter)

email_entry=Entry(sign_up_window,width=30,font=('Calibri',20),bg='gray91',fg='gray63')
email_entry.place(x=310,y=330)
email_entry.insert(0,'Email')
email_entry.bind('<FocusIn>',email_enter)

pass_Entry=Entry(sign_up_window,width=30,font=('Calibri',20),bg='gray91',fg='gray63')
pass_Entry.place(x=310,y=400)
pass_Entry.insert(0,'Password')
pass_Entry.bind('<FocusIn>',password_enter)

register_button=Button(sign_up_window,text="Proceed",font=('Calibri',17),fg='white',bg='blue4',activeforeground='white',activebackground='blue4',cursor='hand2',width=10,command=connect_database)
register_button.place(x=450,y=490)

login_direct=Button(sign_up_window,text="Login Now",font=('Calibri',13),bd=0,fg='blue4',bg='grey86',activeforeground='blue4',activebackground='grey86',cursor='hand2',width=10,command=lambda:login_page())
login_direct.place(x=465,y=560)


mainloop()
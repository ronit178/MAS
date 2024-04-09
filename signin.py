from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

#Functions

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        usernameEntry.config(fg='black')

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        passwordEntry.config(fg='black')
        passwordEntry.config(show='*')

def register_page():
    sign_in_window.destroy()
    import signup

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Please fill all fields...')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='mysql@suhani',database='mas_user_data')
            my_cursor=conn.cursor()
            
        except:
            messagebox.showerror('Error','Database connection failed')
            return
        
        query='select * from user_data where username=%s and password=%s'
        my_cursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=my_cursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Inavalid user name or password')
        else:
            messagebox.showerror('Error','login Success')






#GUI
sign_in_window=Tk()
sign_in_window.geometry('1055x750+10+10')
sign_in_window.resizable(0,0)
sign_in_window.title('Login')
bg1Image=ImageTk.PhotoImage(file='login_page.png')
bgLabel=Label(sign_in_window,image=bg1Image)
bgLabel.place(x=0,y=0)

usernameEntry=Entry(sign_in_window,width=30,font=('Calibri',20),bg='gray91',fg='gray63')
usernameEntry.place(x=90,y=260)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

passwordEntry=Entry(sign_in_window,width=30,font=('Calibri',20),bg='gray91',fg='gray63')
passwordEntry.place(x=90,y=350)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)


login_button=Button(sign_in_window,text="Sign in",font=('Calibri',17),fg='white',bg='blue4',activeforeground='white',activebackground='blue4',cursor='hand2',width=10,command=login_user)
login_button.place(x=245,y=470)

register_create=Button(sign_in_window,text="Register",font=('Calibri',17),fg='blue4',bg='gray87',activeforeground='blue4',activebackground='gray87',cursor='hand2',width=10,command=lambda:register_page())
register_create.place(x=760,y=350)



mainloop()


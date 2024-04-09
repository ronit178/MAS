from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def combined_func():
    
    welcome_window.withdraw()
    login_page_direct()

def homepage():

    def combined_func_go_to_signin():
        homepage_window.withdraw()
        login_page_direct()


    homepage_window=Toplevel()
    homepage_window.geometry('1056x750+10+10')
    homepage_window.resizable(0,0)
    homepage_window.title('Homepage')
    bg2Image=ImageTk.PhotoImage(file='homepage_bg.png')
    bgLabel=Label(homepage_window,image=bg2Image)
    bgLabel.image = bg2Image
    bgLabel.place(x=0,y=0)

    scan_button=Button(homepage_window,text="Scan",font=('Calibri',17),bd=0,fg='blue4',bg='alice blue',activeforeground='blue4',activebackground='light cyan',cursor='hand2',width=10)
    scan_button.place(x=640,y=440)

    logout_button=Button(homepage_window,text="Logout",font=('Calibri',17),bd=0,fg='blue4',bg='alice blue',activeforeground='blue4',activebackground='light cyan',cursor='hand2',width=9,command=combined_func_go_to_signin)
    logout_button.place(x=110,y=640)




def login_page_direct():

    if 'sign_in_window' in globals():
            sign_in_window.lift()
            return

    def user_enter(event):
        if usernameEntry.get()=='Username':
            usernameEntry.delete(0,END)
            usernameEntry.config(fg='black')

    def pass_enter(event):
        if passwordEntry.get()=='Password':
            passwordEntry.delete(0,END)
            passwordEntry.config(fg='black')
            passwordEntry.config(show='*')

    def combined_func_gotoregis():
        sign_in_window.withdraw()
        register_page()

    

    
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
                sign_in_window.withdraw()
                homepage()



    #GUI
    sign_in_window=Toplevel()
    sign_in_window.geometry('1055x750+10+10')
    sign_in_window.resizable(0,0)
    sign_in_window.title('Login')
    bg1Image=ImageTk.PhotoImage(file='login_page.png')
    bgLabel=Label(sign_in_window,image=bg1Image)
    bgLabel.image = bg1Image
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

    register_create=Button(sign_in_window,text="Register",font=('Calibri',17),fg='blue4',bg='gray87',activeforeground='blue4',activebackground='gray87',cursor='hand2',width=10,command=combined_func_gotoregis)
    register_create.place(x=760,y=350)


welcome_window=Tk()
welcome_window.geometry('1042x750+10+10')
welcome_window.resizable(0,0)
welcome_window.title('Welcome to our Application!')
bg2Image=ImageTk.PhotoImage(file='welcome_screen.png')
bgLabel=Label(welcome_window,image=bg2Image)
bgLabel.place(x=0,y=0)

start_button=Button(welcome_window,text='Start Now',font=('Calibri',20),bd=0,fg='blue4',bg='grey86',cursor='hand2',width=10,activeforeground='blue4',activebackground='grey86',command=combined_func)
start_button.place(x=440,y=388)




def register_page():
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


    def combined_func_register():
        sign_up_window.withdraw()
        login_page_direct()





    #GUI
    sign_up_window=Toplevel()
    sign_up_window.geometry('1060x750+10+10')
    sign_up_window.resizable(0,0)
    sign_up_window.title('Register')
    bgImg=ImageTk.PhotoImage(Image.open("register_page.png"))
    bgLabel1=Label(sign_up_window,image=bgImg)
    bgLabel.image = bgImg
    bgLabel1.place(x=0,y=0)

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

    login_direct=Button(sign_up_window,text="Login Now",font=('Calibri',13),bd=0,fg='blue4',bg='grey86',activeforeground='blue4',activebackground='grey86',cursor='hand2',width=10,command=combined_func_register)
    login_direct.place(x=465,y=560)    









welcome_window.mainloop()





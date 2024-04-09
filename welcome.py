from tkinter import *
from PIL import ImageTk


def login_page_direct():
    welcome_window.destroy()
    import signin
    
    

welcome_window=Tk()
welcome_window.geometry('1042x750+10+10')
welcome_window.resizable(0,0)
welcome_window.title('Welcome to our Application!')
bg2Image=ImageTk.PhotoImage(file='welcome_screen.png')
bgLabel=Label(welcome_window,image=bg2Image)
bgLabel.place(x=0,y=0)

start_button=Button(welcome_window,text='Start Now',font=('Calibri',20),bd=0,fg='blue4',bg='grey86',cursor='hand2',width=10,activeforeground='blue4',activebackground='grey86',command=lambda:login_page_direct())
start_button.place(x=440,y=388)

mainloop()
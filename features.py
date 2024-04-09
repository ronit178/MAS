from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

feature_window=Tk()
feature_window.geometry('1051x750+10+10')
feature_window.resizable(0,0)
feature_window.title('Scores')
bg4Image=ImageTk.PhotoImage(file='feature_page.png')
bgLabel=Label(feature_window,image=bg4Image)
bgLabel.place(x=0,y=0)

feature_window.mainloop()


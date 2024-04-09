from tkinter import *
from PIL import ImageTk
import subprocess
import tkinter as tk
from subprocess import Popen, PIPE
homepage_window=Tk()
homepage_window.geometry('1056x750+10+10')
homepage_window.resizable(0,0)
homepage_window.title('Homepage')
bg2Image=ImageTk.PhotoImage(file='homepage_bg.png')
bgLabel=Label(homepage_window,image=bg2Image)
bgLabel.place(x=0,y=0)

def run_mas():
    # Replace 'python' with the path to your Python interpreter if necessary
    mas_process = Popen(['python', 'MAS.py'], stdout=PIPE)

    output = mas_process.communicate()[0].decode()

    # Create a new window for the output
    new_window = tk.Tk()
    new_window.geometry('1056x750+10+10')
    new_window.title('MAS Output')
    new_window.resizable(0, 0)

    # Create a scrollable Text widget to accommodate potentially large output
    text_scroll_bar = tk.Scrollbar(new_window)
    text_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar on the right side

    text_widget = tk.Text(new_window, yscrollcommand=text_scroll_bar.set)
    text_widget.insert('end', output)
    text_widget.configure(state='disabled')  # Disable editing for a cleaner view
    text_widget.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

    text_scroll_bar.config(command=text_widget.yview)  # Connect scrollbar to text widget

    new_window.mainloop()

scan_button=Button(homepage_window, text="Scan", font=('Calibri',17), bd=0, fg='blue4', bg='alice blue', activeforeground='blue4', activebackground='light cyan', cursor='hand2', width=10, command=run_mas)
scan_button.place(x=640,y=440)

logout_button=Button(homepage_window,text="Logout",font=('Calibri',17),fg='blue4',bg='alice blue',activeforeground='blue4',activebackground='light cyan',cursor='hand2',width=9)
logout_button.place(x=110,y=640)

homepage_window.mainloop()



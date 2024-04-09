import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk
import subprocess
import os

def run_script():
    # Execute the powershell.ps1 script
    print("Executing powershell.ps1 script...")
    subprocess.call(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'powershell.ps1'])

    # Check if the output.txt file exists
    if not os.path.exists('output.txt'):
        print("Error: output.txt file does not exist.")
        return

    # Create a new tab for the output
    new_tab = ttk.Notebook(homepage_window)
    new_tab.place(x=0, y=0, width=1056, height=750)

    # Add a label to display the output
    output_label = ttk.Label(new_tab, text="Output:\n\n")
    output_label.pack(expand=True, fill='both')

    # Read the output file and display it in the label
    with open('output.txt', 'r') as f:
        output_text = f.read()
    output_label.config(text=output_text)
    print(f"Output text: {output_text}")

homepage_window = tk.Tk()
homepage_window.geometry('1056x750+10+10')
homepage_window.resizable(0, 0)
homepage_window.title('Homepage')

bg_image = ImageTk.PhotoImage(file='homepage_bg.png')  # Use a variable name for clarity
bg_label = tk.Label(homepage_window, image=bg_image)
bg_label.place(x=0, y=0)

scan_button = tk.Button(
    homepage_window,
    text="Scan",
    font=('Calibri', 17),
    bd=0,
    fg='blue4',
    bg='alice blue',
    activeforeground='blue4',
    activebackground='light cyan',
    cursor='hand2',
    width=10,
    command=run_script  # Bind the run_script function to the button click
)
scan_button.place(x=640, y=440)

logout_button = tk.Button(
    homepage_window,
    text="Logout",
    font=('Calibri', 17),
    fg='blue4',
    bg='alice blue',
    activeforeground='blue4',
    activebackground='light cyan',
    cursor='hand2',
    width=9
)
logout_button.place(x=110, y=640)

homepage_window.mainloop()
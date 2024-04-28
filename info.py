from tkinter import *
from PIL import ImageTk

our_sol_window=Tk()
our_sol_window.geometry('1049x750+10+10')
our_sol_window.resizable(0,0)
our_sol_window.title('Information')
bg1Image=ImageTk.PhotoImage(file='info_page.png')
bgLabel=Label(our_sol_window,image=bg1Image)
bgLabel.place(x=0,y=0)

mal_label=Label(our_sol_window,text="Our Solution",font=('Calibri',22),fg='alice blue',bg='medium blue',bd=0)
mal_label.place(x=400,y=30)

logout_button=Button(our_sol_window,text="back",font=('Calibri',14),bd=0,fg='blue4',bg='gray83',activeforeground='blue4',activebackground='gray83',cursor='hand2',width=7)
logout_button.place(x=900,y=25)

info_m_label=Label(our_sol_window,text="""This design aims to develop a comprehensive scoring system to estimate the security of computer systems and effectively describe implicit malware pitfalls. By relating crucial features suceptible to malware impact, similar as zero interpretation, antivirus software, number of LNK lines, and TCP connections, we upgrade this data into a final set of pivotal features to form our scoring methodology.
                   
Vision Through this design, we fantasize a significantly bettered security geography for computer systems. By furnishing a standardized and objective assessment of security, druggies will gain precious perceptivity into implicit vulnerabilities and areas for enhancement. As a result, associations can proactively adress security issues, alleviate pitfalls, and enhance overall system protection. This action aligns with our association's commitment to advancing cybersecurity measures, icing robust defense mechanisms against evolving pitfalls.
""",font=('Calibri',17),fg='black',bg='grey86',bd=0,justify="left",wraplength=1000)
info_m_label.place(x=10,y=100)



our_sol_window.mainloop()


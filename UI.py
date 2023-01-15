"""
colour pallet (main)=#ebac4d

"""

import subprocess
from tkinter import*
from tkinter import messagebox as tmb #text message box
#import main.py
root=Tk()
root.title("QUIZOOO")

def startfunction():
    subprocess.Popen(args=['python','main.py'])
    root.destroy()

def home():#defining The home page
    start_frame=Frame(root,height=scrh,width=scrw,bg="#ebac4d")
    start_frame.pack()
    exitbut=Button(start_frame,text="Exit",font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:root.destroy())
    exitbut.place(relx=0.5,rely=0.9,anchor=S)
    starbut=Button(start_frame,text="Start",font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:startfunction())
    starbut.place(relx=0.5,rely=0.5,anchor=S)


scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width

root.geometry("%dx%d"%(scrw,scrh))#Setting window to full screen
home()
print("Start Screen Loaded")
root.mainloop()

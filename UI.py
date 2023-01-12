"""
colour pallet (main)=#ebac4d

"""

import subprocess
from tkinter import*
from tkinter import messagebox as tmb #text message box
#import main.py
root=Tk()
root.title("QUIZOOO")

def home():#defining The home page
    start_frame=Frame(root,height=scrh,width=scrw,bg="#ebac4d")
    start_frame.pack()
    exitbut=Button(start_frame,text="Exit",font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:root.destroy())
    exitbut.place(relx=0.5,rely=0.9,anchor=S)
    starbut=Button(start_frame,text="Start",font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:subprocess.Popen(args=['python','main.py']))
    starbut.place(relx=0.5,rely=0.5,anchor=S)

def play():#defining The play button
    
    return
 
def result():#defining The result page

    total_questions = 20 #test_variable 1
    count_right = 10    #test_variable 2

    count_wrong = total_questions - count_right
    right_answer = f"Correct: {count_right}"
    wrong_answer = f"Wrong: {count_wrong}"
    
    the_score = int(count_right/total_questions*100)
    the_result= f"Score:{the_score}%"
    tmb.showinfo("Result",f"{the_result}\n{right_answer}\n{wrong_answer}")
    return

scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width

root.geometry("%dx%d"%(scrw,scrh))#Setting window to full screen
home()
#result()
print("Start Screen Loaded")
root.mainloop()

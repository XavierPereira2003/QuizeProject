
"""
This is the functional unit of the project where all the logic for cheaking for correct answer


"""

class Question:
    """
    This class is intended for making, displaying and removing  the questions seen on the quize page.
    """
    def __init__(self,frame,hight,width,quest):
        self.options=list(quest["dis"])
        self.options.append(quest["ans"])
        shuffle(self.options)
        self.ans=quest["ans"]
        self.QuestionLabel=Label(frame,text=quest["ques"],height=2,font=("Times New Roman",35,'italic'),bg='#ebac4d',wraplength=1000, justify="center")
        self.choice=StringVar()
        self.option1=Radiobutton(frame, text=self.options[0],font=("Times New Roman",35),bg='#ebac4d',wraplength=500, variable=self.choice, value=self.options[0])
        self.option2=Radiobutton(frame, text=self.options[1],font=("Times New Roman",35),bg='#ebac4d',wraplength=500, variable=self.choice, value=self.options[1])
        self.option3=Radiobutton(frame, text=self.options[2],font=("Times New Roman",35),bg='#ebac4d',wraplength=500, variable=self.choice, value=self.options[2])
        self.option4=Radiobutton(frame, text=self.options[3],font=("Times New Roman",35),bg='#ebac4d',wraplength=500, variable=self.choice, value=self.options[3])
        

    def show(self):
        self.QuestionLabel.place(relx=0.5,rely=0.15,anchor=N)
        self.option1.place(relx=0.25,rely=0.30,anchor=N)
        self.option2.place(relx=0.75,rely=0.30,anchor=N)
        self.option3.place(relx=0.25,rely=0.75,anchor=S)
        self.option4.place(relx=0.75,rely=0.75,anchor=S)
        

    def Destroy(self):
        self.playeranswer=self.choice
        self.QuestionLabel.destroy()
        self.option1.destroy()
        self.option2.destroy()
        self.option3.destroy()
        self.option4.destroy()


global start_frame,question_fram,time_fram,ques_list_fram

def main():
    """
    This is functional unit of the program. In here we build the main quiz page.
    """
    global cur
    cur=0
    def timer():#This is the functional timer for the project.
        global Time
        Time=60
        while Time!=0:
            time=Label(time_fram,text="%d:%d"%(Time//60,Time%60),width=300,height=3,font=("Times New Roman",80),bg='#ebac4d')
            time.pack()
            Time-=1
            sleep(1)
            time.destroy()
        result()
    def next():
        global cur
        try:
            if 0<=cur<9:
                print("1Next=",cur)
                Quest_list[cur].Destroy()
                cur+=1
                Quest_list[cur].show()
                print("2Next=",cur)
            else:
                print(cur)
                cur=9
                Quest_list[cur].show()
                messagebox.showinfo(title="Quize Project", message="You Have reached the end of the quiz")
        except:
            cur=0
            Quest_list[cur].show()

    def prev():
        global cur
        try:
            if 0<cur<=9:
                print("1Prev=",cur)
                Quest_list[cur].Destroy()
                cur=cur-1
                Quest_list[cur].show()
                print("2Prev=",cur)
            else:
                messagebox.showinfo(title="Quize Project", message="You are at the begining of the quiz")
        except:
            cur=0
            Quest_list[cur].show()

    def result():
        ques_list_fram.destroy()
        question_fram.destroy()
        time_fram.destroy()
        count=0
        for i in range(10):
            if Quest_list[i].choice==Quest_list[i].ans:
                count+=1
        messagebox.showinfo(title="Quize Project", message="You got %d out 10 coreect"%(count))
        home()
        

    #DO NOT CHANGE THIS ORDER(The arrangement of the frames will mess up)
    global question_fram,time_fram,ques_list_fram
    question_fram=Frame(root,height=scrh,width=scrw*0.66666,bg="#ebac4d")
    time_fram=Frame(root,height=scrh*0.25,width=scrw*(1-0.66666),bg="#ebac4d")
    ques_list_fram=Frame(root,height=scrh*0.75,width=scrw*(1-0.66666),bg="#ebac4d")

    question_fram.pack(side=LEFT)
    time_fram.pack(side=TOP)
    ques_list_fram.pack(side=BOTTOM) 

    next_but= Button(ques_list_fram,text="Next",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2', command=lambda:next())
    prev_but= Button(ques_list_fram,text="Prevous",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=lambda:prev())
    next_but.place(relx=0.5,rely=0.3,anchor=N)
    prev_but.place(relx=0.5,rely=0.5,anchor=N)

    #Creating a list of questions
    global Quest_list
    Quest_list=list()
    for i in range(10):
        Quest_list.append(Question(question_fram,scrh-scrh*0.20,scrw*0.66666,question[i]))
    
    
    
    Quest_list[cur].show()

    #Timer Starts
    t1=threading.Thread(target=timer)
    t1.start()

def home_to_main():
    start_frame.destroy()
    main()

     

#Importing Libraires
from tkinter import *
from time import sleep
import threading
import json
from random import randint,shuffle
from tkinter import messagebox



def home():#defining The home page
    global start_frame

    start_frame=Frame(root,height=scrh,width=scrw,bg="#ebac4d")
    start_frame.pack()
    my_label=Label(root, text="Quiz Project", font=("Times New Roman", 70, "bold"),bg="#ebac4d")
    my_label.place(relx =0.5, rely = 0.1, anchor=N)
    exitbut=Button(start_frame,text="Exit", width =10, font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:root.destroy())
    exitbut.place(relx=0.5,rely=0.7,anchor=S)
    starbut=Button(start_frame,text="Start", width =10, font=("Times New Roman",25,"bold"),activebackground="#247371",bg="#4debe8",command=lambda:home_to_main())
    starbut.place(relx=0.5,rely=0.5,anchor=S)

#Preprocessing

root=Tk()
root.title("QUIZOOO")

scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width
root.geometry("%dx%d"%(scrw,scrh))

"""
In this part we are choosing the questions
"""
global question
question=[]
with open("question.json") as quest:
    quest=json.load(quest)
    for i in range(10):
        #This part is done so no same question appear twice
        while(True):
            k=randint(0,len(quest)-1)
            if quest[k] not in question:
                question.append(quest[i])
                break

shuffle(question)
home()
#main()
root.mainloop()

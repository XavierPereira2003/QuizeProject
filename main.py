
"""
This is the functional unit of the project where all the logic for cheaking for correct answer


"""
class Question:
    """
    This class is intended for making, displaying and changing the questions seen on the quize page.
    """
    def __init__(self,frame,hight,width,quest):
        self.options=list(quest["dis"])
        self.options.append(quest["ans"])
        shuffle(self.options)
        self.ans=quest["ans"]
        self.QuestionLabel=Label(frame,text=quest["ques"],height=2,font=("garamond",12,'italic'),bg='#dec06f')
        self.choice=StringVar()
        self.option1=Radiobutton(frame, text=self.options[0], variable=self.choice, value=self.options[0])
        self.option2=Radiobutton(frame, text=self.options[1], variable=self.choice, value=self.options[1])
        self.option3=Radiobutton(frame, text=self.options[2], variable=self.choice, value=self.options[2])
        self.option4=Radiobutton(frame, text=self.options[3], variable=self.choice, value=self.options[3])
        

    def Pack(self):
        self.QuestionLabel.place(relx=0.5,rely=0.35,anchor=N)
        self.option1.place(relx=0.5,rely=0.35,anchor=N)
        self.option2.place(relx=0.,rely=0.35,anchor=N)
        self.option3.place(relx=0.5,rely=0.35,anchor=N)
        self.option4.place(relx=0.5,rely=0.35,anchor=N)
        

    def destroy(self):
        self.destroy()



def main():
    """
    This is functional unit of the program. In here we build the main quiz page.
    """
    """
    def timer():#This is the functional timer for the project.
        global Time
        Time=90
        while Time!=0:
            time=Label(time_fram,text="%d:%d"%(Time//60,Time%60),width=300,height=2,font=("garamond",80,'italic'),bg='#dec06f')
            time.pack()
            Time-=1
            sleep(1)
            time.destroy()
    """
    #DO NOT CHANGE THIS ORDER(The arrangement of the frames will mess up)
    question_fram=Frame(root,height=scrh,width=scrw*0.66666,bg="#ebac4d")
    question_fram.pack(side=LEFT)
    time_fram=Frame(root,height=scrh*0.25,width=scrw*(1-0.66666),bg="#03bafc")
    time_fram.pack(side=TOP)
    ques_list_fram=Frame(root,height=scrh*0.75,width=scrw*(1-0.66666),bg="#bafc03")
    ques_list_fram.pack(side=BOTTOM) 
    next_but= Button(ques_list_fram,text="Next",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2')# command=)
    prev_but= Button(ques_list_fram,text="Prevous",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2')
    next_but.place(relx=0.5,rely=0.3,anchor=N)
    prev_but.place(relx=0.5,rely=0.5,anchor=N)
    #t1=threading.Thread(target=timer)
    #t1.start()
    test=Question(question_fram,scrh-scrh*0.20,scrw*0.66666,question[0])
    test.Pack()

# #
from tkinter import *
from time import sleep
import threading
import json
from random import randint,shuffle
#Preprocessing
root=Tk()
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

main()
 
root.mainloop()


# def result():#defining The result page

#     total_questions = 20 #test_variable 1
#     count_right = 10    #test_variable 2

#     count_wrong = total_questions - count_right
#     right_answer = f"Correct: {count_right}"
#     wrong_answer = f"Wrong: {count_wrong}"
    
#     the_score = int(count_right/total_questions*100)
#     the_result= f"Score:{the_score}%"
#     tmb.showinfo("Result",f"{the_result}\n{right_answer}\n{wrong_answer}")
#     return

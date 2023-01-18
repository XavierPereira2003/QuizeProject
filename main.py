
"""
This is the functional unit of the project where all the logic for cheaking for correct answer


"""
class Question:
    """
    This class is intended for making, displaying and changing the questions seen on the quize page.
    """
    def __init__(self,frame,quest,ans,dis):
        self.QuestionLabel=Label(frame,text="Hello",width=300,height=2,font=("garamond",80,'italic'),bg='#dec06f')

    def pack(self):
        self.pack()
    def destroy(self):
        self.destroy()



def main():
    """
    This is functional unit of the program. In here we build the main quiz page.
    """
    def timer():#This is the functional timer for the project.
        global Time
        Time=30
        while Time!=0:
            time=Label(time_fram,text="%d"%(Time),width=300,height=2,font=("garamond",80,'italic'),bg='#dec06f')
            time.pack()
            Time-=1
            sleep(1)
            time.destroy()
    #DO NOT CHANGE THIS ORDER(The arrangement of the frames will mess up)
    question_fram=Frame(root,height=scrh,width=scrw*0.66666,bg="#ebac4d")
    question_fram.pack(side=LEFT)
    time_fram=Frame(root,height=scrh*0.25,width=scrw*(1-0.66666),bg="#03bafc")
    time_fram.pack(side=TOP)
    ques_list_fram=Frame(root,height=scrh*0.75,width=scrw*(1-0.66666),bg="#bafc03")
    ques_list_fram.pack(side=BOTTOM) 
    t1=threading.Thread(target=timer)
    t1.start()

# #
from tkinter import *
from time import sleep
import threading
import json
from random import randint
#Preprocessing
root=Tk()
scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width
root.geometry("%dx%d"%(scrw,scrh))

"""
In this part we are choosing the questions
"""
Question=[]
with open("question.json") as quest:
    quest=json.load(quest)
    for i in range(10):
        #This part is done so no same question appear twice
        while(True):
            k=randint(0,len(quest)-1)
            if quest(k) not in Question:
                Question.append(quest[i])
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

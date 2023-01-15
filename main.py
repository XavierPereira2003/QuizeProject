"""
JSON file format 
[
    {
    "ques":"Question",
    "ans":"ans",
    "dis":[,,,,,]
    
    },
    

]

"""
from tkinter import *
import time


#Preprocessing
root=Tk()
scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width

root.geometry("%dx%d"%(scrw,scrh))

# class quesbut():
#     def __ini__():
def main():
    def Question_fram():
        question_fram=Frame(root,height=scrh,width=scrw*0.66666,bg="#ebac4d")
        question_fram.pack(side=LEFT)
    
        
    def Time_fram():
        time_fram=Frame(root,height=scrh*0.25,width=scrw*(1-0.66666),bg="#03bafc")
        time_fram.pack(side=TOP)


    #DO NOT CHANGE THIS ORDER(The arrangement of the frames will mess up)
    Question_fram()
    Time_fram()
    ques_list_fram=Frame(root,height=scrh*0.75,width=scrw*(1-0.66666),bg="#bafc03")
    ques_list_fram.pack(side=BOTTOM)

main()
# #with open("question.json") as question:
    
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

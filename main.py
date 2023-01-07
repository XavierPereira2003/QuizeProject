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
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
    question_fram=Frame(root,height=scrh,width=scrw*0.66666,bg="#ebac4d")
    question_fram.pack(side=LEFT)
    time_fram=Frame(root,height=scrh*0.25,width=scrw*(1-0.66666),bg="#03bafc")
    time_fram.pack(side=TOP)
    ques_list_fram=Frame(root,height=scrh*0.75,width=scrw*(1-0.66666),bg="#bafc03")
    ques_list_fram.pack(side=RIGHT)
main()
# #with open("question.json") as question:
    
root.mainloop()
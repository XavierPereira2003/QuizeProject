from tkinter import*
global start_frame
root=Tk()
root.title("QUIZOOO")
def home():
    start_frame=Frame(root,height=scrh,width=scrw)
    start_frame.pack()

scrh=root.winfo_screenheight()  # Getting screen height
scrw=root.winfo_screenwidth()   # Getting Screen width

root.geometry("%dx%d"%(scrw,scrh))
temp=start_frame=Frame(root,height=scrh,width=scrw,bg="#ebac4d")
temp.pack()
#root.attributes('-fullscreen',True)
home()
root.mainloop()

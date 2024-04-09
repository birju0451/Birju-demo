from tkinter import*
root=Tk()
root.title("About frame")
root.geometry("400x300")
#FRAME:-
f1=Frame(root,bg="green",borderwidth=9)
f1.pack(side=LEFT,fill=Y)

f2=Frame(root,bg="green",borderwidth=9)
f2.pack(side=TOP,fill=X)

#LABEL FOR FRAME
L1=Label(f1,text='in this day indian cricker team is very sad',fg="red")
L1.pack()

L2=Label(f2,text='virat kohali',padx=1000,fg='red')
L2.pack(fill=X)

root.mainloop()
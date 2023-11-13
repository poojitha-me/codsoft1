from tkinter import *
import math
def click(value):
    ex=entryFeild.get()
    ans='null'
    try:
        if value=='C':
           ex=ex[0:len(ex)-1]
           entryFeild.delete(0, END)
           entryFeild.insert(0,ex)
           return;
        elif value=='CE':
           entryFeild.delete(0,END)
        elif value=='√':
           ans=math.sqrt(eval(ex))     
        elif value=='=':
            ans=eval(ex)
        else:
            entryFeild.insert(END,value)
            return;
        entryFeild.delete(0,END)
        entryFeild.insert(0,ans)
    except SyntaxError:
        pass
root=Tk()
root.title('scientific calculator')
root.config(bg='cyan')
root.geometry('400x450+100+100')
entryFeild=Entry(root,font=('arial',20,'bold'),bg='plum',fg='sea green',bd=10,relief=SUNKEN,width=30)
entryFeild.grid(row=0,column=0,columnspan=10)
button_text_list=["C", "CE", "√", "/",
                    "7", "8", "9", "-",
                    "4", "5", "6", "*", 
                    "1", "2", "3", "+",
                    "0", ".", "%", "="]
rowvalue=1
columnvalue=0
for i in button_text_list:
    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='khaki3',fg='black',
              font=('arial',18 ,'bold'),activebackground='cyan',command=lambda button=i:click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>3:
        rowvalue+=1
        columnvalue=0
root.mainloop()
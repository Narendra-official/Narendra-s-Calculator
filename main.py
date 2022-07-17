from tkinter import *
def click(num):
    global op
    op=op+str(num)
    iptext.set(op)
def evaluate():
    global op
    output=str(eval(op))
    iptext.set(output)
def clearDisplay():
    global op
    op=""
    iptext.set(op)
calc=Tk()
calc.title("Narendra's Calculator")

op=""
iptext=StringVar()
iparea=Entry(calc,font=('large,_font',26,'bold'),bd=20,justify="right",insertwidth=4,textvariable=iptext).grid(columnspan=10)
bt7=Button(calc,font=('arial',17,'bold'),command=lambda:click(7),bg="Yellow",text="7",bd=7,padx=15,pady=14).grid(row=1,column=0)
bt8=Button(calc,font=('arial',17,'bold'),command=lambda:click(8),bg="Yellow",text="8",bd=7,padx=15,pady=14).grid(row=1,column=1)
bt9=Button(calc,font=('arial',17,'bold'),command=lambda:click(9),bg="Yellow",text="9",bd=7,padx=15,pady=14).grid(row=1,column=2)
add=Button(calc,font=('arial',17,'bold'),command=lambda:click('+'),bg="Yellow",text="+",bd=7,padx=15,pady=14).grid(row=1,column=3)
bt4=Button(calc,font=('arial',17,'bold'),command=lambda:click(4),bg="Yellow",text="4",bd=7,padx=15,pady=14).grid(row=2,column=0)
bt5=Button(calc,font=('arial',17,'bold'),command=lambda:click(5),bg="Yellow",text="5",bd=7,padx=15,pady=14).grid(row=2,column=1)
bt6=Button(calc,font=('arial',17,'bold'),command=lambda:click(6),bg="Yellow",text="6",bd=7,padx=15,pady=14).grid(row=2,column=2)
sub=Button(calc,font=('arial',17,'bold'),command=lambda:click('-'),bg="Yellow",text="-",bd=7,padx=15,pady=14).grid(row=2,column=3)
bt1=Button(calc,font=('arial',17,'bold'),command=lambda:click(1),bg="Yellow",text="1",bd=7,padx=15,pady=14).grid(row=3,column=0)
bt2=Button(calc,font=('arial',17,'bold'),command=lambda:click(2),bg="Yellow",text="2",bd=7,padx=15,pady=14).grid(row=3,column=1)
bt3=Button(calc,font=('arial',17,'bold'),command=lambda:click(3),bg="Yellow",text="3",bd=7,padx=15,pady=14).grid(row=3,column=2)
mul=Button(calc,font=('arial',17,'bold'),command=lambda:click('*'),bg="Yellow",text="x",bd=7,padx=15,pady=14).grid(row=3,column=3)
bt0=Button(calc,font=('arial',17,'bold'),command=lambda:click(0),bg="Yellow",text="0",bd=7,padx=15,pady=14).grid(row=4,column=0)
btC=Button(calc,font=('arial',17,'bold'),command=clearDisplay,bg="Yellow",text="C",bd=7,padx=15,pady=14).grid(row=4,column=1)
div=Button(calc,font=('arial',17,'bold'),command=lambda:click('.'),bg="Yellow",text=".",bd=7,padx=15,pady=14).grid(row=4,column=2)
eql=Button(calc,font=('arial',20,'bold'),command=evaluate,bg="Yellow",text="=",bd=14,padx=15,pady=10).grid(row=7,column=3)
div=Button(calc,font=('arial',17,'bold'),command=lambda:click('/'),bg="Yellow",text="÷",bd=7,padx=15,pady=14).grid(row=4,column=3)
calc.mainloop(),


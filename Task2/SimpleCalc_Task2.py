#TASK 2

#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result



import tkinter as tk
top=tk.Tk()
top.title("Simple Calculator")
top.geometry("600x300")

E=tk.Entry(top,width=100)
E.grid(columnspan=4)

def select(n):
    a = E.get()
    E.delete(0,tk.END)
    E.insert(0,str(a)+str(n))

def addition():
    a1 = E.get()
    global expression
    global operation
    operation = "add"
    expression = int(a1)
    E.delete(0,tk.END)

def subtraction():
    a1 = E.get()
    global expression
    global operation
    operation = "subtract"
    expression = int(a1)
    E.delete(0,tk.END)

def multiplication():
    a1 = E.get()
    global expression
    global operation
    operation = "multiply"
    expression = int(a1)
    E.delete(0,tk.END)

def division():
    a1 = E.get()
    global expression
    global operation
    operation = "divide"
    expression = int(a1)
    E.delete(0,tk.END)

def modulo():
    a1 = E.get()
    global expression
    global operation
    operation = "modulo"
    expression = int(a1)
    E.delete(0,tk.END)

def ac():
    E.delete(0,tk.END)

def clear():
    a1 = E.get()
    a11 = a1[:-1]
    E.delete(0,tk.END)
    E.insert(0,a11)

def equals():
    a2 = E.get()
    E.delete(0,tk.END)
    if operation == "add":
        E.insert(0,expression+int(a2))
    elif operation == "subtract":
        E.insert(0,expression-int(a2))
    elif operation == "multiply":
        E.insert(0,expression*int(a2))
    elif operation == "divide":
        b = expression/int(a2)
        if(expressio%int(a2)==0):
            E.insert(0,int(b))
        else:
            E.insert(0,r)
    elif operation == "modulo":
        E.insert(0,exprression%int(a2))
    else:
        E.insert("Syntax Error")
        E.insert(0,expression/int(a2))

B1=tk.Button(top,text="AC",height=2,width=20,command=ac)
B1.grid(row=1,column=0)

B2=tk.Button(top,text="%",height=2,width=20,command=modulo)
B2.grid(row=1,column=1)

B3=tk.Button(top,text="clear",height=2,width=20,command=clear)
B3.grid(row=1,column=2)

B4=tk.Button(top,text="/",height=2,width=20,command=division)
B4.grid(row=1,column=3)


B5=tk.Button(top,text="7",height=2,width=20,command=lambda:select(7))
B5.grid(row=2,column=0)

B6=tk.Button(top,text="8",height=2,width=20,command=lambda:select(8))
B6.grid(row=2,column=1)

B7=tk.Button(top,text="9",height=2,width=20,command=lambda:select(9))
B7.grid(row=2,column=2)

B8=tk.Button(top,text="x",height=2,width=20,command=multiplication)
B8.grid(row=2,column=3)


B9=tk.Button(top,text="4",height=2,width=20,command=lambda:select(4))
B9.grid(row=3,column=0)

B10=tk.Button(top,text="5",height=2,width=20,command=lambda:select(5))
B10.grid(row=3,column=1)

B11=tk.Button(top,text="6",height=2,width=20,command=lambda:select(6))
B11.grid(row=3,column=2)

B12=tk.Button(top,text="-",height=2,width=20,command=subtraction)
B12.grid(row=3,column=3)


B13=tk.Button(top,text="1",height=2,width=20,command=lambda:select(1))
B13.grid(row=4,column=0)

B14=tk.Button(top,text="2",height=2,width=20,command=lambda:select(2))
B14.grid(row=4,column=1)

B15=tk.Button(top,text="3",height=2,width=20,command=lambda:select(3))
B15.grid(row=4,column=2)

B16=tk.Button(top,text="+",height=2,width=20,command=addition)
B16.grid(row=4,column=3)


B17=tk.Button(top,text="0",height=2,width=20,command=lambda:select(0))
B17.grid(row=5,column=0)

B20=tk.Button(top,text="=",height=2,width=20,command=equals)
B20.grid(row=5,column=1)

top.mainloop()


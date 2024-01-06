# A password generator is a useful tool that generates strong and random passwords for users.
# This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

import random
import tkinter as tk
top=tk.Tk()
top.title("Password Generator")
top.geometry("500x300")
top.configure(background="#190033")

l=tk.LabelFrame(top,text="What is the length of password required?")
l.pack(pady=20)

e=tk.Entry(l)
e.pack(padx=20,pady=20)

def generatePassword():
    n=int(e.get())
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./<>_+-=?;':[]{}!@#$%&*()"
    password=""
    for x in range(0,n):
        a=random.choice(characters)
        password+=a
    e1.insert(0,password)

l1=tk.LabelFrame(top,text="Password!:")
l1.pack(pady=10)

e1=tk.Entry(l1,text="")
e1.pack(pady=20)

f=tk.Frame(top,background="#190033")
f.pack(pady=20)

b1=tk.Button(f,fg="blue",text="Generate Password",command=generatePassword)
b1.grid(column=0,row=0,padx=20)

top.mainloop()

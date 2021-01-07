from tkinter import *
from tkinter import IntVar
from typing import Type

root = Tk()
root.geometry("700x500")

def getvals():
    print("Processing...")
    print("Accepted")

#Heading
Label(root, text="REGISTRATION FORM", font="arial 16 bold").grid(row=0, column=10)

#Field Names
name = Label(root, text="Name", font="arial 10").grid(row=1, column=2)
gender = Label(root, text="Gender", font="arial 10").grid(row=2, column=2)
phone = Label(root, text="Phone No.", font="arial 10").grid(row=3, column=2)
email = Label(root, text="Email", font="arial 10").grid(row=4, column=2)

#Variables for storing data
nameValue = StringVar
genderValue = StringVar
phoneValue = StringVar
emailValue = StringVar
checkValue = IntVar

#Creating Entry field
nameEntry = Entry(root, textvariable=nameValue).grid(row=1, column=3)
genderEntry = Entry(root, textvariable=genderValue).grid(row=2, column=3)
phoneEntry = Entry(root, textvariable=phoneValue).grid(row=3, column=3)
emailEntry = Entry(root, textvariable=emailValue).grid(row=4, column=3)

#Creating checkbutton
checkbutton = Checkbutton(text="Remember Me?", variable=checkValue).grid(row=6, column=3)

#Creating Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()

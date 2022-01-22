from tkinter import *

root = Tk()


def getvals():
    print("accepted")


# Heading
root.geometry("500x300")
Label(root, text="python registration form", font="arial 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyvalue = Entry(root, textvariable=emergencyvalue)
paymentmoodvalue = Entry(root, textvariable=paymentmoodvalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyvalue.grid(row=4, column=3)
paymentmoodvalue.grid(row=5, column=3)

# Checkbox
checkbtn = Checkbutton(text="remenber me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# Submit button
Button(text="submit", command=getvals).grid(row=10, column=3)

root.mainloop()

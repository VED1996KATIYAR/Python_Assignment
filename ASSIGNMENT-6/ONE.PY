from tkinter import *

# Create Window
root = Tk()
root.title("Calculator")
root.geometry("450x450")

# Entry Field
entry = Entry(root, width=20, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert value
def click(value):
    entry.insert(END, value)

# Function to clear entry
def clear():
    entry.delete(0, END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button List
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# Create Buttons
for (text, row, col) in buttons:
    if text == "C":
        Button(root, text=text, width=6, height=2,
               font=("Arial",16), command=clear).grid(row=row, column=col, padx=5, pady=5)

    elif text == "=":
        Button(root, text=text, width=6, height=2,
               font=("Arial",16), command=equal).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(root, text=text, width=6, height=2,
               font=("Arial",16),
               command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
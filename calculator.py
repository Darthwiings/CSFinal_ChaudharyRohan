
from tkinter import *
#Initialize Tkinter window
space = Tk()
space.configure(background = "light grey")
space.geometry("260x255")
space.resizable(width=False, height=False)
space.title("CALCULATOR")


equation = StringVar()
expression = ""
 
#Functions

#Store input
def updateBox(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
 
# Equals to button
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
   
    except:
        equation.set(" error ")
        expression = ""
 
# Clear space 
def clear():
    global expression
    expression = ""
    equation.set("")

# Input field
InputField =  Entry(space, bg = "light yellow", font =("Arial",15), textvariable = equation)
InputField.grid(columnspan= 5)

#Buttons
button1 = Button(space, text = "1", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(1))
button2 = Button(space, text = "2", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(2))
button3 = Button(space, text = "3", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(3))
button4 = Button(space, text = "4", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(4))
button5 = Button(space, text = "5", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(5))
button6 = Button(space, text = "6", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(6))
button7 = Button(space, text = "7", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(7))
button8 = Button(space, text = "8", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(8))
button9 = Button(space, text = "9", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(9))
button0 = Button(space, text = "0", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(0))
buttonlbracket = Button(space, text = "(", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox("("))
buttonrbracket = Button(space, text = ")", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox(")"))

plus = Button(space, text = "+", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox("+"))
minus = Button(space, text = "-", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox("-"))
multiply = Button(space, text = "*", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox("*"))
divide = Button(space, text = "/", bg = "light yellow",width = "6", height = "2", command=lambda: updateBox("/"))
equal  = Button(space, text = "=", bg = "light yellow", width = "6", height = "2", command=equalpress)
clear = Button(space, text = "C", bg = "light yellow", width = "6", height = "2", command=clear)
decimalpoint = Button(space, text = ".", bg = "light yellow", width = "6", height = "2", command=lambda: updateBox("."))

#Gridding buttons
button1.grid(row= 2, column = 0)
button2.grid(row= 2, column = 1)
button3.grid(row= 2, column = 2)
button4.grid(row= 3, column = 0)
button5.grid(row= 3, column = 1)
button6.grid(row= 3, column = 2)
button7.grid(row= 4, column = 0)
button8.grid(row= 4, column = 1)
button9.grid(row= 4, column = 2)
button0.grid(row=2, column= 3)

plus.grid(row=5, column= 0)
minus.grid(row=5, column= 1)
multiply.grid(row=5, column= 2)
divide.grid(row=5, column= 3)
equal.grid(row=4, column= 3)
clear.grid(row=3, column= 3)
decimalpoint.grid(row=5, column= 4)
buttonlbracket.grid(row=4,column=4)
buttonrbracket.grid(row=3,column=4)






space.mainloop()



from tkinter import *
expression = " "
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)
def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "
    except:
        equation.set("error")
        expression = " "
def clear():
    global expression
    expression = " "
    equation.set(" ")


root = Tk()
root.configure(background= "cyan")
root.title("Calculator")
root.geometry("500x500")
    
equation = StringVar()
textbook = Entry(root, textvariable = equation)
textbook.grid(columnspan= 4, padx = 100, pady = 50)
equation.set("Enter your expression")
b1 = Button(root, text = 1, fg = "white", bg = "black", command= lambda: press(1), height= 1, width =7)
b1.grid(column=0, row= 2)

b2 = Button(root, text = 2, fg = "white", bg = "black", command= lambda: press(2), height= 1, width =7)
b2.grid(column=1, row = 2)

b3 = Button(root, text = 3, fg = "white", bg = "black", command= lambda: press(3), height= 1, width =7)
b3.grid(column= 2, row=2)

divide = Button(root, text = "/", fg = "white", bg = "black", command= lambda: press("/"), height= 1, width =7)
divide.grid(column = 3, row = 2)

b4 = Button(root, text = 4, fg = "white", bg = "black", command= lambda: press(4), height= 1, width =7)
b4.grid(column= 0, row = 3)

b5 = Button(root, text = 5, fg = "white", bg = "black", command= lambda: press(5), height= 1, width =7)
b5.grid(column = 1, row= 3)

b6 = Button(root, text = 6, fg = "white", bg = "black", command= lambda: press(6), height= 1, width =7)
b6.grid(column= 2, row= 3)



multiply = Button(root, text = "*", fg = "white", bg = "black", command= lambda: press("*"), height= 1, width =7)
multiply.grid(column= 3, row = 3)





b7 = Button(root, text = 7, fg = "white", bg = "black", command= lambda: press(7), height= 1, width =7)
b7.grid(column=0, row = 4)

b8 = Button(root, text = 8, fg = "white", bg = "black", command= lambda: press(8), height= 1, width =7)
b8.grid(column= 1, row = 4)

b9 = Button(root, text = 9, fg = "white", bg = "black", command= lambda: press(9), height= 1, width =7)
b9.grid(column = 2, row= 4)

Subtraction = Button(root, text = "-", fg = "white", bg = "black", command= lambda: press("-"), height= 1, width =7)
Subtraction.grid(column= 3, row = 4)

b0 = Button(root, text = 0, fg = "white", bg = "black", command= lambda: press(0), height= 1, width =7)
b0.grid(column=0, row = 5)

Decimal = Button(root, text = ".", fg = "white", bg = "black", command= lambda: press("."), height= 1, width =7)
Decimal.grid(column= 1, row = 5)

equivalent = Button(root, text = "=", fg = "white", bg = "black", command=  equal, height= 1, width =7)
equivalent.grid(column= 2, row = 5)

Addition = Button(root, text = "+", fg = "white", bg = "black", command= lambda: press("+"), height= 1, width =7)
Addition.grid(column= 3, row = 5)

Clear = Button(root, text = "C", fg = "white", bg = "black", command= clear, height= 1, width =7)
Clear.grid(column= 0, row = 6)

root.mainloop()
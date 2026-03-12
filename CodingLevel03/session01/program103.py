def find_sum():
    a = float(entryfirstnumber.get())
    b = float(entrysecondnumber.get())
    summ = a + b
    output_msg = f'The sum of {a} and {b} is {summ}'
    labelresult.configure(text = output_msg)

def find_difference():
    a = float(entryfirstnumber.get())
    b = float(entrysecondnumber.get())
    difference = a - b
    output_msg = f'The difference between {a} and {b} is {difference}'
    labelresult.configure(text = output_msg)

def find_product():
    a = float(entryfirstnumber.get())
    b = float(entrysecondnumber.get())
    product = a * b
    output_msg = f'The product of {a} and {b} is {product}'
    labelresult.configure(text = output_msg)

def find_quotient():
    a = float(entryfirstnumber.get())
    b = float(entrysecondnumber.get())
    quotient = a//b
    output_msg = f'The quotient when {a} is divided by {b} is {quotient}'
    labelresult.configure(text = output_msg)

import tkinter as tk

root_window = tk.Tk()

root_window.title("My first window")

labelfirstnumber = tk.Label(root_window, text = 'Enter first number')
entryfirstnumber = tk.Entry(root_window)

labelsecondnumber = tk.Label(root_window, text = 'Enter second number')
entrysecondnumber = tk.Entry(root_window)

labelresult = tk.Label(root_window, text = 'Your result will appear here')

buttonsum = tk.Button(root_window, text = 'Addition', command = find_sum)
buttondifference = tk.Button(root_window, text = 'Subtraction', command = find_difference)
buttonproduct = tk.Button(root_window, text = 'Multiplication', command = find_product)
buttonquotient = tk.Button(root_window, text = 'Division', command = find_quotient)

labelfirstnumber.grid(row = 0, column = 0)
entryfirstnumber.grid(row = 0, column = 1)

labelsecondnumber.grid(row = 1, column = 0)
entrysecondnumber.grid(row = 1, column = 1)

buttonsum.grid(row = 2, column = 0)
buttondifference.grid(row = 2, column = 1)
buttonproduct.grid(row = 3, column = 0)
buttonquotient.grid(row = 3, column = 1)

labelresult.grid(row = 4, columnspan = 2)

root_window.mainloop()
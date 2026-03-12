import tkinter as tk
root_window = tk.Tk()
root_window.title("My first window")

labelfirstnumber = tk.Label(root_window, text = 'Enter first number')
entryfirstnumber = tk.Entry(root_window)

labelsecondnumber = tk.Label(root_window, text = 'Enter second number')
entrysecondnumber = tk.Entry(root_window)

labelfirstnumber.pack()
entryfirstnumber.pack()

labelsecondnumber.pack()
entrysecondnumber.pack()

root_window.mainloop()
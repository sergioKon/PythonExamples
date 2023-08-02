''' 
#from tkinter import ttk
root = tk.Tk()
frm = ttk.Frame(root, padding=500)
frm.grid()

ttk.Label(frm, text=" Hello World! ").grid(column=0,row=0)
ttk.Button(frm, text=" Quit ", command=root.destroy).grid(column=1, row=0)
root.mainloop() 
'''

import tkinter as tk

def hello(event):
    print("Single Click, Button-l") 
    frame2.destroy
window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.X, side=tk.LEFT, expand=False)
frame1.bind('frame1', hello)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=75, height=100, bg="blue")
frame3.pack()


window.mainloop()
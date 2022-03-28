import tkinter

mainWindow = tkinter.Tk()

lb = tkinter.Listbox(mainWindow)
lb.grid(row=0, column=0, sticky='nse')
lb.insert((1, 2, 3))

mainWindow.mainloop()


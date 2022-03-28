import tkinter

c1 = [["C", 7, 4, 1, 0],
      ["CE", 8, 5, 2,'='],
      ['x', 9, 6, 3, 'x'],
      ['x', '+', '-', '*', '/']]
x = 1
y = 0

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('480x480-8-200')
mainWindow['padx'] = 20
mainWindow['pady'] = 20

mainWindow.minsize(250, 250)
field = tkinter.Entry(mainWindow)
field.grid(row=0, column=0, columnspan=4, sticky='snew')



for n in range(0, 8):
    mainWindow.columnconfigure(n, weight=1)
    mainWindow.rowconfigure(n, weight=1)

for i in c1:
    for val in i:
        if val == 'x':
            x += 1
            continue
        if val == '=':
            tkinter.Button(mainWindow, text=i[x - 1]).grid(row=x, column=y, sticky='swen', columnspan=2)
            continue
        tkinter.Button(mainWindow, text=i[x - 1]).grid(row=x, column=y, sticky='swen')
        x += 1
    y += 1
    x = 1

mainWindow.mainloop()




from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('get text demo')
ws.geometry('200x200')


def welcomeMessage():
    name = name_Tf.get()
    return messagebox.showinfo('message', f'Hi! {name}, Welcome to python guides.')


ytlabel = Label(ws, text="Enter Youtube URL").pack()
name_Tf = Entry(ws)
name_Tf.pack()

Button(ws, text="Click Here", command=welcomeMessage).pack()

ws.mainloop()
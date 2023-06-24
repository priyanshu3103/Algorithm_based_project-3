from  tkinter import Tk
from tkinter import Label
import time
import sys

windows = Tk()
# windows.geometry("500x100")
windows.title("Digital Clock")
windows.config(bg='white')

def get_time():

    time_c= time.strftime("%I:%M:%S %p")
    clock.config(text=time_c)
    clock.after(100,get_time)


# Label(windows,font=('Arial',40),text='Digital Clock',bg='white',fg='black').pack()
clock =Label(windows,font=('Times new roman',100),bg='white',fg='black')
clock.pack()

get_time()
windows.mainloop()
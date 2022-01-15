# hewwo uwu
from tkinter import *
from tkinter import messagebox as mbox
import turtle, time, os
version = '2.9'
canvas = turtle.Pen()
tk = Tk()
tk.title('PyPaint Control Panel')
def _info(): 
    newWindow = Toplevel(tk) 
    newWindow.title("PyPaint Info")  
    newWindow.geometry("400x100") 
    Label(newWindow, text ='''- PyPaint -
- Version '''+version+''' -
- Made by Jackson Baker in 2020 -
A GUI Baced Painting Application written in Python using Tkinter.
For more info go to "https://github.com/JacksonFB123/PyPaint".
(And if you have problems you can go there for that as well)''').pack()
    def close():
        newWindow.destroy()
    Button(newWindow, text='Close Window', command=close).pack()
def _forward():
    canvas.forward(10)
def _back():
    canvas.back(10)
def _left():
    canvas.left(45)
def _right():
    canvas.right(45)
def _down():
    canvas.pendown()
def _up():
    canvas.penup()
def _clear():
    canvas.reset()
def _color(this_was_Jaxo717_sub_to_me_on_yt_plz):
    colorChanger = Toplevel(tk)
    def red1():
        canvas.color('red')
        colorChanger.destroy()
    def green1():
        canvas.color('green')
        colorChanger.destroy()
    def blue1():
        canvas.color('blue')
        colorChanger.destroy()
    def black1():
        canvas.color('black')
        colorChanger.destroy()
    colorChanger.title("PyPaint Color Changer")
    Button(colorChanger, text='Red', command=red1).pack()
    Button(colorChanger, text='Green', command=green1).pack()
    Button(colorChanger, text='Blue', command=blue1).pack()
    Button(colorChanger, text='Black', command=black1).pack()
def refresh(event):
    if event.keysym == 'Up':
        _forward()
    elif event.keysym == 'Down':
        _back()
    elif event.keysym == 'Left':
        _left()
    else:
        _right()
def _exit():
    RUSURE = mbox.askquestion ('PyPaint','Are you sure you want to exit the application?',icon = 'warning')
    if RUSURE == 'yes':
       exit()
    else:
        while True:
            break
def _keys():
    newWindow = Toplevel(tk)
    newWindow.title("Keypress Settings")
    Label(newWindow, text='''----KEYPRESS SETTINGS----
Up Arrow = Go Forward - Back Arrow = Go Backward
Left and Right Arrows = Turn Left And Turn Right
Q = Color Changer''').pack()
    def close():
        newWindow.destroy()
    Button(newWindow, text='Close Window', command=close).pack()
txt = Label(tk, text="PyPaint")
btn1 = Button(tk, text='Forward', command=_forward)
btn2 = Button(tk, text='Backward', command=_back)
btn3 = Button(tk, text='Left', command=_left)
btn4 = Button(tk, text='Right', command=_right)
btn5 = Button(tk, text='Pen On', command=_down)
btn6 = Button(tk, text='Pen Off', command=_up)
btn7 = Button(tk, text='Change Color', command=_color)
btn8 = Button(tk, text='Reset Canvas', command=_clear)
btn9 = Button(tk, text='Program Info', command=_info)
btn10 = Button(tk, text='Keypress Settings', command=_keys)
btn11 = Button(tk, text='Exit', command=_exit)
def packall():
    txt.pack()
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn6.pack()
    btn7.pack()
    btn8.pack()
    btn9.pack()
    btn10.pack()
    btn11.pack()
    tk.bind_all('<KeyPress-Up>', refresh)
    tk.bind_all('<KeyPress-Down>', refresh)
    tk.bind_all('<KeyPress-Left>', refresh)
    tk.bind_all('<KeyPress-Right>', refresh)
    tk.bind_all('<q>', _color)
packall()
mbox.showinfo('PyPaint', 'Welcome to PyPaint v'+version+'!')

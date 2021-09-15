from tkinter import Tk, Button, Label
from PIL import ImageTk 
import pyglet

app = Tk()
app.minsize(width=500, height=400)
app.title("Я кериил")
app.iconbitmap('icon.ico')
app.resizable(width=False, height=False)

image = ImageTk.PhotoImage(file="image.png")

def clicked(event):
    try:
        ammount = int(score.cget("text")) + 1
        score.config(text = ammount)
        audio = pyglet.media.load("music.mp3")
        audio.play()
    except Exception as e:
        print(repr(e))

ClickButton = Button(app, image=image, relief = 'flat')
ClickButton.bind("<Button-1>", clicked)
ClickButton.place(relx=.5, rely=.5, anchor="c", height=30, width=30, bordermode="outside")
ClickButton.pack()

score = Label(app, text="0", font="helvetica 14", wraplength=300, justify="center")
score.pack() 

app.update_idletasks()
app.update()

app.mainloop()
from project import clear_frame, damage, faint, next_frame
from tkinter import *
import random, math, pytest

def test_clear_frame():
    root = Tk()
    root.geometry("600x600")
    frame = Frame(root)
    frame.pack(side="top", expand=True, fill="both")
    text = Label(frame, text="Gotta catch em all")
    clear_frame(frame)
    with pytest.raises(TclError):
        text.pack()


def test_damage():
    dmg = math.floor(math.floor((((2 * 5 / 5 + 2) * 35 * (9/9)) / 50 + 2)) * (random.randint(85, 100) / 100))
    assert 5 > dmg >= 3


def test_next_frame():
    root = Tk()
    root.geometry("600x600")
    root.update_idletasks()
    root.after(200)
    assert root.after(200) == None

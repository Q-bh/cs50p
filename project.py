from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time, random



"""
    img = ImageTk.PhotoImage(Image.open("sprites/squirtle_front.png"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
"""

def main():

    def menu_screen():
        global poke50, bulbasaur_front, bulbasaur_back, charmander_front, charmander_back, squirtle_front, squirtle_back, red, blue, blue_throw, terrain, red_pokemon, blue_pokemon, bulbasaur, charmander, squirtle, pokeball

        poke50 = PhotoImage(file='ui/poke50.png')
        bulbasaur_front = PhotoImage(file='sprites/bulbasaur_front.png').zoom(3,3)
        bulbasaur_back = PhotoImage(file='sprites/bulbasaur_back.png').zoom(3,3)
        charmander_front = PhotoImage(file='sprites/charmander_front.png').zoom(3,3)
        charmander_back = PhotoImage(file='sprites/charmander_back.png').zoom(3,3)
        squirtle_front = PhotoImage(file='sprites/squirtle_front.png').zoom(3,3)
        squirtle_back =PhotoImage(file='sprites/squirtle_back.png').zoom(3,3)
        red = PhotoImage(file='sprites/red.png').zoom(3,3)
        blue = PhotoImage(file='sprites/blue.png').zoom(3,3)
        blue_throw = PhotoImage(file='sprites/blue_throw.png').zoom(3,3)
        terrain = PhotoImage(file='sprites/terrain.png').zoom(3,3)
        pokeball = PhotoImage(file='sprites/pokeball.png').zoom(3,3)

        red_pokemon = None
        blue_pokemon = None

        bulbasaur = {
            "Name": "BULBASAUR",
            "FSprite": bulbasaur_front, "BSprite": bulbasaur_back,
            "HP": 19, "Attack": 49, "Defense": 49, "Speed": 45,
            "Move 1": "Tackle", "Move 2": "Growl"
            }

        charmander = {
            "Name": "CHARMANDER",
            "FSprite": charmander_front, "BSprite": charmander_back,
            "HP": 18, "Attack": 52, "Defense": 43, "Speed": 65,
            "Move 1": "Scratch", "Move 2": "Growl"
            }

        squirtle = {
            "Name": "SQUIRTLE",
            "FSprite": squirtle_front, "BSprite": squirtle_back,
            "HP": 19, "Attack": 48, "Defense": 65, "Speed": 43,
            "Move 1": "Tackle", "Move 2": "Tail Whip"
            }

        clear_frame(frame)

        canvas = Canvas(frame, width=350, height=200)
        canvas.pack(side="top")
        canvas.create_image(175, 100, image=poke50)

        Label(frame, text="A CS50P Project", font=("Fixedsys", 25)).pack(pady=30)

        Button(frame, text='Start', font=("Fixedsys", 15), width=30, command=starters).pack()
        Button(frame, text='Help', font=("Fixedsys", 15), width=30, command=help_screen).pack()
        Button(frame, text='Quit', font=("Fixedsys", 15), width=30, command=root.destroy).pack()



    def help_screen():
        clear_frame(frame)
        text = Text(frame)
        text.insert(INSERT, "WIP")
        text.pack()
        Button(frame, text='Back', font=("Modern", 15), width=30, command=menu_screen).pack()



    def starters():
        clear_frame(frame)
        Label(frame, text="Choose your Pokémon", font=("Fixedsys", 25)).pack(pady=20)
        Button(frame, image=bulbasaur_front, width=200, command=bulbasaur_select).pack(side='left')
        Button(frame, image=charmander_front, width=200, command=charmander_select).pack(side='left')
        Button(frame, image=squirtle_front, width=200, command=squirtle_select).pack(side='left')



    def bulbasaur_select():
        pokemon_select([bulbasaur_front, "GRASS", "BULBASAUR", bulbasaur])

    def charmander_select():
        pokemon_select([charmander_front, "FIRE", "CHARMANDER", charmander])

    def squirtle_select():
        pokemon_select([squirtle_front, "WATER", "SQUIRTLE", squirtle])



    def pokemon_select(list):
        global red_pokemon, blue_pokemon
        clear_frame(frame)
        canvas = Canvas(frame, width=600, height=600)
        canvas.pack(side="top")
        canvas.create_image(300, 250, image=list[0])
        Label(
            frame, text=f"So, RED, you've decided on the\n{list[1]} POKéMON {list[2]}?", font=("Fixedsys", 22), borderwidth=1, relief="sunken", justify="left"
            ).place(relx=0.045, rely=0.8, anchor=SW)
        Button(frame, text='YES', font=("Fixedsys", 15), width=30, command=battle_start).place(relx=0.15, rely=0.875, anchor=SW)
        Button(frame, text='NO', font=("Fixedsys", 15), width=30, command=starters).place(relx=0.15, rely=0.95, anchor=SW)
        red_pokemon = list[3]
        if list[1] == 'GRASS':
            blue_pokemon = charmander
        elif list[1] == 'FIRE':
            blue_pokemon = squirtle
        else:
            blue_pokemon = bulbasaur



    def battle_start():
        clear_frame(frame)
        canvas = Canvas(frame, width=600, height=600)
        canvas.pack(side="top")
        canvas.create_image(300, 250, image=terrain)
        canvas.create_image(100, 322, image=red)
        blu = canvas.create_image(460, 200, image=blue)
        text = Label(
            frame, text="RIVAL BLUE\nwould like to battle!     ", font=("Fixedsys", 25), borderwidth=1, relief="sunken", justify="left"
            )
        text.place(relx=0.045, rely=0.85, anchor=SW)
        next_frame(root, 2500)
        text.configure(text=f'BLUE sent                 \nout {blue_pokemon['Name']}!')
        canvas.itemconfigure(blu, image=blue_throw)
        pball = canvas.create_image(460, 272, image=pokeball)
        for _ in range(11):
            next_frame(root, 50)
            canvas.move(blu, 20, 0)
        canvas.move(pball, 0, -30)
        canvas.itemconfigure(pball, image=blue_pokemon['FSprite'])
        for _ in range(2):
            next_frame(root, 100)
            canvas.move(pball, 0, -20)
            next_frame(root, 100)
            canvas.move(pball, 0, 20)




    root = Tk()
    root.geometry("600x600")

    frame = Frame(root)
    frame.pack(side="top", expand=True, fill="both")

    menu_screen()

    root.mainloop()


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()



def next_frame(root, i):
    root.update_idletasks()
    root.after(i)


def function_n():
    ...


if __name__ == "__main__":
    main()

from tkinter import *
import random, math



def main():
    global root

    def canvas_create(frame, width, height, ix, iy, image):
        global canvas
        canvas = Canvas(frame, width=width, height=height)
        canvas.pack(side="top")
        canvas.create_image(ix, iy, image=image)



    def menu_screen():
        global poke50, bulbasaur_front, bulbasaur_back, charmander_front, charmander_back, squirtle_front, squirtle_back, oak, red, blue, blue_throw, terrain
        global red_pokemon, blue_pokemon, bulbasaur, charmander, squirtle, pokeball, redgrowl_stacks, bluegrowl_stacks, redtw_stacks, bluetw_stacks

        poke50 = PhotoImage(file='ui/poke50.png')
        bulbasaur_front, bulbasaur_back = PhotoImage(file='sprites/bulbasaur_front.png').zoom(3,3), PhotoImage(file='sprites/bulbasaur_back.png').zoom(3,3)
        charmander_front, charmander_back = PhotoImage(file='sprites/charmander_front.png').zoom(3,3), PhotoImage(file='sprites/charmander_back.png').zoom(3,3)
        squirtle_front, squirtle_back = PhotoImage(file='sprites/squirtle_front.png').zoom(3,3), PhotoImage(file='sprites/squirtle_back.png').zoom(3,3)
        oak = PhotoImage(file='sprites/oak.png').zoom(3,3)
        red = PhotoImage(file='sprites/red.png').zoom(3,3)
        blue, blue_throw = PhotoImage(file='sprites/blue.png').zoom(3,3), PhotoImage(file='sprites/blue_throw.png').zoom(3,3)
        terrain = PhotoImage(file='sprites/terrain.png').zoom(3,3)
        pokeball = PhotoImage(file='sprites/pokeball.png').zoom(3,3)


        redgrowl_stacks, bluegrowl_stacks, redtw_stacks, bluetw_stacks = 0, 0, 0, 0
        red_pokemon, blue_pokemon = None, None

        bulbasaur= {
            "Name": "BULBASAUR",
            "FSprite": bulbasaur_front, "BSprite": bulbasaur_back,
            "FLink": PhotoImage(file='sprites/bulbasaur_front.png'), "BLink": PhotoImage(file='sprites/bulbasaur_back.png'),
            "Current HP": 19, "HP": 19, "Attack": 9, "Real Attack": 9, "Defense": 9, "Real Defense": 9,
            "Move 1": "Tackle", "Move 1 Command": tackle, "Power": 35,
            "Move 2": "Growl", "Move 2 Command": growl
            }

        charmander = {
            "Name": "CHARMANDER",
            "FSprite": charmander_front, "BSprite": charmander_back,
            "FLink": PhotoImage(file='sprites/charmander_front.png'), "BLink": PhotoImage(file='sprites/charmander_back.png'),
            "Current HP": 18, "HP": 18, "Attack": 10, "Real Attack": 10, "Defense": 9, "Real Defense": 9,
            "Move 1": "Scratch", "Move 1 Command": scratch, "Power": 40,
            "Move 2": "Growl", "Move 2 Command": growl,
            }

        squirtle = {
            "Name": "SQUIRTLE",
            "FSprite": squirtle_front, "BSprite": squirtle_back,
            "FLink": PhotoImage(file='sprites/squirtle_front.png'), "BLink": PhotoImage(file='sprites/squirtle_back.png'),
            "Current HP": 19, "HP": 19, "Attack": 9, "Real Attack": 9, "Defense": 11, "Real Defense": 11,
            "Move 1": "Tackle", "Move 1 Command": tackle, "Power": 35,
            "Move 2": "Tail Whip", "Move 2 Command": tail_whip
            }



        clear_frame(frame)

        canvas_create(frame, 350, 200, 175, 100, poke50)
        Label(frame, text="A CS50P Project", font=("Fixedsys", 25)).pack(pady=30)
        for button in [['Start', starters], ['Help', help_screen], ['Quit', root.destroy]]:
            Button(frame, text=button[0], font=("Fixedsys", 15), width=30, command=button[1]).pack()



    def help_screen():
        clear_frame(frame)
        text = Text(frame, font=("Fixedsys", 10))
        text.insert(INSERT, """From README.md:
    This is POKé50!
    POKé50 is a simplified recreation of the first rival battle from the Pokémon FireRed and LeafGreen video game with Python.

    Included features:
    - FireRed and LeafGreen sprites (Red, Blue, Professor Oak, Pokémon, Poké Balls, battle background)
    - FireRed and LeafGreen starter Pokémon with their Level 5 movesets (Bulbasaur, Charmander, and Squirtle)
    - Generation 3 battle system (1/16 critical hit chance, 2x damage on critical hits, random 0.85-1x damage modifier)
    - Simplified battle UI (Attacks only. All other options are removed for the sake of simplicity and lack of purpose during battle)
    - Functional move system with correct move powers, accuracies, and status effects (including the six-stack status effect limit)
    - Correct and fully functional damage calculation system, accounting for critical hits and stat decreases (Critical hits will bypass attack decreases)
    - Simplified animations (Entering battle, Pokémon moves, Pokémon fainting, ending battle)
    - Simplified but mostly canonical dialogue, altering based on rival defeat or victory

    Excluded features:
    - Speed, Special Attack, and Special Defense stats
    - IVs, EVs, and natures (All Pokémon are assumed to have 0 IVs and EVs in every included stat, and a neutral nature)
    - "Continue" button during battle; Pokémon moves and dialogue will progess automatically regardless of user input
    - Sound

    Disclaimer: Sprite animation and configuration is likely to be inconsistent throughout the program. This may be a result of the computer or software being used to run the program, rather than the program itself. As a result, some animations may appear to be choppy or missing movement. Most notably, a Pokémon's HP UI may shift to the left after the Pokémon has been hit by an attack.""")
        text.pack()
        Button(frame, text='Back', font=("Modern", 15), width=30, command=menu_screen).pack()



    def starters():
        clear_frame(frame)
        Label(frame, text="Choose your Pokémon", font=("Fixedsys", 25)).pack(pady=20)
        for pokemon in [[bulbasaur_front, bulbasaur_select], [charmander_front, charmander_select], [squirtle_front, squirtle_select]]:
            Button(frame, image=pokemon[0], width=200, command=pokemon[1]).pack(side='left')

    def bulbasaur_select():
        pokemon_select([bulbasaur_front, "GRASS", "BULBASAUR", bulbasaur])
    def charmander_select():
        pokemon_select([charmander_front, "FIRE", "CHARMANDER", charmander])
    def squirtle_select():
        pokemon_select([squirtle_front, "WATER", "SQUIRTLE", squirtle])

    def pokemon_select(list):
        global red_pokemon, blue_pokemon
        clear_frame(frame)
        canvas_create(frame, 600, 600, 300, 250, list[0])
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
        global canvas, pball, pball2, text, bluemove, blu

        clear_frame(frame)

        canvas_create(frame, 600, 600, 300, 250, terrain)
        blu, reb = canvas.create_image(-40, 200, image=blue), canvas.create_image(600, 322, image=red)



        for _ in range(25):
            next_frame(50)
            canvas.move(reb, -20, 0)
            canvas.move(blu, 20, 0)
        text = Label(frame, text="RIVAL BLUE\nwould like to battle!     ", font=("Fixedsys", 25), borderwidth=1, relief="sunken", justify="left")
        text.place(relx=0.045, rely=0.845, anchor=SW)
        next_frame(2500)

        text.configure(text=f'BLUE sent                 \nout {blue_pokemon['Name']}!')
        canvas.itemconfigure(blu, image=blue_throw)
        pball = canvas.create_image(460, 272, image=pokeball)
        for _ in range(11):
            next_frame(50)
            canvas.move(blu, 20, 0)

        canvas.move(pball, 0, -30)
        canvas.itemconfigure(pball, image=blue_pokemon['FSprite'])
        next_frame(200)
        shake_anim(pball, (-20, 20, -20, 20))
        next_frame(200)

        text.configure(text=f'Go! {red_pokemon['Name']}!\n                          ')
        next_frame(200)
        pball2 = canvas.create_image(150, 322, image=pokeball)
        for i in range(12):
            i += i+0.5
            next_frame(50)
            canvas.move(reb, -24, 0)
            canvas.move(pball2, 0, i)
        next_frame(500)

        canvas.itemconfigure(pball2, image=red_pokemon['BSprite'])
        if red_pokemon == charmander:
            canvas.move(pball2, 0, -20)
        canvas.move(pball2, 0, -22)
        for _ in range(5):
            next_frame(40)
            canvas.move(pball2, 0, -10)
        shake_anim(pball2, (-23, 16.5, -23, 16.5))
        bluemove = False
        battle()



    def battle():
        global move1, move2, bluemove, redhp, bluehp

        if blue_pokemon['Current HP'] == 0:
            blue_faint()
        elif red_pokemon['Current HP'] == 0:
            red_faint()

        elif bluemove:
            bluemove = False
            random.choice([blue_pokemon['Move 1 Command'], blue_pokemon['Move 2 Command']])(blue=True)

        else:
            redhp = Label(frame, text=f"{red_pokemon['Name']}    Lv5\n           {red_pokemon['Current HP']}/{red_pokemon['HP']}", font=("Fixedsys", 20))
            redhp.place(relx=0.48, rely=0.65, anchor=SW)
            bluehp = Label(frame, text=f"{blue_pokemon['Name']}    Lv5\n           {blue_pokemon['Current HP']}/{blue_pokemon['HP']}", font=("Fixedsys", 20))
            bluehp.place(relx=0.05, rely=0.275, anchor=SW)
            text.configure(text=f'What will                 \n{red_pokemon['Name']} do?')
            move1 = Button(frame, text=red_pokemon['Move 1'], font=("Fixedsys", 15), width=10, command=red_pokemon['Move 1 Command'])
            move1.place(relx=0.65, rely=0.771, anchor=SW)
            move2 = Button(frame, text=red_pokemon['Move 2'], font=("Fixedsys", 15), width=10, command=red_pokemon['Move 2 Command'])
            move2.place(relx=0.65, rely=0.835, anchor=SW)
            bluemove=True



    def attack(move, rbmove, blue=None, debuff=None, bluestacks=None, redstacks=None):
        clear_text()
        if blue:
            text.configure(text=f"{blue_pokemon['Name']}\nused {move}!              ")
            if debuff:
                rbmove(red_pokemon, bluestacks, pball, pball2, blue=True)
            else:
                rbmove(blue_pokemon, red_pokemon, blue=True)
        else:
            text.configure(text=f"{red_pokemon['Name']}\nused {move}!              ")
            if debuff:
                rbmove(blue_pokemon, redstacks, pball2, pball)
            else:
                rbmove(red_pokemon, blue_pokemon)

    def generalattack(attacker, target, blue=None):
        if blue:
            attack_anim(pball, pball2, blue=True)
        else:
            attack_anim(pball2, pball)
        damage(attacker, target)
        next_frame(500)
        battle()

    def generaldebuff(target, stacks, attackerball, targetball, dict_stat, blue=None):
        global redgrowl_stacks, bluegrowl_stacks, redtw_stacks, bluetw_stacks
        if stacks > 5:
            next_frame(1000)
            text.configure(text=f"{target['Name']}'s {dict_stat.upper()}\nwon't go lower!           ")
            next_frame(1500)
            battle()
        else:
            if blue:
                target[dict_stat] = math.floor(target[f'Real {dict_stat}'] * 2 / (3 + stacks))
                if dict_stat.upper() == 'ATTACK':
                    bluegrowl_stacks += 1
                    debuff_anim(attackerball, targetball, blue=True)
                else:
                    bluetw_stacks += 1
                    debuff_anim(attackerball, targetball, blue=True, tw=True)
            else:
                target[dict_stat] = math.floor(target[f'Real {dict_stat}'] * 2 / (3 + stacks))
                if dict_stat.upper() == 'ATTACK':
                    redgrowl_stacks += 1
                    debuff_anim(attackerball, targetball, blue=True)
                else:
                    redtw_stacks += 1
                    debuff_anim(attackerball, targetball, tw=True)
            next_frame(500)
            text.configure(text=f"{target['Name']}'s\n{dict_stat.upper()} fell!             ")
            next_frame(1000)
            battle()



    def tackle(blue=None):
        attack('TACKLE', rbtackle, blue)

    def rbtackle(attacker, target, blue=None):
        if random.randint(1, 100) <= 5:
            next_frame(1000)
            text.configure(text=f"{attacker['Name']}'s\nattack missed!            ")
            next_frame(1000)
            battle()
        else:
            generalattack(attacker, target, blue)



    def scratch(blue=None):
        attack('SCRATCH', rbscratch, blue)

    def rbscratch(attacker, target, blue=None):
        generalattack(attacker, target, blue)



    def growl(blue=None):
        attack('GROWL', rbgrowl, blue, debuff=True, bluestacks=bluegrowl_stacks, redstacks=redgrowl_stacks)

    def rbgrowl(target, stacks, attackerball, targetball, blue=None):
        generaldebuff(target, stacks, attackerball, targetball, 'Attack', blue)



    def tail_whip(blue=None):
        attack('TAIL WHIP', rbtail_whip, blue, debuff=True, bluestacks=bluetw_stacks, redstacks=redtw_stacks)

    def rbtail_whip(target, stacks, attackerball, targetball, blue=None):
        generaldebuff(target, stacks, attackerball, targetball, 'Defense', blue)



    def attack_anim(attacker, target, blue=None):
        for i in [20, attacker], [-20, attacker], [300, target], [-300, target], [300, target], [-300, target]:
            next_frame(100)
            if blue:
                canvas.move(i[1], -i[0], 0)
            else:
                canvas.move(i[1], i[0], 0)
        next_frame(100)



    def debuff_anim(attacker, target, blue=None, tw=None):
        if not tw:
            shake_anim(attacker, (-20, 20, -20, 20))
        else:
            for i in (20, -20, 20, -20):
                next_frame(100)
                if blue:
                    canvas.move(attacker, 0, i)
                else:
                    canvas.move(attacker, 0, -i)
                next_frame(100)
                if blue:
                    canvas.move(attacker, -i, 0)
                else:
                    canvas.move(attacker, i, 0)
        for i in (20, -40, 40, -40, 40, -40, 40, -20):
            next_frame(100)
            if blue:
                canvas.move(target, -i, 0)
            else:
                canvas.move(target, i, 0)



    def shake_anim(sprite, tup):
        for i in tup:
            next_frame(100)
            canvas.move(sprite, 0, i)



    def blue_slide1(str):
        global blu, text
        clear_frame(frame)
        canvas_create(frame, 600, 600, 300, 250, terrain)
        blu = canvas.create_image(680, 200, image=blue)
        text = Label(
            frame, text=str, font=("Fixedsys", 25), borderwidth=1, relief="sunken", justify="left"
            )
        text.place(relx=0.045, rely=0.845, anchor=SW)

    def blue_slide2(sprite, time, screen, str):
        for _ in range(22):
            next_frame(50)
            canvas.move(sprite, -10, 0)
        next_frame(time)
        screen(str)



    def end_screen(str):
        clear_frame(frame)
        canvas_create(frame, 350, 270, 175, 150, oak)
        Label(frame, text=str, font=("Fixedsys", 12)).pack(pady=30)
        Button(frame, text='Return to Main Menu', font=("Fixedsys", 15), width=30, command=menu_screen).pack()
        Button(frame, text='Quit', font=("Fixedsys", 15), width=30, command=root.destroy).pack()


    def blue_faint():
        global blu
        blue_slide1("BLUE: WHAT? Unbelievable!\nI picked the wrong POKéMON!")
        if red_pokemon == charmander:
            canvas.create_image(150, 355, image=red_pokemon['BSprite'])
        else:
            canvas.create_image(150, 375, image=red_pokemon['BSprite'])
        blue_slide2(blu, 3000, end_screen, "Hm! Excellent!\nBattle other TRAINERS and make your POKéMON strong!")

    def red_faint():
        global blu, text
        blue_slide1(f"BLUE: {blue_pokemon['Name']},\ncome back!                ")
        bluemon = canvas.create_image(460, 242, image=blue_pokemon['FSprite'])
        for i in range(1, 11):
                canvas.move(bluemon, 30, -10)
                x = blue_pokemon['FLink'].subsample(i,i)
                canvas.itemconfigure(bluemon, image=x)
                next_frame(100)
        next_frame(1000)
        text.configure(text="BLUE: Yeah!\nAm I great or what!       ")
        blue_slide2(blu, 2500, end_screen, "Hm... How disappointing...\nYou must strengthen your POKéMON by battling wild POKéMON.")



    root = Tk()
    root.geometry("600x600")

    frame = Frame(root)
    frame.pack(side="top", expand=True, fill="both")

    menu_screen()

    root.mainloop()



def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()



def clear_text():
    text.configure(text=f'\n                          ')
    move1.pack()
    move2.pack()



def next_frame(i):
    root.update_idletasks()
    root.after(i)


def damage(attacker, target):
    critchance = False
    if random.randint(1, 16) == 16:
        dmg = math.floor(math.floor((((2 * 5 / 5 + 2) * attacker['Power'] * (attacker['Real Attack']/target['Defense'])) / 50 + 2)) * (random.randint(85, 100) / 100) * 2)
        critchance = True
    else:
        dmg = math.floor(math.floor((((2 * 5 / 5 + 2) * attacker['Power'] * (attacker['Attack']/target['Defense'])) / 50 + 2)) * (random.randint(85, 100) / 100))
    target['Current HP'] -= dmg
    if target['Current HP'] < 1:
        target['Current HP'] = 0
    redhp.configure(text=f"{red_pokemon['Name']}    Lv5\n           {red_pokemon['Current HP']}/{red_pokemon['HP']}")
    bluehp.configure(text=f"{blue_pokemon['Name']}    Lv5\n           {blue_pokemon['Current HP']}/{blue_pokemon['HP']}")
    if critchance:
        text.configure(text="A critical hit!\n                          ")
        next_frame(500)
    if target['Current HP'] == 0:
        next_frame(500)
        if target == blue_pokemon:
            faint(blue_pokemon, pball, 'FLink', blue=True)
        else:
            faint(red_pokemon, pball2, 'BLink')



def faint(target, ball, link, blue=None):
    for i in range(1, 11):
        if blue:
            canvas.move(ball, 30, -10)
        else:
            canvas.move(ball, -30, 10)
        x = target[link].subsample(i,i)
        canvas.itemconfigure(ball, image=x)
        next_frame(100)
    text.configure(text=f"{target['Name']}\nfainted!                  ")
    next_frame(1500)

if __name__ == "__main__":
    main()

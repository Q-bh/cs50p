# POKé50
#### Video Demo:  https://www.youtube.com/watch?v=R4x3KD7vt0k
#### Description:
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
- Options to view a help text that reprints a simplified version of README.md, quit the program, return to the main menu after the rival battle

Excluded features:
- Speed, Special Attack, and Special Defense stats
- IVs, EVs, and natures (All Pokémon are assumed to have 0 IVs and EVs in every included stat, and a neutral nature)
- "Continue" button during battle; Pokémon moves and dialogue will progess automatically regardless of user input
- Sound

Disclaimer: Sprite animation and configuration is likely to be inconsistent throughout the program. This may be a result of the computer or software being used to run the program, rather than the program itself. As a result, some animations may appear to be choppy or missing movement. Most notably, a Pokémon's HP UI may shift to the left after the Pokémon has been hit by an attack.

import os
import random
import sys

current_dir = ""

# Get keyblades ID
# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    current_dir = f"{os.path.dirname(sys.executable)}"
elif __file__:
    current_dir = f"{os.path.dirname(__file__)}"

files = os.listdir(f"{current_dir}/obj")
random_list = []
keyblade_list = []
for file in files:
    keyblade_list.append(file)

# Shuffle keyblades
random_list = keyblade_list.copy()
random.shuffle(random_list)

# Write the mod.yml
f = open(f"{current_dir}/mod.yml", 'w')
f.write('''title: Keyblade Effects Rando
originalAuthor: Rikysonic
game: kh2
description: A Keyblade Effects Randomizer for KH2. It will randomize every keyblade effects when swinging and hitting enemies. Make sure to run Randomizer.exe in openkh/mods/Rikysonic/Keyblade-Effects-Rando to generate a new rando.
''')
f.write('assets:\n')
for i in range(len(keyblade_list)):
    old = keyblade_list[i]
    new = random_list[i]
    old = 'obj/' + old
    new = 'obj/' + new
    f.write('- name: ' + old + '\n  method: copy\n  source:\n  - name: ' + new + '\n')
f.close()

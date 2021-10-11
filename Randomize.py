import os
import random
import sys

# Get keyblades ID
current_dir = os.path.realpath(__file__).replace(os.path.basename(__file__), '')
# current_dir = os.path.dirname(sys.executable) + "\\"
files = os.listdir(current_dir + 'obj')
random_list = []
keyblade_list = []
for file in files:
    keyblade_list.append(file)

# Shuffle keyblades
random_list = keyblade_list.copy()
random.shuffle(random_list)

# Write the mod.yml
f = open(current_dir + 'mod.yml', 'w')
f.write('assets:\n')
for i in range(len(keyblade_list)):
    old = keyblade_list[i]
    new = random_list[i]
    old = 'obj/' + old
    new = 'obj/' + new
    f.write('- name: ' + old + '\n  method: copy\n  source:\n  - name: ' + new + '\n')
f.close()

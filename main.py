import keyboard
import time

time.sleep(5)
with open("text.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
for line in lines:
    if line.__contains__("}"):
        keyboard.press("down")
    else:
        line_mod = line.strip(' ')
        keyboard.write(line_mod)
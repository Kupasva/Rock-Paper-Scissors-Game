from pyfiglet import figlet_format
from termcolor import colored
msg = input("write a word:")

color = input("choose color:")

valid_color = ('red', 'green', 'blue', 'cyan', 'white')

if color not in valid_color:
    color = "white"

accii_art = figlet_format(msg,font='slant')

color_ascii = colored(accii_art,color)
print(color_ascii)
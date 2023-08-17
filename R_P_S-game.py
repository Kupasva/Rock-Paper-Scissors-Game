from pyfiglet import figlet_format
#from colorama import Fore, Back, Style
from termcolor import  colored

msg = input("enter some text")

art = figlet_format(msg)
print(art)
colour = colored(art, 'red')
# choice = input("write a color")

from asciimatics.screen import Screen
from time import sleep

def clas(screen):
    screen.print_at("Hello world!",0,0)
    screen.refresh()
    sleep(3)

Screen.wrapper(clas)
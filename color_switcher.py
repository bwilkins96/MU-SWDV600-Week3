# A program that produces a window that changes color when clicked

from graphics import *

def main():
    win = GraphWin('Color Switcher', 500, 500)
    win.setBackground('black')
    
    win.getMouse()
    win.setBackground('green')
    win.getMouse()

    win.close()

main()
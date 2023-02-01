# A program that produces a window with a green gradient

from graphics import *

def main():
    NUM_RECTANGLES = 252    # 252 / 6 = 42

    win = GraphWin('Gradient Bar', 400, 300)
    win.setCoords(0, 0, 100, 100)

    fromLeft = 0
    for i in range(NUM_RECTANGLES):
        bottomLeft = Point(100 / NUM_RECTANGLES * fromLeft, 0)
        upperRight = Point((100 / NUM_RECTANGLES * fromLeft) + (100 / NUM_RECTANGLES), 100)

        fillColor = color_rgb(0, round(fromLeft * (255 / NUM_RECTANGLES)), 0)

        rect = Rectangle(bottomLeft, upperRight)
        rect.setFill(fillColor) 
        rect.setOutline(fillColor)
        rect.draw(win)

        fromLeft += 1

    win.getMouse()

main()
# A program that produces a window with a graphical representation of a baseball field

from graphics import *

def main():
    win = GraphWin('Baseball Diamond', 720, 500)
    win.setCoords(0, 0, 100, 100)
    win.setBackground('green3')

    mound = Circle(Point(50, 50), 5)
    mound.setFill('tan')
    mound.setOutline('white')
    mound.draw(win)

    firstBase = Rectangle(Point(72.5, 52.5), Point(77.5, 47.5))
    secondBase = Rectangle(Point(52.5, 77.5), Point(47.5, 72.5))
    thirdBase = Rectangle(Point(22.5, 52.5), Point(27.5, 47.5))

    homeBase = Polygon(
        Point(47.5, 27.5), Point(52.5, 27.5), Point(52.5, 25), Point(50, 22.5), Point(47.5, 25)
    )

    for base in [firstBase, secondBase, thirdBase, homeBase]:
        base.setFill('white')
        base.setOutline('white')
        base.draw(win)

    followLine1 = Line(Point(52.5, 25), Point(77.5, 47.5))
    followLine2 = Line(Point(47.5, 25), Point(22.5, 47.5))

    for line in [followLine1, followLine2]:
        line.setFill('white')
        line.draw(win)

    win.getMouse()
    win.close()

main()
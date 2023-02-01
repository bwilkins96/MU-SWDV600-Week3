# A program that produces a drawing of a house 
# that changes between day and night when clicked
# and increments a counter up to 100

from graphics import *

def main():
    win = GraphWin('Python House', 650, 400)
    win.setCoords(0, 0, 100, 100)

    grass = Rectangle(Point(0,0), Point(100, 15))
    grass.setFill('green3')
    grass.setOutline('green3')
    grass.draw(win)

    sky = Rectangle(Point(0, 15), Point(100, 100))
    sky.setFill('sky blue')
    sky.setOutline('sky blue')
    sky.draw(win)

    house = Rectangle(Point(25, 15), Point(75, 60))
    house.setFill('yellow2')
    house.draw(win)

    door = Rectangle(Point(46, 15), Point(54, 40))
    door.setFill('tan2')
    door.draw(win)

    leftWindow = Rectangle(Point(30, 30), Point(40, 45))
    leftWindow.setFill('light steel blue')
    leftWindow.draw(win)

    rightWindow = leftWindow.clone()
    rightWindow.move(30, 0)
    rightWindow.draw(win)

    roof = Polygon(Point(25, 60), Point(50, 85), Point(75, 60))
    roof.setFill('brown')
    roof.draw(win)

    leftWindowPane1 = Line(Point(30, 37.5), Point(40, 37.5))
    leftWindowPane2 = Line(Point(35, 30), Point(35, 45))
    leftWindowPane1.draw(win)
    leftWindowPane2.draw(win)

    rightWindowPane1 = leftWindowPane1.clone()
    rightWindowPane1.move(30, 0)
    rightWindowPane2 = leftWindowPane2.clone()
    rightWindowPane2.move(30, 0)
    rightWindowPane1.draw(win)
    rightWindowPane2.draw(win)

    doorKnob = Circle(Point(52.5, 27), 0.8)
    doorKnob.setFill('gold')
    doorKnob.draw(win)

    sun = Circle(Point(10, 90), 9.175)
    sun.setFill('yellow')
    sun.setOutline('yellow')
    sun.draw(win)

    clickNum = 0
    address = Text(Point(50, 45), clickNum)
    address.draw(win)

    current = 'day'
    for i in range(101):
        win.getMouse()
        clickNum += 1

        if current == 'day':
            sky.setFill('black')
            sky.setOutline('black')
            sun.setFill('white')
            sun.setOutline('white')
            grass.setFill('green4')
            grass.setOutline('green4')
            leftWindow.setFill('yellow')
            rightWindow.setFill('yellow')
            house.setFill('yellow4')
            door.setFill('tan3')
            
            current = 'night'
        else:
            sky.setFill('sky blue')
            sky.setOutline('sky blue')
            sun.setFill('yellow')
            sun.setOutline('yellow')
            grass.setFill('green3')
            grass.setOutline('green3')
            leftWindow.setFill('light steel blue')
            rightWindow.setFill('light steel blue')
            house.setFill('yellow2')
            door.setFill('tan2')

            current = 'day'

        address.setText(clickNum)

    win.close()

main()
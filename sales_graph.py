# A program that produces a window where a user can input the total number of sales
# over a 3 day period. The program then draws a bar graph based on the input, and 
# calculates the total and average number of sales 

from graphics import *

def main():
    TEXT_HEIGHT = 50
    GRAPH_HEIGHT = 50
    HORIZONTAL_MARGIN = 20
    GRAPH_WIDTH = 3 * 128
    BAR_INSET = 5

    WINDOW_WIDTH = GRAPH_WIDTH + (2 * HORIZONTAL_MARGIN)
    WINDOW_HEIGHT = GRAPH_HEIGHT + (2 * TEXT_HEIGHT)

    win = GraphWin('Sales Bar Grapher', WINDOW_WIDTH, WINDOW_HEIGHT)

    labelPoint = Point(50, TEXT_HEIGHT/2)
    entryPoint = labelPoint.clone()
    entryPoint.move(77.5, 0)

    salesEntryLabel = Text(labelPoint, 'Enter Sales:')
    salesEntryLabel.draw(win)

    salesEntry = Entry(entryPoint, 5)
    salesEntry.draw(win)

    topAxisPoint = Point(HORIZONTAL_MARGIN, TEXT_HEIGHT)
    bottomAxisPoint = Point(HORIZONTAL_MARGIN, WINDOW_HEIGHT - TEXT_HEIGHT)

    axisLine = Line( topAxisPoint, bottomAxisPoint)
    axisLine.draw(win)
    
    totalSales = 0
    for i in range(3):
        win.getMouse()
        nextSales = int(salesEntry.getText())

        topLeftRectPoint = topAxisPoint.clone()
        topLeftRectPoint.move(totalSales, BAR_INSET)

        bottomRightRectPoint = bottomAxisPoint.clone()
        bottomRightRectPoint.move(totalSales + nextSales, -BAR_INSET)

        salesRect = Rectangle(topLeftRectPoint, bottomRightRectPoint)
        salesRect.draw(win)

        salesTextPoint = topAxisPoint.clone()
        salesTextPoint.move(totalSales + (nextSales / 2), GRAPH_HEIGHT / 2)
        salesAmountText = Text(salesTextPoint, f'{nextSales}')
        salesAmountText.draw(win)

        totalSales += nextSales
        salesEntry.setText('')
        
    totalTextPoint = Point(50, WINDOW_HEIGHT - (TEXT_HEIGHT / 2))
    totalText = Text(totalTextPoint, f'Total: {totalSales}')
    totalText.draw(win)

    averageTextPoint = totalTextPoint.clone()
    averageTextPoint.move(125, 0)
    averageText = Text(averageTextPoint, f'Average: {round(totalSales / 3, 2)}')
    averageText.draw(win)

    win.getMouse()

main()
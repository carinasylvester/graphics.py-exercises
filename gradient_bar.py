# gradient_bar.py
#
# This program creates a green-colored gradient bar
#
# Carina Sylvester

from graphics import *
import math 
    
def main():
    
    def drawRectangle(rectangle, number, color):
        moveX = number * 100
        rectangle.move(moveX, 0)
        rectangle.setFill(color)
        rectangle.setWidth(0)
        rectangle.draw(win)
    
    # Number of rectangles to draw
    numberOfRectangles = 64
    
    # Creates the graphics window
    win = GraphWin('Color Gradient', 400, 200)
    
    # Creates a coordinate system
    win.setCoords(0, 0, numberOfRectangles * 100, 100)
    
    # Calculates each shade of green
    nextGreen = 255 / (numberOfRectangles - 1)
    
    for rectangleNumber in range(0, numberOfRectangles):
        green = math.floor(rectangleNumber * nextGreen)
        color = color_rgb(0, green, 0)
        drawRectangle(Rectangle(Point(0,0), Point(200,100)), rectangleNumber, color)
        
main()
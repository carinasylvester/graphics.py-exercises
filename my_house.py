# my_house.py
#
# This program draws an outdoor scene of a house.
#
# Carina Sylvester

from graphics import *

def main():
    def drawItem(item, color):
        item.setFill(color)
        item.setOutline(color)
        item.draw(win)
        
    # Creates window
    win = GraphWin('My House', 300, 300, autoflush=False)
    
    # Creates coordinate system
    win.setCoords(0, 0, 200, 200)
    
    # Draws text
    text = Text(Point(100, 180), 'Welcome To My House!')
    text.setTextColor('purple')
    text.draw(win)
    
    # Draws sun (circle)
    sun = Circle(Point(170, 155), 15)
    drawItem(sun, 'yellow')
    
    # Draws grass (rectangle)
    grass = Rectangle(Point(0, 0), Point(200, 70))
    drawItem(grass, 'green')
    
    # Draws house (rectangle)
    house = Rectangle(Point(60, 40), Point(140, 120))
    drawItem(house, 'blue')
    
    # Draws roof (polygon)
    roof = Polygon(Point(60, 120), Point(140, 120), Point(100, 165))
    drawItem(roof, 'red')
     
    # Draws door (rectangle)
    door = Rectangle(Point(90, 70), Point(110, 40))
    drawItem(door, 'brown')
    
    # Draws walkway, left border (line)
    leftLine = Line(Point(90, 40), Point(90,0))
    leftLine.setWidth(5)
    drawItem(leftLine, 'grey')
    
    # Draws walkway, right border (line)
    rightLine = Line(Point(110, 40), Point(110, 0))
    rightLine.setWidth(5)
    drawItem(rightLine, 'grey')
    
    # Waits for mouse click
    win.getMouse()
    
    # Interactive Sunset
    for i in range(17):
        sun.move(0, -5)
        update(60)
   
main()
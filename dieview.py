# dieview.py
# Copied again from the book on Feb 24 -- hasn't been checked yet!

from graphics import *

class DieView:
    """DieView is a widget that displays a graphical representation of a
    standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a vew of a die, e.g.:
        d1 = DieView(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides of length 20."""

        # First define some standard value
        self.win = win
        self.background = "white"   # Color of die face
        self.foreground = "black"   # Color of the pips
        self.psize = 0.1 * size     # Radius of each pip
        hsize = size / 2.0          # Half the size of the die
        offset = 0.6 * hsize        # Distance from enter to outer pips

        # Creates a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = []
        pipSpecs = [(cx-offset, cy-offset),
                    (cx-offset, cy),
                    (cx-offset, cy+offset),
                    (cx, cy),
                    (cx+offset, cy-offset),
                    (cx+offset, cy),
                    (cx+offset, cy+offset)]

        for cxSpec, cySpec in pipSpecs:
            self.pips.append(self.__makePip(cxSpec, cySpec))

        # Create a table for which pips are on for each value
        self.onTable = [ [], [3], [2,4], [2,3,4],
                         [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6] ]

        self.setValue(1)

    def __makePip(self, x, y):
        """ Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

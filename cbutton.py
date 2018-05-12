# cbutton.py

from graphics import *
# Changes to be made: coloring for possible moves after a player rolls

class CButton:
    """A button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method returns true if the
    button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button, eg:
        qb = Button(myWin, centerPoint, radius, "Quit")"""
        # Center should be given in format Point(x, y)
        self.cx, self.cy = center.getX(), center.getY()
        self.radius = radius
        self.circ = Circle(center, radius)
        self.circ.setFill("lightgray")
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        dx = p.getX() - self.cx
        dy = p.getY() - self.cy
        return self.active and dx * dx + dy * dy <= self.radius * self.radius

    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill("black")
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill("darkgrey")
        self.circ.setWidth(1)
        self.active = False

    def optionMarble(self):
        "Sets the button to black to show options for play."
        self.circ.setFill("black")

    def setMarble(self, color):
        "Sets the button to the color of the player on it"
        self.circ.setFill(color)

    def removeMarble(self):
        "Sets the button back to active or deactive color."
        self.circ.setFill("lightgray")

# cdieview.py
# Modified version of dieview
# March 17, 2018

from dieview import DieView
from graphics import *

class ColorDieView(DieView):

    def setValue(self, value):
        self.value = value
        DieView.setValue(self, value)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

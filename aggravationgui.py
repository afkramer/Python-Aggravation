# aggravationgui.py
# Started on March 11, 2018

# Lessons learned:
    # Next time use inheritance for the CButton class

from graphics import *
from button import Button   # Rectangular buttons for GUI
from cdieview import ColorDieView
from cbutton import CButton   # Circular buttons for spaces in the board

class AggravationInterface:
    def __init__(self):
        self.win = GraphWin("Aggravation!", 1044, 864) #coord * 3.6
        self.win.setCoords(-20, -20, 270, 220)
        background = Rectangle(Point(-10,-10), Point(190,190))
        background.setFill("light slate gray")
        background.draw(self.win)
        # !! Game title -- Aggravation! (with image?) upper right hand corner?
        # Set up board with number of players and their colors
        # Stars for special holes

        # Title line can be used for instructions
        self.instruct = Text(Point(90, 205), "")
        self.instruct.setSize(20)
        self.instruct.setStyle("bold")
        self.instruct.draw(self.win)

        # Set up the dice needed
        self.dice = []
        self.dice.append(ColorDieView(self.win, Point(215, 156),25))
        self.dice.append(ColorDieView(self.win, Point(245, 156),25))

        # Make the dice gray until players are set up
        for i in range(len(self.dice)):   
            self.dice[i].setColor("gray")
   
        self.bMain = []
        self.bMain.append(Button(self.win, Point(230,60),
                                   50,15,"Start the game!"))
        self.bMain.append(Button(self.win,Point(230,36),50,15,
                                   "Rules of the game"))
        self.bMain.append(Button(self.win,Point(230,12),50,15,"Quit"))    
        self.bMain.append(Button(self.win, Point(230,126),56,15, "Roll Dice"))

        for i in range(3):  # Don't activate button "Roll Dice"
            self.bMain[i].activate()
        
        # Set up holes on the board
        # Starts at upper right hole and goes clockwise around board
        # 56 holes around the board

        holeSpecs = [(120,180),(120,168),(120,156),(120,144),(120,132),
                     (120,120),(132,120),(144,120),(156,120),(168,120),
                     (180,120),(180,105),(180,90),(180,75),
                     (180,60),(168,60),(156,60),(144,60),(132,60),
                     (120,60),(120,48),(120,36),(120,24),(120,12),
                     (120,0),(105,0),(90,0),(75,0),
                     (60,0),(60,12),(60,24),(60,36),(60,48),
                     (60,60),(48,60),(36,60),(24,60),(12,60),
                     (0,60),(0,75),(0,90),(0,105),
                     (0,120),(12,120),(24,120),(36,120),(48,120),
                     (60,120),(60,132),(60,144),(60,156),(60,168),
                     (60,180),(75,180),(90,180),(105,180)]
        
        self.centHole = CButton(self.win, Point(90,90),4,"")
        self.bases = []
        self.homes = []

        self.holes = []   # Create holes around the board
        for (cx, cy) in holeSpecs:
            self.holes.append(CButton(self.win, Point(cx,cy),4,""))

        # Any way to clean this up with for loops or something?
        ulBaseSpecs = [(36,144),(24,156),(12,168),(0,180)]
        self.ulBase = []   # Create base holes on upper left
        for (cx, cy) in ulBaseSpecs:
            self.ulBase.append(CButton(self.win, Point(cx,cy),4,""))
        self.bases.append(self.ulBase)

        ulHomeSpecs = [(90,168),(90,156),(90,144),(90,132)]
        self.ulHome = []  # Create home holes for upper left in center screen
        for (cx, cy) in ulHomeSpecs:
            self.ulHome.append(CButton(self.win, Point(cx,cy),4,""))
        self.homes.append(self.ulHome)

        urBaseSpecs = [(144,144),(156,156),(168,168),(180,180)]
        self.urBase = []   # Create base holes on upper right
        for (cx,cy) in urBaseSpecs:
            self.urBase.append(CButton(self.win, Point(cx,cy),4,""))
        self.bases.append(self.urBase)

        urHomeSpecs = [(168,90),(156,90),(144,90),(132,90)]
        self.urHome = []  # Create home holes for upper right on right side
        for (cx,cy) in urHomeSpecs:
            self.urHome.append(CButton(self.win, Point(cx,cy),4,""))
        self.homes.append(self.urHome)

        lrBaseSpecs = [(144,36),(156,24),(168,12),(180,0)]
        self.lrBase = []
        for (cx,cy) in lrBaseSpecs: # Create base holes lower right
            self.lrBase.append(CButton(self.win, Point(cx,cy),4,""))
        self.bases.append(self.lrBase)

        lrHomeSpecs = [(90,12),(90,24),(90,36),(90,48)]
        self.lrHome = []  # Create home holes on bottom of screen
        for (cx, cy) in lrHomeSpecs:
            self.lrHome.append(CButton(self.win, Point(cx,cy),4,""))
        self.homes.append(self.lrHome)

        llBaseSpecs = [(36,36),(24,24),(12,12),(0,0)]
        self.llBase = []    # Create base on lower left
        for (cx,cy) in llBaseSpecs:
            self.llBase.append(CButton(self.win, Point(cx,cy),4,""))
        self.bases.append(self.llBase)

        llHomeSpecs = [(12,90),(24,90),(36,90),(48,90)]
        self.llHome = []  # Create home on left side of screen
        for (cx, cy) in llHomeSpecs:
            self.llHome.append(CButton(self.win, Point(cx,cy),4,""))
        self.homes.append(self.llHome)

    def setBoard(self, players):
        # Set up the marbles on the board
        # Label player quadrants
        pass
    
    def setInstruct(self, text):
        self.instruct.setText(text)

    def choose(self, winName, choices, buttons):
        # Flexible so that this can be used for moving marbles to new holes
        # You have to enter winName because there are three total windows

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # Get mouse clicks until an active button is clicked
        while True:
            p = winName.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # Function exit

    def wantToPlay(self):
        self.setInstruct('Click "Start the game!" to begin')
        choices = ("Start the game!", "Rules of the game", "Quit")
        return self.choose(self.win, choices, self.bMain) == "Start the game!"

    # New window pops up to select players and marble colors
    def playerSetup(self):    
        self.playerWin = GraphWin("Set up players", 400, 550)

        # Text as instruction for how to set up players
        self.text1 = Text(Point(200,40), "")
        self.text1.setSize(18)
        self.text1.draw(self.playerWin)

        self.text2 = Text(Point(200,90), "")
        self.text2.setSize(14)
        self.text2.draw(self.playerWin)

        # Create color buttons
        self.setupBut = []
        self.colSpecs = [(50, 150), (150,150), (250,150), (350,150),
                         (50, 200), (150,200), (250,200), (350,200),
                         (50, 250), (150,250), (250,250),(350,250),
                         (50, 300), (150,300), (250,300),(350,300)]

        self.colors = ["blue", "deep sky blue", "powder blue", "dark blue",
                       "red", "orange", "yellow", "deep pink",
                       "green", "yellow green", "aquamarine", "lime",
                       "dark magenta", "dark violet",
                       "medium purple", "light pink"]

        # Make the buttons with colored rectangles
        label = 0
        for (cx, cy) in self.colSpecs:
            self.setupBut.append(Button(self.playerWin,Point(cx,cy),
                                          40,40,str(label)))
            xmin, xmax = (cx - 15), (cx + 15)
            ymin, ymax = (cy - 15), (cy + 15)
            rect = Rectangle(Point(xmin, ymin), Point(xmax, ymax))
            rect.setFill(self.colors[label])  #Use label count as index select
            rect.setOutline(self.colors[label])
            rect.draw(self.playerWin)
            label += 1

        self.text3 = Text(Point(200,350),"")
        self.text3.setSize(14)
        self.text3.draw(self.playerWin)

        self.playerName = Entry(Point(200,380),20)
        self.playerName.setFill("white")
        self.playerName.draw(self.playerWin)

        self.setupBut.append(Button(self.playerWin,Point(200,440),140,40,
                                   "Save player"))
        self.setupBut.append(Button(self.playerWin,Point(100,500),140,40,
                                   "Let's play!"))
        self.setupBut.append(Button(self.playerWin,Point(300,500),140,40,
                                   "Cancel"))

    def closePlayerSetup(self):
        self.playerWin.close()

    def createPlayer(self, num, cols):
        # Return chosen color and name
        # After two players have been set up, choose to start game
        # Cancel is always a valid choice
        
        #Clear the name text if entered
        self.text3.setText("")
        # Set up color choices
        colchoices = ["0","1","2","3","4","5","6","7",
                   "8","9","10","11","12","13","14","15"]
        # Set up button choices           
        butchoices = ["Cancel"]

        self.playerName.setText("")
        
        if num > 1:   # Two players have already been set up
            butchoices.append("Let's play!")
            self.text1.setText("Set up a player or start the game!")
        else:   # Fewer than two players set up
            self.text1.setText("Set up a player please.")

        for i in cols:
            if i in colchoices:
                colchoices.remove(i)  # Only activate color buttons not yet in use
                
        # Wait for player to choose color
        self.text2.setText("Please select a color.")
        colorNum = self.choose(self.playerWin, (colchoices+butchoices), self.setupBut)

        if colorNum == "Let's play!" or colorNum == "Cancel":
            return colorNum, None, None

        self.text2.setText("")
        self.text3.setText("Please enter your name.")

        choices = ("Save player", "Cancel")
        userSelect = self.choose(self.playerWin, choices, self.setupBut)
        if userSelect == "Save player":
            return colorNum, self.colors[int(colorNum)], self.playerName.getText()
        else:
            return "Cancel", None, None                          

    def startRollsWin(self):
        # Open a new window with die for players to find initial player

        self.startWin = GraphWin("Who goes first?",350,300)

        self.rollText1 = Text(Point(175,50),"")
        self.rollText1.setSize(18)
        self.rollText1.draw(self.startWin)

        self.rollText2 = Text(Point(175,75),"")
        self.rollText2.setSize(18)
        self.rollText2.draw(self.startWin)
 
        self.die = ColorDieView(self.startWin,Point(175,150),100)
        self.die.setColor("black")

        self.bRoll = []
        self.bRoll.append(Button(self.startWin,
                                       Point(250,250),120,50,"OK"))
        self.bRoll.append(Button(self.startWin,
                                       Point(100,250),120,50,"Roll die"))

    def closeRollsWin(self):
        self.startWin.close()

    def startRoll(self, text1, text2, val):
        # The specified player can roll the die to see who is first
        self.rollText1.setText(text1)   #Set instructions
        self.rollText2.setText(text2)
        if self.choose(self.startWin, "Roll die", self.bRoll) == "Roll die":
            # Set the die to the value from app
            self.die.setValue(val)

            if self.choose(self.startWin, "OK", self.bRoll) == "OK":
                self.die.setValue(1) #Exit loop, return control to app

    def turn(self):
        choices = ("Rules of the game", "Quit", "Roll dice")
        ans = self.choose(self.win, choices, self.bMain)
        if ans == "Roll dice":
            pass

    def moveMarbles(spaces):
        pass
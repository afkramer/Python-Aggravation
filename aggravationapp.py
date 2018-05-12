# aggravationapp.py
# Started on March 11, 2018

# Classic game of aggravation

from random import randrange
from aggravationgui import AggravationInterface
from playerhelper import getPlayers  #Helper until player setup finished

class AggravationApp:
    def __init__(self, interface):
        self.interface = interface
        self.players = []
        self.dice = Dice()

    def run(self):
        if self.interface.wantToPlay():
            #self.interface.playerSetup()
            
            # If self.createPlayers() == "Cancel" then go back to wantToPlay()?
            self.interface.playerSetup()
            if self.createPlayers() == "Cancel":
                pass
                # reset the board so that players can be set up again
                # Can I call back to run()??
            # Print the players to a file to check if it worked?
            
            ind = self.startPlayer()  #Returns player index who starts

            # Play until all players are in their home bases
            # Option to stop early?
            # Splash screen for winner of the game?

            while not self.gameOver():
                #self.turn(ind)
                #ind = self.nextPlayer(ind)

    def createPlayers(self):
        # Let users select number of players and color for each player
        # Each player selects color, enters name       

        num = 0    # Set up running count of the players to be set up
        colors = []   # Set up holder for colors already taken
        
        # Keep setting up players until max # of players reached
        while num <= 3:
            colorNum, colorName, name = self.interface.createPlayer(num, colors)
            if colorNum == "Let's play!":
                break
            elif colorNum == "Cancel":
                self.players = []  # Reset player list to empty set
                return "Cancel"
                break
            elif name == "":
                # Player didn't enter a name -- set up generic name
                self.players.append(Player(num, colorName, ("Player " + str(num+1))))
                colors.append(colorNum)  #Keep track of chosen colors
            else:
                self.players.append(Player(num, colorName, name))
                colors.append(colorNum)  #Keep track of chosen colors
            num += 1
        
        testfile = open("newtestplayers.txt", "w")
        for pl in self.players:
            print("Num: {0} Name: {1} Color: {2}".format(pl.getNumber(), pl.getName(), pl.getColor()), \
            file = testfile)
        testfile.close()

        self.interface.closePlayerSetup()    

    def startPlayer(self):
        
        self.interface.startRollsWin() # Pull up window with die and two buttons
        rolls = []  # Set up holder for throw values to find max
        for player in self.players:
            self.dice.rollAll()   # Roll both die (only return one value)
            val = self.dice.oneValue()
            rolls.append(val)   # Keep track of the value
            text1 = "{0}: please roll the die!".format(player.getName())
            self.interface.startRoll(text1, "", val)

        while True:
            if rolls.count(max(rolls)) == 1:
                break  #Only one max, no tiebreak
                
            else:
                # There's a tie -- players will be asked to roll again
                # Only one of these players can win
                top = max(rolls)  # Holder for the highest value
                for i in range(len(rolls)):
                    if rolls[i] == top:
                        self.dice.rollAll()
                        rolls[i] = val = self.dice.oneValue()
                        text1 = "{0}: please roll again." \
                                .format(self.players[i].getName())
                        text2 = "There's a tie!"
                        self.interface.startRoll(text1, text2, val)
                    else:
                        rolls[i] = 0  #set to 0 so only max players can win
                        
        self.interface.closeRollsWin()
            
        return rolls.index(max(rolls))
        
    def nextPlayer(self, index):
        # Switch to the next player
        if index == (len(self.players) - 1):
            return 0
        else:
            return index + 1

    def turn(self, player):
        # This method should be called if the player selects "roll dice"
        self.dice.rollAll()
        vals = self.dice.allValue()
        self.interface.setDice()
        spaces = self.possibleMoves(player, vals)

        #Loop while open possibilities are still available
        #Communication between GUI / app
            #Open moves -> GUI
            #Marble moved -> APP
            #Open moves recalculated -> GUI
            #Marble moved
            #Possibility to undo moves?

        while spaces != []: #While there are moves available
            marble, spaces = self.interface.moveMarbles(spaces)

        # If a six is rolled, the player gets another turn
        if vals[0] == 6 or vals[1] == 6:
            self.turn(player)

    def possibleMoves(self, player, rolls):
        # AFter the first marble is set, repeat this function
            # Make sure only left over roll is included in possibilities
                    
        # Each turn:
            # Roll dice
            # 1 or 6 --> marbles may leave base (if there are any)
            # Roll a 6 -> extra turn
            # Marbles in play may move regularly around the board
            # Marbles in play may land on star or center
                # Next turn they may make special moves to leave star or center
                # Leave center must be a 1!
            # Enter home: has to be exactly correct roll

        base = player.getBase()
        positions = player.getPositions()
        home = player.getHome()

        possible = []

        if 1 in base:
            if (1 in rolls or 6 in rolls) and (not 0 in positions):
                possible.append(0)

        for pos in positions:
            if not (pos + rolls[0]) in positions:
                possible.append(pos+rolls[0])
            if not (pos + rolls[1]) in positions:
                possible.append(pos+rolls[1])

        # How to calculate home base moves possible???
        # Return index of available spaces -- these map to coordinates of actual holes        
        return spaces

        
    def gameOver(self):
        for player in self.players:
            if player.getHome() == [1,1,1,1]:
                return True
            
class Player:
    def __init__(self, num, color, name):
        # Use beginning window for players to choose marble color
        self.num = num  # num has to start at 0 otherwise board doesn't work
        self.color = color
        self.name = name
        
        # Refer to base of interface.bases by using player index
        self.base = [1,1,1,1]
        self.positions = [-1,-1,-1,-1]
        self.home = [0,0,0,0]
        self.spaces = list(range(self.num*14,56)) + \
                        list(range(0,self.num*14))
        del(self.spaces[55])        

    def getNumber(self):
        """ Returns player number."""
        return self.num
    
    def getColor(self):
        """ Returns player color. To be used for indicating marbles in play."""
        return self.color

    def getName(self):
        """ Returns player name. To be used for player instructions on board."""
        return self.name

    def getBase(self):
        return self.base

    def getPositions(self):
        return self.positions

    def getHome(self):
        return self.home

    def move(self, marble, spaces):
        self.positions[marble] += spaces

    def knockedOut(self, marble):
        # Take marble off the board and return to the home base
        self.positions[marble] = -1
        ind = self.home.index(0)
        self.home[ind] = 1

class Dice:
    def __init__(self):
        self.dice = [0]*2
        self.rollAll()

    def rollAll(self):
        self.dice[0] = randrange(1,7)
        self.dice[1] = randrange(1,7)

    def oneValue(self):
        return self.dice[0]

    def allValue(self):
        return self.dice[:]

inter = AggravationInterface()   #create GUI
app = AggravationApp(inter)    # Create an App object
app.run()

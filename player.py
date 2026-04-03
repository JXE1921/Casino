from time import sleep
from cards import Cards
'''
Importing Libraries needed to make the Class work.
'''

class Player:
        '''
        This class is designed to store the methods of what happens to the player and is also responsible for
        creating all players needed for the game as instances of this class.
        '''
        number_of_players = 0 
        starting_balance = 0

        def __init__(self,name,position):
            '''
            Initialises the player with the following attributes. Note: all player's start with the same starting balance.
            This method also determines the each player's cards the second it is called. This is not yet the case for the dealer,
            he is not an instance of this class.
            '''
            self.position = position
            self.name = name
            self.cards = Cards.start_dealing_cards()
            self.starting_balance = Player.starting_balance

        def __str__(self):
            return f"You are {self.name} and have a balance of £{self.starting_balance}"
        def __repr__(self):
            return f"Name : {self.name} , Position : {self.position} , Cards : {self.cards} , Bal : {self.starting_balance}"
        ''' Simple formating functions used to check the if the code is proceeding as intended as minising logic errors. '''

        def set_up(count,bal):
            ''' Simple method to assign class variables to the user's input. '''
            Player.number_of_players = count
            Player.starting_balance = bal

        def create(player_count):
            '''
            Complicated method that initally asks the user if they wish to assign a name to every player and 
            then adds them as objects to the player cards. If the user wishes to assign them a name, that is used
            for the player's attributes, but if not, default names are provided such as Player 1, Player 2, ...etc
            and then their are used for the player's attributes. Also, it will run continously until a valid input is provided and 
            simultaneously created a list of objects called player list which is then returned to the main program for later use.
            '''
            while True:
                try:
                    sleep(1)
                    name = input("Would you like to give each Player a name(Yes/No): \n")
                    if name.capitalize().strip("!£$%^&*") == "Yes": 
                        try:
                            playerlist = [] # This is the list to be returned to the game.py file
                            for count in range(0,player_count):
                                sleep(1)
                                playername = input(f"What is the name of Player {count+1}:\n").capitalize().strip("!£$%^&*")
                                player = Player(playername,count + 1) # This is the instance of the class with a custom name
                                playerlist.append(player)
                            return playerlist
                        except:
                            sleep(1)
                            print("Sorry, please enter a valid name for the Player")
                            continue
                    elif name.capitalize().strip("!£$%^&*") == "No":
                        playerlist = []
                        for count in range(player_count):
                            playername = "Player " + str(count+1)
                            player = Player(playername, count + 1) # This is the instance of the class with a default name
                            playerlist.append(player)
                        return playerlist
                    else:
                        sleep(1)
                        print("Sorry, that's not a valid option. Please try again")
                        continue
                except:
                    sleep(1)
                    print("Sorry, please try again and enter either Yes or No")
                    continue
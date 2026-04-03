from game import Blackjack
''' Imports the Blackjack class from game.py which is responsible for starting the game '''

if __name__ == '__main__':
    number_of_players = 5
    starting_balance = 1500
    ''' These parameters control the game and determine the starting amount of players and their inital balance as well. '''

    game  = Blackjack(number_of_players,starting_balance) # Creates an instance of the Blackjack class
    game.run() # Starts the game

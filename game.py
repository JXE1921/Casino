from random import randint
from time import sleep
import msvcrt # TODO: Learn more about this library
from money import Money 
from cards import Cards
from player import Player
'''
Imports neccessary files and python libraries to start the Game. 
This is where the game is controlled and all other classes and functions are called.
# TODO: Create a folder that contains all these python libraries and then import it.
'''

class Blackjack:
    '''
    This class starts the game and is where the main branch of coding is linked back to.
    '''
    def __init__(self,number_of_players,balance):
        ''' Instance of class with params coming from main.py '''
        self.number_of_players = number_of_players
        self.balance = balance
        
    def check_number_of_players(player_count): 
        ''' Simple check to deteremine if the amount of player's is an integer and between 1-7 as per casino rules. '''
        try:
            if player_count > 0  and player_count < 8:
                return True
            return False
        except:
            print("Sorry, that is in an invalid amount of players. Please enter a reasonble amount of players(Up to 7 max)")
            return False

    def start_game(playerlist): 
        '''
        This function recieves a list of objects created in the Player class and then iterates through 
        each player asking them if they want another card or if they want to stand. Uses Cards class
        # TODO: Add the Score class and check whether or not the player has reached blackjack first
        '''
        for player in playerlist:
            while True:
                try:
                    Cards.print_player_cards(player) 
                    ''' Tells the player their cards by accessing player attribute, player.cards in card class '''
                    choice = input(f"{player.name},Do you want to hit or stand? \n").capitalize().strip("!£$%^&*")
                    if choice == "Hit":
                        Cards.deal_another_player_card(player)
                        ''' Deals the player another card using card class and then appends it to player.cards '''
                    elif choice == "Stand":
                        break
                except :
                    print("Sorry, that's not a valid option, please try again")

    def run(self):
        if Blackjack.check_number_of_players(self.number_of_players) and Money.check_balance(self.balance):
            '''
            Initial check to see if the starting balance and the amount of players is a reasonble value
            '''
            Player.set_up(self.number_of_players,self.balance)
            Money.set_up(self.number_of_players, self.balance)
            '''
            Sets up the class variables to be the corresponding input of the user
            in both the Player and Money class for later usage and for the object attributes.
            '''
            print("Welcome to the royal tempest")
            print("Press any key to continue...")
            msvcrt.getch()
            print("If you need the rules, you can navigate back to the home page\n" + "Other wise Lets play some BlackJack\n")
            sleep(1)
            player_count = self.number_of_players
            player_list = Player.create(player_count)
            '''
            Calls a method to create objects and assign names, positions, balances and other attributes
            in the player class which is FUNDAMENTAL for starting the game. This line completes the initialisation phase of the game
            and marks the start of the rest.
            '''
            Blackjack.start_game(player_list)
            '''
            Starts the game and uses the list of objects in the player class.
            '''




# Rules:
# 1-7 Players
# Players play against dealer
# Player gets 2 face up ad dealer gets 1 face up
# Ace is one or eleven
# If a player wins, the get their entire bet
# If a player gets balckjack, they get 1.5 times their orginal bet
# BlackJack can only be achieved with 2 cards, not any more
# 3 Options, Hit, Stay, Double down
# Doubling their orginal bet for one and one cad only = Doubling down. Shown by card turning sideways
# If the players 2 cards are a pair, they ahve the option to split. This means they double their orginal bet and the dealer splits their hand into 2 diff hands
# Most casino's only allow you to split up to 2 times
# bet is made before the cards are dealt
# Dealer must hit if less than 16, and stay if more than 16
# only players with a higher face value than then the dealer win if the delaer doesn't bust
# If they get a push, same value as dealer, they don't win or lost their bet



# TODO: Learn about these things:
# @classmethods
# django
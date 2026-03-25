from random import randint
from time import sleep
import msvcrt
from money import Money
from cards import Cards



def GetNumberOfPlayers():  # Asks user for number of players and then checks if it is a valid amount, then returns value back to the main function
   while True:
        try:
            sleep(1)
            number_of_players = int(input("Please state the number of Players joining the casino today(Up to 7 max): \n"))
            if number_of_players >7 or number_of_players <1 :
                sleep(1)
                print("\nSorry the maximum number of Players is 7 and the minimum number of players is 1. Please try again\n")
                continue
        except:
            sleep(1)
            print("\nSorry, the number of Players must be a whole number. Please try again\n")
            continue
        return number_of_players
           

def Name(players): # Creates a list based on player names and then send that into a diff funtion to generate balance
    while True:
        try:
            sleep(1)
            name = input("Would you like to give each Player a name(Yes/No): \n")
            if name.capitalize().strip("!£$%^&*") == "Yes": # If User chooses to name every player
                try:
                    playerlist = []
                    for count in range(0,players):
                        sleep(1)
                        playername = input(f"What is the name of Player {count+1}:\n").capitalize().strip("!£$%^&*")
                        playerlist.append(playername)
                    Balancelist = Money.initialiseBalance(playerlist) # Calls class method to create a list of objects
                    return Balancelist, playerlist
                    break
                except:
                    sleep(1)
                    print("Sorry, please enter a valid name for the Player")
                    continue
            elif name.capitalize().strip("!£$%^&*") == "No":
                playerlist = []
                for count in range(players):
                    playerlist.append("Player "+str(count+1))
                Balancelist = Money.initialiseBalance(playerlist) # Calls class method to create a list of objects
                return Balancelist , None
                break
            else: # Add some more tweaks
                sleep(1)
                print("Sorry, that's not a valid option. Please try again")
                continue
        except:
            sleep(1)
            print("Sorry, please try again and enter either Yes or No")
            continue
                   

def Start_game(playerlist): # Gives a player an infinite number cards but needs the score system
   for player in playerlist:
      while True:
         try:
            Money.print_player_cards(player)
            choice = input(f"{player.name},Do you want to hit or stand? \n").capitalize().strip("!£$%^&*")
            if choice == "Hit":
               Cards.deal_another_player_card(player,playerlist)
            elif choice == "Stand":
               break
         except:
            print("Sorry, that's not a valid option, please try again")



def Main():
    print("Welcome to the royal tempest")
    print("Press any key to continue...")
    msvcrt.getch()
    #print("\033[31mThis text is red\033[0m")
    print("If you need the rules, you can navigate back to the home page\n" + "Other wise Lets play some BlackJack\n")
    sleep(1)
    Playercount = GetNumberOfPlayers()
    Balance_list,Names = Name(Playercount) # This is a temporary list of objects that contain every player in the game excluding the cards that they are going to be dealt, Also gives a list of player names and is None if no names were given
    Card_list = Cards.start_dealing_cards(Playercount)
    Player_card_list = Cards.Assign_cards(Balance_list,Card_list)# This is a list of objects that contain every player in the game including the cards that have been dealt to them in the first round
    Start_game(Player_card_list)

   


Main()
   

# Rules:
# 7 Players
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
class Money:

    player_count = 0 # Class variables tht allow for giving each player the inital balance
    balance = 1000

    def __init__(self,position,name): # Object method to add the player to the class
        self.position = position
        self.name = name
        Money.player_count +=1
        self.balance = Money.balance
        self.list = [] # Stores a list of the player's cards
   
    def __repr__(self): # Simple formatting function
        return f"{self.position}: £{self.balance}"

    def initialiseBalance(list): # Given a list of names, it returns a list of objects within the class
        playerlist = []
        for count in range(0,len(list)):
            playerlist.append(Money("Player "+ str(count+1), list[count]))
        return playerlist

    def print_player_cards(player): # Designed to use show the player their cards each time they choose to hit
        for i in range(0,len(player.list)-1):
            if i == 0:
                print(f"This is your {i+1}st card, {player.list[i]}\n")
            elif i == 1:
                print(f"This is your {i+1}nd card, {player.list[i]}\n")
            elif i == 2:
                print(f"This is your {i+1}rd card, {player.list[i]}\n")
            else:
                print(f"This is your {i+1}th card, {player.list[i]}\n")


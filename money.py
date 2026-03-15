
class Money:

    player_count = 0 # Class variables tht allow for giving each player the inital balance
    balance = 1000

    def __init__(self,position,name): # Object method to add the player to the class
        self.position = position
        self.name = name
        Money.player_count +=1
        self.balance = Money.balance
    
    def __repr__(self): # Simple formatting function
        return f"{self.position}: £{self.balance}"

    def initialiseBalance(list): # Given a list of names, it returns a list of objects within the class
        playerlist = []
        for count in range(0,len(list)):
            playerlist.append(Money("Player "+ str(count+1), list[count]))
        return playerlist


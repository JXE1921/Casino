class Money:
    '''
    This class is designed to handle all things relating to the money of the player's and also their betting. 
    There is an instance of this class as it is easier to keep track of the player's balances but that this means 
    additional code will be needed in the main function to account for this. It will also handle the gambling aspect of the game.
    '''

    player_count = 0 
    balance = 1000

    def __init__(self,name):
        '''
        Instances of the class
        '''
        self.name = name
        self.balance = Money.balance

    def __repr__(self):
        ''' Simple formating functions used to check the if the code is proceeding as intended as minising logic errors. '''
        return f" Name: {self.name}, £{self.balance}"

    def set_up(player_count,bal):
        ''' Simple method to assign class variables to the user's input. '''
        Money.balance = bal
        Money.player_count = player_count

    def check_balance(num):
        ''' Simple check to make sure the starting balance is a valid integer between the range of 
        500 to 10,000'''
        try:
            if num >= 500 and num <= 10000:
                return True
            print("Sorry, please choose a starting balance in the range of 500 to 10,000")
            return False
        except:
            print("Sory, that isn't an acceptable amount of money. Please enter a starting balance in the range of 500 to 10,000")
            return False
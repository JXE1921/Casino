from random import randint
from deck import Deck

class Cards(Deck):
    '''
    This class is responsible for everything needing and relating to the cards of the player and dealer.
    It also inherits the the Deck class which contains no methods but just class variables.
    '''

    def distributed_cards(card):
        ''' Simple check to make sure the same card isn't dealt twice. '''
        if card not in Cards.check_deck:
            Cards.check_deck.add(card)
            return True
        return False

    def start_dealing_cards():
        '''
        This method will constantly run until it generated legal cards for the player to be dealt. 
        It also has a simple check that will break the code if the Deck has been used up and needs to be re-
        shuffled
        # TODO: Add code to make the user aware if the deck has been used up.
        '''
        player_cards = []
        while len(player_cards) != 2:
            if len(Cards.check_deck) == 52: return None
            randomnum1 = randint(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            if Cards.distributed_cards(card): player_cards.append(card)
        return player_cards

    def dealer_cards():
        '''
        This method is similiar to the previous method where it will keep running 
        until it generates the dealer just one legal card.
        #TODO: Use the Score class the generate all the dealer's cards first and then the player's cards.
        '''
        dealer_card_list = []
        while True:
            randomnum1 = randint(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            if Cards.distributed_cards(card):
                dealer_card_list.append(card)
                return dealer_card_list

    def deal_another_player_card(player):
        ''' Similiar to the previous two methods, generates the player one more legal card and then appends that to it's attributes '''
        while True:
            randomnum1 = randint(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            if Cards.distributed_cards(card):
                player.cards.append(card)
                break    

    def print_player_cards(player):
        ''' Simple method to print the cards of te player '''
        for i in player.cards: print(f"Your card is {i} \n ") 
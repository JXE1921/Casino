from random import *

class Cards:

    # List of all possible cards in a deck
    deck = ["Diamonds A","Diamonds 2", "Diamonds 3"  , "Diamonds 4" , "Diamonds 5" , "Diamonds 6" , "Diamonds 7" , "Diamonds 8" , "Diamonds 9" , "Diamonds 10" , "Diamonds J" , "Diamonds Q" , "Diamonds K",
            "Hearts A","Hearts 2", "Hearts 3" , "Hearts 4" , "Hearts 5" , "Hearts 6" , "Hearts 7" , "Hearts 8" , "Hearts 9" , "Hearts 10" , "Hearts J" , "Hearts Q" , "Hearts K",
            "Spades A","Spades 2", "Spades 3" , "Spades 4" , "Spades 5" , "Spades 6" , "Spades 7" , "Spades 8" , "Spades 9" , "Spades 10" , "Spades J" , "Spades Q" , "Spades K",
            "Clovers A","Clovers 2", "Clovers 3" , "Clovers 4" , "Clovers 5" , "Clovers 6" , "Clovers 7" , "Clovers 8" , "Clovers 9" , "Clovers 10" , "Clovers J" , "Clovers Q" , "Clovers K"
            ]
    check_deck = set()  # Using set data structure to adds cards when they can be distributed

    def distributed_cards(card): # Designed to check whether or not the cards have been distributed
        if card not in Cards.check_deck:
            Cards.check_deck.add(card)
            return True
        return False



    def start_dealing_cards(player_count): # Designed to iterate until a valid amount of legal cards can be distributed back to the user
        player_cards = []
        while len(player_cards) != player_count * 2:
            randomnum1 = randint(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            check = Cards.distributed_cards(card)
            if check:
                player_cards.append(card)
            else:
                continue
        return player_cards

    def dealer_cards(): # Designed to return one valid card for the dealer
        dealer_card_list = []
        while True:
            randomnum1 = random(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            check = Cards.distributed_cards(card)
            if check:
                dealer_card_list.append(card)
                return dealer_card_list
                break
            else:
                continue
    def assign_cards(playerlist,cardlist):
        for player in playerlist:
            player.list.append(cardlist[0])
            cardlist.pop(0)
            player.list.append(cardlist[0])
            cardlist.pop(0)
        return playerlist

    def deal_another_player_card(player,playerlist): # A function that allows the player to get another card
        while True:
            randomnum1 = randint(0,len(Cards.deck)-1)
            card = Cards.deck[randomnum1]
            check = Cards.distributed_cards(card)
            if check:
                player.list.append(card)
                break
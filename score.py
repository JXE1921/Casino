from ace import Ace
''' Only used when the player gets and Ace'''

class Score:
    '''
    The whole purpose of this class is calculate the score and keep a running total of all the value 
    of all the plaery's cards as well as the dealers. It uses the Ace class if either the dealer or player gets an ace 
    to keep the code organised by creating instances of this class.
    # TODO: Add an instance to this class to make it easier to track the player's cards but additional code will be needed
    '''
    points = {"2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "10": 10,
                "J": 10,
                "Q": 10,
                "K": 10,}
    ''' For mapping the cards to their corresponding value but Ace'''

    def assign_score(card_list):
        '''
        This method will turn a list of player cards into a list of their correspoding values and assign the 
        value of an Ace to 0. For example, ["Diamonds 2","Spades K","Hearts A"] becomes [2,10,0] which is then
        later used.
        '''
        value = []
        for card in card_list:
            cards = card.split(" ")
            value.append(cards[1])
        score = []
        for index in value:
            score.append(Score.points.get(index, 0))

    def sum_score(point_list):
        ''' Simple function that calculates the sum of elements in a list of integers but if there is a 0 as one of the elements
        it calls the Ace class return's that value.'''
        if 0 in point_list: return Ace.calculate_sum(point_list)
        sum = 0
        for element in point_list:
            sum += element
        return sum

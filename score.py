class Score:
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
            
    def assign_score(card_list):
        value = []
        for card in card_list:
            cards = card.split(" ")
            value.append(cards[1])
        score = []
        for index in value:
            score.append(self.points.get(index, 0))
    
    def sum_score(point_list):
        if 0 in point_list:
            return do_some_complicated_ace_stuff(point_list)
        sum = 0
        for element in point_list:
            sum += element
        return sum

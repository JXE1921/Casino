class Score(self):
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
            
    def assign_score(self, card_list):
        value = []
        for card in card_list:
            cards = card.split(" ")
            value.append(cards[1])
        score = []
        for index in value:
            score.append(self.points.get(index, 0))
    
    def sum_score(point_list):
        if 0 in point_list:
            do_some_complicated_ace_stuff(point_list)
            return None
        sum = 0
        for element in point_list:
            sum += element
        return sum




data = ["Apple A","Banana B","Orange C"]

grades = [item.split()[-1] for item in data]
print(grades)
# ['A', 'B', 'C']
grade_map = {
    "A": 3,
    "B": 2,
    "C": 1
}

numeric = [grade_map[g] for g in grades]
print(numeric)
# [3, 2, 1]
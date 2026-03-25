class Score():
    def Assign_score(card_list):
        value = [card.split()-1 for card in card_list]
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
        #score = [value[]





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
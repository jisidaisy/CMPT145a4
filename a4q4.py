import random

suits = ['H', 'D', 'S', 'C']
cardset = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valuedict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13}


class Card:
    def create(self):
        self.cardlist = []
        self.len = 52
        for i in range(len(suits)):
            for j in range(len(cardset)):
                self.cardlist.append(cardset[j] + suits[i])

        return self.cardlist

    def deal(self, p, q, cardobj):
        if p * q > cardobj.len:
            print("Not Enough Cards")
            return
        indexval = random.sample(range(0, cardobj.len), p * q)
        a = []
        for i in indexval:
            a.append(cardobj.cardlist[i]);
        for i in a:
            cardobj.cardlist.remove(i)
        cardobj.len = len(cardobj.cardlist)

        b = []
        for i in range(q):
            b.append(a[i * p:i * p + p])

        return b

    def value(self, cardstring):
        return valuedict[cardstring[0]]

    def highest(self, list_of_cards):
        highest = list_of_cards[0]
        for i in range(1, len(list_of_cards)):
            if self.value(list_of_cards[i]) > self.value(highest):
                highest = list_of_cards[i]
        return highest

    def lowest(self, list_of_cards):
        lowest = list_of_cards[0]
        for i in range(1, len(list_of_cards)):
            if self.value(list_of_cards[i]) < self.value(lowest):
                lowest = list_of_cards[i]
        return lowest

    def average(self,list_of_cards):
        """Takes a list of cards, and returns the average (float) value of this given list of cards."""
        total = 0
        for i in list_of_cards:
            total += Card.value(i)
        return total /len(list_of_cards)

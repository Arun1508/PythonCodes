import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:


    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank+' of '+self.suit
        #return ("{} of {}".format(self.rank,self.suit))

#c =Card('Two','Hearts')
#print(c)

class Deck:

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
        all_cards = ''
        for card in self.deck:
            all_cards += '\n'+card.__str__()
        return all_cards

    def suffle_cards(self):
        random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop()


#d = Deck()
#print(d)
#print(d.pop_card())

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces  = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adj__ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces  -= 1

    def __str__(self):
        return str(self.value)
#d = Deck()
#h = Hand()
#pp = d.pop_card()
#h.add_card(pp)
#print('Added pp',pp)
#c = Card('Ace','Hearts')
#h.add_card(c)
#print(h)




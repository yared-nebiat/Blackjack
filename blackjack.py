import random as r

class Card:
    def __init__(self):
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.tens = ["10", "J", "Q", "K"]
        self.deck = []
        self.dealt = []
        for i in self.values:
            for j in self.suits:
                self.card = (i,j)
                self.deck.append(self.card)
        del self.card
    

class Deck(Card):
    def __init__(self):
        Card.__init__(self)
        self.shuffle()

    def deal(self, num):
        self.last_card = self.deck.pop()
        self.dealt.append(self.last_card)
        if num == 1:
            return self.last_card
        else:
            return [self.last_card, self.deal(num-1)]

    def shuffle(self):
        if len(self.deck) != 52:
            for i in self.dealt:
                self.deck.append(i)
            self.dealt = []
        else:
            r.shuffle(self.deck)


class Player:
    def __init__(self, name, bal):
        self.hand = []
        self.name = name
        self.bal = bal
        self.wager = 0

    def wins(self, rate):
        payout = rate*self.wager
        self.bal += self.wager + payout
        print("{} wins ${}".format(self.name, payout))
        self.wager = 0

    def has_blackjack(self):
        if (self.hand[0][0] == 'A' or self.hand[1][0] =='A') and (self.hand[0][0] in Card().tens or self.hand[1][0] in Card().tens):
            return True
        return False

    def hand_total(self):
        self.total = 0
        self.ace_count = 0
        for card in self.hand:
            if card[0] in Card().tens:
                self.total += 10
            elif card[0] == 'A':
                self.ace_count += 1
                self.total += 11
            else:
                self.total += int(card[0])
        if self.total > 21 and self.ace_count > 0:
            self.total -= 10
        return self.total

    def busted(self):
        if self.hand_total()>21:
            return True
        return False

    def hit(self):
        self.new_card = Deck().deal(1)
        self.hand.append(self.new_card)
        return self.new_card
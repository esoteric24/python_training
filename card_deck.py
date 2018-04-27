import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

suits = ['clubs', 'diamonds', 'spades', 'hearts']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = []

def cycle_ranks(suit, ranks, deck):
    for rank in ranks:
        card = Card(suit, rank)
        deck.append(card)
    return deck

def printable_cards(deck):
    printDeck = []
    for card in deck:
        cardString = card.rank + ' of ' + card.suit
        printDeck.append(cardString)
    return printDeck

for suit in suits:
    deck = cycle_ranks(suit, ranks, deck)

random.shuffle(deck)

def deal_cards(deck):
    dealtCards = []
    for x in range(4):
        card = deck.pop(0)
        dealtCards.append(card)
    return dealtCards

dealtCards = deal_cards(deck)
dealtStrings = printable_cards(dealtCards)

print('{0:^30}{1:^30}'.format('PLAYER\'S CARDS', 'DEALER\'S CARDS'))
print('{0:^30}{1:^30}'.format(dealtStrings[0], dealtStrings[1]))
print('{0:^30}{1:^30}'.format(dealtStrings[2], '--------------'))

playerHand = [dealtCards[0], dealtCards[2]]
dealerHand = [dealtCards[1], dealtCards[3]]

def value_card(card):
    tenVals = ['10', 'jack', 'queen', 'king']
    value = 0
    for slot in tenVals:
        if card.rank == slot:
            value = 10
    if value == 0:
        if card.rank == 'ace':
            value = 'ace'
        else:
            value = int(card.rank)
    return value

def value_hand(cards):
    values = []
    for card in cards:
        value = value_card(card)
        values.append(value)
    aces = 0
    for value in values:
        if value == 'ace':
            aces = aces + 1
    for x in range(aces):
        values.remove('ace')
    valueSum = sum(values)
    while aces != 0:
        if (11*aces) + valueSum > 21:
            valueSum = valueSum + 1
            aces = aces - 1
        else:
            valueSum = (11*aces) + valueSum
            aces = 0
    return valueSum

playerVal = value_hand(playerHand)
dealerVal = value_hand(dealerHand)

# print(' ')
print('{0:^0}{1:^15}{2:^45}'.format('TOTALS:', playerVal, '???'))

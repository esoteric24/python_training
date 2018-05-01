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
playerStrings = [dealtStrings[0], dealtStrings[2]]
dealerHand = [dealtCards[1], dealtCards[3]]
dealerStrings = [dealtStrings[1], dealtStrings[3]]

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

dealerFaceVal = value_card(dealerHand[0])
if dealerFaceVal == 'ace':
    dealerFaceVal = 11

print(' ')
print('{0:^0}{1:^15}{2:^45}'.format('TOTALS:', playerVal, '{0} + ???'.format(dealerFaceVal)))
print(' ')

def print_hand(hand):
    length = len(hand)
    for number in range(length):
        print('{0:^30}'.format(hand[number - 1]))

def execute_hit1(deck, xHand, xStrings):
    dealtCard = deck.pop(0)
    xHand.append(dealtCard)
    cardString = dealtCard.rank + ' of ' + dealtCard.suit
    xStrings.append(cardString)
    print(' ')
    print('{0:^0}{1:^20}'.format('CARD:', cardString))

def execute_hit2(xVal):
    print(' ')
    print('{0:^0}{1:^17}'.format('TOTAL:', xVal))
    print(' ')

def execute_stand(label, xStrings, xVal):
     print(' ')
     print('{0:^26}'.format('{0} FINAL CARDS').format(label))
     print_hand(xStrings)
     print(' ')
     print('{0:^0}{1:^16}'.format('TOTAL:', xVal))
     print(' ')


while True:
    playerRes = input('PLAYER: HIT OR STAND? ')
    label = 'PLAYER\'S'
    if playerRes == 'hit':
        execute_hit1(deck, playerHand, playerStrings)
        playerVal = value_hand(playerHand)
        if playerVal > 21:
            execute_stand(label, playerStrings, playerVal)
            print('{0:^28}'.format('BUST'))
            print(' ')
            break
        else:
            execute_hit2(playerVal)
    elif playerRes == 'stand':
        execute_stand(label, playerStrings, playerVal)
        break
    else:
        print('Invalid input: try again')

while True:
    label = 'DEALER\'S'
    if dealerVal < 17:
        print('DEALER HITS')
        execute_hit1(deck, dealerHand, dealerStrings)
        dealerVal = value_hand(dealerHand)
        if dealerVal > 21:
            execute_stand(label, dealerStrings, dealerVal)
            print('{0:^28}'.format('BUST'))
            print(' ')
            break
        else:
            execute_hit2(dealerVal)
    elif dealerVal > 16:
        print('DEALER STANDS')
        execute_stand(label, dealerStrings, dealerVal)
        break

if playerVal > 21:
    playerVal = 'BUST'
if dealerVal > 21:
    dealerVal = 'BUST'

print('{0:^30}{1:^30}'.format('PLAYER\'S TOTAL', 'DEALER\'S TOTAL'))
print('{0:^30}{1:^30}'.format(playerVal, dealerVal))

dealerWin = '{0:^60}'.format('DEALER WINS')
playerWin = '{0:^60}'.format('PLAYER WINS')
tie = '{0:^60}'.format('TIE')

if playerVal == 'BUST':
    print(dealerWin)
elif dealerVal == 'BUST':
    if playerVal != 'BUST':
        print(playerWin)
else:
    if playerVal > dealerVal:
        print(playerWin)
    elif dealerVal > playerVal:
        print(dealerWin)
    else:
        if playerVal == 21 and dealerVal == 21:
            if len(playerHand) == 2:
                print(playerWin)
            elif len(dealerHand) == 2:
                print(dealerWin)
            else:
                print(tie)
        else:
            print(tie)
print(' ')

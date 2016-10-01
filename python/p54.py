#!/usr/bin/env python3

'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD
                Pair of Fives           Pair of Eights          Player 2
2	 	5D 8C 9S JS AC 	        2C 5C 7D 8S QH
                Highest card Ace        Highest card Queen 	Player 1
3	 	2D 9C AS AH AC   	3D 6D 7D TD QD
                Three Aces              Flush with Diamonds 	Player 2
4	 	4D 6S 9H QH QC 	        3D 6D 7H QD QS
                Pair of Queens          Pair of Queens       
                Highest card Nine       Highest card Seven 	Player 1
5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D
                Full House              Full House
                With Three Fours        with Three Threes 	Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

import requests

CARD_VALUES = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
               '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q':10, 'K':11, 'A':12}


RESULTS = {'nothing': 0, 'one pair': 1, 'two pairs': 2, 'three of a kind': 3,
           'straight': 4, 'flush': 5, 'full house': 6, 'four of a kind': 7,
           'straight flush': 8, 'royal flush': 9}


def card_values(cards):
    values = [0] * len(CARD_VALUES)
    for c in cards:
        values[CARD_VALUES[c[0]]] += 1
    return values


def evaluate_hand(cards):
    values = card_values(cards)
    # nothing, straight (flush), royal flush, flush
    if max(values) < 2:
        flush = False
        # flush
        if len(set([c[1] for c in cards])) == 1:
            flush = True
        # straight/royal
        if values[values.index(1):values.index(1)+5] == [1] * 5:
            # royal
            if values.index(1) == CARD_VALUES['T'] and flush:
                return RESULTS['royal flush']
            if flush:
                return RESULTS['straight flush']
            return RESULTS['straight']
        if flush:
            return RESULTS['flush']
        return RESULTS['nothing']
    # pair, two pairs
    if max(values) == 2:
        if values.count(2) == 1:
            return RESULTS['one pair']
        return RESULTS['two pairs']
    # three of a kind, full hourse
    if max(values) == 3:
        if 2 in values:
            return RESULTS['full house']
        return RESULTS['three of a kind']
    return RESULTS['four of a kind']


def test_evaluate_hand():
    assert evaluate_hand(['5H','5C', '6S', '7S', 'KD']) == RESULTS['one pair']
    assert evaluate_hand(['2C','3S', '8S', '8D', 'TD']) == RESULTS['one pair']
    assert evaluate_hand(['5D','8C', '9S', 'JS', 'AC']) == RESULTS['nothing']
    assert evaluate_hand(['2C','5C', '7D', '8S', 'QH']) == RESULTS['nothing']
    assert evaluate_hand(['2D','9C', 'AS', 'AH', 'AC']) == RESULTS['three of a kind']
    assert evaluate_hand(['3D','6D', '7D', 'TD', 'QD']) == RESULTS['flush']
    assert evaluate_hand(['4D','6S', '9H', 'QH', 'QC']) == RESULTS['one pair']
    assert evaluate_hand(['3D','6D', '7H', 'QD', 'QS']) == RESULTS['one pair']
    assert evaluate_hand(['2H','2D', '4C', '4D', '4S']) == RESULTS['full house']
    assert evaluate_hand(['3C','3D', '3S', '9S', '9D']) == RESULTS['full house']

    
def get_data():
    page_req = requests.get('https://projecteuler.net/project/resources/p054_poker.txt')
    return page_req.text


def did1win(cards):
    player1 = evaluate_hand(cards[:5])
    player2 = evaluate_hand(cards[5:])

    if player1 > player2:
        return True
    if player1 < player2:
        return False

    # reversed to allow use of index
    values1 = card_values(cards[:5])[::-1]
    values2 = card_values(cards[5:])[::-1]

    for i in range(max(values1), 0, -1):
        if values1.index(i) < values2.index(i):
            return True
        if values1.index(i) > values2.index(i):
            return False
        if values1.count(i) == 2:
            if values1.index(i, values1.index(i)+1) < values2.index(i, values2.index(i)+1):
                return True
            if values1.index(i, values1.index(i)+1) > values2.index(i, values2.index(i)+1):
                return False
            
    return False


def test_did1win():
    assert did1win(['5H','5C', '6S', '7S', 'KD', '2C','3S', '8S', '8D', 'TD']) is False
    assert did1win(['5D','8C', '9S', 'JS', 'AC', '2C','5C', '7D', '8S', 'QH']) is True
    assert did1win(['2D','9C', 'AS', 'AH', 'AC', '3D','6D', '7D', 'TD', 'QD']) is False
    assert did1win(['4D','6S', '9H', 'QH', 'QC', '3D','6D', '7H', 'QD', 'QS']) is True
    assert did1win(['2H','2D', '4C', '4D', '4S', '3C','3D', '3S', '9S', '9D']) is True
    assert did1win(['3C','3D', '5S', '9S', '9D', '4H','4D', '3C', '5D', '5S']) is True
    assert did1win(['3C','3D', '5S', '6S', '6D', '4H','5D', '5C', '6D', '6S']) is False


poker_data = get_data()

wonby1 = 0
for line in poker_data.split('\n'):
    if len(line) == 0:
        continue
    cols = line.split()
    if did1win(cols):
        wonby1 += 1

print(wonby1)


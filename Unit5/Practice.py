class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def is_valid(self):
        self.suit_val = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.rank_val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if self.suit in self.suit_val and self.rank in self.rank_val:  # Check if the suit is valid
            return True
        
        return False 
    
    def get_value(self):

        while self.is_valid:
            if self.rank == "Ace":
                return 1
            elif self.rank == "Jack":
                return 11
            elif self.rank == "Queen":
                return 12
            elif self.rank == "King":
                return 13
            else:
                return self.rank


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

        def remove_card(self, card):
            self.cards.remove(card)


card = Card("Spades", "8")

"""
Create an instance of the class and store it in a variable 
named card2. The object should have suit "Clubs" and rank "Ace".
Then, call the method print_card() on your card.
"""
def print_card(self):
	print(f"{self.rank} of {self.suit}")

card2 = Card("Clubs", "Ace")
print_card(card2)


"""
Using the same Card class from Problem 2, 
update your code so that the suit of card is 
"Hearts" instead of "Clubs".

Use the print_card() method to verify that card was updated.

Expected Output: Ace of Hearts
"""

card2.suit = "Hearts"
print_card(card2)


"""
Update the Card class with a new method 
is_valid() that takes in no parameters except 
self. The method should return True if:

The suit is one of the following values: 
"Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: 
"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
"""

my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())


"""
Update the Card class with a new method get_value() that 
takes in no parameters except self.

The function returns the card's value depending on the card's rank:
"""

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())


"""
Add the following Hand class to 
your code that represents a player's hand of cards.

A new instance of Hand is always empty.
"""

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

# player1_hand = Hand()
# # cards = []

# player1_hand.add_card(card_one)
# # cards = [card_one]

# player1_hand.add_card(card_two)
# # cards = [card_one, card_two]

# player1_hand.remove_card(card_one)
# # cards = [card_two]


"""
Write a function sum_hand() that takes in 
an instance of Hand as a parameter and returns 
the summed value of all cards in the hand.
"""


def sum_hand(hand):
	total = 0
    
    for card in hand.cards:
        if not card.is_valid():
            return None
        total += card.get_value()
    return total



card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)
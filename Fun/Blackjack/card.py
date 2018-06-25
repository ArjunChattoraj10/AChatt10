"""Module providing a class for standard playing cards (no jokers).

Implementation adapted from chapter 18 of the course text,
_Think Python_, by Allen B. Downey.
"""


class Card(object):
    """Represents a standard playing card.

    Class variables:
        SUIT_NAMES: list of valid suit names:
            ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        NUM_SUITS: number of valid suits: 4
        RANK_NAMES: translation table of ranks to names:
            RANK_NAME[1] is 'Ace',
            RANK_NAME[2] is '2',
            ...
            RANK_NAME[13] is 'King',
        NUM_RANKS: number of valid ranks: 13


    Instance Attributes:
        suit: The suit of this particular card.
              The name of this suit is given by Card.SUIT_NAMES[suit].
              [int, in 0..Card.NUM_SUITS-1]
        rank: The rank of this particular card.
              The name of this rank is given by Card.RANK_NAMES[rank].
              [int, in 1..Card.NUM_RANKS]

    For example, if we execute c = Card(0, 12), Card.SUIT_NAMES[c.suit] is 'Clubs'
    and Card.RANK_NAMES[c.rank] is '12', so this card is the Queen of Clubs.
    """

    # class variable definitions.
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    NUM_SUITS  = len(SUIT_NAMES)

    # Starts at None so that we can treat RANK_NAMES as a translation table:
    # RANK_NAME[1] is 'Ace', RANK_NAME[13] is 'King', etc.
    RANK_NAMES = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']
    NUM_RANKS  = 13

    def __init__(self, s, r):
        """Initializer: A new Card with suit encoding s and rank encoding r.

        Example: if we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since Card.SUIT_NAMES[c.suit] is 'Clubs' and
        Card.RANK_NAMES[c.rank] is 'Queen'.

        Preconditions: s in 0..Card.NUM_SUITS-1 (inclusive) and
        r in 1..Card.NUM_RANKS (inclusive)"""
        self.suit = s
        self.rank = r

    def __str__(self):
        """Returns: Readable string representation of this card.
        Example: '2 of Hearts'"""
        return Card.RANK_NAMES[self.rank] + ' of ' + Card.SUIT_NAMES[self.suit]

    def __repr__(self):
        """Returns: Unambiguous string representation of this card.
        Example: 'Card(3,2): 2 of Spades'"""
        return 'Card('+ str(self.suit) + ',' + str(self.rank) + "): " +str(self)

    # We've included __eq__ so that we can do testing of equality of cards and
    # lists of cards.
    def __eq__(self, other):
        """Returns: True or False depending on whether self has the same suit
        and rank as other.
        Precondition: other is a Card."""
        return (isinstance(other,Card) and
                (self.suit, self.rank) == (other.suit, other.rank))

    def __ne__(self, other):
        """Returns: True or False depending on whether self does not have
        the same suit or the same rank as other.
        Precondition: other is a Card."""
        return not self.__eq__(other)


def full_deck():
    """Returns: list of the standard 52 cards"""
    output = []  # list of cards so far to be returned
    for suit in range(Card.NUM_SUITS):
        for rank in range(1,Card.NUM_RANKS+1):  # skip the None value
            output.append(Card(suit,rank))
    return output


def print_cards(clist):
    """Print cards in list clist, using human-readable format rather than
    what the standard for __repr__ is. Does not return anything.

    Example printout:
    Queen of Clubs
    2 of Spades

    Precondition: clist is a list of Cards, possibly empty."""
    for c in clist:
        print(str(c))
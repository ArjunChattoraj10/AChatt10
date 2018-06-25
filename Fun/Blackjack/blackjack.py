"""Module for a very simple version of the game Blackjack"""
import card, random


class Blackjack(object):
    """Represents the state of a game of blackjack with one player.

    Instance Attributes:
        playerHand: list of the Cards held by the player [list of Cards]
        dealerHand: list of the Cards held by the dealer [list of Cards]
        deck: list of the remaining Cards to draw from   [list of Cards]

    The deck attribute is assumed to hold enough Cards for the game
    to be able to run to completion (i.e., the deck will not run out
    of cards for the player or dealer to draw from)."""

    def __init__(self,d):
        """Initializer: a new Blackjack game with the two hands initialized.

        The player's hand playerHand will be the first two cards in d.
        The dealer's hand dealerHand will be the third card in d.
        These three cards are removed from d, and then this Blackjack instance's
        deck will be resultant d (with those three cards removed)

        We have d as a parameter because we allow the caller, such as a casino,
        to "stack the deck" (choose the arrangement of the cards, insert
        extra cards, etc.) to its advantage!

        Precondition: deck is a list of Cards.  It contains at least
        three Cards (more is preferable)."""
        
        self.playerHand = [d.pop(0),d.pop(0)]
        self.dealerHand = [d.pop(0)]
        self.deck = d
        

    def __str__(self):
        """Returns: string describing <player's score> and <dealer's score>

        Example returned string: "player: 12; dealer: 20"

        Here, we are assuming that all that matters is the score, which is true
        if aces are always 11. If one changes the specifications so that what
        Cards each player is holding matters, then the specification and output
        of this method should change accordingly.
        """
        
        return "player: " + str(self.playerScore()) + "; dealer: " + str(self.dealerScore())
        # REPLACE WITH YOUR IMPLEMENTATION

    def dealerScore(self):
        """Returns: score for the dealer."""
        return _score(self.dealerHand)
        # REPLACE WITH YOUR IMPLEMENTATION

    def playerScore(self):
        """Returns: score for the player."""
        return _score(self.playerHand)

    def playerBust(self):
        """Returns: True if player has gone bust (score is over 21),
        and False otherwise"""
        
        if self.playerScore() > 21:
            return True
        else:
            return False
        

    def dealerBust(self):
        """Returns: True if dealer has gone bust (score is over 21),
        and False otherwise"""
        if self.dealerScore() > 21:
            return True
        else:
            return False


# HELPER FUNCTION.
def _score(clist):
    """Returns: simplified-blackjack score for clist

    In our version of blackjack, aces always count as 11 points and face cards
    count as 10 points.

    Example: input: [2 of Hearts, Ace of spades], output: 13
    Example: input: [King of Diamonds, 3 of Clubs], output 13

    Precondition: clist is a list of Cards"""
    s = 0  # score to return
    for c in clist:
        if c.rank >= 11:  # c is a face card
            s = s + 10
        elif c.rank == 1:  # c is an ace
            s = s + 11
        else:
            s = s + c.rank
    return s


def play_a_game():
    """Create and play a new blackjack game.

    This function provides a text-based interface for blackjack.
    It will continue to run until the end of the game."""

    # Create a new shuffled full deck
    deck = card.full_deck()
    random.shuffle(deck)

    # Start a new game. Player gets two cards; dealer gets one
    game = Blackjack(deck)

    # Tell player the scoring rules
    print('Welcome to CS 1110 Blackjack.')
    print('Rules: Face cards are 10 points. Aces are 11 points.')
    print('       All other cards are at face value.')
    print()

    # Show initial deal
    print('Your hand: ')
    card.print_cards(game.playerHand)
    print()
    print('Dealer\'s hand: ')
    card.print_cards(game.dealerHand)
    print()

    # While player has not busted out, ask if player wants to draw
    player_halted = False  # True if player wants to halt, False otherwise
    while not game.playerBust() and not player_halted:
        # ri: input received from player
        ri = _prompt_player('Type h for new card, s to stop: ', ['h', 's'])

        player_halted = (ri == 's')
        if (not player_halted):
            game.playerHand.append(game.deck.pop(0))
            print("You drew the " + str(game.playerHand[-1]))
            print()

    if game.playerBust():
        print("You went bust, dealer wins.")
    else:
        _dealer_turn(game)

    print()
    print("The final scores were " + str(game))


def _prompt_player(prompt,valid):
    """Returns: the choice of a player for a given prompt.

    This is a helper function for play_a_game().  It asks
    the user a question, and waits for a response.  It checks
    if the response is valid against a list of acceptable
    answers.  If it is not valid, it asks the question again.
    Otherwise, it returns the player's answer.

    This function has been factored out of play_a_game()
    so that play_a_game() is more compact and readable.

    Precondition: prompt is a string. valid is a list of
    strings representing the valid responses."""
    # Ask the question for the first time.
    # ri: input received from player
    ri = input(prompt)

    # Continue to ask while the response is not valid.
    while not (ri in valid):
        print('Invalid response.  Answer must be one of '+str(valid))
        print()
        ri = input(prompt)

    return(ri)


def _dealer_turn(game):
    """Performs the dealer's turn, printing out the result.

    The function uses standard BlackJack rules: the dealer
    stands above 17, but hits otherwise.

    This function has been factored out of play_a_game()
    so that play_a_game() is more compact and readable.
"""
    # Dealer draws until at 17 or above or goes bust
    while game.dealerScore() < 17 and not game.dealerBust():
        game.dealerHand.append(game.deck.pop(0))
        print("Dealer drew the " + str(game.dealerHand[-1]))

    print
    if (game.dealerBust()):
        print("Dealer went bust, you win!")
    elif (game.dealerScore() > game.playerScore()):
        print("Dealer outscored you, dealer wins.")
    elif (game.dealerScore() < game.playerScore()):
        print("You outscored dealer, you win!")
    else:
        print("The game was a tie.")

# Script code
if __name__ == '__main__':
    play_a_game()

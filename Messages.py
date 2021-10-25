
class Messages:

    # General:
    WRONG_MESS = """Wrong value, try again: """

    # Game:
    START_MESS = "Welcome To Poker Texas Holdem!"
    PLAYERS_MESS = "Please enter how many players (between 2 and 10): "
    NAME_OF_PLAYER = "Enter the name of player number {0}: "
    BALANCE = "Enter balance (greater than 0): "
    PLAY_AGAIN = "Would you like to play again? Y = yes, N = no"
    BYE = "See you!"
    SAME_PLAYERS = "Stick with the same players?"

    # Player:
    ITS_YOUR_TURN = """================
    {0}, It's your turn!
    Your Balance: {1}$
    Already Paid This Round: {2}$
    Your Cards:"""
    CALL_OR_FOLD = "what to do next? C = call, F = fold: "
    CALL_OR_RAISE_OR_FOLD = "what to do next? C = call, R = raise, F = fold: "
    RAISE_BY = "By how much money to raise? "
    DONT_HAVE_THAT_MUCH = "You dont have that much money in your balance, try again: "

    # Table:
    OPEN_CARDS = """================
THE OPEN CARDS ARE: """
    MONEY_IN_STACK = "Right now the amount of money collected:"

    # PokerRules:
    WINNER = """Congratulations: """
    ONE_WINNER = "Your hand: {0}, you won {1}$!"
    COUPLE_WINNERS = "You had the same hands: {0}, each one won {1}$!"
from Card import Card
from CardStack import CardStack
from Messages import Messages
from MoneyStack import MoneyStack


class Player:
    """
    A poker player class.
    """

    def __init__(self, name: str, money: int):
        """
        A constructor for a player.
        :param name: The name of the player
        :param balance: The amount of money the player is enteting the game with.
        """
        self.cards_stack = CardStack()
        self.name = name
        self.balance = MoneyStack(money)
        self.active = True
        self.round_money = MoneyStack(0)
        self.already_raised = False

    def get_name(self) -> str:
        return self.name

    def get_balance(self) -> int:
        return self.balance.get_money()

    def get_round_money(self) -> int:
        return self.round_money.get_money()

    def get_already_raised(self):
        """
        Check if the player already used "raise" operation in the given round.
        :return: A boolean value.
        """
        return self.already_raised

    def set_already_raised(self, expr: bool):
        """
        A setter for the raise state.
        :param expr: A boolean value.
        :return: None.
        """
        self.already_raised = expr

    def is_active(self) -> bool:
        """
        Check if the player is in a "fold" state.
        :return: A boolen value.
        """
        return self.active

    def play_round(self, money_each_player: int) -> int:
        """
        Play a single round.
        :param money_each_player: The amount of money each player that want to play has to pay this round.
        :return: How much the player paid over the money each player pays this round.
        """
        # If all of the balance already been paid.
        if self.round_money == self.balance:
            self.do_call(money_each_player)
            return 0
        print(Messages.ITS_YOUR_TURN.format(self.name, self.balance, self.round_money))
        print(self.cards_stack)
        next_move = self.next_move(money_each_player)
        raised_by = 0
        if next_move == "C":
            self.do_call(money_each_player)
        elif next_move == "R":
            raised_by = self.do_raise(money_each_player)
        elif next_move == "F":
            self.do_fold()
        return raised_by

    def next_move(self, money_each_player: int) -> str:
        """
        Checks what the next move that the player want to take.
        :param money_each_player: The amount of money each player that want to play has to pay this round.
        :return: The move: C = call, R = raise, F = fold.
        """
        next_move = None

        # If money is raised beyond balance:
        if self.balance.get_money() - (money_each_player - self.round_money.get_money()) <= 0 or self.already_raised:
            next_move = input(Messages.CALL_OR_FOLD.format(self.name))
            while next_move != "C" and next_move != "F":
                next_move = input(Messages.WRONG_MESS)

        # Free to do everything
        else:
            next_move = input(Messages.CALL_OR_RAISE_OR_FOLD.format(self.name))
            while next_move != "C" and next_move != "R" and next_move != "F":
                next_move = input(Messages.WRONG_MESS)
        return next_move

    def do_call(self, money_each_player: int) -> None:
        """
        A call move by the player.
        :param money_each_player: The amount of money each player that want to play has to pay this round.
        :return: None.
        """
        delta = money_each_player - self.round_money.get_money()  # How much more need to pay
        if self.balance.get_money() > delta:
            self.balance.pay_money(delta)
            self.round_money.add_money(delta)
        else:
            self.round_money.add_money(self.balance.pay_all_money())

    def do_fold(self) -> None:
        """
        A fold move by the player.
        :return: None.
        """
        self.active = False

    def do_raise(self, money_each_player: int) -> int:
        """
        A raise move by the player.
        :param money_each_player: The amount of money each player that want to play has to pay this round.
        :return: How much the player raised by.
        """
        can_raise_by = self.balance.get_money() - (money_each_player - self.round_money.get_money())
        raise_by = input(Messages.RAISE_BY)
        while not raise_by.isdigit() or int(raise_by) > can_raise_by:
            if not raise_by.isdigit():
                print(Messages.WRONG_MESS)
                raise_by = input(Messages.RAISE_BY)
            else:
                print(Messages.DONT_HAVE_THAT_MUCH)
                raise_by = input(Messages.RAISE_BY)
        delta = (money_each_player - self.round_money.get_money()) + int(raise_by)
        self.round_money.add_money(self.balance.pay_money(delta))
        self.already_raised = True
        return int(raise_by)

    def pay_round_money(self) -> int:
        """
        Pay the money the player spent this round.
        :return: The amount of money.
        """
        return self.round_money.pay_all_money()

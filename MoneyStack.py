
class MoneyStack:
    """
    Money stack.
    """

    # CLI Messages:
    MONEY_IN_STACK = "Right now the amount of money collected: {0}"

    def __init__(self):
        """
        A constructor for a stack of money.
        """
        self.money = 0

    def get_money(self) -> int:
        """
        A getter for the money in the stack.
        :return: The money in the stack.
        """
        return self.money

    def add_money(self, money: int) -> None:
        """
        Add money to the stack.
        :param money:
        :return:
        """
        self.money += money

    def give_money(self) -> None:
        """
        Take money from the stack.
        :return:
        """
        money = self.money
        self.money = 0
        return money

    def print_money(self) -> None:
        """
        Print the amount of money in the stack.
        :return: None.
        """
        print(MoneyStack.MONEY_IN_STACK.format(self.money))
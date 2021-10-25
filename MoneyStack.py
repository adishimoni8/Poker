
class MoneyStack:
    """
    Money stack.
    """

    def __init__(self, money=0):
        """
        A constructor for a stack of money.
        """
        self.money = money

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

    def pay_money(self, money) -> int:
        """
        Take money from the stack.
        :return:
        """
        self.money -= money
        return money

    def pay_all_money(self) -> int:
        money = self.money
        self.money = 0
        return money

    def __str__(self):
        return str(self.money) + "$"



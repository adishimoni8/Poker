

class HandsChecker(object):
    """
    A static class (Helper for the PokerRules class) that has method which takes a single player's cards with stack
    cards, and check poker hands upon in. All of the method's names are self explanatory.
    """

    @staticmethod
    def check_royal_flush(player):
        lst = [[0 for i in range(13)] for j in range(4)]
        for card in player.cards_stack.get_cards():
            lst[card.get_kind().value][card.get_num().value] += 1
        lst_of_kinds = [True, True, True, True]
        for i in range(4):
            for j in range(8, 13):
                if lst[i][j] == 0:
                    lst_of_kinds[i] = False
                    break
        return any(lst_of_kinds)

    @staticmethod
    def check_straight_flush(player):
        return HandsChecker.check_straight(player) and HandsChecker.check_flush(player)

    @staticmethod
    def check_four_of_a_kind(player):
        lst = HandsChecker.get_numbers(player)
        for i in range(len(lst)):
            if lst[i] >= 4:
                return True
        return False

    @staticmethod
    def check_full_house(player):
        lst = HandsChecker.get_numbers(player)
        three = 0
        two = 0
        for i in range(len(lst)):
            if lst[i] >= 2:
                two += 1
            if lst[i] >=3:
                three += 1
        return (three >= 2) or (three == 1 and two > three)

    @staticmethod
    def check_flush(player):
        lst = HandsChecker.get_kinds(player)
        for i in range(len(lst)):
            if lst[i] >= 5:
                return True
        return False

    @staticmethod
    def check_straight(player):
        lst = HandsChecker.get_numbers(player)
        val = 0
        for i in range(len(lst)):
            if lst[i] > 0:
                val += 1
            else:
                val = 0
            if val == 5:
                return True
        return False

    @staticmethod
    def check_three_of_a_kind(player):
        lst = HandsChecker.get_numbers(player)
        for i in range(len(lst)):
            if lst[i] >= 3:
                return True
        return False

    @staticmethod
    def check_two_pair(player):
        lst = HandsChecker.get_numbers(player)
        val = 0
        for i in range(len(lst)):
            if lst[i] >= 2:
                val += 1
        return val >= 2

    @staticmethod
    def check_pair(player):
        lst = HandsChecker.get_numbers(player)
        for i in range(len(lst)):
            if lst[i] >= 2:
                return True
        return False

    @staticmethod
    def get_numbers(player):
        lst = [0 for i in range(13)]
        for card in player.cards_stack.get_cards():
            lst[card.get_num().value] += 1
        return lst

    @staticmethod
    def get_kinds(player):
        lst = [0 for i in range(4)]
        for card in player.cards_stack.get_cards():
            lst[card.get_kind().value] += 1
        return lst

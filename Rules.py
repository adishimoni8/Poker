
class Rules:

    def __init__(self, players_cards, stack_cards) -> None:
        self.players_cards = players_cards
        self.stack_cards = stack_cards
        self.types_and_grades = [[self.check_royal_flush, 10],
                                 [self.check_straight_flush, 9],
                                 [self.check_four_of_a_kind, 8],
                                 [self.check_full_house, 7],
                                 [self.check_flush, 6],
                                 [self.check_straight, 5],
                                 [self.check_three_of_a_kind, 4],
                                 [self.check_two_pair, 3],
                                 [self.check_pair, 2],
                                 [self.check_high_card, 1]]

    def find_winner(self) -> int:
        pass

    def check_royal_flush(self):
        pass

    def check_straight_flush(self):
        pass

    def check_four_of_a_kind(self):
        pass

    def check_full_house(self):
        pass

    def check_flush(self):
        pass

    def check_straight(self):
        pass

    def check_three_of_a_kind(self):
        pass

    def check_two_pair(self):
        pass

    def check_pair(self):
        pass

    def check_high_card(self):
        pass







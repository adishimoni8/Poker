from Table import Table


class Game:
    """A Game class"""

    def __init__(self) -> None:
        """
        Initialize game object.
        """
        self.keep_play = True

    def start(self) -> None:
        """
        start a poker game.
        :return: None.
        """
        while self.keep_play: # While keep play is true keep playing.
            num_of_players = input("How Many Players? ")
            while not num_of_players.isdigit():
                num_of_players = input("Wrong value! How Many Players? ")
            num_of_players = int(num_of_players)
            table = Table(num_of_players)
            table.play_game()
            keep_play = input("Keep playing? Y for yes, N for no")
            while keep_play != 'Y' and keep_play != 'N':
                keep_play = input("Keep playing? Y for yes, N for no")
            if keep_play == 'N':
                self.keep_play = False


if __name__ == '__main__':
    game = Game()
    game.start()

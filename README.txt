POKER TEXAS HOLDEM
==================
made by: Adi Shimoni

FILES CONTAINED
==================
Game.py - The file that runs the game.
Table.py - A class of a table of which the game runs on.
Player.py - A class of a player.
Card.py - A class of a single card.
CardStack.py - A stack of cards.
Deck.py - A class of deck of cards with basic methods upon it.
Dealer - A class of a dealer of cards.
MoneyStack.py - A stack of money sits on the table.
Rules.py - A static class contains the set of rules of poker (how many rounds, and decides the winner).
HandChecker - A helper static class for the Rules.py, takes a single player and the open cards, and check if the player has a given hand by poker rules.
README - this file.

EXTRA INFORMATION
==================
- I decided that each player handles it's own money and not use stack, because the money logic is pretty complex for a simple stack. Although, If I would like to enhance the program, firsly I will take care for the money stack to be more complex and handle the kind of logic I used for the player.

- In order for a round to be in the correct order, in the table class I added some little comments "# Helper for the round to end correctly." that show where this logic is handled.

- To test that the winning logic is handled correctly, I added a simple commented test in the main function, you can enhance it to check it more carefully if needed.

- I think I followed the exact rules of poker, but I didn't play it much before, so excuse me if there are some incorrectness in the rules.

Thank you, and enjoy!

POKER
=====
made by: Adi Shimoni

FILES
=====
Game.py - The file that runs the game.
Table.py - A class of a table of which the game runs on.
Player.py - A class of a player.
Deck.py - A class of deck of cards with basic methods upon it
Rules.py - The rules of Poker to decide the winner

NOTES
=====
- This is an overall skeleton of a poker "texas holdem" style game, built in an OOP style with classes contacting
  with each other.
- Rules class is not entirely complete - the idea was to take the cards of all of the active player with the
  open cards in the deck and to grade the highest hand using the rules of poker. The class is skeletoned in
  a way that each possible hand has a matching indicating method (to decide whether a given player has this hand)
  the method find winner supposed to iterate over all of the active player and map each with the given function in
  a descending order (by the hand grade).
- The game still contains bugs and not fully tested, among them:
     - checking for huge number of players.
     - deciding who the winner is.
     - saving the information from the last game to continue playing with the last game's balances.
     - sometimes need to check for correctnesses of values given by the user in the CLI - it can sometimes crash
       and terminate the program.

Thank you, and enjoy!




from game.card import Card
from game.player import Player


class Director:
    """
A class named Director will control the flow of the game. It will have a primary method, self.start_game(), to start the game, initialize a player and first card, and control the main game loop. The loop will display the current card and get the players guess. A new card will be generated and compared to players guess and points updated. If the player still has points, the player will be asked if they want to play again. The loop will repeat as long as the player wants to keep playing and their points are above zero.

    """

    def __init__(self):
        """Constructs a new Director. Initialize user and current card.
        """
        self.player = Player()
        self.current_card = Card()
        self.next_card = None


    def start_game(self):
        """Starts the game by running the main game loop."""
        player = self.player
        while player.current_points > 0 and player.keep_playing():
            self.display_card()
            self.get_players_guess()
            self.generate_new_card()
            self.update_points()
            self.play_again()


    def display_card(self):
        """ Display the current card. """
        print()
        print(f"The current card is: {self.current_card.value}.")


    def get_players_guess(self):
        """Ask the player if next card will be higher or lower."""
        self.player.current_guess = input("Higher or lower? [h/l] ")


    def generate_new_card(self):
        """ Generate next card and display. """
        self.next_card = Card()
        print(f"Next card was: {self.next_card.value}")


    def update_points(self):
        """ Compare next card with players guess and update points. """

        current_value = self.current_card.value
        next_value = self.next_card.value
        player = self.player

        if player.guessed_higher() and next_value > current_value:
            player.earns(100)
        elif player.guessed_lower() and next_value < current_value:
            player.earns(100)
        else:
            player.loses(75)
        
        print(f"Your score is: {player.current_points}")
        self.current_card = self.next_card


    def play_again(self):
        """ If the player has more than zero points, ask if they want to play again. """
        player = self.player
        if player.current_points > 0:
            player.play_again = input("Play again? [y/n] ")


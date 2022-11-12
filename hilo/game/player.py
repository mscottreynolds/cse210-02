class Player:
    """
A class named Player will keep track of the players current points and current guess. It will have two attributes, self.current_points, which will be initialized with 300, self.current_guess which will store the users current guess, and self.play_again which will be initialized with 'y' to indicate the users desire to keep playing.
    """

    def __init__(self):
        """Constructs a new instance of Player, initialize starting points, current guess, and play again flag.
        """

        self.current_points = 300
        self.current_guess = None
        self.play_again = 'y'

    def earns(self, points):
        """ Player earns specified points, add to specified points to current_points.
        Return new value."""
        self.current_points += points
        return self.current_points


    def loses(self, points):
        """ Player loses specified points. Subtract points and return new value. """
        self.current_points -= points
        return self.current_points
    

    def keep_playing(self):
        """ Returns true if the player wants to keep playing. i.e. play_again == 'y' """
        return self.play_again.upper()[:1] == 'Y'


    def guessed_higher(self):
        """Return True if the player guessed higher. """
        return self.current_guess.upper()[:1] == 'H'

    
    def guessed_lower(self):
        """ Return true if the player guessed lower. """
        return self.current_guess.upper()[:1] == 'L'
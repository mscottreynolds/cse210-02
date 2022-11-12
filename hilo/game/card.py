import random

class Card:
    """A class named Card will be used to represent a card drawn by the director. It will have one attribute, self.value, which will be initialized with a random value from 1 to 13.

    Attributes:
        value (int): The value of the card, random from 1 to 13.
    """
# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card and initalize value.
        """
        self.value = random.randint(1, 13)

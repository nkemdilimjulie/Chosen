
from abc import ABC, abstractmethod


class Die(ABC):
    ''' same as die.py: The file "dice.py" contains the derived classes - D4, D6, D8, D10 
        which implement the "roll abstractmethod of this class" 
        please, see dice_game file'''
    def __init__(self) -> None:
        self.face: int  # Here we are just declaring that the face will be an integer
        self.roll()

    @abstractmethod
    def roll(self) -> None: ...

    def __str__(self) -> str:
        # String representation # Works with print()
        return f"{self.face}"

    def __repr__(self) -> str:
        #  Get object representation # Works without print()
        return f"{self.face}"
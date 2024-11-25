from random import randint

from die_abstract_parent import Die


class D4(Die):
    ''' randomly picks one number within the range of 1-4 as a face of a die '''
    def roll(self):
        self.face = randint(1, 4)


class D6(Die):
    ''' randomly picks one number within the range of 1-6 as a face of a die '''
    def roll(self):
        self.face = randint(1, 6)


class D8(Die):
    ''' randomly picks one number within the range of 1-6 as a face of a die '''
    def roll(self):
        self.face = randint(1, 8)


class D10(Die):
    ''' randomly picks one number within the range of 1-10 as a face of a die '''
    def roll(self):
        self.face = randint(1, 10)

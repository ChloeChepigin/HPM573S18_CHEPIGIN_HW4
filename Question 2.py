from enum import Enum
import numpy as np

class CoinSide(Enum):
    """side the coin lands on"""
    HEADS = 1
    TAILS = 0

class Game:
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._CoinSide = CoinSide.HEADS
        self._countTails = 0
        self._countWIN = 0
        self._totalFlips = 20
        self._flipNumber = 1

    def nextFlip(self):
        if self._CoinSide == CoinSide.HEADS:
            if self._rnd.sample() > 0.6:
                self._CoinSide = CoinSide.HEADS
            elif self._rnd.sample() < 0.6:
                self._CoinSide = CoinSide.TAILS
                self._countTails = 1
        elif self._CoinSide == CoinSide.TAILS:
            if self._rnd.sample() < 0.6:
                self._CoinSide = CoinSide.TAILS
                self._countTails += 1
            if self._rnd.sample() > 0.6:
                self._CoinSide = CoinSide.HEADS
                if self._countTails >= 2:
                    self._countWIN += 1
                self._countTails = 0

        self._flipNumber += 1

    def play(self):
        for i in range(1, self._totalFlips+1):
            self._rnd = np.random
            self._seed = (self._id * self._flipNumber)
            self.nextFlip()

    def get_reward(self):
        self.play()
        self._reward = -250 + self._countWIN*100
        return self._reward

class Cohort:
    def __init__(self, id, num_realization):    #id is the id of the cohort
        self._players = [] #number of trials
        n = 1   #counter

        while n <= num_realization:
            player=Game(id=id*num_realization+n)
            self._players.append(player)
            n += 1

    def simulate(self):
        gameReward = []
        for player in self._players:
            gameReward.append(player.get_reward())
        return sum(gameReward)/len(gameReward)

NUM_REALIZATION = 1000
Trial=Cohort(id=1, num_realization=NUM_REALIZATION)
print(Trial.simulate())
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def fabric_coat(self):
        pass

    @abstractmethod
    def fabric_suit(self):
        pass

class Coat(Clothes):
    def fabric_coat(self, size):
        x =  size / 6.5 + 0.5
        return x
    def fabric_suit(self):
        pass

class Suit(Clothes):
    def fabric_coat(self):
        pass
    def fabric_suit(self, length):
        y = 2 * length + 0.3
        return y

coat_1 = Coat()
suit_1 = Suit()
print(coat_1.fabric_coat(10))
print(suit_1.fabric_suit(5))
from abc import ABC, abstractmethod

class StateCard(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

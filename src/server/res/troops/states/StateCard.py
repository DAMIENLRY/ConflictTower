from abc import ABC, abstractmethod

class StateCard(ABC):
    
    @abstractmethod
    def handle_request(self):
        pass
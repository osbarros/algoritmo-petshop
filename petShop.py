from abc import ABC, abstractmethod


class PetShop(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calcula_valor(self):
        pass



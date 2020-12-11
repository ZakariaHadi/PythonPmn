import Point
from abc import abstractmethod


class Forme:
    def __init__(self,x,y):
        self.origine = Point(x,y)

    @abstractmethod
    def calculerDistance(self):
        pass

    @abstractmethod
    def calculerPerimetre(self):
        pass

    @abstractmethod
    def afficher(self):
        pass
from abc import   ABC


class Food(ABC):
    def __init__(self, qnty):
        self.quantity = qnty


class Vegetable(Food):
    pass


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass
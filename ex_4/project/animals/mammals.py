from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def weight_increment(self):
        return 0.10


class Dog(Mammal):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def allowed_food(self):
        return [Meat, Vegetable]

    @property
    def weight_increment(self):
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

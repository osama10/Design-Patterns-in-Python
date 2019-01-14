"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.

This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).

*Where is the pattern used practically?
*References:
https://sourcemaking.com/design_patterns/builder
*TL;DR80
Decouples the creation of a complex object and its representation.
"""

#Interface Builder


class Builder(object):

    def build(self):
        raise NotImplementedError


class KidsMealBuilder(Builder):

    _main_meal = ""
    _side_meal = ""
    _drink = ""
    _toy = ""

    def build_main_meal(self, main_meal):
        self._main_meal = main_meal
        return self

    def build_side_meal(self, side_meal):
        self._side_meal = side_meal
        return self

    def build_drink(self, drink):
        self._drink = drink
        return self

    def build_toy(self, toy):
        self._toy = toy
        return self

    def build(self):
        return KidsMeal(self._main_meal, self._side_meal, self._drink, self._toy)


class Cashier(object):

    _order = []

    def __init__(self, builder, order):
        self._builder = builder
        self._order = order

    def construct(self):
        return self._builder.build_main_meal(self._order[0]).\
            build_side_meal(self._order[1]).\
            build_drink(self._order[2]).\
            build_toy(self._order[3]).\
            build()


# Concrete Buildings
class KidsMeal(object):

    def __init__(self, main_meal, side_meal, drink, toy):
        self._main_meal = main_meal
        self._side_meal = side_meal
        self._drink = drink
        self._toy = toy

    def __repr__(self):
        return "Here is your meal : Main Meal | {} - Side  | {}  Drink | {} Toy | {} ".format(self._main_meal, self._side_meal, self._drink, self._toy)


def main():
    builder = KidsMealBuilder()
    cashier = Cashier(builder=builder, order= ["Big Zing", "Fries", "Sting", "Car"])
    kids_meal = cashier.construct()
    print(kids_meal)


if __name__ == "__main__":
    main()



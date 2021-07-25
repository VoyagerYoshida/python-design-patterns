from abstract_factory import AbstractPizzaFactory, Dough, Source, Topping


# ConcreteFactory
class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        print("[ PizzaFactoryA ] Constructor")

    # createproduct
    def add_dough(self, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_dough()")
        return WheatDough(amount)

    # createproduct
    def add_source(self, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_source()")
        return TomatoSource(amount)

    # createproduct
    def add_topping(self, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_topping()")
        return CoanTopping(amount)


# ConcreteProducts
class WheatDough(Dough):
    def check(self):
        print(" -> [ WheatDough ] amount: {}".format(self.amount))


class TomatoSource(Source):
    def check(self):
        print(" -> [ TomatoSource ] amount: {}".format(self.amount))


class CoanTopping(Topping):
    def check(self):
        print(" -> [ CoanTopping ] amount: {}".format(self.amount))

from abstract_factory import AbstractPizzaFactory, Dough, Source, Topping


# ConcreteFactory
class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        print("[ PizzaFactoryB ] Constructor")

    # createproduct
    def add_dough(self, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_dough()")
        return RiceFlourDough(amount)

    # createproduct
    def add_source(self, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_source()")
        return BasilSource(amount)

    # createproduct
    def add_topping(self, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_topping()")
        return CheeseTopping(amount)


# ConcreteProducts
class RiceFlourDough(Dough):
    def check(self):
        print(" -> [ RiceFlourDough ] amount: {}".format(self.amount))


class BasilSource(Source):
    def check(self):
        print(" -> [ BasilSource ] amount: {}".format(self.amount))

class CheeseTopping(Topping):
    def check(self):
        print(" -> [ CheeseTopping ] amount: {}".format(self.amount))

# Concrete Factory
class PizzaFactoryA:
    def __init__(self):
        print(" -> [ PizzaFactoryA ] Constructor")

    def check_pizza(self):
        print("[ PizzaFactoryA ] Method check_pizza()")
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod
    def add_dough(Class, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_dough()")
        return Class.WheatDough(amount)

    @classmethod
    def add_source(Class, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_source()")
        return Class.TomatoSource(amount)

    @classmethod
    def add_topping(Class, amount=1):
        print(" -> [ PizzaFactoryA ] Method add_topping()")
        return Class.CoanTopping(amount)

    class WheatDough:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryA / WheatDough ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryA / WheatDough ] amount: {}".format(self.amount))

    class TomatoSource:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryA / TomatoSource ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryA / TomatoSource ] amount: {}".format(self.amount))

    class CoanTopping:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryA / CoanTopping ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryA / CoanTopping ] amount: {}".format(self.amount))

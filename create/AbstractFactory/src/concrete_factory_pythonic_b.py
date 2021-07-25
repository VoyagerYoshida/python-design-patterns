# Concrete Factory
class PizzaFactoryB:
    def __init__(self):
        print(" -> [ PizzaFactoryB ] Constructor")

    def check_pizza(self):
        print("[ PizzaFactoryB ] Method check_pizza()")
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod
    def add_dough(Class, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_dough()")
        return Class.RiceFlourDough(amount)

    @classmethod
    def add_source(Class, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_source()")
        return Class.BasilSource(amount)

    @classmethod
    def add_topping(Class, amount=1):
        print(" -> [ PizzaFactoryB ] Method add_topping()")
        return Class.CheeseTopping(amount)

    class RiceFlourDough:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryB / RiceFlourDough ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryB / RiceFlourDough ] amount: {}".format(self.amount))

    class BasilSource:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryB / BasilSource ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryB / BasilSource ] amount: {}".format(self.amount))

    class CheeseTopping:
        def __init__(self, amount=1):
            print("     -> [ PizzaFactoryB / CheeseTopping ] Constructor")
            self.amount = amount

        def check(self):
            print(" -> [ PizzaFactoryB / CheeseTopping ] amount: {}".format(self.amount))

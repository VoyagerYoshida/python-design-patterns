# AbstractFactory
class AbstractPizzaFactory:
    def __init__(self, pizza_factory, amount_str="normal"):
        print(" -> ( AbstractPizzaFactory ) Constructor")
        self.amount_dict = {"high": 1.2, "normal": 1.0, "low": 0.8}
        self.factory = pizza_factory

    def make_pizza(self, amount_str):
        print("( AbstractPizzaFactory ) Method make_pizza()")
        amount = self.amount_dict[amount_str]
        self.pizza_materials = []
        self.pizza_materials.append(self.factory.add_dough(amount))
        self.pizza_materials.append(self.factory.add_source(amount))
        self.pizza_materials.append(self.factory.add_topping(amount))

    def check_pizza(self):
        print("( AbstractPizzaFactory ) Method check_pizza()")
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    # createproduct
    def add_dough(self, amount=1):
        pass

    # createproduct
    def add_source(self, amount=1):
        pass

    # createproduct
    def add_topping(self, amount=1):
        pass


# AbstractProducts
class Dough:
    def __init__(self, amount):
        print("     -> ( Dough ) Constructor")
        self.amount = amount

    def check(self):
        pass


class Source:
    def __init__(self, amount):
        print("     -> ( Source ) Constructor")
        self.amount = amount

    def check(self):
        pass


class Topping:
    def __init__(self, amount):
        print("     -> ( Topping ) Constructor")
        self.amount = amount

    def check(self):
        pass

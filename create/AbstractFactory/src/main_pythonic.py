from concrete_factory_pythonic_a import PizzaFactoryA
from concrete_factory_pythonic_b import PizzaFactoryB


def make_pizza(PizzaFactory, amount_str):
    print("Func make_pizza()")
    pizza = PizzaFactory()

    amount_dict = {"high": 1.2, "normal": 1.0, "low": 0.8}
    amount = amount_dict[amount_str]

    pizza.pizza_materials = []
    pizza.pizza_materials.append(pizza.add_dough(amount))
    pizza.pizza_materials.append(pizza.add_source(amount))
    pizza.pizza_materials.append(pizza.add_topping(amount))

    return pizza


def main():
    print("--- Pizza 1 ---")
    factory_a = make_pizza(PizzaFactoryA, "high")
    print("---------------")
    factory_a.check_pizza()

    print("--- Pizza 2 ---")
    factory_b = make_pizza(PizzaFactoryB, "normal")
    print("---------------")
    factory_b.check_pizza()


if __name__ == "__main__":
    main()

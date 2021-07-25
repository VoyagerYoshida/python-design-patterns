from abstract_factory import AbstractPizzaFactory
from concrete_factory_a import PizzaFactoryA
from concrete_factory_b import PizzaFactoryB


def main():
    print("--- Pizza 1 ---")
    factory_a = AbstractPizzaFactory(PizzaFactoryA())
    print("---------------")
    factory_a.make_pizza("high")
    print("---------------")
    factory_a.check_pizza()

    print("--- Pizza 2 ---")
    factory_b = AbstractPizzaFactory(PizzaFactoryB())
    print("---------------")
    factory_b.make_pizza("normal")
    print("---------------")
    factory_b.check_pizza()
    

if __name__ == '__main__':
    main()

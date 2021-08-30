import copy
from copy_class import Point


def main():
    point1 = Point(2, 3)
    point2 = copy.deepcopy(point1)

    print("result1:")
    print("x", point1.x, point2.x)
    print("y", point1.y, point2.y)

    point1.x = 5
    print("result2(point1.x = 5):")
    print("x", point1.x, point2.x)
    print("y", point1.y, point2.y)


if __name__ == "__main__":
    main()
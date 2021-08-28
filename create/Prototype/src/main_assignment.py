import copy


def main():
    point1 = Point(2, 3)
    """
    変更点(point2 = copy.deepcopy(point1) -> point2 = point1)
    """
    point2 = point1

    print("result1:")
    print("x", point1.x, point2.x)
    print("y", point1.y, point2.y)

    print("result2(point1.x = 5):")
    point1.x = 5
    print("x", point1.x, point2.x)
    print("y", point1.y, point2.y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    main()

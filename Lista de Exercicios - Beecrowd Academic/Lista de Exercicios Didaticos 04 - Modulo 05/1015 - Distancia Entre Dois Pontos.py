import math


def distance_points(x1, y1, x2, y2):
    norm = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    print(f'{norm:.4f}')


def main():
    point_1 = list(map(float, input().split()))
    point_2 = list(map(float, input().split()))

    distance_points(point_1[0], point_1[1], point_2[0], point_2[1])


if __name__ == "__main__":
    main()

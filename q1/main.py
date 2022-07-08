"""
1.定義一個方法，回傳1-100的和
"""


def sum_1_to_100() -> int:
    ret = 0
    for i in range(1, 101):
        ret += i
    return ret


if __name__ == '__main__':
    print(sum_1_to_100())

def ln(x, precision: int):
    res = x
    f = x
    for i in range(1, precision):
        f *= -x * (i / (i + 1))
        res += f
    return res


def sin(x, precision: int):
    res = x
    f = x
    for i in range(1, precision):
        f *= - x*x / ((i + 1) * (i + 2))
        res += f
    return res


def cos(x, precision: int):
    res = 1
    f = 1
    for i in range(1, precision):
        f *= - x*x / ((i) * (i + 1))
        res += f
    return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(cos(3.14, 500))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

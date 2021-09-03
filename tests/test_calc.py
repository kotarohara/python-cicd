from calc.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 10


if __name__ == '__main__':
    print("Run `py.test -svv`")
def get_sum_of_digits(*args):
    assert all([True if type(arg) in [int, float] else False for arg in args]), "Все аргументы должны быть числами"
    return sum(args)


if __name__ == "__main__":
    result = get_sum_of_digits(4, 5, 3.14, 7, 8, 9)
    print(result)

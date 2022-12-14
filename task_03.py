def fibonacci(n):
    assert isinstance(n, int), "n должно быть целым числом"
    assert 0 <= n <= 999, "n должно быть от 0 до 999 (ограничение глубины рекурсии)"

    return n if n in [0, 1] else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))

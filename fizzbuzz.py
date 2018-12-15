# python3


def fizz_buzz(num=100):
    for i in range(1, num + 1):
        yield ''.join(['Fizz' if i % 3 == 0 else '',
                       'Buzz' if i % 5 == 0 else '']) or i

result = list(fizz_buzz())

# enter from cmd

##### How to measure function execution speed:
# python -m timeit -s "l = [1, 2, 3]" "list(reversed(l))"
# python -m timeit -s "l = [1, 2, 3]" "for i in l[::-1]" # 2-3x faster!

##### zip - возврат пар элементов из соотв массивов, пока один из них не кончится
# for hero, color in zip(heroes, colors):
    # print hero, 'is', color

##### формирование словарей из массивов
# heroes_with_colors = dict(zip(heros, colors))

##### yield - функция генератора, можно сделать функция,
##### которая будет выдавать по строке из файла
# def iterate_lines(f):
    # for line in f:
        # line = line.strip(' \n')
        # if not line:
            # continue
        # if line.startswith('#'):
            # continue
        # yield line

##### в файле используем вот так:
# f = open('config.txt')
# try:
    # for line in iterate_lines(f):
        # do_some_stuff(line)
# finally:
    # f.close()

##### контекстный менеджер
with open('config.txt') as f:
    process_file(f)

from contextlib import contextmanager

@contextmanager
def ignoreErrors(*errors):
    try:
        yield
    except errors:
        pass

with ignoreErrors(KeyError, AttributeError):
    raise KeyError

#  V
#  V
#  V
#  V
with open('config.txt') as f:
    for line in iterate_lines(f):
        do_some_stuff(line)

# =================================================

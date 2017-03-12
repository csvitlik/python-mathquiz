from __future__ import absolute_import, division, print_function
import random
import sys

if sys.version[0] == '3':
    raw_input = input


def myeval(a, op, b):
    result = None
    try:
        result = eval('{}{}{}'.format(a, op, b))
    except:
        pass
    return result


def myinput(s):
    result = None
    try:
        result = raw_input(s)
    except:
        pass
    return result


def numberatlevel(level):
    levels = [6, 7, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32]

    if level < 0:
        level = 0
    elif level > len(levels):
        level = len(levels)

    return random.randint(2, 2**levels[level])


def randompair(level):
    a = numberatlevel(level)
    b = numberatlevel(level)
    tries = 0
    while a == b or 0 != (a % b):
        tries += 1
        b = numberatlevel(level)
        if tries > 9999:
            a = numberatlevel(level)
            tries = 0

    return a, b


def main():
    level = 3  # current level
    ops = ['+', '-', '*', '/', '**']  # supported operations
    op = ops[0]  # current operation
    running = True  # currently running

    while running:
        a, b = randompair(level)
        ans = myeval(a, op, b)

        while True:
            res = myinput('  {:10d}\n{} {:10d}\n'.format(a, op, b))

            if res == None or res == 'q':
                running = False
                break

            if res == '<':
                level -= 1

            if res == '>':
                level += 1

            if res == '?':
                print(int(ans))
                break

            if res in ops:
                op = res
                break

            try:
                if int(res) == int(ans):
                    print('Good!')
                    break
                else:
                    print('Try again!')
            except:
                break

    return 0

if __name__ == '__main__':
    exit(main())

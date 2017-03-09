from __future__ import absolute_import, division, print_function
import random
import sys

if sys.version[0] == '3':
    raw_input = input

def myeval(a,op,b):
    result = None
    try:
        result = eval('{}{}{}'.format(a,op,b))
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
    return random.randint(2, 2**level)

def main():
    levels = [32, 24, 16, 14, 12, 8, 7, 6]
    level = levels[3] # current level

    ops = ['+', '-', '*', '/', '**']
    op = ops[0] # current operation

    running = True # currently running

    while running:
        a = numberatlevel(level)
        b = numberatlevel(level)
        tries = 0
        while a == b or 0 != (a % b):
            tries += 1
            b = numberatlevel(level)
            if tries > 9999:
                a = numberatlevel(level)
                tries = 0


        ans = myeval(a,op,b)
        while True:
            res = myinput('  {:10d}\n{} {:10d}\n'.format(a,op,b))

            if res == None or res == 'q':
                running = False
                break

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

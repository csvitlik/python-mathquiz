'''Math Quiz main module.'''

from __future__ import absolute_import, division, print_function
import random
import sys

if sys.version[0] == '3':
    raw_input = input


class MathQuiz:

    def __init__(self):
        '''Initialize Math Quiz.'''

        self.level = 3                         # Default level
        self.ops = ['+', '-', '*', '/', '**']  # Supported operations
        self.op = self.ops[0]                  # Current operation
        self.running = True                    # Currently running Quiz

    def run(self):
        '''Run Math Quiz.'''

        while self.running:
            a, b = self.randompair()

            # Evaluate answer value first
            ans = self.myeval(a, b)

            while True:
                res = self.myinput(
                    '  {:10d}\n{} {:10d}\n'.format(a, self.op, b))

                # 'q' to Quit
                if res == None or res == 'q':
                    self.running = False
                    break

                # '<' to decrease difficulty
                if res == '<':
                    self.level -= 1

                # '>' to increase difficulty
                if res == '>':
                    self.level += 1

                # '?' to display answer and skip to next question
                if res == '?':
                    print(int(ans))
                    break

                # Enter any supported operation to switch to using that
                # instead of the current operation.
                if res in self.ops:
                    self.op = res
                    break

                # Evaluate user input
                try:
                    if int(res) == int(ans):
                        print('Good!')
                        break
                    else:
                        print('Try again!')
                except:
                    break

    def randompair(self):
        '''Generate a random a,b pair  using numberatlevel.'''

        a = self.numberatlevel()
        b = self.numberatlevel()
        tries = 0

        while a == b or 0 != (a % b):
            tries += 1
            b = self.numberatlevel()
            if tries > 9999:
                a = self.numberatlevel()
                tries = 0

        return a, b

    def numberatlevel(self):
        '''Generate a random number based on self.level.
        Levels increase in difficult over [0, len(levels)].
        Invalid (out of range) levels are clipped to [0, len(levels)].'''

        levels = [6, 7, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32]

        if self.level < 0:
            self.level = 0
        elif self.level > len(levels):
            self.level = len(levels)

        return random.randint(2, 2**levels[self.level])

    def myeval(self, a, b):
        '''Wrap eval.'''

        result = None

        try:
            result = eval('{}{}{}'.format(a, self.op, b))
        except:
            print('Invalid op:', self.op)
            op = '+'
            pass

        return result

    def myinput(self, s):
        '''Wrap raw_input/input.'''

        try:
            result = raw_input(s)
        except EOFError:
            exit(1)

        return result

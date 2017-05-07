'''Math Quiz main module.'''

from __future__ import absolute_import, division, print_function
import random
import sys
import re

if sys.version[0] == '3':
    raw_input = input


class MathQuiz:

    def __init__(self):
        '''Initialize Math Quiz.'''

        self.level = 3                         # Default level
        self.ops = ['+', '-', '*', '/', '**']  # Supported operations
        self.op = self.ops[0]                  # Current operation
        self.running = True                    # Currently running Quiz

    def MakeTexSheet(self, op='+', nquestions=50):
        '''Make a TeX worksheet.'''

        if op in self.ops:
            self.op = op
        else:
            op = '+'

        latex_footer = ''
        latex_header = ''
        with open('tex/footer.tex', 'r') as tex:
            latex_footer = tex.read()
        with open('tex/header.tex', 'r') as tex:
            latex_header = tex.read()

        with open('question.tex', 'w') as qsheet:
            with open('answer.tex', 'w') as asheet:
                asheet.write(latex_header)
                asheet.write('{\Huge Math Quiz Answer Sheet}\\\\')
                asheet.write('\\begin{multicols}{3}')

                qsheet.write(latex_header)
                qsheet.write('{\Huge Math Quiz Question Sheet}\\\\')
                qsheet.write('\\begin{multicols}{3}')

                Nquestions = nquestions
                while nquestions > 0:
                    Q, A = self.MakeQuestion()
                    op = self.op
                    if op == '*':
                        op = '\\times'
                    if op == '/':
                        _q = '\\frac{'
                        _q += Q.replace('/', '}{')
                        _q += '}'
                        Q = _q
                    q = '\\begin{align*} ' + \
                        Q.replace(self.op, '&\\\\'+op) + \
                        ' & = xxx \\numberthis \\end{align*}'
                    a = q.replace('xxx', str(A))
                    q = q.replace('xxx', '\\rule[1pt]{0.3\\linewidth}{.4pt}')

                    asheet.write('{}\n'.format(a))
                    qsheet.write('{}\n'.format(q))
                    nquestions -= 1

                asheet.write('\\end{multicols}')
                asheet.write(latex_footer)
                qsheet.write('\\end{multicols}')
                qsheet.write(latex_footer)

    def Interactive(self):
        '''Interactive Math Quiz.'''

        while self.running:
            question, answer = self.MakeQuestion()

            while True:
                resp = self.Input(question)

                # 'q' to Quit
                if resp == None or resp == 'q':
                    self.running = False
                    break

                # '<' to decrease difficulty
                if resp == '<':
                    self.level -= 1

                # '>' to increase difficulty
                if resp == '>':
                    self.level += 1

                # '?' to display answer and skip to next question
                if resp == '?':
                    print(int(answer))
                    break

                # Enter any supported operation to switch to using that
                # instead of the current operation.
                if resp in self.ops:
                    self.op = resp
                    break

                # Evaluate user input
                try:
                    if int(resp) == int(answer):
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

    def Eval(self, question):
        '''Wrap eval.'''

        result = None

        try:
            result = eval(question)
        except:
            print('Invalid formula:', question)
            op = '+'
            pass

        return int(result)

    def Input(self, s):
        '''Wrap raw_input/input.'''

        try:
            result = raw_input(s + '=?\n')
        except EOFError:
            exit(1)

        return result

    def MakeQuestion(self, nargs=2):
        args = dict()
        question = ''

        Nargs = nargs

        while nargs > 0:
            a, b = self.randompair()
            args[nargs] = b
            args[nargs - 1] = a
            nargs -= 2

        args_keys = args.keys()
        for i in range(Nargs):
            question += '{}'.format(args[args_keys[i]])
            if i + 1 < Nargs:
                question += self.op

        # Evaluate answer value first
        answer = self.Eval(question)

        return question, answer

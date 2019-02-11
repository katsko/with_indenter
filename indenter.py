#!/usr/bin/env python3


class Indenter:

    AMOUNT = 4

    def __init__(self):
        self.indent = ''

    def __enter__(self):
        self.indent += ' ' * self.AMOUNT
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent = self.indent[self.AMOUNT:]

    def print(self, text=None):
        if text is None:
            print()
        else:
            print(f'{self.indent}{text}')

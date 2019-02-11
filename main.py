#!/usr/bin/env python3
from indenter import Indenter


def main():
    with Indenter() as indent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            indent.print()
            indent.print('hello friend')
            with indent:
                indent.print('bonjour les amis')
        indent.print('hey')


if __name__ == '__main__':
    main()

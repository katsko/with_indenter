#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from indenter import Indenter


class TestIndenterCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_indenter_without_context(self, mock_stdout):
        Indenter().print('abc\ndef')
        assert mock_stdout.getvalue() == 'abc\ndef\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_indenter_without_context_three_times(self, mock_stdout):
        indenter = Indenter()
        indenter.print('abc')
        indenter.print('def')
        indenter.print('ghi')
        assert mock_stdout.getvalue() == 'abc\ndef\nghi\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_indenter_without_context_empty_line(self, mock_stdout):
        indenter = Indenter()
        indenter.print('abc')
        indenter.print()
        indenter.print('ghi')
        assert mock_stdout.getvalue() == 'abc\n\nghi\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_indenter(self, mock_stdout):
        indenter = Indenter()
        indenter.print('abc')
        indenter.print()
        indenter.print('ghi')
        with indenter:
            indenter.print('jkl')
            with indenter:
                indenter.print('mno')
            indenter.print('pqi')
        indenter.print('stu')
        with indenter:
            indenter.print('vwx')
        assert (mock_stdout.getvalue() == 'abc\n\nghi\n    jkl\n        '
                                          'mno\n    pqi\nstu\n    vwx\n')


if __name__ == '__main__':
    unittest.main()

import unittest

from play import check_win


class TicTacToeTest(unittest.TestCase):
    
    def test_check_win_horizontal(self):
        board = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_vertical(self):
        board = [['O', 'X', 'O'], ['O', 'X', ' '], ['O', ' ', 'X']]
        self.assertTrue(check_win(board, 'O'))

    def test_check_win_diagonal(self):
        board = [['X', 'O', 'O'], ['O', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_tie(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
        self.assertFalse(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

if __name__ == '__main__':
    unittest.main()

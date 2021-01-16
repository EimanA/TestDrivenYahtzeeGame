from unittest import TestCase
from yahtzee import get_valid_option
import unittest.mock


class TestGetValidOption(TestCase):
    @unittest.mock.patch('builtins.input', side_effect=['1'])
    def test_get_valid_option_first(self, mock_input):
        options = {1: 'Aces', 2: 'Fours', 3: 'Fives', 4: 'Sixes', 5: 'Four of a kind', 6: 'Full house',
                   7: 'Small Straight', 8: 'Large Straight', 9: 'Yahtzee', 10: 'Chance'}
        expected = 'Aces'
        actual = get_valid_option(options)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['5'])
    def test_get_valid_option_middle(self, mock_input):
        options = {1: 'Aces', 2: 'Fours', 3: 'Fives', 4: 'Sixes', 5: 'Four of a kind', 6: 'Full house',
                   7: 'Small Straight', 8: 'Large Straight', 9: 'Yahtzee', 10: 'Chance'}
        expected = 'Four of a kind'
        actual = get_valid_option(options)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['10'])
    def test_get_valid_option_last(self, mock_input):
        options = {1: 'Aces', 2: 'Fours', 3: 'Fives', 4: 'Sixes', 5: 'Four of a kind', 6: 'Full house',
                   7: 'Small Straight', 8: 'Large Straight', 9: 'Yahtzee', 10: 'Chance'}
        expected = 'Chance'
        actual = get_valid_option(options)
        self.assertEqual(expected, actual)

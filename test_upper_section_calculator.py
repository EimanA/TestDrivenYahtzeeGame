from unittest import TestCase
from yahtzee import upper_section_calculator
import unittest.mock
import io


class TestUpperSectionCalculator(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_upper_section_calculator_no_instance(self, mock_stdout):
        chosen_dices = [5, 3, 5, 1, 5]
        chosen_item = 'Fours'
        expected = 0
        expected_output = '\n[32mYou gained 0 points for Fours. It will be saved in your score sheet.[00m\n\n'
        actual = upper_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_upper_section_calculator_one_instance(self, mock_stdout):
        chosen_dices = [4, 3, 5, 1, 5]
        chosen_item = 'Fours'
        expected = 4
        expected_output = '\n[32mYou gained 4 points for Fours. It will be saved in your score sheet.[00m\n\n'
        actual = upper_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_upper_section_calculator_many_instances(self, mock_stdout):
        chosen_dices = [4, 3, 4, 1, 4]
        chosen_item = 'Fours'
        expected = 12
        expected_output = '\n[32mYou gained 12 points for Fours. It will be saved in your score sheet.[00m\n\n'
        actual = upper_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_upper_section_calculator_full_instances(self, mock_stdout):
        chosen_dices = [1, 1, 1, 1, 1]
        chosen_item = 'Aces'
        expected = 5
        expected_output = '\n[32mYou gained 5 points for Aces. It will be saved in your score sheet.[00m\n\n'
        actual = upper_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

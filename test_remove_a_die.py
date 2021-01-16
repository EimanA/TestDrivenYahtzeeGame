from unittest import TestCase
from yahtzee import remove_a_die
import unittest.mock
import io


class TestRemoveADie(TestCase):
    @unittest.mock.patch('builtins.input', side_effect=['1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_empty_list_creation(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6, 6]
        list_of_kept_dices = [2]
        expected_output = '[32m1[00m- Face of this die is 2\n'
        expected = ([5, 1, 6, 6, 2], [])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_first_item(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6]
        list_of_kept_dices = [2, 6]
        expected_output = '[32m1[00m- Face of this die is 2\n\
[32m2[00m- Face of this die is 6\n'
        expected = ([5, 1, 6, 2], [6])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['2'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_second_item(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6]
        list_of_kept_dices = [2, 6]
        expected_output = '[32m1[00m- Face of this die is 2\n\
[32m2[00m- Face of this die is 6\n'
        expected = ([5, 1, 6, 6], [2])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['3'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_unavailable_index(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6]
        list_of_kept_dices = [2, 6]
        expected_output = '[32m1[00m- Face of this die is 2\n\
[32m2[00m- Face of this die is 6\n\
[91mThis is not one of the valid options![00m\n'
        expected = ([5, 1, 6], [2, 6])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['0'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_unavailable_index_2(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6]
        list_of_kept_dices = [2, 6]
        expected_output = '[32m1[00m- Face of this die is 2\n\
[32m2[00m- Face of this die is 6\n\
[91mThis is not one of the valid options![00m\n'
        expected = ([5, 1, 6], [2, 6])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('builtins.input', side_effect=['n'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_a_die_invalid_index(self, mock_stdout, mock_input):
        list_of_unwanted_dices = [5, 1, 6]
        list_of_kept_dices = [2, 6]
        expected_output = '[32m1[00m- Face of this die is 2\n\
[32m2[00m- Face of this die is 6\n\
[91mThis is not one of the valid options![00m\n'
        expected = ([5, 1, 6], [2, 6])
        actual = remove_a_die(list_of_unwanted_dices, list_of_kept_dices)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

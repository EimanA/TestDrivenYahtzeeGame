from unittest import TestCase
from yahtzee import dice_generator
import unittest.mock
import io


# The output format may change on the exam day
class TestDiceGenerator(TestCase):
    @unittest.mock.patch('random.choices', return_value=[2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dice_generator_one_die_to_roll(self, mock_stdout, mock):
        kept_faces = [4, 4, 4, 4]
        will_be_rolled_faces = [1]
        expected = ([2, 4, 4, 4, 4], [2])
        expected_output = '\nThe faces of your new dices are: 2\n\n' \
                          '[32mThe full list of your dices are: 2, 4, 4, 4, 4 [00m\n'
        actual = dice_generator(kept_faces, will_be_rolled_faces)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('random.choices', return_value=[2, 4, 2, 6, 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dice_generator_five_dices_to_roll(self, mock_stdout, mock):
        kept_faces = []
        will_be_rolled_faces = [1, 4, 2, 6, 1]
        expected = ([2, 4, 2, 6, 2], [2, 4, 2, 6, 2])
        expected_output = '\nThe faces of your new dices are: 2, 4, 2, 6, 2\n\n' \
                          '[32mThe full list of your dices are: 2, 4, 2, 6, 2 [00m\n'
        actual = dice_generator(kept_faces, will_be_rolled_faces)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('random.choices', return_value=[2, 4, 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dice_generator_three_dices_to_roll(self, mock_stdout, mock):
        kept_faces = [2, 2]
        will_be_rolled_faces = [1, 3, 5]
        expected = ([2, 4, 2, 2, 2], [2, 4, 2])
        expected_output = '\nThe faces of your new dices are: 2, 4, 2\n\n' \
                          '[32mThe full list of your dices are: 2, 4, 2, 2, 2 [00m\n'
        actual = dice_generator(kept_faces, will_be_rolled_faces)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

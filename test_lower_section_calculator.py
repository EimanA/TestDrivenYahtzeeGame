from unittest import TestCase
from yahtzee import lower_section_calculator
import unittest.mock
import io


class TestLowerSectionCalculator(TestCase):
    def test_lower_section_calculator_is_three_of_a_kind(self):
        chosen_dices = [5, 3, 5, 1, 5]
        chosen_item = 'Three of a kind'
        expected = 19
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_not_three_of_a_kind(self):
        chosen_dices = [5, 3, 4, 1, 5]
        chosen_item = 'Three of a kind'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_more_than_three_of_a_kind(self):
        chosen_dices = [5, 5, 5, 1, 5]
        chosen_item = 'Three of a kind'
        expected = 21
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_four_of_a_kind(self):
        chosen_dices = [5, 5, 5, 1, 5]
        chosen_item = 'Four of a kind'
        expected = 21
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_not_four_of_a_kind(self):
        chosen_dices = [5, 3, 2, 3, 3]
        chosen_item = 'Four of a kind'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_more_than_four_of_a_kind(self):
        chosen_dices = [3, 3, 3, 3, 3]
        chosen_item = 'Four of a kind'
        expected = 15
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_full_house(self):
        chosen_dices = [5, 4, 5, 4, 5]
        chosen_item = 'Full house'
        expected = 25
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_not_full_house(self):
        chosen_dices = [5, 3, 2, 3, 3]
        chosen_item = 'Full house'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    # A hot debate was found online regarding this matter. So, I considered it to be a valid full house.
    def test_lower_section_calculator_is_more_than_a_full_house(self):
        chosen_dices = [3, 3, 3, 3, 3]
        chosen_item = 'Full house'
        expected = 25
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_small_straight_low(self):
        chosen_dices = [2, 6, 4, 3, 1]
        chosen_item = 'Small Straight'
        expected = 30
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_small_straight_middle(self):
        chosen_dices = [2, 5, 4, 3, 5]
        chosen_item = 'Small Straight'
        expected = 30
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_small_straight_high(self):
        chosen_dices = [4, 5, 1, 3, 6]
        chosen_item = 'Small Straight'
        expected = 30
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_not_small_straight(self):
        chosen_dices = [1, 5, 4, 3, 5]
        chosen_item = 'Small Straight'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_more_than_small_straight_high(self):
        chosen_dices = [5, 2, 3, 6, 4]
        chosen_item = 'Small Straight'
        expected = 30
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_more_than_small_straight_low(self):
        chosen_dices = [5, 2, 3, 1, 4]
        chosen_item = 'Small Straight'
        expected = 30
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_large_straight_low(self):
        chosen_dices = [2, 5, 4, 3, 1]
        chosen_item = 'Large Straight'
        expected = 40
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_large_straight_high(self):
        chosen_dices = [4, 5, 2, 3, 6]
        chosen_item = 'Large Straight'
        expected = 40
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_not_large_straight(self):
        chosen_dices = [4, 5, 1, 3, 6]
        chosen_item = 'Large Straight'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    # Yahtzee bonuses will be checked and calculated in the engine function. A rewrite of 50 will happen if it wouldn't
    # be the first time but the correct printed result and updating the 100 bonus points will happen in the engine
    # calculator which called this function. Unit test was written related to this matter.
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_lower_section_calculator_is_yahtzee(self, mock_stdout):
        chosen_dices = [4, 4, 4, 4, 4]
        chosen_item = 'Yahtzee'
        expected = 50
        expected_output = '[32mYAAAAHTZEEEEE![00m\n'
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_lower_section_calculator_is_not_yahtzee(self):
        chosen_dices = [4, 1, 4, 4, 4]
        chosen_item = 'Yahtzee'
        expected = 0
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

    def test_lower_section_calculator_is_selected_as_chance(self):
        chosen_dices = [2, 1, 4, 4, 6]
        chosen_item = 'Chance'
        expected = 17
        actual = lower_section_calculator(chosen_dices, chosen_item)
        self.assertEqual(expected, actual)

from unittest import TestCase
from yahtzee import score_calculator_engine
import unittest.mock
import io


class TestScoreCalculatorEngine(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_upper_section_zero_points_gain(self, mock_stdout):
        option = 'Sixes'
        dices = [5, 4, 1, 5, 4]
        score_sheet = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,
                                         'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 17, 'lower_section':
                           {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}

        expected = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,
                                      'Sixes': 0}, 'Total Score': 17, 'Upper Section Bonus': 0,
                    'Total of Upper Section': 17, 'lower_section':
                        {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
        expected_output = '\n[32mYou gained 0 points for Sixes. It will be saved in your score sheet.[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_upper_section_no_bonus_added(self, mock_stdout):
        option = 'Fives'
        dices = [5, 4, 1, 5, 4]
        score_sheet = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,
                                         'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 17, 'lower_section':
                           {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}

        expected = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': 10, 'Sixes': None},
                    'Total Score': 27, 'Upper Section Bonus': 0, 'Total of Upper Section': 27, 'lower_section':
                        {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 97}
        expected_output = '\n[32mYou gained 10 points for Fives. It will be saved in your score sheet.[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_upper_section_with_added_bonus_at_that_moment(self, mock_stdout):
        option = 'Fives'
        dices = [5, 5, 1, 5, 4]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 112}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': 15, 'Sixes': 18},
                    'Total Score': 67, 'Upper Section Bonus': 35, 'Total of Upper Section': 102, 'lower_section':
                        {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 172}
        expected_output = '\n[32mYou gained 15 points for Fives. It will be saved in your score sheet.[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # As mentioned above, no test will be required for a situation that we had a previously gained 0 points for a
    # yahtzee and another 5 of a kind will appear. Another function will take care of all possible selections. (Either
    # Yahtzee or anything else)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_with_no_added_yahtzee_bonus(self, mock_stdout):
        option = 'Yahtzee'
        dices = [5, 5, 5, 5, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 20, 'Grand Total': 62}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 122}
        expected_output = '[32mYAAAAHTZEEEEE![00m\n\n' \
                          '[32mYou gained 50 points for Yahtzee. It will be saved in your score sheet.[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_with_added_yahtzee_bonus(self, mock_stdout):
        option = 'Yahtzee'
        dices = [5, 5, 5, 5, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 122}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                    'Yahtzee Bonus': 100, 'Total of Lower Section': 170, 'Grand Total': 222}
        expected_output = '[32mYAAAAHTZEEEEE![00m\n\n' \
                          '[32mYou gained 100 points for Yahtzee. It will be saved in your score sheet.[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_valid_three_of_a_kind(self, mock_stdout):
        option = 'Three of a kind'
        dices = [5, 1, 5, 5, 6]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': 22, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 44, 'Grand Total': 96}
        expected_output = '\n[32mYou gained 22 points for Three of a kind. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_invalid_three_of_a_kind(self, mock_stdout):
        option = 'Three of a kind'
        dices = [5, 1, 5, 4, 6]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': 0, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}
        expected_output = '\n[32mYou gained 0 points for Three of a kind. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_more_than_three_of_a_kind(self, mock_stdout):
        option = 'Three of a kind'
        dices = [5, 1, 5, 5, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': 23, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 45, 'Grand Total': 97}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': 21, 'Four of a kind': 23, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 66, 'Grand Total': 118}
        expected_output = '\n[32mYou gained 21 points for Three of a kind. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # No further need for more than or less than 4 of a kind as it was previously tested for 3 of a kind.
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_four_of_a_kind(self, mock_stdout):
        option = 'Four of a kind'
        dices = [5, 1, 5, 5, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': 21, 'Full house': None, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 43, 'Grand Total': 95}
        expected_output = '\n[32mYou gained 21 points for Four of a kind. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_full_house(self, mock_stdout):
        option = 'Full house'
        dices = [5, 3, 5, 5, 3]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': 25, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 47, 'Grand Total': 99}
        expected_output = '\n[32mYou gained 25 points for Full house. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Checking for a three as a full house
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_invalid_full_house_three_of_a_kind(self, mock_stdout):
        option = 'Full house'
        dices = [5, 1, 5, 5, 3]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': 0, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}
        expected_output = '\n[32mYou gained 0 points for Full house. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Checking for two pairs as a full house
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_invalid_full_house_two_pairs(self, mock_stdout):
        option = 'Full house'
        dices = [5, 1, 5, 3, 3]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': 0, 'Small Straight': None,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}
        expected_output = '\n[32mYou gained 0 points for Full house. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_small_straight_low(self, mock_stdout):
        option = 'Small Straight'
        dices = [2, 6, 4, 3, 1]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 52, 'Grand Total': 104}
        expected_output = '\n[32mYou gained 30 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_small_straight_middle(self, mock_stdout):
        option = 'Small Straight'
        dices = [2, 5, 4, 3, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 52, 'Grand Total': 104}
        expected_output = '\n[32mYou gained 30 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_small_straight_high(self, mock_stdout):
        option = 'Small Straight'
        dices = [4, 5, 1, 3, 6]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 52, 'Grand Total': 104}
        expected_output = '\n[32mYou gained 30 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_not_a_small_straight(self, mock_stdout):
        option = 'Small Straight'
        dices = [1, 5, 4, 3, 5]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 0,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}
        expected_output = '\n[32mYou gained 0 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_more_than_a_small_straight_high(self, mock_stdout):
        option = 'Small Straight'
        dices = [5, 2, 3, 6, 4]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 62, 'Grand Total': 114}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 92, 'Grand Total': 144}
        expected_output = '\n[32mYou gained 30 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_more_than_a_small_straight_low(self, mock_stdout):
        option = 'Small Straight'
        dices = [5, 2, 3, 1, 4]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 62, 'Grand Total': 114}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 92, 'Grand Total': 144}
        expected_output = '\n[32mYou gained 30 points for Small Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_a_large_straight_low(self, mock_stdout):
        option = 'Large Straight'
        dices = [2, 5, 4, 3, 1]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 62, 'Grand Total': 114}
        expected_output = '\n[32mYou gained 40 points for Large Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_a_large_straight_high(self, mock_stdout):
        option = 'Large Straight'
        dices = [4, 5, 2, 3, 6]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': 40, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 62, 'Grand Total': 114}
        expected_output = '\n[32mYou gained 40 points for Large Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_not_a_large_straight(self, mock_stdout):
        option = 'Large Straight'
        dices = [4, 5, 1, 3, 6]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': 22},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                         'Large Straight': 0, 'Yahtzee': None, 'Chance': 22},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 22, 'Grand Total': 74}
        expected_output = '\n[32mYou gained 0 points for Large Straight. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_calculator_engine_from_lower_section_chance(self, mock_stdout):
        option = 'Chance'
        dices = [4, 2, 6, 3, 2]
        score_sheet = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None,
                                         'Sixes': 18}, 'Total Score': 52, 'Upper Section Bonus': 0,
                       'Total of Upper Section': 52, 'lower_section':
                           {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                            'Large Straight': None, 'Yahtzee': None, 'Chance': None},
                       'Yahtzee Bonus': 0, 'Total of Lower Section': 30, 'Grand Total': 82}

        expected = {'upper_section': {'Aces': 2, 'Twos': 8, 'Threes': 12, 'Fours': 12, 'Fives': None, 'Sixes': 18},
                    'Total Score': 52, 'Upper Section Bonus': 0, 'Total of Upper Section': 52, 'lower_section':
                        {'Three of a kind': None, 'Four of a kind': None, 'Full house': None, 'Small Straight': 30,
                         'Large Straight': None, 'Yahtzee': None, 'Chance': 17},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 47, 'Grand Total': 99}
        expected_output = '\n[32mYou gained 17 points for Chance. It will be saved in your score sheet.' \
                          '[00m\n\n'
        actual = score_calculator_engine(dices, score_sheet, option)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

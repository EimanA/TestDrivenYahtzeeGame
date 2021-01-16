from unittest import TestCase
from yahtzee import score_sheet_printer_selector
import unittest.mock
import io


class TestScoreSheetPrinterSelector(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_sheet_printer_selector_select_mode(self, mock_stdout):
        scores = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None, 'Sixes': None},
                  'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':
                      {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                       'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                  'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
        mode = 'select'
        expected_output = '\n---------------Upper Section Items---------------\n' \
                          'Enter [32m1[00m to choose Aces for this turn.\n' \
                          '[34mFor Twos you have already gained 8 points.[00m\n' \
                          '[34mFor Threes you have already gained 9 points.[00m\n' \
                          'Enter [32m2[00m to choose Fours for this turn.\n' \
                          'Enter [32m3[00m to choose Fives for this turn.\n' \
                          'Enter [32m4[00m to choose Sixes for this turn.\n\n' \
                          '---------------Upper Section Results---------------\n' \
                          'For Total Score you have gained 17 points.\n' \
                          'For Upper Section Bonus you have gained 0 points.\n' \
                          'For Total of Upper Section you have gained 17 points.\n\n\n' \
                          '---------------Lower Section Items---------------\n' \
                          '[34mFor Three of a kind you have already gained 20 points.[00m\n' \
                          'Enter [32m5[00m to choose Four of a kind for this turn.\n' \
                          'Enter [32m6[00m to choose Full house for this turn.\n' \
                          'Enter [32m7[00m to choose Small Straight for this turn.\n' \
                          'Enter [32m8[00m to choose Large Straight for this turn.\n' \
                          'Enter [32m9[00m to choose Yahtzee for this turn.\n' \
                          'Enter [32m10[00m to choose Chance for this turn.\n\n' \
                          '---------------Lower Section Results---------------\n' \
                          'For Yahtzee Bonus you have gained 0 points.\n' \
                          'For Total of Lower Section you have gained 70 points.\n' \
                          'For Grand Total you have gained 87 points.\n\n'
        expected = {1: 'Aces', 2: 'Fours', 3: 'Fives', 4: 'Sixes', 5: 'Four of a kind', 6: 'Full house',
                    7: 'Small Straight', 8: 'Large Straight', 9: 'Yahtzee', 10: 'Chance'}
        actual = score_sheet_printer_selector(scores, mode)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_score_sheet_printer_selector_print_mode(self, mock_stdout):
        scores = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None, 'Sixes': None},
                  'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':
                      {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None,
                       'Large Straight': None, 'Yahtzee': 50, 'Chance': None},
                  'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
        mode = 'print'
        expected_output = '\n---------------Upper Section Items---------------\n' \
                          'For Aces you have not gained any points yet.\n' \
                          '[34mFor Twos you have already gained 8 points.[00m\n' \
                          '[34mFor Threes you have already gained 9 points.[00m\n' \
                          'For Fours you have not gained any points yet.\n' \
                          'For Fives you have not gained any points yet.\n' \
                          'For Sixes you have not gained any points yet.\n\n' \
                          '---------------Upper Section Results---------------\n' \
                          'For Total Score you have gained 17 points.\n' \
                          'For Upper Section Bonus you have gained 0 points.\n' \
                          'For Total of Upper Section you have gained 17 points.\n\n\n' \
                          '---------------Lower Section Items---------------\n' \
                          '[34mFor Three of a kind you have already gained 20 points.[00m\n' \
                          'For Four of a kind you have not gained any points yet.\n' \
                          'For Full house you have not gained any points yet.\n' \
                          'For Small Straight you have not gained any points yet.\n' \
                          'For Large Straight you have not gained any points yet.\n' \
                          '[34mFor Yahtzee you have already gained 50 points.[00m\n' \
                          'For Chance you have not gained any points yet.\n\n' \
                          '---------------Lower Section Results---------------\n' \
                          'For Yahtzee Bonus you have gained 0 points.\n' \
                          'For Total of Lower Section you have gained 70 points.\n' \
                          'For Grand Total you have gained 87 points.\n\n'
        expected = {}  # will e thrown away (won't be assigned/passed in this mode).
        actual = score_sheet_printer_selector(scores, mode)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(expected, actual)

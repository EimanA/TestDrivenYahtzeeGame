"""
Eiman Ardakanian
2020-12-11
A Yahtzee game written in 6 hours for a hackathon and test-driven style exam
"""
import random
import re
import doctest
import itertools


def LOWER_SECTION_REGEX_PATTERN() -> tuple:
    """
    Return a correct regular expression for each pattern in lower section and any number of given dices(>5).

    Returning a tuple to insist on the assumed fact that it is a constant or immutable object!
    :postcondition: This function is not responsible for the number of given dices.
            (will be generated in its own function)
    :return: a single item tuple containing a dictionary of regex patterns for lower section.
    """
    regex_pattern = ({'Three of a kind': r'([1-6])\1{2}',
                      'Four of a kind': r'([1-6])\1{3}',
                      'Full house': r'(([1-6])\2{2}([1-6])\3|([1-6])\4([1-6])\5{2})',
                      'Small Straight': r'(1.?2.?3.?4|2.?3.?4.?5|3.?4.?5.?6)',
                      'Large Straight': r'(12345|23456)',
                      'Yahtzee': r'([1-6])\1{4}',
                      'Chance': r'.*'}, )  # potentially any valid 5 dices can be assumed as Chance!

    return regex_pattern


def FIXED_SCORES() -> tuple:
    """
    Return a single item tuple containing a dictionary of fixed scores as a constant.

    Returning a tuple to insist on the assumed fact that it is a constant or immutable object!
    :return: a single item tuple containing a dictionary of fixed scores as a constant
    """
    fixed_scores = ({'Yahtzee': 50, 'Full house': 25, 'Large Straight': 40, 'Small Straight': 30}, )

    return fixed_scores


def dice_selector(unwanted_dices: list, kept_dices: list) -> tuple:
    """
    Create two new lists of "unwanted dices" to roll and "kept dices" to keep for the next rolling phase based on
    players choice.

    This function will get help from two additional functions to relocate dices between these two lists. This function
    will let players choose as many times as they want to relocate dices between these two lists.
    :precondition: the combination of these two lists should present 5 dices that we have in this game with 6 faces.
    :postcondition: this function will give a new combination of these two lists that will present 5 dices that we have
                in this game with 6 faces.
    :param unwanted_dices: a list of previously selected dices to roll in the previous phase
    :param kept_dices: a list of previously selected dices to keep in the previous phase
    :return: a tuple of 2 lists containing new list_of_unwanted_dices and new list_of_kept_dices

    Unittests were written for both helper functions that are relocating dices between 2 lists.
    """
    user_choice = 0
    while user_choice != '3':
        if len(unwanted_dices) == 0:
            print('\n\033[32mYou currently have no selected die for the next roll.')
        else:
            print(f'\n\033[32mYour dices for the next roll are: ', ', '.join([str(die) for die in unwanted_dices]))
        if len(kept_dices) == 0:
            print('You currently have no selected die in your kept list.\033[00m')
        else:
            print('You currently kept dices with these faces: ',
                  ', '.join([str(die) for die in kept_dices]), '\n\033[00m')

        user_choice = input('Enter 1 to add a die to your kept dices\nEnter 2 to remove a die from your kept dices\n'
                            'Enter 3 if you are done with selecting dices to keep and want to roll others\n1/2/3? ')
        if user_choice == '1' and len(unwanted_dices) != 0:  # There is at least a die that user wants to keep
            unwanted_dices, kept_dices = keep_a_die(unwanted_dices, kept_dices)
        elif user_choice == '2' and len(kept_dices) != 0:  # There is at least a die that user wants to remove
            unwanted_dices, kept_dices = remove_a_die(unwanted_dices, kept_dices)
        elif user_choice != '3':
            print('\033[91mThis command is not possible!\033[00m')

    return unwanted_dices, kept_dices  # a return because of initial values assignment in the first rolling attempt!


def remove_a_die(dices_to_roll: list, kept_dices: list) -> tuple:
    """
    Relocate a selected die by the user from the kept list of dices to the list of dices that the player wants to roll

    :precondition: the kept_dices list can not be empty (will be tested in its caller function).
    :param dices_to_roll: a list of previously selected dices to roll in the previous phase
    :param kept_dices: a list of previously selected dices to keep in the previous phase
    :return: a tuple of 2 lists containing new unwanted_dices and new kept_dices

    Unittests were written as writing doctests for this small function is not a valid option because of dependencies on
    user input functionality (getting user choice based on printed options and removing the selected die from the kept
    list)
    """
    for die_number, die_face in zip(itertools.count(1), kept_dices):  # iterating with zip and itertools.count
        print(f'\033[32m{die_number}\033[00m- Face of this die is {die_face}')

    selected_item = input('Please enter one die number from the left column that you want to remove: ')

    # in addition to unacceptable non-int or indexes, user should not enter 0 or negative numbers which might be valid!
    if selected_item not in [str(number) for number in range(1, len(kept_dices)+1)]:
        print('\033[91mThis is not one of the valid options!\033[00m')
    else:
        try:
            dices_to_roll.append(kept_dices.pop(int(selected_item)-1))   # relocate the item with that index
        except (IndexError, ValueError):
            print('\033[91mThis is not one of the valid options!\033[00m')

    return dices_to_roll, kept_dices  # Just for checking in unit tests.


def keep_a_die(unwanted_dices: list, dices_to_keep: list) -> tuple:
    """
    Relocate a selected die by the user from the previous list of unwanted dices to the list of dices that the player
    wants to keep

    :param unwanted_dices: a list of previously selected dices to roll in the previous phase
    :param dices_to_keep: a list of previously selected dices to keep in the previous phase
    :return: a tuple of 2 lists containing new unwanted_dices and new kept_dices

    Unittests were written as writing doctests for this small function is not a valid option because of dependencies on
    user input functionality (getting user choice based on printed options and adding the selected die to the kept list)
    """
    for die_number, die_face in enumerate(unwanted_dices, 1):  # iterating with enumerate in contrast to previous one
        print(f'\033[32m{die_number}\033[00m- Face of this die is {die_face}')

    selected_item = input('Please enter one die number from the left column that you want to keep: ')

    # in addition to unacceptable non-int or indexes, user should not enter 0 or negative numbers which might be valid!
    if selected_item not in [str(number) for number in range(1, len(unwanted_dices) + 1)]:
        print('\033[91mThis is not one of the valid options!\033[00m')
    else:
        try:
            dices_to_keep.append(unwanted_dices.pop(int(selected_item) - 1))  # relocate the item with that index
        except (IndexError, ValueError):
            print('\033[91mThis is not one of the valid options!\033[00m')

    return unwanted_dices, dices_to_keep  # Just for checking in unit tests.


def score_sheet_printer_selector(scores: dict, mode: str) -> dict:
    """
    Print the current score sheet (with 2 similar functionalities depending on the mode string: print or print with a
    numbered available items to select from)

    :precondition: this function needs the same structure and order corresponding to the designed nested dictionary for
                the score sheets. (two nested dictionaries for upper and lower sections and totals of each which are
                not nested)
    :precondition: this function will correctly print the score sheets to let players see the current scores or to
                choose from its numbered available items in each section that have not been selected before (not int).
    :param scores: Dictionary of one player score sheet
    :param mode: A string representing the mode of this function: plain or numbered available items to select from.
    :return: a dictionary of all available options in select mode (an empty dictionary which will be thrown away in
            print mode)

    >>> gained_scores = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,\
    'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':\
    {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
    >>> this_mode = 'select'
    >>> score_sheet_printer_selector(gained_scores, this_mode)
    <BLANKLINE>
    ---------------Upper Section Items---------------
    Enter [32m1[00m to choose Aces for this turn.
    [34mFor Twos you have already gained 8 points.[00m
    [34mFor Threes you have already gained 9 points.[00m
    Enter [32m2[00m to choose Fours for this turn.
    Enter [32m3[00m to choose Fives for this turn.
    Enter [32m4[00m to choose Sixes for this turn.
    <BLANKLINE>
    ---------------Upper Section Results---------------
    For Total Score you have gained 17 points.
    For Upper Section Bonus you have gained 0 points.
    For Total of Upper Section you have gained 17 points.
    <BLANKLINE>
    <BLANKLINE>
    ---------------Lower Section Items---------------
    [34mFor Three of a kind you have already gained 20 points.[00m
    Enter [32m5[00m to choose Four of a kind for this turn.
    Enter [32m6[00m to choose Full house for this turn.
    Enter [32m7[00m to choose Small Straight for this turn.
    Enter [32m8[00m to choose Large Straight for this turn.
    Enter [32m9[00m to choose Yahtzee for this turn.
    Enter [32m10[00m to choose Chance for this turn.
    <BLANKLINE>
    ---------------Lower Section Results---------------
    For Yahtzee Bonus you have gained 0 points.
    For Total of Lower Section you have gained 70 points.
    For Grand Total you have gained 87 points.
    <BLANKLINE>
    {1: 'Aces', 2: 'Fours', 3: 'Fives', 4: 'Sixes', 5: 'Four of a kind', 6: 'Full house', 7: 'Small Straight', \
8: 'Large Straight', 9: 'Yahtzee', 10: 'Chance'}

    >>> gained_scores = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,\
    'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':\
    {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
    >>> this_mode = 'print'
    >>> score_sheet_printer_selector(gained_scores, this_mode)
    <BLANKLINE>
    ---------------Upper Section Items---------------
    For Aces you have not gained any points yet.
    [34mFor Twos you have already gained 8 points.[00m
    [34mFor Threes you have already gained 9 points.[00m
    For Fours you have not gained any points yet.
    For Fives you have not gained any points yet.
    For Sixes you have not gained any points yet.
    <BLANKLINE>
    ---------------Upper Section Results---------------
    For Total Score you have gained 17 points.
    For Upper Section Bonus you have gained 0 points.
    For Total of Upper Section you have gained 17 points.
    <BLANKLINE>
    <BLANKLINE>
    ---------------Lower Section Items---------------
    [34mFor Three of a kind you have already gained 20 points.[00m
    For Four of a kind you have not gained any points yet.
    For Full house you have not gained any points yet.
    For Small Straight you have not gained any points yet.
    For Large Straight you have not gained any points yet.
    [34mFor Yahtzee you have already gained 50 points.[00m
    For Chance you have not gained any points yet.
    <BLANKLINE>
    ---------------Lower Section Results---------------
    For Yahtzee Bonus you have gained 0 points.
    For Total of Lower Section you have gained 70 points.
    For Grand Total you have gained 87 points.
    <BLANKLINE>
    {}

    # this empty dictionary will be thrown away for "print" only mode/functionality!
    """
    dictionary_of_options = {}
    counter = 1
    print(f'\n---------------Upper Section Items---------------')
    for key, value in scores['upper_section'].items():
        if value is None and mode == 'select':  # items not chosen before and mode is "select" (one additional step)
            print(f'Enter \033[32m{counter}\033[00m to choose {key} for this turn.')  # print a coloured number
            dictionary_of_options[counter] = key  # and add it to dictionary of options
            counter += 1

        elif value is None and mode == 'print':  # items not chosen before and mode is a simple "print" of score board.
            print(f'For {key} you have not gained any points yet.')

        else:  # items chosen before and mode is either a simple "print" of score sheet or with selectable numbers.
            print(f'\033[34mFor {key} you have already gained {value} points.\033[00m')
    print(f'\n---------------Upper Section Results---------------')
    print(f'For Total Score you have gained {scores["Total Score"]} points.')
    print(f'For Upper Section Bonus you have gained {scores["Upper Section Bonus"]} points.')
    print(f'For Total of Upper Section you have gained {scores["Total of Upper Section"]} points.\n')

    # for printing the lower section I have to call another function here because of the 20 lines limitation:
    dictionary_of_options = lower_section_printer_selector(counter, dictionary_of_options, mode, scores)
    return dictionary_of_options  # will be thrown away as an empty dictionary for "print" only mode/functionality!


def lower_section_printer_selector(counter: int, dictionary_of_options: dict, mode: str, scores: dict) -> dict:
    """
    Print the lower section of score sheet.

    This function was created because of 20 lines limitation which will not allow to implement all the necessities
    in the same first function.

    :precondition: same as above (upper section printer) This function should receive everything (parameters) from its
                previous function to work correctly, as its just the continuation of another function.
    :param counter: an integer to count the number of available/selectable items and print them in select mode on the
                screen
    :param dictionary_of_options: all possible items to select from filled in the previous upper section function which
                its key will be the counter number while counting.
    :param mode: a string corresponding to the print or select mode.
    :param scores: the dictionary of score sheets.
    :return: that same dictionary but fully filled here by all possible items to select from which its key will be the
            counter number while counting.

    As this function is just the continuation of the above function for the lower section, it was doc tested as a whole
    in the function above and will be unit tested as one unit because it will be called from its parent.
    """
    print(f'\n---------------Lower Section Items---------------')
    for key, value in scores['lower_section'].items():
        # important: special case for making Yahtzee selectable once more after it was gained OR for other None values
        if mode == 'select' and ((key == 'Yahtzee' and scores['lower_section']['Yahtzee'] == 50) or value is None):
            print(f'Enter \033[32m{counter}\033[00m to choose {key} for this turn.')
            dictionary_of_options[counter] = key
            counter += 1

        elif value is None and mode == 'print':  # items not chosen before and mode is a simple "print" of score board.
            print(f'For {key} you have not gained any points yet.')
        else:  # items chosen before and mode is either a simple "print" of score sheet or with selectable numbers.
            print(f'\033[34mFor {key} you have already gained {value} points.\033[00m')
    print(f'\n---------------Lower Section Results---------------')
    print(f'For Yahtzee Bonus you have gained {scores["Yahtzee Bonus"]} points.')
    print(f'For Total of Lower Section you have gained {scores["Total of Lower Section"]} points.')
    print(f'For Grand Total you have gained {scores["Grand Total"]} points.\n')

    return dictionary_of_options


def get_valid_option(options: dict) -> str:
    """
    Return the selected numbered item from the given dictionary by user input.

    :precondition: the given dictionary must have sequential keys starting from 1 which player can choose the preferred
                item from the score sheet which its value will be returned.
    :param options: a dictionary of numbered items still valid to choose from the score sheet.
    :return: a string representing the key of the chosen item.

    Unit tests were written as this function has both prints and inputs allowing user to select a valid option.
    """
    selected_item = input(f'Enter a valid option from these possible options equal or less than {len(options)}: ')
    try:
        return options[int(selected_item)]
    except (KeyError, ValueError):
        print('\033[91mThis is not one of the valid options! Try again\033[00m')
        # a recursion to finally get a choice from an available option in the score sheet. (Just to use a recursion)
        return get_valid_option(options)


def upper_section_calculator(chosen_dices: list, chosen_item: str) -> int:
    """
    Calculate the count*value of a given die face in a list of five dices for upper section scores.

    :param chosen_dices: a list of 5 dices with 6 faces from 1 to 6 in integer
    :param chosen_item: a string representing the face of a chosen die (e.g. Aces)
    :return: A number(integer) representing the count*value of chosen item.

    >>> dices = [4, 3, 4, 1, 4]
    >>> selected_item = 'Fours'
    >>> upper_section_calculator(dices, selected_item)
    <BLANKLINE>
    [32mYou gained 12 points for Fours. It will be saved in your score sheet.[00m
    <BLANKLINE>
    12
    >>> dices = [4, 3, 4, 1, 4]
    >>> selected_item = 'Fives'
    >>> upper_section_calculator(dices, selected_item)
    <BLANKLINE>
    [32mYou gained 0 points for Fives. It will be saved in your score sheet.[00m
    <BLANKLINE>
    0
    """
    # Aces -> index + 1 = 1 -> result = 1 * number of Aces(ones)
    chosen_face_in_integer = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes'].index(chosen_item) + 1

    result = chosen_face_in_integer * chosen_dices.count(chosen_face_in_integer)

    print(f'\n\033[32mYou gained {result} points for {chosen_item}. It will be saved in your score sheet.\033[00m\n')
    return result


def lower_section_calculator(faces_of_dices: list, chosen_item: str) -> int:
    """
    Calculate a 'fixed value' or 'sum' in a list of five dices based on their regex for lower section scores.

    :precondition: a list of 5 dices with 6 faces from 1 to 6 in integer would be able to create the satisfactory result
    :postcondition: if it will be met, the calculation of result/score will be passed based on the assumed rules.
    :param faces_of_dices: a list of 5 dices with 6 faces from 1 to 6 in integer
    :param chosen_item: a string representing the face of a possible set (e.g. Yahtzee, Four of a kind)
    :return: A number(integer) representing the calculated score (fix or sum) of chosen item.

    >>> chosen_dices = [4, 3, 4, 1, 4]
    >>> selected_item = 'Three of a kind'
    >>> lower_section_calculator(chosen_dices, selected_item)
    16
    >>> chosen_dices = [4, 3, 4, 1, 4]
    >>> selected_item = 'Four of a kind'
    >>> lower_section_calculator(chosen_dices, selected_item)
    0
    >>> chosen_dices = [4, 4, 4, 4, 4]
    >>> selected_item = 'Yahtzee'
    >>> lower_section_calculator(chosen_dices, selected_item)
    [32mYAAAAHTZEEEEE![00m
    50
    """
    lower_section_regex = LOWER_SECTION_REGEX_PATTERN()
    fixed_scores_in_lower_section = FIXED_SCORES()
    score = 0
    sorted_string_of_faces = ''.join(sorted([str(die) for die in faces_of_dices]))

    # lower_section_regex[0] is our single dictionary for regex patterns inside our tuple returned from CONSTANT func.
    if (re.compile(lower_section_regex[0][chosen_item])).search(sorted_string_of_faces):
        # fixed_scores_in_lower_section[0] is our single dictionary of fixed scores inside our tuple returned from that
        # CONSTANT function.
        if chosen_item in fixed_scores_in_lower_section[0]:
            if chosen_item == 'Yahtzee':
                print('\033[32mYAAAAHTZEEEEE!\033[00m')  # Hooray!

            # the line below will be executed for any found pattern based on user choice including Yahtzee, even if it
            # is not the first time that we receive 50 points for it (no need). Our bonus adder is somewhere else.
            score = fixed_scores_in_lower_section[0][chosen_item]

        else:  # other scores that are not fixed!
            for die in faces_of_dices:
                score += die
    return score


def score_calculator_engine(dices_list: list, scores: dict, selected_option: str) -> dict:
    """
    Calculate and write all the items on the score sheet for unselectable items and drive the calculation for selectable
    ones with the help of 2 helper functions.

    :precondition: the selected option must be previously checked in its designated own function for this purpose (the
        place to check if it is a free and selectable item is not here) The score board must be a well designed
        structure that was mentioned previously and the selected option must be a string representing an item inside one
        of its lower or upper section keys. (e.g. score_board['upper_section'][selected_option]). The dices list should
        also be a valid list of 5 6-faced dices.
    :postcondition: This function will correctly calculate the score of each selected item and also it will finally
        check and update for Yahtzee bonuses or upper section bonuses if it will be a case, upper and lower totals and
        finally will update the grand total in each turn.
    :param dices_list: a list of 5 integers representing faces of our 6-faces dices.
    :param scores: a dictionary representing our score sheets.
    :param selected_option: a string representing a key of selectable items in upper and lower sections items.
    :return: an updated dictionary representing our score sheets based on the new selected item and the changes in other
        values/scores like totals and bonuses.

    >>> option = 'Fives'
    >>> dices = [5, 4, 1, 5, 4]
    >>> score_sheet = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,\
    'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':\
    {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
    >>> score_calculator_engine(dices, score_sheet, option)
    <BLANKLINE>
    [32mYou gained 10 points for Fives. It will be saved in your score sheet.[00m
    <BLANKLINE>
    {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': 10, 'Sixes': None}, \
'Total Score': 27, 'Upper Section Bonus': 0, 'Total of Upper Section': 27, 'lower_section': {'Three of a kind': 20, \
'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None, 'Yahtzee': 50, \
'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 97}

    >>> option = 'Four of a kind'
    >>> dices = [4, 4, 1, 4, 4]
    >>> score_sheet = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,\
    'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':\
    {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
    >>> score_calculator_engine(dices, score_sheet, option)
    <BLANKLINE>
    [32mYou gained 17 points for Four of a kind. It will be saved in your score sheet.[00m
    <BLANKLINE>
    {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None, 'Sixes': None}, \
'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section': {'Three of a kind': 20, \
'Four of a kind': 17, 'Full house': None, 'Small Straight': None, 'Large Straight': None, 'Yahtzee': 50, \
'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 87, 'Grand Total': 104}

    # Yahtzee with a bonus point
    >>> option = 'Yahtzee'
    >>> dices = [4, 4, 4, 4, 4]
    >>> score_sheet = {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None,\
    'Sixes': None}, 'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section':\
    {'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None,\
    'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 0, 'Total of Lower Section': 70, 'Grand Total': 87}
    >>> score_calculator_engine(dices, score_sheet, option)
    [32mYAAAAHTZEEEEE![00m
    <BLANKLINE>
    [32mYou gained 100 points for Yahtzee. It will be saved in your score sheet.[00m
    <BLANKLINE>
    {'upper_section': {'Aces': None, 'Twos': 8, 'Threes': 9, 'Fours': None, 'Fives': None, 'Sixes': None}, \
'Total Score': 17, 'Upper Section Bonus': 0, 'Total of Upper Section': 17, 'lower_section': \
{'Three of a kind': 20, 'Four of a kind': None, 'Full house': None, 'Small Straight': None, 'Large Straight': None\
, 'Yahtzee': 50, 'Chance': None}, 'Yahtzee Bonus': 100, 'Total of Lower Section': 170, 'Grand Total': 187}
    """
    if selected_option in scores['upper_section']:  # calculate these after each turn if change is here
        scores['upper_section'][selected_option] = upper_section_calculator(dices_list, selected_option)
        scores['Total Score'] += scores['upper_section'][selected_option]

        scores['Upper Section Bonus'] = 35 if scores['Total Score'] > 62 else 0
        scores['Total of Upper Section'] = scores['Total Score'] + scores['Upper Section Bonus']

    elif selected_option == 'Yahtzee' and scores['lower_section']['Yahtzee'] == 50:  # special case
        scores['Yahtzee Bonus'] += 100 if lower_section_calculator(dices_list, selected_option) == 50 else 0

        scores['Total of Lower Section'] += scores['Yahtzee Bonus']
        print(f'\n\033[32mYou gained 100 points for {selected_option}. It will be saved in your score sheet.\033[00m\n')

    else: # calculate these after each turn if change is here
        scores['lower_section'][selected_option] = lower_section_calculator(dices_list, selected_option)
        print(f'\n\033[32mYou gained {scores["lower_section"][selected_option]} points for {selected_option}. '
              f'It will be saved in your score sheet.\033[00m\n')

        scores['Total of Lower Section'] += scores['lower_section'][selected_option]

    scores['Grand Total'] = scores['Total of Upper Section'] + scores['Total of Lower Section']
    return scores


def dice_generator(kept_faces: list, will_be_rolled_faces: list) -> tuple:
    """
    Generate a new list of faces based on the number of selected unwanted dices by the player.

    This function will also print the face of new randomly generated dices and the whole 5 dices based on the kept list
    after each roll.
    :param kept_faces: a list of kept dices
    :param will_be_rolled_faces: a list of unwanted dices which will be replaced by the newly generated ones.
    :return: a tuple containing a complete list of whole dices + a list of newly generated ones.
    """
    will_be_rolled_faces = random.choices(range(1, 7), k=len(will_be_rolled_faces))
    print('\nThe faces of your new dices are:', ', '.join([str(die) for die in will_be_rolled_faces]))

    list_of_dices = will_be_rolled_faces + kept_faces
    print('\n\033[32mThe full list of your dices are:', ', '.join([str(die) for die in list_of_dices]), '\033[00m')

    return list_of_dices, will_be_rolled_faces


def one_turn_engine(player_choice: str, new_dices: list, kept_dices: list, roll_number: int, score_sheet: dict) \
        -> tuple:
    """
    Drive the whole commands (printing of score sheets requests, selecting and rolling dices, and finally managing the
    players choice for selecting an option to receive scores) of each turn.


    This function will manage each given command inside its caller (turn_menu function) and returns back to get another
    command until a turn ends.

    :precondition: a well designed dictionary representing the design of this program in all stages which has two nested
            dictionaries inside of it representing selectable upper and lower section options. a roll number which won't
            pass 3. (starts from zero) The updated player choice in main menus after each stage checked to be between 1
            and 3. Two lists of 0-5 deices representing the faces of unwanted and kept dices.
    :postcondition: this function will return the updated score sheets, increased roll numbers, and updated lists of
    unwanted and kept dices after each stage of a turn to the turn starter(=menu) function.

    :param player_choice: a number (str) between 1 and 3 representing selecting and rolling dices OR printing of score
    sheets requests OR finally getting the players choice and calculating/updating the receive scores based on that.
    :param new_dices: a list representing the faces of rolled dices in each stage.
    :param kept_dices: a list representing the faces of kept dices in each stage.
    :param roll_number: an integer representing the number of times the player rolled the selected dices.
    :param score_sheet: a dictionary representing the score sheet of each player which will be updated finally.
    :return: a tuple containing 2 lists of kept and unwanted dices plus the score sheet and roll number. Note: This is
        necessary as this function will get back to menu and return after user commands in stages of each turn.
    """
    list_of_dices = new_dices + kept_dices
    if player_choice == '2':  # print a simple score sheet ("in print mode without adding option numbers)
        score_sheet_printer_selector(score_sheet, 'print')

    elif player_choice == '1':
        # as mentioned above, this function call needs returns because of this else statement for the first rolling
        # attempt:
        (new_dices, kept_dices) = dice_selector(new_dices, kept_dices) if roll_number != 0 else ([0, 0, 0, 0, 0], [])

        list_of_dices, new_dices = dice_generator(kept_faces=kept_dices, will_be_rolled_faces=new_dices)
        roll_number += 1

    # 3rd roll condition below will happen only if the last roll happens above without leaving this function for another
    # unnecessary loop and options "to print" or "to finish the turn soon" (the reason of using if instead of elif)
    if player_choice == '3' or roll_number == 3:
        print('Ok! Please enter one of these available options from the list below: ')
        all_possible_options = score_sheet_printer_selector(score_sheet, 'select')  # a call in "select" mode

        print('\n\033[32mThe full list of your dices are: ', ', '.join([str(die) for die in list_of_dices]), '\033[00m')
        selected_option = get_valid_option(all_possible_options)  # get a valid option from remaining options/scores.

        score_sheet = score_calculator_engine(list_of_dices, score_sheet, selected_option)  # calculate and print score
        score_sheet_printer_selector(score_sheet, 'print')

    # return these for another roll OR final score change (when roll == 3 or the player ends the turn sooner)
    return new_dices, kept_dices, roll_number, score_sheet


def turn_menu(score_sheet: dict) -> dict:
    """
    Get user commands and let helper function (engine) act based on user preferences in each stage of rolling the dices.

    :precondition: a well designed dictionary representing the design of this program in all stages which has two nested
            dictionaries inside of it representing selectable upper and lower section options.
    :postcondition: this function will return the updated score sheet after each turn to the main function.
    :param score_sheet: a dictionary representing the score sheet of each player.
    :return: a dictionary representing the updated score sheet of each player after each turn.
    """
    kept_dices, newly_generated_dices, player_choice, roll_number = [], [0, 0, 0, 0, 0], None, 0

    while player_choice != '1':  # just the beginning of each turn until the player selects 1 to start rolling.
        player_choice = input('Enter 1 to Roll your dices\nEnter 2 to Print your score sheet\n1-2? ')
        if player_choice not in ['1', '2']:
            print('\033[91mThis is not one of the valid options!\033[00m')
        if player_choice == '2':
            score_sheet_printer_selector(score_sheet, 'print')

    # a turn will begin until it ends after 3 rolls or a sooner request. Each time menu below will be printed for input:
    while roll_number < 3 and player_choice != '3':
        if roll_number != 0:  # This menu is not needed before the first roll
            player_choice = input('Enter 1 to Select and Roll your dices\nEnter 2 to Print your score sheet\n'
                                  'Enter 3 to End this Turn soon (Selecting one option based on current dices)\n1-3? ')

        if player_choice not in ['1', '2', '3']:
            print('\033[91mThis is not one of the valid options!\033[00m')
        # for a new roll, printing the score sheet or calculating scores and ending the turn in this while loop
        else:  # call the engine and return back for another menu selection (until roll_number = 3 or player_choice =3)
            newly_generated_dices, kept_dices, roll_number, score_sheet = \
                    one_turn_engine(player_choice, newly_generated_dices, kept_dices, roll_number, score_sheet)

    return score_sheet


def player_1_score_sheet() -> dict:
    """
    Return Player 1 Score sheet.

    :return: A nested dictionary representing the first player's upper and lower section scores inside additional
        dictionaries, plus bonuses and totals inside the main one.
    """
    first_sheet = {'upper_section': {'Aces': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None,
                                     'Sixes': None},
                   'Total Score': 0, 'Upper Section Bonus': 0, 'Total of Upper Section': 0,
                   'lower_section': {'Three of a kind': None, 'Four of a kind': None, 'Full house': None,
                                     'Small Straight': None, 'Large Straight': None, 'Yahtzee': None, 'Chance': None},
                   'Yahtzee Bonus': 0, 'Total of Lower Section': 0, 'Grand Total': 0}
    return first_sheet


def player_2_score_sheet() -> dict:
    """
    Return Player 2 Score sheet.

    :return: A nested dictionary representing the second player's upper and lower section scores inside additional
        dictionaries, plus bonuses and totals inside the main one.
    """
    second_sheet = {'upper_section': {'Aces': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None,
                                      'Sixes': None},
                    'Total Score': 0, 'Upper Section Bonus': 0, 'Total of Upper Section': 0,
                    'lower_section': {'Three of a kind': None, 'Four of a kind': None, 'Full house': None,
                                      'Small Straight': None, 'Large Straight': None, 'Yahtzee': None, 'Chance': None},
                    'Yahtzee Bonus': 0, 'Total of Lower Section': 0, 'Grand Total': 0}
    return second_sheet


def main():
    """
    Drive the game by passing the score sheets to menus and engines in each turn until declaring the winner when game
    will be over.
    :postcondition: the winner (or a tie) will be declared correctly with the gained grand total score.
    """
    score_sheet_1, score_sheet_2 = player_1_score_sheet(), player_2_score_sheet()
    game = 'Began'
    while game != 'Over':
        # Run each of the first if-statements (individually/separate ifs) until the third condition will be met:
        if None in score_sheet_1['upper_section'].values() or None in score_sheet_1['lower_section'].values():
            print('\n\033[91mJules Turn\033[00m')
            score_sheet_1 = turn_menu(score_sheet_1)

        if None in score_sheet_2['upper_section'].values() or None in score_sheet_2['lower_section'].values():
            print('\n\033[91mBack to Jim\033[00m')
            score_sheet_2 = turn_menu(score_sheet_2)

        if None not in score_sheet_1['upper_section'].values() and None not in score_sheet_2['upper_section'].values() \
                and None not in score_sheet_1['lower_section'].values() \
                and None not in score_sheet_2['lower_section'].values():
            game = 'Over'  # no remaining Nones in each players upper and lower sections

    if score_sheet_1['Grand Total'] > score_sheet_2['Grand Total']:
        print(f'\n\033[91mCongratulation Jules! You won this game by {score_sheet_1["Grand Total"]} points\033[00m')
    elif score_sheet_1['Grand Total'] < score_sheet_2['Grand Total']:
        print(f'\n\033[91mCongratulation Jim! You won this game by {score_sheet_2["Grand Total"]} points\033[00m')
    else:
        print(f'\n\033[91mA Tie with {score_sheet_2["Grand Total"]} points!\033[00m')


if __name__ == "__main__":
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
    main()

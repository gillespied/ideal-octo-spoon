from .load_dictionaries import number_dict, tens_dict


def number_to_word(number):
    """Returns a string containing the number spelled out in words.
    Arguments:
        number -- an int, float or parse-able string.
    Returns:
        str -- the number spelled out.
    """

    # before proceeding further, check if the input is valid
    number = validate_input(number)

    # check if the number is negative
    number, minus = is_negative(number)

    # parse digits before the decimal place
    before = before_the_point(number)

    # parse number after decimal
    after = after_the_point(number)

    # combine all the strings
    number_in_words = (minus + before + after).strip()

    return number_in_words


def validate_input(number):
    """Checks if number is valid.
    Arguments:
        number {float or int} -- a validated number.
    """
    assert isinstance(number, (float, int, str)), \
        "Number must be an int, float or string which parses"

    if isinstance(number, str):

        try:
            number = float(number)

        except ValueError as err:
            print("Could not convert string to a number", err)

    if int(number) == float(number):
        # no decimal places, convert string to integer
        number = int(number)
    else:
        number = float(number)

    max_number = max([int(x) for x in list(tens_dict.keys())])
    assert number < 100*(10**max_number), \
        "Number must be less than 999*10**{}".format(max_number)

    return number


def is_negative(number):
    """Checks if number is negative, returns the absolute value and a string
    describing its sign.
    Arguments:
        number {float or int} -- a negative or positive number.
    Returns:
        number -- the absolute value of the number
        negative -- the string 'minus ' if number < 0 else an empty string.
    """

    if number < 0:
        number = abs(number)
        negative = 'minus '
    else:
        negative = ''

    return number, negative


def before_the_point(number):
    """Returns words spelling out the number supplied.
    Arguments:
        number {float or int} -- number to be spelled out.
        tens_dict {[type]} -- dictionary containing words for 10**(3x).
        number_dict {[type]} -- dict of english numbers to words.
    Returns:
        str-- words spelling out the number supplied.
    """

    # ensure no decimal places, cast to int.
    number = int(number)

    # find the highest 10**3 in the number
    highest_ten_three = len(str(number)) // 3

    # use it to find the modifier list
    list_of_tens = [tens_dict[str(x)]
                    for x in range(highest_ten_three * 3, -1, -3)]

    # use integer floor division to separate the number
    # into group of up to three numbers
    groups_of_three = [(number // 10 ** (i * 3)) % 1000
                       for i in range(highest_ten_three, -1, -1)]

    merged_lists = merge_before_point(groups_of_three, list_of_tens)

    words = " ".join(merged_lists)

    return words


def merge_before_point(groups_of_three, list_of_tens):
    """Merges lists of numbers with 10**3 modifier words.
    Arguments:
            groups_of_three {list(int)} -- a list containing numbers
            between 0-999.
            list_of_tens {list(str)} -- a list of word describing
            number suffixes
            number_dict {dict} -- a dictionary of english numbers 0-100
    Returns:
            merged_lists {list} -- the merged list
    """

    assert type(groups_of_three) is list, "Groups of three must be a list"
    assert type(list_of_tens) is list, "List of tens must be a list"

    merged_list = list()

    for index, item in enumerate(groups_of_three):

        # if the group is empty, ignore unless its the last
        # group
        if item > 0 or index == len(groups_of_three) - 1:
            merged_list.append(parse_three(item))
            merged_list.append(list_of_tens[index])

    return merged_list


def parse_three(number):
    """Return numbers from 0-999 as words.
    Arguments:
        number {int} -- an integer between 0 and 999.
        number_dict {dict} -- a dictionary containing
        english words for numbers.
    Returns:
        words {str} -- a string containing the words as numbers.
    """

    assert 0 <= number < 1000, "Number must be in range [0-1000]"
    # separate the group into hundreds, tens, units
    hundreds = number // 100
    tens = (number - hundreds * 100) // 10
    ones = (number - hundreds * 100 - tens * 10)

    words = list()

    # if any hundreds exist, look up the number in the dictionary
    if hundreds > 0:
        words.append(number_dict[str(hundreds)])
        words.append('hundred')

    if tens > 1 and ones is not 0:
        words.append(number_dict[str(tens * 10)])
        words.append(number_dict[str(ones)])

    elif tens <= 1 and ones > 0:
        words.append(number_dict[str(tens * 10 + ones)])

    elif tens >= 1 and ones is 0:
        words.append(number_dict[str(tens * 10)])

    elif hundreds is 0 and tens is 0 and ones is 0:
        words.append(number_dict[str(0)])
    else:
        ""

    words = " ".join(words)

    return words


def after_the_point(number):
    """Returns words describing the numbers after the decimal point.
    Arguments:
        number {float} -- number to be converted to words.
        number_dict {dict} -- dictionary of english words corresponding to numbers.
    Returns:
        str -- String containing words spelling out the number supplied
    """

    # if the number has digits after the decimal place, use list comprehension
    # to look up the values in the numberDict
    if number % 1 > 0:
        words = 'point ' + ' '.join(
            [number_dict[num] for num in str(number).split('.')[1]])
    else:
        words = ''

    return words

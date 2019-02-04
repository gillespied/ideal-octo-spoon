"""Returns dictionaries of english words for numbers.

Returns:
number_dict -- a dictionary of numbers as english words
tens_dict -- a dictionary of modifiers for english words, e.g., millions
"""
number_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
}

tens_dict = {
    '0': '',
    '1': 'ten',
    '2': 'hundred',
    '3': 'thousand',
    '6': 'million',
    '9': 'billion',
    '12': 'trillion',
}


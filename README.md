# number_to_word
[![Build Status](https://travis-ci.org/gillespied/ideal-octo-spoon.svg?branch=master)](https://travis-ci.org/gillespied/ideal-octo-spoon)

A package for converting numbers to english words, e.g., 

```python
from number_to_word import number_to_word

number_to_word.number_to_word(111)
```

returns

```python
'one hundred eleven'
```

Inputs must be float, int or a castable string, e.g., `'111'`, not `a string`

# Install

To install clone the directory, change directory and run `setup.py`. Run tests with `pytest`.

```bash
git clone https://github.com/gillespied/number_to_word.git
cd number_to_word
python setup.py -q install
pytest
```


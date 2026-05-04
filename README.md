# basic-python-project

Small collection of beginner Python utility scripts and exercises.

Badges
------

[![Python CI](https://github.com/ali-ezz/basic-python-project/actions/workflows/python-ci.yml/badge.svg)](https://github.com/ali-ezz/basic-python-project/actions)
[![CodeQL](https://github.com/ali-ezz/basic-python-project/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/ali-ezz/basic-python-project/actions)
[![Coverage Status](https://codecov.io/gh/ali-ezz/basic-python-project/branch/main/graph/badge.svg)](https://codecov.io/gh/ali-ezz/basic-python-project)
[![Release](https://img.shields.io/github/v/release/ali-ezz/basic-python-project?color=brightgreen)](https://github.com/ali-ezz/basic-python-project/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Overview
--------

This repository contains a few small utilities:

- `from_roman_to_english.py` - convert Roman numerals to integers (`roman_to_int`).
- `max_number.py` - simple `find_max` helper.
- `number_to_words.py` - convert digits to spoken words.
- `roll_dice.py` - small `Dice` class that rolls six-sided dice.
- `sigma.py` - tiny example returning the string "sigma".
- `symbol_to_emoji.py` - map text emoticons to emoji characters.

Getting started
---------------

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install test dependencies:

```bash
pip install -r requirements.txt
```

Running tests
-------------

Run the test suite with:

```bash
pytest -q
```

Contributing
------------

See `CONTRIBUTING.md` for guidelines on submitting issues and pull requests.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.

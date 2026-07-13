# Interactive Password Generator

A simple Python command-line script to generate randomized passwords based on your choice of character sets.

## Features

- Choose any password length.
- Mix and match specific character types: numbers, symbols, lowercase, or uppercase letters.
- Quick shortcut to include all character sets at once.
- Continuous loop to generate multiple passwords without restarting.

## Requirements

- Python 3.x (uses built-in `random` module, no installations needed)

## How to Use

1. Run the script:
   ```bash
   python password_generator.py
   ```
2. Enter your desired password length.
3. Choose your character sets by typing their numbers together (e.g., type `12` for numbers + symbols, or `1234` for everything).

### Character Options
- `1` = Numbers (`1234567890`)
- `2` = Symbols (`!@#$%^&*`)
- `3` = Lowercase letters (`a-z`)
- `4` = Uppercase letters (`A-Z`)
- `5` = All characters combined

4. Type `y` to generate another password, or `n` to exit.

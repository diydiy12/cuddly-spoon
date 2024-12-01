"""
This program searches for the index of the first occurrence of a search string (needle) in a text
string (haystack) using a naive search algorithm.
"""
__author__ = "7273843, Muhsen"


print("Given the Code: ['😅', '🎲', '🎯', '🥰', '🎮', '🧗', '🐯', '🎴', '🦁', '🎨'], please solve the "
      "following puzzle:")

a = int(input("Please give here the a first number/integer for the puzzle: "))
b = int(input("Please give here the your second number/integer for the puzzle: "))

def puzzle(a, b):
    code = ['😅', '🎲', '🎯', '🥰', '🎮', '🧗', '🐯', '🎴', '🦁', '🎨']

    def integer_to_symbol(number):
        list_of_symbols = "".join(code[int(digit)] for digit in str(number))
        return list_of_symbols

    a_symbols = integer_to_symbol(a)
    b_symbols = integer_to_symbol(b)
    c = a + b
    c_symbols = integer_to_symbol(c)

    return f"{a_symbols} + {b_symbols} = {c_symbols}"

print(puzzle(a, b))
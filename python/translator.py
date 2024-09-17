import sys

braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

braille_num = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital_indicator = '.....O'
number_indicator = '.O.OOO'

english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_num = {v: k for k, v in braille_num.items()}

def detect_input_type(input_str):
    if all(c in 'O.' for c in input_str):
        return 'braille'
    else:
        return 'english'

def english_to_braille(input_str):
    translated = []
    number_mode = False

    for char in input_str:
        if char.isdigit():
            if not number_mode:
                translated.append(number_indicator)
                number_mode = True
            translated.append(braille_num[char])
        elif char.isalpha():
            if char.isupper():
                translated.append(capital_indicator)
            translated.append(braille_alphabet[char.lower()])
            number_mode = False
        elif char == ' ':
            translated.append('......')
            number_mode = False
        else:
            translated.append('?')

    return ''.join(translated)

def braille_to_english(input_str):
    translated = []
    capitalize_next = False
    number_mode = False

    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i+6]

        if braille_char == capital_indicator:
            capitalize_next = True
            continue
        elif braille_char == number_indicator:
            number_mode = True
            continue
        elif braille_char == '......':
            translated.append(' ')
            continue

        if number_mode:
            if braille_char in english_num:
                translated.append(english_num[braille_char])
            number_mode = False
        elif braille_char in english_alphabet:
            char = english_alphabet[braille_char]
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            translated.append(char)
        else:
            translated.append('?')

    return ''.join(translated)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input_string>")
        return

    # Join all arguments into a single input string
    input_str = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_str)

    if input_type == 'english':
        output = english_to_braille(input_str)
    else:
        output = braille_to_english(input_str)
    
    print(output)


if __name__ == '__main__':
    main()

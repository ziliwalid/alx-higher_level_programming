def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev = 0

    for symbol in roman_string:
        value = roman_numerals.get(symbol, 0)
        if value > prev:
            result += value - 2 * prev
        else:
            result += value
        prev = value

    return result


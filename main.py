numbers = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}
number_notation = {
    0: '',
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trillion',
    5: 'quadrillion',
    6: 'quintillion',
    7: 'sextillion',
    8: 'septillion',
    9: 'octillion'
}


def number_to_3_element_boards(x: str) -> list:
    length, number, fr = len(x) - 1, [], []
    for _ in x:
        if len(fr) == 3:
            fr.reverse()
            number.append(fr)
            fr = []
        fr.append(x[length])
        length += -1
    fr.reverse()
    number.append(fr)
    number.reverse()
    return number


def transform_the_array_into_a_readable_version(array: list) -> list:
    result = []
    for i in array:
        i_segment = []
        if len(i) == 3:
            if i[0] != '0':
                i_segment.extend((f'{i[0]}', '100'))
            else:
                i_segment.append('0')
            if i[1] != '1' and i[1] != '0':
                i_segment.extend((f'{"" if i[1] == "0" else i[1] + "0"}', f'{i[2]}'))
            else:
                i_segment.append(f'{i[1] + i[2]}')
            result.append(i_segment)
        elif len(i) == 2:
            if i[0] != '1' and i[0] != '0':
                i_segment.extend((f'{"" if i[0] == "0" else i[0] + "0"}', f'{i[1]}'))
            else:
                i_segment.append(i[0] + i[1])
            result.append(i_segment)
        else:
            result.append([i[0]])
    return result


def numbers_to_word(num: list) -> str:
    lenght = len(x) - 1
    number = []
    for i in num:
        for g in i:
            try:
                if i[0] != '0' and i[1] != '00':
                    number.append(numbers.get(int(g)))
                    number.append(number_notation.get(lenght))
            except IndexError:
                number.append(numbers.get(int(g)))
                number.append(number_notation.get(lenght))

        lenght -= 1
    return " ".join(" ".join(number).split())


x = '10000'
print(x)
print(numbers_to_word(transform_the_array_into_a_readable_version(number_to_3_element_boards(x))))

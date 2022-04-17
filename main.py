numbers = {
    0: 'zero',
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
    1000: 'thousand',
}

'''
1231 -> 1 1000 2 100 30 1
6578 -> 6 1000 5 100 70 8
1012 -> 1 1000 12
9313 -> 9 1000 3 100 13

1231 ->1321 -> 123 1 ->1 
'''
x = '20111'


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


arr = number_to_3_element_boards(x)
print(arr)

def transform_the_array_into_a_readable_version(array: list) -> list:
    for i in array:
        fial = []
        if len(i) == 3:
            if i[0] != '0':
                fial.extend((f'{i[0]}', '100'))
            else:
                fial.append('0')
            if i[1] != '1' and i[1] != '0':
                fial.extend((f'{"" if i[1] == "0" else i[1] + "0"}', f'{i[2]}'))
            else:
                fial.append(f'{i[1] + i[2]}')
            print(fial)
        elif len(i) == 2:
            if i[0] != '1' and i[0] != '0':
                fial.extend((f'{"" if i[0] == "0" else i[0] + "0"}', f'{i[1]}'))
            else:
                fial.append(i[0] + i[1])
            print(fial)

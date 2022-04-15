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


def split_number(x):
    zero = ''.join(['0' for _ in range(len(x) - 1)])
    number = []
    print(x)
    for i in x:
        if i != '0':
            number.append(i)
            if len(zero) >= 2:
                number.append('1' + zero)
            if len(zero) == 1:
                number.pop()
                number.append(i+zero)
        else:
            number.append('0')
        zero = zero[:-1]
        print(number)
    return number


if __name__ == '__main__':
    x = '142'
    number = split_number(x)
    print(number)
    fin = []
    for i in number:
        if i != '0':
            fin.append(numbers.get(int(i)))
    print(" ".join(fin))

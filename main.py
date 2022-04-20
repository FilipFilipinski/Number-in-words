from data import *


def number_to_3_element_boards(array: str) -> list:
    length, number, three_element_array = len(array) - 1, [], []
    for _ in array:
        if len(three_element_array) == 3:
            three_element_array.reverse()
            number.append(three_element_array)
            three_element_array = []
        three_element_array.append(array[length])
        length += -1
    three_element_array.reverse()
    number.append(three_element_array)
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
    length, number = len(num) - 1, []
    for i in num:
        multiples = 0
        for g in i:
            try:
                if i[0] != '0' and i[1] != '00':
                    number.append(numbers.get(int(g)))
                    if i[-1] == g:
                        if i[0] == i[-1]:
                            if multiples == 1:
                                number.append(number_notation.get(length))
                            else:
                                multiples += 1
                        else:
                            number.append(number_notation.get(length))

                elif i[0] == '0' and i[0] == g:
                    number.append(numbers.get(int(i[1])))
                    if i[-1] != '00':
                        try:
                            number.append(numbers.get(int(i[2])))
                        except IndexError:
                            pass
                        number.append(number_notation.get(length))
            except IndexError:
                number.append(numbers.get(int(g)))
                number.append(number_notation.get(length))

        length -= 1
    return " ".join(" ".join(number).split())


def main(x: str) -> str:
    b = number_to_3_element_boards(x)
    a = transform_the_array_into_a_readable_version(b)
    result = numbers_to_word(a)
    #print(a)
    return result


def test():
    assert main('1') == 'one', "Should be one"
    assert main('11') == 'eleven', "Should be eleven"
    assert main('21') == 'twenty one', "Should be eleven"
    assert main('1101') == 'one thousand one hundred one', "Should be one thousand one hundred one"
    assert main('110101') == 'one hundred ten thousand one hundred one'
    assert main('100002') == 'one hundred thousand two'
    assert main('1002001') == 'one million two thousand one'
    assert main('12123123') == 'twelve million one hundred twenty three thousand one hundred twenty three'
    assert main('100120003') == 'one hundred million one hundred twenty thousand three'
    assert main('121212122') == 'one hundred twenty one million two hundred twelve thousand one hundred twenty two'

    print("Everything passed")


if __name__ == '__main__':
    test()

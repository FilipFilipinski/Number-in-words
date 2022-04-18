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
        for g in i:
            try:
                if i[0] != '0' and i[1] != '00':
                    number.append(numbers.get(int(g)))
                    if i[3] == g:
                        number.append(number_notation.get(length))
                elif i[0] == '0' and i[0] == g:
                    number.append(numbers.get(int(i[1])))
                    if i[1] != '00':
                        number.append(number_notation.get(length))
            except IndexError:
                number.append(numbers.get(int(g)))
                number.append(number_notation.get(length))

        length -= 1
    return " ".join(" ".join(number).split())


def main(x: str) -> str:
    b = number_to_3_element_boards(x)
    print(b)
    a = transform_the_array_into_a_readable_version(b)
    print(a)
    result = numbers_to_word(a)
    print(result)
    return result


if __name__ == '__main__':
    print(main('1123213123123123123123'))

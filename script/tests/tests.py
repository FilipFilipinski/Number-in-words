from script.main import *


def test():
    assert main_script('1') == 'one', "Should be one"
    assert main_script('11') == 'eleven', "Should be eleven"
    assert main_script('21') == 'twenty one', "Should be twenty one"
    assert main_script('1101') == 'one thousand one hundred one', "Should be one thousand one hundred one"
    assert main_script('110101') == 'one hundred ten thousand one hundred one'
    assert main_script('100002') == 'one hundred thousand two'
    assert main_script('1002001') == 'one million two thousand one'
    assert main_script('12123123') == 'twelve million one hundred twenty three thousand one hundred twenty three'
    assert main_script('100120003') == 'one hundred million one hundred twenty thousand three'
    assert main_script('121212122') == 'one hundred twenty one million two hundred twelve thousand one hundred twenty two'
    print('APPA HOP HOP, tests passed')


if __name__ == '__main__':
    test()

"""
This program split given large number into hundreds, tens and units.
"""


def split_number(num):
    result = []
    i = 10
    while num > 0:
        c = num % i
        num = num - c
        i = i*10
        result.append(c)
    return list(reversed(result))


if __name__ == '__main__':
    print(__doc__)

    test_cases = [
        (1, [1]),
        (1025, [1000,0,20,5]),
    ]

    for testnum, test in enumerate(test_cases):
        inp = test[0]
        expected = test[1]
        result = split_number(test[0])
        print('test number: {}; input: {}; expected output: {}; actual output: {}'.format(
            testnum, inp, expected, result))
        if expected == result:
            print('SUCCESS')
        else:
            print('ERROR')

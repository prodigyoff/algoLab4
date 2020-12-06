import re


def fill_list_of_degrees(number: int, binary_number_length: int):
    """
    Returns list of binary degrees from given decimal number

    >>> fill_list_of_degrees(5, 7)
    ['1111101', '11001', '101', '1']
    >>> fill_list_of_degrees(5, 9)
    ['1001110001', '1111101', '11001', '101', '1']

    """
    degrees = ['1']
    for i in range(binary_number_length):
        if len(degrees[i]) >= binary_number_length:
            break
        degrees.append(bin(number ** (i + 1))[2:])
    degrees.reverse()
    return degrees


def fantz(binary_number: str, number: int):
    """
    Running through testcases given in task and a few edge cases.
    Returns optimal number of replaces needed to represent given binary number as a few degrees of decimal number

    >>> fantz('101101101', 5)
    3
    >>> fantz('1111101', 5)
    1
    >>> fantz('110011011', 5)
    3
    >>> fantz('100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001', 7)
    5
    >>> fantz('0', 5)
    0
    >>> fantz('00001', 5)
    1
    >>> fantz('101110011', 5)
    3
    """
    binary_number = binary_number.lstrip('0')
    counter = 0
    degrees = fill_list_of_degrees(number, len(binary_number))

    for degree in degrees:
        result_number, replaces_amount = re.subn(degree, '', binary_number)
        if replaces_amount == 0:
            continue
        binary_number = result_number
        counter += replaces_amount
        if binary_number == '':
            break
    if binary_number != '':
        return -1
    return counter


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

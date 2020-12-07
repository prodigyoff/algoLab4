import re


def fill_list_of_powers(decimal_number: int, binary_number_length: int):
    """
    Returns list of binary powers from given decimal number

    >>> fill_list_of_powers(5, 7)
    ['1111101', '11001', '101', '1']
    >>> fill_list_of_powers(5, 9)
    ['1001110001', '1111101', '11001', '101', '1']

    """
    powers_list = ['1']
    for i in range(binary_number_length):
        if len(powers_list[i]) >= binary_number_length:
            break
        powers_list.append(bin(decimal_number ** (i + 1))[2:])
    powers_list.reverse()
    return powers_list


def fantz(binary_number: str, decimal_number: int):
    """
    Running through testcases given in task and a few edge cases.
    Returns optimal number of replaces needed to represent given binary number as a few powers of decimal number

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
    replaces_counter = 0
    powers = fill_list_of_powers(decimal_number, len(binary_number))

    for power in powers:
        result_number, replaces_amount = re.subn(power, '', binary_number)
        if replaces_amount == 0:
            continue
        binary_number = result_number
        replaces_counter += replaces_amount
        if binary_number == '':
            break
    if binary_number != '':
        return -1
    return replaces_counter


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()

import re


def fill_list_of_powers(decimal_number: int, binary_number_length: int):
    powers_list = ['1']
    for i in range(binary_number_length):
        if len(powers_list[i]) >= binary_number_length:
            break
        powers_list.append(bin(decimal_number ** (i + 1))[2:])
    powers_list.reverse()
    return powers_list


def fantz(binary_number: str, decimal_number: int):
    binary_number = binary_number.lstrip('0')
    if len(binary_number) == 0:
        return -1
    replaces_counter = 0
    powers = fill_list_of_powers(decimal_number, len(binary_number))

    for power in powers:
        result_number, replaces_amount = re.subn(power, '', binary_number)
        if replaces_amount == 0:
            continue
        binary_number = result_number
        replaces_counter += replaces_amount
        if len(binary_number) == 0:
            break
    if len(binary_number) != 0:
        return -1
    return replaces_counter

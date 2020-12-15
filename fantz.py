def fill_list_of_powers(decimal_number: int, binary_number_length: int) -> list:
    powers_list = ['1']
    for i in range(binary_number_length):
        if len(powers_list[i]) > binary_number_length:
            powers_list.reverse()
            return powers_list[1:]
        powers_list.append(bin(decimal_number ** (i + 1))[2:])
    powers_list.reverse()
    return powers_list[1:]


def any_power_in_remainder(powers: list, binary_number: str) -> bool:
    if binary_number.replace('_', '') == '':
        return True
    for power in powers:
        if power in binary_number and len(power) <= len(binary_number):
            return True
    return False


def last_element_check(binary_number: str, rest: str) -> bool:
    if not rest:
        return True
    if binary_number[-1] == rest[-1] or rest.count('1') == len(rest):
        return True
    return False


def fantz(binary_number: str, decimal_number: int) -> int:
    powers: list = fill_list_of_powers(decimal_number, len(binary_number))
    replaces_counter: int = 0
    for power in powers:
        if len(power) > len(binary_number):
            continue
        if power in binary_number:
            if (secondary_replaces_counter := binary_number.count(power)) \
                    and any_power_in_remainder(powers, rest := binary_number.replace(power, '_')) \
                    and (len(rest) < 2 or last_element_check(binary_number.replace('_', ''), rest.replace('_', ''))):
                binary_number = rest
                replaces_counter += secondary_replaces_counter

    binary_number = binary_number.replace('_', '')
    if replaces_counter == 0 or binary_number:
        return -1
    return replaces_counter


def fantz_launcher(binary_number: str, decimal_number: int) -> int:
    binary_number = binary_number.lstrip('0')
    if not binary_number:
        return -1
    elif len(binary_number) == 1:
        return 1
    else:
        return fantz(binary_number, decimal_number)

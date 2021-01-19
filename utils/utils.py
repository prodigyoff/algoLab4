from typing import Tuple


def file_reader(file_location: str) -> Tuple[str, int]:
    with open(file_location, 'r') as fileIn:
        binary_number, decimal_number = fileIn.readline().split()
    return binary_number, decimal_number


def file_writer(file_location: str, result: int) -> None:
    with open(file_location, 'w') as fileOut:
        fileOut.write(str(result))

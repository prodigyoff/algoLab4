from fantz import *
from utils.utils import file_reader, file_writer

INPUT_FILE_LOCATION = 'data/fantz1.in'
OUTPUT_FILE_LOCATION = 'fantz.out'

if __name__ == '__main__':
    binary_number, decimal_number = file_reader(INPUT_FILE_LOCATION)
    result = fantz_launcher(str(binary_number), int(decimal_number))
    print(f'Binary number: {binary_number}  Decimal number: {decimal_number} \n'
          f'Replaces amount: {result}')
    file_writer(OUTPUT_FILE_LOCATION, result)

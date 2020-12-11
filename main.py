from fantz import *

INPUT_FILE_LOCATION = 'data/fantz.in'
OUTPUT_FILE_LOCATION = 'data/fantz.out'

if __name__ == '__main__':
    binary_numbers = ['101101101', '1111101', '110011011',
                      '101110011']
    decimal_number = 5
    for i in range(len(binary_numbers)):
        print(f'Binary number: {binary_numbers[i]}  Decimal number: {decimal_number} \n'
              f'Replacements amount:  {fantz_launcher(binary_numbers[i], decimal_number)}')

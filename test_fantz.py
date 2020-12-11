import unittest
from fantz import *
from utils.utils import file_reader, file_writer


class TestFantz(unittest.TestCase):

    def testFantzTaskCases(self):
        binary_number, decimal_number = file_reader('data/fantz2.in')
        self.assertEqual(1, fantz_launcher(str(binary_number), int(decimal_number)))
        binary_number, decimal_number = file_reader('data/fantz3.in')
        self.assertEqual(3, fantz_launcher(str(binary_number), int(decimal_number)))
        binary_number, decimal_number = file_reader('data/fantz4.in')
        self.assertEqual(5, fantz_launcher(str(binary_number), 7))

    def testFantzIncorrectInputCases(self):
        self.assertEqual(-1, fantz_launcher('0', 5))
        self.assertEqual(1, fantz_launcher('00001', 5))

    def testFantzEdgeCases(self):
        self.assertEqual(5, fantz_launcher('101111101', 5))
        self.assertEqual(-1, fantz_launcher('11111100', 2))
        self.assertEqual(-1, fantz_launcher('10101', 5))
        self.assertEqual(-1, fantz_launcher('10110011', 5))

    def testFillListOfPowers(self):
        self.assertEqual(['1111101', '11001', '101', '1'], fill_list_of_powers(5, 7))
        self.assertEqual(['1001110001', '1111101', '11001', '101', '1'], fill_list_of_powers(5, 10))

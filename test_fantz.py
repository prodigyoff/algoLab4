import unittest
from fantz import *


class TestFantz(unittest.TestCase):

    def testFantzTaskCases(self):
        self.assertEqual(3, fantz_launcher('101101101', 5))
        self.assertEqual(1, fantz_launcher('1111101', 5))
        self.assertEqual(3, fantz_launcher('110011011', 5))
        self.assertEqual(5, fantz_launcher(
            '100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001',
            7))
        self.assertEqual(3, fantz_launcher('101110011', 5))

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

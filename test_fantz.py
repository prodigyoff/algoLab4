import unittest
from fantz import *


class TestFantz(unittest.TestCase):

    def testFantz(self):
        self.assertEqual(fantz('0', 5), -1)
        self.assertEqual(fantz('00001', 5), 1)
        self.assertEqual(fantz('101101101', 5), 3)
        self.assertEqual(fantz('1111101', 5), 1)
        self.assertEqual(fantz('10011101111010010011111011001110010100011110010111001000110'
                               '0111011110100100111110110011100101000110010110000111100101110010001',
                               7), 5)
        self.assertEqual(fantz('101110011', 5), 3)

    def testFillListOfPowers(self):
        self.assertEqual(fill_list_of_powers(5, 7), ['1111101', '11001', '101', '1'])
        self.assertEqual(fill_list_of_powers(5, 9), ['1001110001', '1111101', '11001', '101', '1'])

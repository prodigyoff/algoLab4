import unittest
from fantz import *


class TestFantz(unittest.TestCase):

    def testFantz(self):
        self.assertEqual(fantz_launcher('0', 5), -1)
        self.assertEqual(fantz_launcher('00001', 5), 1)
        self.assertEqual(fantz_launcher('101101101', 5), 3)
        self.assertEqual(fantz_launcher('1111101', 5), 1)
        self.assertEqual(fantz_launcher('100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001',
                                        7), 5)
        self.assertEqual(fantz_launcher('101110011', 5), 3)
        self.assertEqual(fantz_launcher('101111101', 5), 5)
        self.assertEqual(fantz_launcher('100', 2), 1)
        self.assertEqual(fantz_launcher('100001000100', 2), 3)
        self.assertEqual(fantz_launcher('100000010000', 4), 2)
        self.assertEqual(fantz_launcher('11111100', 2), -1)
        self.assertEqual(fantz_launcher('10101', 5), -1)
        self.assertEqual(fantz_launcher('10110011', 5), -1)

    def testFillListOfPowers(self):
        self.assertEqual(fill_list_of_powers(5, 7), ['1111101', '11001', '101', '1'])
        self.assertEqual(fill_list_of_powers(5, 10), ['1001110001', '1111101', '11001', '101', '1'])

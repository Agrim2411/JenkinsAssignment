import unittest
from program import sum

class Testsum(unittest.TestCase):
    def test_sum1(self):
        result1 = sum(9,10,11)
        self.assertEqual(result1, 30)
    def test_sum2(self):
        result2 = sum(1,2,3)
        self.assertEqual(result2, 6)
    def test_sum3(self):
        result3 = sum(20,30,100)
        self.assertEqual(result3, 150)


if __name__ == '__main__':
    unittest.main()

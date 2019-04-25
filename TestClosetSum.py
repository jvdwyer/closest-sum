import unittest
import ClosestSum

class TestMain(unittest.TestCase):

    def test_closest_sum(self):
        arry1 = [19, 14, 6, 11, -16, 14, -16, -9, 16, 13]
        arry2 = [13, 9, -15, -2, -18, 16, 17, 2, -11, -7]
        target = -15
        self.assertEqual(ClosestSum.closest_sum(arry1, arry2, target), (-16, 2))

if __name__ == '__main__':
    unittest.main()
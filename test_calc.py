import unittest
import calc

class TestCalc(unittest.TestCase):                   # unittest.TestCase = provides some capability for testing
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)


    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)


    def test_mul(self):
        self.assertEqual(calc.mul(10,5),50)


    def test_div(self):
        self.assertEqual(calc.div(10,5),2)

        with self.assertRaises(ValueError):             # its assume is not a error
            calc.div(10,0)





if __name__ == "__main__":
    unittest.main()
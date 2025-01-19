import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):

        self.calc = SimpleCalculator()

    def test_addition(self):

        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5,7),12)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6,1),5)
        self.assertEqual(self.calc.subtract(99,90),9)
        self.assertEqual(self.calc.subtract(1,1),0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,0),0)
        self.assertEqual(self.calc.multiply(5,6),30)
        self.assertEqual(self.calc.multiply(5,11),55)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,0),None)
        self.assertEqual(self.calc.divide(100,10),10)
        self.assertEqual(self.calc.divide(0,100),0)

if __name__=='__main__':
    unittest.main()
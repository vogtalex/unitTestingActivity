import unittest
import calculator

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator.add(10, 5), 15)
		self.assertEqual(calculator.subtract(10, 5), 5)
		self.assertEqual(calculator.multiply(10, 5), 50)
		self.assertEqual(calculator.divide(10, 5), 2)

if __name__ == '__main__':
	unittest.main()
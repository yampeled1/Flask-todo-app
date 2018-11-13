import unittest

class MyTestClass(unittest.TestCase):

  def test_equal_numbers(self):
    self.assertEqual(1, 2)

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
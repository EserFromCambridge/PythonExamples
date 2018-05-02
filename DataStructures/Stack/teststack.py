import unittest
from stack import Stack, OverFlowError


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(20)

    def test_size(self):
        self.assertEqual(self.stack.size_limit, 20)
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_size(), 0)

    def test_boundaries(self):
        for i in range(0, 20):
            self.stack.push(i)
        with self.assertRaises(OverFlowError):
            self.stack.push(20)

    # @unittest.skip('Demonstration')
    def test_insert(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), None)

    def test_str(self):
        # self.stack.push(1)
        print(self.stack)
        self.assertTrue(self.stack)

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestStack)
#     return suite


if __name__ == "__main__":
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())

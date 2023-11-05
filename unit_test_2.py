import tutorialprogramrev1
import unittest

class FunctionTest(unittest.TestCase):
    def NameErrorTest(self):
        with self.assertRaises(NameError):
            tutorialprogramrev1.func1(a,6)

if __name__ == "__main__":
    unittest.main()

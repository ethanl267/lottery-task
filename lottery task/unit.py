import unittest

class agetest(unittest.TestCase):
    def test(self):

        x=20
        message="False"
        self.assertIn(x, range(18, 100),message)

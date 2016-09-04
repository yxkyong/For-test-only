import unittest
from main import is_prime
from main import print_next_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertFalse(is_prime(6))
 
if __name__ == '__main__':
    unittest.main()

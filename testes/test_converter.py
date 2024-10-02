import unittest
from preetitouicode.converter import convert_preeti_to_unicode

class TestPreetiToUnicode(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(convert_preeti_to_unicode('åßá'), 'कखग')

if __name__ == '__main__':
    unittest.main()

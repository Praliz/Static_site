import unittest

from file_manipulation import extract_title


class TestMark(unittest.TestCase):
    def test_MultiLine(self):
        doc = """
# Hello World
##line two
## line three
#Hello
    """
        result = extract_title(doc)
        self.assertEqual(result, "Hello World")    

    def test_wrong_h1(self):
        doc = """
#Hello World
##line two
## line three
#Hello
    """
        with self.assertRaises(Exception):
            extract_title(doc)
          

if __name__ == "__main__":
    unittest.main()
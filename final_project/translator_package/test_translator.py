import unittest
from translator import eng_french, french_eng
unittest.main()

class Test(unittest.TestCase):
    def test_eng_french(self):
        self.assertEqual(eng_french("hello"), "bonjour")
        # test when "hello" is given as input the output is "bonjour".
        self.assertNotEqual(eng_french("hello"), "hello")
         # test when "hello" is given as input the output is not "hello".

    def test_french_eng(self):
        self.assertEqual(french_eng("bonjour"), "hello")
        # test when "bonjour" is given as input the output is "hello".
        self.assertNotEqual(french_eng("bonjour"), "bonjour")
        # test when "bonjour" is given as input the output is not "bonjour".

'''Unit Testing of Language Translator IBM_WATSON'''

import unittest
from translator import english_to_french, french_to_english
unittest.main()

class Test(unittest.TestCase):
    '''Class Unit Testing of Language Translator'''

    def test_english_to_french(self):
        '''Unit Testing of Translation from english to french'''
        # test when "hello" is given as input the output is "bonjour".
        self.assertEqual(english_to_french("hello"), "bonjour")
        # test when "hello" is given as input the output is not "hello".
        self.assertNotEqual(english_to_french("hello"), "hello")

    def test_french_to_english(self):
        '''Unit Testing of Translation from french to english'''
        # test when "bonjour" is given as input the output is "hello".
        self.assertEqual(french_to_english("bonjour"), "hello")
        # test when "bonjour" is given as input the output is not "bonjour".
        self.assertNotEqual(french_to_english("bonjour"), "bonjour")

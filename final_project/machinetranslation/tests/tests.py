import unittest

from translator import french_to_english, english_to_french

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(french_to_english('Bonjour')) # Test for null input for frenchToEnglish
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')  # Test for the translation of the world 'Hello' and 'Bonjour'
            

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(english_to_french) # Test for null input in englishToFrench
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Bonjour' and 'Hello'.
        
unittest.main()
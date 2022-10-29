import unittest

from translator import englishToFrench, frenchToEnglish

class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(''), ) # test when null input is given as input the output is nothing.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.

class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(''), ) # test when null input is given as input the output is nothing
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()
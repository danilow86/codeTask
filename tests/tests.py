import unittest
# importing  all the
# functions defined in script.py
import script 

strUpper = "VOLVO RELEASED A NEW CAR WITH THE FOLLOWING SPEC: V6 236HP. IT WILL COST $22647 AND GOING TO BE SOLD IN NEW YORK ONLY"
strLower = "volvo released a new car with the following spec: v6 236hp. it will cost $22647 and going to be sold in new york only"
    

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(strUpper, strLower.upper())

    def test_isupper(self):
        self.assertTrue(strUpper.isupper())
        self.assertFalse(strLower.isupper())

if __name__ == '__main__':
    unittest.main()
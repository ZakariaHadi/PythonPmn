import unittest
sys.path.append('..')
from src.calculette import Calculette

class TestCalculetteMeth(unittest.TestCase):

    meta_data = Calculette()

    def test_add(self):
        self.assertEqual(meta_data.add(10,20),30)

    def test_sous(self):
        self.assertEqual(meta_data.sous(10,20),-10)
        self.assertEqual(meta_data.sous(20,10),10)

    def test_div(self):
       
        self.assertEqual(meta_data.div(10,5),2)
        with self.assertRaises(ZeroDivisionError):
            meta_data.div(10,0)
    
    def test_multi(self):
        self.assertEqual(meta_data.multi(4,20),80)
        self.assertEqual(meta_data.multi(0,10454),0)

if __name__ == '__main__':
    unittest.main()
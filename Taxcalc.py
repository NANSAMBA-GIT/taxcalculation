import unittest

def taxcalc (earning: int):
    if earning < 12000:
        return "pay no tax"
    elif 12000 < earning < 36000:
        return (20/100)*earning 
    else:
        return (40/100)*earning

class test_taxcalculation(unittest.TestCase):
    def test_valid_taxcalc(self):
        self.assertEqual(taxcalc(800), "pay no tax")
        self.assertEqual(taxcalc(20000), 4000)
        self.assertEqual(taxcalc(50000), 20000)
    

if __name__=="__main__":
    unittest.main()
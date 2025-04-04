import unittest


class test_taxcalculation(unittest.TestCase):
    def test_valid_taxcalc(self):
        self.assertequal(taxcalc(400), "pay no tax")
        self.asserteqaual(taxcalc(20000),4000)
        self.assertequal(taxcalc(50000),20000 )

if __name__=="__main__":
    unittest.main()
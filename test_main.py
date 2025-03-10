import unittest
from main import BankCustomer


class TestBankCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 =BankCustomer("Reema","Radi","pass1234") 
        self.customer2 =BankCustomer("reema","Radi","r01222") 
        self.customer3 =BankCustomer("Shouq","Radi","Sh@@ouq1") 
        # self.customer4 =BankCustomer("233","59","sara0909") 
    def test_add_new_customer(self):
        self.assertEqual(self.customer1.add_new_customer(), False) # if customer aleady exists
        self.assertEqual(self.customer2.add_new_customer(), False) # if the customer already exists (case insensitive)
        self.assertEqual(self.customer3.add_new_customer(), True) # if the customer doesn't exists
        # self.assertEqual(self.customer4.add_new_customer(),False)
        
    



if __name__== "__main__":
    unittest.main(verbosity=2)